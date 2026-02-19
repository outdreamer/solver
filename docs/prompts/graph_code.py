"""
- generative LLM prompt:
    - by iterating each sentence from a list of documents composed of sentences where each document has a title, 
        1. generate a graph of sentences as nodes, connected by edge types labeled like 'the following sentence' or a 'title sentence' or a 'summary sentence'
             or an 'elaboration/specification sentence' or a 'contradictory sentence' or a 'modifying sentence' or a 'sentence with subject or predicate nouns in common'
        2. generate a graph of 'verbs of each sentences as edges in the graph' connecting 'subject and predicate nouns of the sentence as nodes in the graph', 
            where each noun node is labeled by type like 'problem', 'solution', 'pattern', 'structure', 'function', 'intent', 'requirement', 'cause', 'change', 'definition', 
            and verbs are standardized to core verbs like 'is', 'equals', 'causes', 'creates', 'changes', 'differs', 'standardizes', 'similarizes', 'organizes', 'integrates', 'optimizes'
        3. generate a set of functions to identify the most adjacent problem nodes or the most adjacent hub problem nodes of a node, identify hub nodes, 
            identify the most adjacent nodes of a node type, identify nodes within n steps away from a node, identify a connection that only connects hub nodes, 
            identify a connection between two nodes with no alternate paths and only one unique path, identify connection patterns in a graph like a 'common alternating sequence of hub nodes and rare nodes', 
            identifies the shortest path between two nodes, identify the shortest path between two nodes that connects to a problem node, 
            identify problem structures in a graph like 'nodes that are not connected with a short path' or 'nodes that are not connected with a short path to a solution node'
    - generate a html visualization of a graph built with nx

- Creates two interconnected graphs from documents:
  1. Sentence-level graph with semantic relationships
  2. Noun-verb-noun triple graph with typed entities and standardized verbs
- Includes comprehensive graph analysis functions for problems, hubs, paths, and patterns.

This comprehensive implementation provides:

## 1. **Two Interconnected Graphs**
- **Sentence Graph**: nodes = sentences, edges = semantic relationships
- **Triple Graph**: nodes = nouns, edges = verbs (subject-verb-object)

## 2. **Edge Types in Sentence Graph**
- `following_sentence` — sequential order
- `title_sentence` — first sentence after title
- `shared_nouns` — sentences with common nouns
- `elaboration` — next sentence with more detail
- `contradictory` — negation/contrast words present

## 3. **Comprehensive Analysis Functions** 
| **Hub & Centrality** | identify_hub_nodes, identify_hubs_by_type |
| **Adjacency** | most_adjacent_problems, most_adjacent_hub_problems, most_adjacent_of_type, nodes_within_n_steps |
| **Path Finding** | shortest_path, shortest_path_through_problem, shortest_path_to_solution |
| **Critical Connections** | bridges_between_hubs, unique_path_connections, articulation_points |
| **Pattern Detection** | alternating_hub_rare_pattern, common_sequences |
| **Problem Structures** | disconnected_node_pairs, nodes_far_from_solutions, isolated_problem_clusters |
| **Statistics** | graph_summary, type_distribution |

pip install networkx spacy pyvis
python -m spacy download en_core_web_sm

"""

import re
import spacy
import json
import textwrap
from pathlib import Path
from dataclasses import dataclass, field
from collections import defaultdict, Counter
from typing import Optional
from itertools import combinations
import networkx as nx
from pyvis.network import Network

COLOR_SCHEMES = {'default': { 'problem': '#ef4444', 'solution': '#10b981', 'pattern': '#8b5cf6', 'structure': '#3b82f6', 'function': '#f59e0b', 'intent': '#ec4899', 'requirement': '#06b6d4', 
    'cause': '#f97316', 'change': '#84cc16', 'definition': '#6366f1', 'concept': '#a855f7', 'unknown': '#94a3b8', 'following_sentence': '#94a3b8', 'title_sentence': '#6366f1', 
    'shared_nouns': '#3b82f6', 'elaboration': '#10b981', 'contradictory': '#ef4444', 'causes': '#f97316', 'creates': '#10b981', 'changes': '#f59e0b', 'requires': '#ef4444', 'default': '#64748b'}
}
VERB_STANDARDIZATION = {
    # Identity
    'is': ['be', 'am', 'are', 'was', 'were', 'being', 'been'],
    'equals': ['equal', 'equate', 'match', 'identical'],
    'represents': ['represent', 'symbolize', 'stand for', 'denote'],
    # Causation
    'causes': ['cause', 'produce', 'generate', 'trigger', 'induce', 'lead to', 'result in'],
    'enables': ['enable', 'allow', 'permit', 'facilitate'],
    'prevents': ['prevent', 'block', 'stop', 'inhibit', 'prohibit'],
    'requires': ['require', 'need', 'necessitate', 'demand'],
    # Transformation
    'creates': ['create', 'make', 'build', 'construct', 'generate', 'produce'],
    'destroys': ['destroy', 'eliminate', 'remove', 'delete'],
    'changes': ['change', 'modify', 'alter', 'transform', 'convert'],
    'reduces': ['reduce', 'decrease', 'diminish', 'lower', 'minimize'],
    'increases': ['increase', 'grow', 'expand', 'enlarge', 'maximize'],
    # Comparison
    'differs': ['differ', 'contrast', 'vary', 'diverge'],
    'similarizes': ['resemble', 'similar', 'alike', 'compare'],
    # Organization
    'organizes': ['organize', 'structure', 'arrange', 'order'],
    'integrates': ['integrate', 'combine', 'merge', 'unify'],
    'separates': ['separate', 'divide', 'split', 'partition'],
    'connects': ['connect', 'link', 'join', 'associate', 'relate'],
    # Optimization
    'optimizes': ['optimize', 'improve', 'enhance', 'refine'],
    'filters': ['filter', 'screen', 'select', 'sift'],
    # Logic
    'implies': ['imply', 'suggest', 'indicate', 'entail'],
    'contradicts': ['contradict', 'oppose', 'conflict'],
    # Action
    'uses': ['use', 'utilize', 'employ', 'apply'],
    'defines': ['define', 'specify', 'determine', 'establish'],
    'describes': ['describe', 'characterize', 'depict', 'explain'],
    'identifies': ['identify', 'recognize', 'detect', 'find'],
    'measures': ['measure', 'quantify', 'assess', 'evaluate'],
}

VERB_TO_STANDARD = {}
for standard, variants in VERB_STANDARDIZATION.items():
    for variant in variants:
        VERB_TO_STANDARD[variant] = standard
        VERB_TO_STANDARD[variant + 's'] = standard
        VERB_TO_STANDARD[variant + 'ed'] = standard
        VERB_TO_STANDARD[variant + 'ing'] = standard

NOUN_TYPE_KEYWORDS = {
    'problem': ['problem', 'issue', 'challenge', 'difficulty', 'obstacle', 'error', 'bug', 'failure'],
    'solution': ['solution', 'answer', 'fix', 'resolution', 'remedy', 'approach', 'method'],
    'pattern': ['pattern', 'template', 'format', 'schema', 'blueprint', 'model'],
    'structure': ['structure', 'architecture', 'framework', 'organization', 'hierarchy'],
    'function': ['function', 'method', 'operation', 'procedure', 'algorithm', 'process'],
    'intent': ['intent', 'goal', 'purpose', 'objective', 'aim', 'target'],
    'requirement': ['requirement', 'constraint', 'condition', 'prerequisite', 'specification'],
    'cause': ['cause', 'reason', 'factor', 'source', 'origin', 'driver'],
    'change': ['change', 'transformation', 'modification', 'evolution', 'shift'],
    'definition': ['definition', 'meaning', 'description', 'specification', 'concept'],
}

@dataclass
class Document:
    title: str
    sentences: list[str]
    
@dataclass
class SentenceNode:
    id: str
    text: str
    doc_title: str
    position: int
    nouns: list[str] = field(default_factory=list)
    verbs: list[str] = field(default_factory=list)
    is_title: bool = False
    
@dataclass
class NounNode:
    id: str
    text: str
    noun_type: str = "unknown"  # problem, solution, pattern, etc.
    frequency: int = 0
    sources: list[str] = field(default_factory=list)

class GraphVisualizer:

    def __init__(self, G: nx.Graph, node_color_attr: str = 'noun_type', edge_color_attr: str = 'kind', color_scheme: str = 'default'):
        self.G = G
        self.node_color_attr = node_color_attr
        self.edge_color_attr = edge_color_attr
        self.color_scheme = COLOR_SCHEMES.get(color_scheme, COLOR_SCHEMES['default'])
        self.edge_colors = COLOR_SCHEMES['default']
        
    def visualize(self, output_path: str = "graph.html", height: str = "900px", width: str = "100%", layout: str = "force_atlas"):
        """ layout: Physics layout ('force_atlas', 'barnes_hut', 'repulsion') """
        net = Network(height=height, width=width,  directed=isinstance(self.G, nx.DiGraph), bgcolor="#0f172a", font_color="#e2e8f0", notebook=False)
        physics_options = self._get_physics_options(layout)
        net.set_options(json.dumps(physics_options))
        for node, data in self.G.nodes(data=True):
            self._add_node(net, node, data)
        for u, v, data in self.G.edges(data=True):
            self._add_edge(net, u, v, data)
        net.save_graph(output_path)
        print(f"✓ Visualization saved to: {output_path}")
        return output_path
    
    def _add_node(self, net, node_id, data: dict):
        node_type = data.get(self.node_color_attr, 'unknown')
        color = self.color_scheme.get(node_type, self.color_scheme['unknown'])
        degree = self.G.degree(node_id)
        frequency = data.get('frequency', 1)
        size = max(10, min(60, 15 + degree * 2 + frequency * 0.5))
        label = self._format_label(node_id, data)
        title = self._format_hover(node_id, data)
        net.add_node(node_id, label=label, title=title, color=color, size=size, shape='dot', font={'size': 12, 'color': '#e2e8f0'})
    
    def _add_edge(self, net, u, v, data: dict):
        edge_type = data.get(self.edge_color_attr, 'default')
        color = self.edge_colors.get(edge_type, self.edge_colors['default'])
        weight = data.get('weight', 1.0)
        width = max(0.5, min(8, weight * 1.5))
        label = ""
        if 'verb' in data:
            label = data['verb']
        elif edge_type != 'default':
            label = edge_type.replace('_', ' ')
        title = self._format_edge_hover(u, v, data)
        net.add_edge(u, v, label=label, title=title, color=color, width=width, arrows='to' if isinstance(self.G, nx.DiGraph) else None, font={'size': 10, 'color': '#94a3b8', 'align': 'middle'})
    
    @staticmethod
    def _format_label(node_id, data: dict) -> str:
        text = data.get('text', str(node_id))
        #if len(text) > 25: # dont truncate long labels
        #    text = text[:22] + "..."
        return text
    
    @staticmethod
    def _format_hover(node_id, data: dict) -> str:
        lines = [f"<b>{data.get('text', node_id)}</b>"]
        if 'noun_type' in data:
            lines.append(f"<i>Type: {data['noun_type']}</i>")
        if 'frequency' in data:
            lines.append(f"Frequency: {data['frequency']}")
        if 'doc' in data:
            lines.append(f"Document: {data['doc']}")
        if 'pos' in data and data['pos'] >= 0:
            lines.append(f"Position: {data['pos']}")
        if 'nouns' in data and data['nouns']:
            nouns_str = ", ".join(data['nouns'][:5])
            if len(data['nouns']) > 5:
                nouns_str += f", ... (+{len(data['nouns'])-5})"
            lines.append(f"Nouns: {nouns_str}")
        if 'verbs' in data and data['verbs']:
            verbs_str = ", ".join(data['verbs'][:5])
            lines.append(f"Verbs: {verbs_str}")
        return "<br>".join(lines)
    
    @staticmethod
    def _format_edge_hover(u, v, data: dict) -> str:
        lines = []
        if 'verb' in data:
            lines.append(f"<b>{data['verb']}</b>")
        if 'kind' in data:
            lines.append(f"Type: {data['kind']}")
        if 'weight' in data:
            lines.append(f"Weight: {data['weight']:.2f}")
        if 'source_sentence' in data:
            lines.append(f"From: {data['source_sentence']}")
        if 'nouns' in data:
            lines.append(f"Shared: {', '.join(data['nouns'][:3])}")
        return "<br>".join(lines) if lines else f"{u} → {v}"
    
    @staticmethod
    def _get_physics_options(layout: str) -> dict:
        base = {
            "physics": {"enabled": True, "stabilization": {"iterations": 200, "fit": True}}, "edges": { "smooth": {"type": "dynamic", "roundness": 0.5} },
            "interaction": { "hover": True, "tooltipDelay": 200, "navigationButtons": True, "keyboard": True },
        }
        if layout == "force_atlas":
            base["physics"]["solver"] = "forceAtlas2Based"
            base["physics"]["forceAtlas2Based"] = { "gravitationalConstant": -50, "centralGravity": 0.01, "springLength": 150, "springConstant": 0.08, "damping": 0.4}
        elif layout == "barnes_hut":
            base["physics"]["solver"] = "barnesHut"
            base["physics"]["barnesHut"] = {"gravitationalConstant": -8000, "centralGravity": 0.3, "springLength": 120, "springConstant": 0.05, "damping": 0.09}
        elif layout == "repulsion":
            base["physics"]["solver"] = "repulsion"
            base["physics"]["repulsion"] = {"nodeDistance": 200, "centralGravity": 0.2, "springLength": 150, "springConstant": 0.05, "damping": 0.09}
        return base

def detect_noun_type(noun_text: str) -> str:
    """Detect the abstract type of a noun based on keywords."""
    text_lower = noun_text.lower()
    for noun_type, keywords in NOUN_TYPE_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            return noun_type
    return "unknown"

class DocumentGraphBuilder:
    def __init__(self, spacy_model: str = "en_core_web_sm"):
        self.nlp = spacy.load(spacy_model)
        self.sentence_graph = nx.DiGraph()
        self.triple_graph = nx.MultiDiGraph()
        self.sentences: dict[str, SentenceNode] = {}
        self.nouns: dict[str, NounNode] = {}
        
    def build(self, documents: list[Document]) -> tuple[nx.DiGraph, nx.MultiDiGraph]:
        for doc in documents:
            self._process_document(doc)
        self._connect_sentences()
        return self.sentence_graph, self.triple_graph
    
    def _process_document(self, doc: Document):
        title_id = f"{doc.title}::title"
        title_node = SentenceNode(id=title_id, text=doc.title, doc_title=doc.title, position=-1, is_title=True)
        self.sentences[title_id] = title_node
        self.sentence_graph.add_node(title_id, **self._node_attrs(title_node))
        prev_sent_id = title_id
        for i, sent_text in enumerate(doc.sentences):
            sent_id = f"{doc.title}::{i}"
            spacy_doc = self.nlp(sent_text)
            nouns = [t.lemma_.lower() for t in spacy_doc if t.pos_ in ("NOUN", "PROPN") and not t.is_stop]
            verbs = [t.lemma_.lower() for t in spacy_doc if t.pos_ == "VERB"]
            sent_node = SentenceNode(id=sent_id, text=sent_text, doc_title=doc.title, position=i, nouns=nouns, verbs=verbs)
            self.sentences[sent_id] = sent_node
            self.sentence_graph.add_node(sent_id, **self._node_attrs(sent_node))
            # Sequential edge
            if prev_sent_id:
                if prev_sent_id == title_id:
                    self.sentence_graph.add_edge(title_id, sent_id, kind="title_sentence")
                else:
                    self.sentence_graph.add_edge(prev_sent_id, sent_id, kind="following_sentence")
            prev_sent_id = sent_id
            # Extract subject-verb-object triples
            self._extract_triples(sent_id, spacy_doc)
    
    def _connect_sentences(self):
        """Add semantic edges between sentences."""
        sent_ids = list(self.sentences.keys())
        for i, sid1 in enumerate(sent_ids):
            s1 = self.sentences[sid1]
            if s1.is_title:
                continue
            for sid2 in sent_ids[i+1:]:
                s2 = self.sentences[sid2]
                if s2.is_title or s1.doc_title != s2.doc_title:
                    continue
                # Shared nouns
                shared_nouns = set(s1.nouns) & set(s2.nouns)
                if shared_nouns:
                    self.sentence_graph.add_edge(sid1, sid2, kind="shared_nouns", nouns=list(shared_nouns))
                # Detect elaboration (next sentence with more detail)
                if s2.position == s1.position + 1 and len(s2.text) > len(s1.text) * 1.2:
                    self.sentence_graph.add_edge(sid1, sid2, kind="elaboration")
                # Detect contradiction (negation words)
                if any(w in s2.text.lower() for w in ['not', 'never', 'no', 'however', 'but']):
                    if shared_nouns:
                        self.sentence_graph.add_edge(sid1, sid2, kind="contradictory")
    
    def _extract_triples(self, sent_id: str, spacy_doc):
        """Extract subject-verb-object triples from a sentence."""
        for token in spacy_doc:
            if token.dep_ in ("nsubj", "nsubjpass"):
                subj = token
                verb = token.head
                # Find object
                for child in verb.children:
                    if child.dep_ in ("dobj", "pobj", "attr"):
                        obj = child
                        self._add_triple(sent_id, subj, verb, obj)
    
    def _add_triple(self, sent_id: str, subj_token, verb_token, obj_token):
        """Add a subject-verb-object triple to the graph."""
        subj_text = subj_token.lemma_.lower()
        verb_text = verb_token.lemma_.lower()
        obj_text = obj_token.lemma_.lower()
        # Standardize verb
        std_verb = VERB_TO_STANDARD.get(verb_text, verb_text)
        # Create/update noun nodes
        for noun_text in [subj_text, obj_text]:
            if noun_text not in self.nouns:
                noun_type = detect_noun_type(noun_text)
                self.nouns[noun_text] = NounNode(id=noun_text, text=noun_text, noun_type=noun_type)
            self.nouns[noun_text].frequency += 1
            self.nouns[noun_text].sources.append(sent_id)
            if noun_text not in self.triple_graph:
                self.triple_graph.add_node(noun_text, text=noun_text, noun_type=self.nouns[noun_text].noun_type, frequency=self.nouns[noun_text].frequency)
        # Add edge
        self.triple_graph.add_edge(subj_text, obj_text, verb=std_verb, source_sentence=sent_id, original_verb=verb_text)
    
    @staticmethod
    def _node_attrs(node: SentenceNode) -> dict:
        return {'text': node.text, 'doc': node.doc_title, 'pos': node.position, 'is_title': node.is_title, 'nouns': node.nouns, 'verbs': node.verbs}

class GraphAnalyzer:
    def __init__(self, sentence_graph: nx.DiGraph, triple_graph: nx.MultiDiGraph):
        self.SG = sentence_graph
        self.TG = triple_graph
        
    def identify_hub_nodes(self, graph: nx.Graph = None, top_n: int = 10) -> list[tuple]:
        """Identify hub nodes by degree centrality."""
        G = graph or self.TG
        degree_centrality = nx.degree_centrality(G)
        return sorted(degree_centrality.items(), key=lambda x: -x[1])[:top_n]
    
    def identify_hubs_by_type(self, noun_type: str, top_n: int = 5) -> list[tuple]:
        """Find hub nodes of a specific type (problem, solution, etc.)."""
        typed_nodes = [
            (n, self.TG.degree(n))
            for n, d in self.TG.nodes(data=True)
            if d.get('noun_type') == noun_type
        ]
        return sorted(typed_nodes, key=lambda x: -x[1])[:top_n]
        
    def most_adjacent_problems(self, node: str, max_n: int = 5) -> list[str]:
        """Find problem nodes most adjacent to a given node."""
        if node not in self.TG:
            return []
        neighbors = list(self.TG.predecessors(node)) + list(self.TG.successors(node))
        problems = [n for n in neighbors if self.TG.nodes[n].get('noun_type') == 'problem']
        return list(dict.fromkeys(problems))[:max_n]  # deduplicate, preserve order
    
    def most_adjacent_hub_problems(self, node: str, max_n: int = 5) -> list[str]:
        """Find high-degree problem nodes adjacent to a given node."""
        problems = self.most_adjacent_problems(node, max_n=100)
        return sorted(problems, key=lambda p: -self.TG.degree(p))[:max_n]
    
    def most_adjacent_of_type(self, node: str, noun_type: str, max_n: int = 5) -> list[str]:
        """Find nodes of a specific type adjacent to a given node."""
        if node not in self.TG:
            return []
        neighbors = list(self.TG.predecessors(node)) + list(self.TG.successors(node))
        typed = [n for n in neighbors if self.TG.nodes[n].get('noun_type') == noun_type]
        return list(dict.fromkeys(typed))[:max_n]
    
    def nodes_within_n_steps(self, node: str, n: int, graph: nx.Graph = None) -> list[str]:
        """Find all nodes within n steps of a given node."""
        G = graph or self.TG
        if node not in G:
            return []
        # BFS to depth n
        lengths = nx.single_source_shortest_path_length(G.to_undirected(), node, cutoff=n)
        return list(lengths.keys())
        
    def shortest_path(self, src: str, dst: str, graph: nx.Graph = None) -> Optional[list[str]]:
        """Find shortest path between two nodes."""
        G = graph or self.TG
        try:
            return nx.shortest_path(G.to_undirected(), src, dst)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None
    
    def shortest_path_through_problem(self, src: str, dst: str) -> Optional[list[str]]:
        """Find shortest path that passes through at least one problem node."""
        try:
            all_paths = nx.all_simple_paths(self.TG.to_undirected(), src, dst, cutoff=10)
            problem_paths = [p for p in all_paths if any(self.TG.nodes[n].get('noun_type') == 'problem' for n in p)]
            if problem_paths:
                return min(problem_paths, key=len)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            pass
        return None
    
    def shortest_path_to_solution(self, node: str) -> Optional[list[str]]:
        """Find shortest path from node to any solution node."""
        if node not in self.TG:
            return None
        solution_nodes = [n for n, d in self.TG.nodes(data=True) if d.get('noun_type') == 'solution']
        paths = []
        for sol in solution_nodes:
            path = self.shortest_path(node, sol)
            if path:
                paths.append(path)
        return min(paths, key=len) if paths else None
        
    def bridges_between_hubs(self, hub_threshold: int = 5) -> list[tuple]:
        """Find edges that only connect high-degree nodes."""
        hubs = {n for n, d in self.TG.degree() if d >= hub_threshold}
        bridges = [(u, v) for u, v in self.TG.edges() if u in hubs and v in hubs]
        return bridges
    
    def unique_path_connections(self) -> list[tuple]:
        """Find node pairs connected by exactly one unique path (bridges)."""
        bridges = list(nx.bridges(self.TG.to_undirected()))
        return bridges
    
    def articulation_points(self, graph: nx.Graph = None) -> list[str]:
        """Find nodes whose removal disconnects the graph."""
        G = graph or self.TG
        return list(nx.articulation_points(G.to_undirected()))
        
    def alternating_hub_rare_pattern(self, min_length: int = 3, hub_threshold: int = 5, rare_threshold: int = 2) -> list[list[str]]:
        """Find paths alternating between hub nodes and rare nodes."""
        hubs = {n for n, d in self.TG.degree() if d >= hub_threshold}
        rare = {n for n, d in self.TG.degree() if d <= rare_threshold}
        patterns = []
        for start in hubs:
            for path in nx.all_simple_paths(self.TG.to_undirected(), start, list(hubs)[:10], cutoff=min_length * 2):
                if len(path) < min_length:
                    continue
                # Check alternation
                is_alternating = True
                for i in range(len(path) - 1):
                    curr_is_hub = path[i] in hubs
                    next_is_hub = path[i+1] in hubs
                    if curr_is_hub == next_is_hub:
                        is_alternating = False
                        break
                if is_alternating:
                    patterns.append(path)
        return patterns[:10]  # limit results
    
    def common_sequences(self, length: int = 3) -> Counter:
        """Find common n-length sequences of node types."""
        sequences = Counter()
        for node in self.TG.nodes():
            neighbors = list(self.TG.successors(node))
            if len(neighbors) >= length - 1:
                for path in nx.all_simple_paths(self.TG, node, neighbors, cutoff=length):
                    if len(path) == length:
                        types = tuple(self.TG.nodes[n].get('noun_type', 'unknown') for n in path)
                        sequences[types] += 1
        return sequences.most_common(10)
        
    def disconnected_node_pairs(self, node_type: Optional[str] = None) -> list[tuple]:
        """Find pairs of nodes with no path between them."""
        G = self.TG.to_undirected()
        nodes = [n for n, d in self.TG.nodes(data=True) if node_type is None or d.get('noun_type') == node_type] 
        disconnected = []
        for i, n1 in enumerate(nodes):
            for n2 in nodes[i+1:]:
                if not nx.has_path(G, n1, n2):
                    disconnected.append((n1, n2))
        return disconnected[:50]  # limit
    
    def nodes_far_from_solutions(self, max_distance: int = 5) -> list[str]:
        """Find nodes with no short path to any solution node."""
        solution_nodes = [n for n, d in self.TG.nodes(data=True) if d.get('noun_type') == 'solution']
        if not solution_nodes:
            return []
        far_nodes = []
        for node in self.TG.nodes():
            if self.TG.nodes[node].get('noun_type') == 'solution':
                continue
            min_dist = float('inf')
            for sol in solution_nodes:
                try:
                    dist = nx.shortest_path_length(self.TG.to_undirected(), node, sol)
                    min_dist = min(min_dist, dist)
                except nx.NetworkXNoPath:
                    pass
            if min_dist > max_distance:
                far_nodes.append(node)
        return far_nodes
    
    def isolated_problem_clusters(self) -> list[list[str]]:
        """Find connected components containing problems but no solutions."""
        G = self.TG.to_undirected()
        components = list(nx.connected_components(G))
        problem_only_clusters = []
        for comp in components:
            types = {self.TG.nodes[n].get('noun_type') for n in comp}
            if 'problem' in types and 'solution' not in types:
                problem_only_clusters.append(list(comp))
        return problem_only_clusters
        
    def graph_summary(self, graph: nx.Graph = None) -> dict:
        """Generate summary statistics for a graph."""
        G = graph or self.TG
        U = G.to_undirected() if isinstance(G, nx.DiGraph) else G
        return {
            'nodes': G.number_of_nodes(),
            'edges': G.number_of_edges(),
            'density': nx.density(G),
            'components': nx.number_connected_components(U),
            'avg_degree': sum(d for n, d in G.degree()) / max(G.number_of_nodes(), 1),
            #'avg_clustering': nx.average_clustering(U),
            'diameter': nx.diameter(U) if nx.is_connected(U) else None,
        }
    
    def type_distribution(self) -> Counter:
        """Distribution of noun types in the triple graph."""
        types = [d.get('noun_type', 'unknown') for n, d in self.TG.nodes(data=True)]
        return Counter(types)

if __name__ == "__main__":
    docs = [
        Document(title="System Architecture", sentences=["The system architecture defines the overall structure.", "A modular architecture enables flexible changes.", "The problem with monolithic systems is tight coupling.",  "Microservices provide a solution to scalability issues.", "Each service requires clear interface definitions."]),
        Document(title="Performance Optimization", sentences=["Performance optimization improves system efficiency.", "Caching reduces database query latency.", "However, caching introduces consistency problems.", "A distributed cache requires careful synchronization.", "The solution involves using eventual consistency models."]),
    ]
    builder = DocumentGraphBuilder()
    SG, TG = builder.build(docs)
    print(f"\nSentence Graph: {SG.number_of_nodes()} nodes, {SG.number_of_edges()} edges")
    print(f"Triple Graph: {TG.number_of_nodes()} nodes, {TG.number_of_edges()} edges")
    analyzer = GraphAnalyzer(SG, TG)
    print("\n\nHUB ANALYSIS\nTop hub nodes:")
    for node, centrality in analyzer.identify_hub_nodes(top_n=5):
        ntype = TG.nodes[node].get('noun_type', 'unknown')
        print(f"  {node:<25} [{ntype:<12}] degree={TG.degree(node)}")
    print("\nTop problem hubs:")
    for node, degree in analyzer.identify_hubs_by_type('problem', top_n=3):
        print(f"  {node:<25} degree={degree}")
    print("\n\nTYPE DISTRIBUTION")
    for ntype, count in analyzer.type_distribution().most_common():
        print(f"  {ntype:<15} {count:>3}")
    print("\n\nPROBLEM STRUCTURES\nNodes far from solutions:")
    far = analyzer.nodes_far_from_solutions(max_distance=3)
    for node in far[:5]:
        print(f"  {node}")
    print("\nIsolated problem clusters:")
    clusters = analyzer.isolated_problem_clusters()
    for i, cluster in enumerate(clusters):
        print(f"  Cluster {i+1}: {', '.join(cluster[:5])}")
    print("\n\nPATH ANALYSIS")
    if 'problem' in TG and 'solution' in TG:
        path = analyzer.shortest_path('problem', 'solution')
        if path:
            print(f"\nShortest path problem → solution:\n  {' → '.join(path)}")
    print("\nBridges (unique path connections):")
    bridges = analyzer.unique_path_connections()
    for u, v in bridges[:5]:
        print(f"  {u} ←→ {v}")
    print("\n\nGRAPH SUMMARY")
    summary = analyzer.graph_summary()
    for key, val in summary.items():
        print(f"  {key:<20} {val}")
    print(f"\nSystem Graph: {SG.number_of_nodes()} nodes, {SG.number_of_edges()} edges\n")
    print(f"Triple Graph: {TG.number_of_nodes()} nodes, {TG.number_of_edges()} edges\n")
    print("Generating Pyvis visualizations SG_graph_pyvis.html and TG_graph_pyvis.html")
    sviz = GraphVisualizer(SG, color_scheme='default')
    sviz.visualize("SG_graph_pyvis.html", layout="force_atlas")
    tviz = GraphVisualizer(TG, color_scheme='default')
    tviz.visualize("TG_graph_pyvis.html", layout="force_atlas")