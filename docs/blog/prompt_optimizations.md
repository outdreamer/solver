# Prompt optimizations


## Prompt optimization examples

Prompt optimizations optimally involve applying interface structures like the following.


### Structure coverage

This involves identifying 'variation' in an 'interface/problem space/possibility space/graph/structure', identifying similarities connecting the variation, and including enough of the similarities/variants in the prompt to cover the structure. 

For example, asking an LLM to 'identify errors in code' would benefit from including specific example errors or general error types with 'many different sources/starting points/requirements/other interface structures' to increase coverage of the graph of possible errors.


### Constants/Variation

This involves applying a pattern of 'doing some of the work for the model' by adding domain knowledge like 'which structures are constant or variable', applying these as assumptions in the prompt, similar to how 'providing examples' does some of the work for the model. Relatedly, identifying requirements/certainties and possibilities/uncertainties is also useful to identify and apply as assumptions in the prompt.

Similarly, the prompt can include a 'useful prompt-specific definition of relevance' (like 'for this prompt, apply general relevance or relevance on this graph') to specify what 'generality/types/variables of connections' the LLM should identify/generate.


### Variation matching

The complexity/variation of the prompt should match the target complexity/variation of the solution, which also 'does some of the work for the model' (like how 'for a complex problem, a larger set of examples or more specific definitions is often useful').


### Meta-prompting

Applying self-optimization intents to the prompt can be useful, such as 'identify these error types (like invalid assumptions or a suboptimal intent/solution metric) in the prompt, and correct them before returning an answer'.


### Relevant graph filtering

This involves 'identifying a relevant graph' to apply the prompt to, which also 'does some of the work for the model'.


## Optimization invalidations

These prompt optimizations can be invalidated by 'organizing the model by relevance' or by 'identifying/generating relevant graphs'.

There are 'optimizations to these prompt optimizations' like 'optimizations that fulfill multiple/relevant optimization metrics' which invalidate optimization variants.