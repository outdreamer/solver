# Learning


## Learning Definition

Learning is 'updating a function, to improve/optimize the function'.

There are many structures that can implement the concept of 'learning'.


## Standard neural network learning function

The standard neural network:
1. generates a set of changes to generate a possible function
2. checks its error function value
3. identifies causal changes of error/solution value
4. updates the changes to prioritize changes that cause the solution and de-prioritize changes that cause the error.
5. repeats the process of generating a function with prioritized changes, checking the error, identifying causes of error/solution value, and updating priority of changes to reflect causes of error/solution value.


## Alternate learning functions

Alternate structures to 'update a function, to optimize the function' include:
- identifying functions that can generate changes to 'trivially/otherwise relevantly change any function into any other function', indexing functions/function sequences by the 'degree of variation' they can consistently apply, and applying the changes likeliest to generate another function by the 'degree of variation' applied by a function sequence and the 'degree of variation' likely required to generate the optimal function
- identifying 'generally/commonly/powerfully/otherwise relevantly optimizing changes of a function' or 'changes required to optimize a function for an optimization metric (structure/combination), given its initial score on that metric', identifying which optimization metrics are relevant, and applying the changes to generate optimizations implementing the relevant optimization metrics.


## Relevance as a learning structure

Relevance may seem like just a 'constant definition' that is difficult to integrate into an 'update function of a function, to optimize the function'.

The following blog lists ways that relevance can be applied to neural networks:
https://github.com/outdreamer/solver/blob/master/docs/blog/relevance_integrations_networks.md