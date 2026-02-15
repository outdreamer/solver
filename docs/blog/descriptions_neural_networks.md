# Descriptions of Neural Networks

Different descriptions of neural networks can identify different implementations of neural networks.

The optimal description can identify optimal implementations.


## Sub-optimal descriptions of neural networks

Examples:
- a function network (this is so general it can describe anything and wont help filter implementations)
- matrix multiplication sequences (this is irrelevant, matrix multiplication doesn't determine the network's meaning)
- a multi-layer perceptron with backpropagation (this is overly specific to one neural network implementation)


## More optimal descriptions of neural networks

Examples:
- a solution function-update function, an error identification function, and an error-integration function with the update function (this is a good abstraction that allows identifying useful variants)
- a network of different change types, with different priorities
- a network of relevant functions connected by relevance scores (this is directly related to relevance, like all neural networks should be)