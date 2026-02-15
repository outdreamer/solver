# Learning


## Learning Definition

Learning is 'updating a function/structure, to improve/optimize the function/structure'. It involves a function to update a function, and a function to identify errors, and a function to integrate identified errors with function updates.

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


## Update/Identify/Integrate functions

Examples of function-update functions:
- change the weights/activations of variables of a function
- change the 'connection functions or structures' of variables of a function
- change the variables of a function (like integrating common/general variables into a data set)
- change the input component/causal/generative functions of a function
- change standard/common or maximally different functions to generate functions

Identify error functions:
- identify differences in error/solution function maxima position (mapping the solution to the error function by its features like its maxima)
- identify area of differences in error/solution outputs
- identify relevant error types like 'errors of over-generalization/over-uniqueness'

Integrate errors with update function:
- apply 'proportional opposing changes of errors' to change the solution function (weights/activations or connection functions or variables or other changes applied by the function-update function)
- identify 'error-causing variables/weights' and apply 'incremental reductions of error-causing variables/weights'


## Neural networks as change-connecting structures (difference-similarizing structures)

Apply variants of neural networks with different 'change structures':
- apply a 'change/variable node network connected by layers of different functions'
- apply a 'function node network, connected by common/relevant changes of functions'
- apply a 'function node network, connected by different functions'
- apply a 'function node network of maximally different functions'


## Intent of learning

The point of learning is to identify relevant structures, so starting learning by applying identified relevant structures (like interfaces and relevant graphs) is useful.


## Relevance as a learning structure

Relevance may seem like just a 'constant definition' that is difficult to integrate into an 'update function of a function, to optimize the function'.

The following blog lists ways that relevance can be applied to neural networks:
https://github.com/outdreamer/solver/blob/master/docs/blog/relevance_integrations_networks.md

Examples of applying relevance to create a 'function-updating function' and an 'error-identification function'
- identifying opposing error types like 'general function shape accuracy' and 'local/specific accuracy' to apply 'alternating changes to implement a change for correcting one of the error types'
- applying optimization changes to correct error types like 'generality-optimizing changes' and 'generality/complexity-optimizing changes'
- applying 'sequences of prioritized error types' to 'identify/correct first'