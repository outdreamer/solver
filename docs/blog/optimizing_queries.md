# Optimizing Queries to Optimize Results

Queries can be connected to 'info identified by the query' which can be connected to 'info identified by the info identified by the query'.

Queries like 'identify if there are multiple different errors triggered by the same cause' identifies info like the 'size/scope of the cause of the error', 'sequences of the error and related errors', and 'errors caused by the error'.

The query identifies a structure, and the structure identified by the query identifies other structures it can interact with ('multiple different errors' can interact with 'error size/scope', 'error sequences' and 'errors caused by an error', interacting with these other structures such as by 'being an input to/component of these other structures').

Specifically, queries should be filtered/generated/optimized to:
- identify structures that are 'maximally identifiable'
- identify structures which are an 'input to/component of/causes of/abstractions of/otherwise similar to/interactive with' other structures intended to be identified
- identify structures which can be 'uniquely/otherwise relevantly connected' to other structures intended to be identified like 'unique causes/requirements/limits', connected by interactions like 'inputs/components/causes/etc'
- identify structures which are 'clearly solutions/errors/other types' so they can be acted on
- identify structures which identify 'maximally distant' structures (as in 'uniquely identify maximally indirect structures' which is a 'high information' filter)
- identify structures when combined/sequenced/structured with any other query
- identify structures that are maximally relevant (as in 'common/powerful/causative/otherwise important/relevant')

The clarity of the 'type/uniqueness/causality' adds useful optimization metrics like 'certainty' to the information being identified.

To implement this sort of query optimization, generate graphs like:
- a graph of problem structures like 'error types (like specific errors)' connected to the 'difference structures/combinations/sequences that are relevant to identifying relevant info of that error type'
- a graph of queries to apply, in case of success/failure of other queries
	- specifically, a graph of prioritized queries to apply, in sequences based on 'general variable importance' or 'variable relevance to other variables', like checking general simple variable differences first, then general simple variable difference combinations, then specific simple variable difference combinations
- a graph of 'causal/otherwise similar differences' like 'differences that have a cause in common' or 'differences that cause each other'
- a graph that 'separates causative and non-causative variables of an error type' and 'connects causative variables' and 'connects non-causative variables'
- an integrated graph of these graphs