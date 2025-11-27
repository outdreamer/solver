- Linear Algebra insights
	- Matrices are linear transformations.
	- Eigenvectors = invariant directions.
	- Singular values = how much each axis is stretched.
	- Determinant = how much volume is scaled.
	- Orthogonal matrices = pure rotations/reflections (no distortion).
	- Rank = number of dimensions preserved.

- Linear algebra components
	- Scalars, Vectors, Matrices, Tensors: the basic objects. Scalars are single numbers; vectors are ordered 1-D arrays; matrices are 2-D arrays; and tensors generalize that to arbitrary numbers of axes. 

- Linear algebra functions
	- Matrix addition/multiplication, dot product, matrix-vector multiplication, elementwise hadamard product, transpose
	- Transpose: flipping a matrix across its main diagonal. Vectors are special cases of matrices, so you can transpose a row vector into a column vector, etc. 
	- Addition and scalar multiplication (broadcasting): Matrices (or vectors) of the same shape can be added elementwise. You can also multiply by scalars (scaling). Importantly: one can also broadcast a vector to add to each row of a matrix 
	- Matrix multiplication corresponds to linear transformations; for instance, the operations in a fully connected layer of a neural network, or transformations of data via weight matrices, are exactly these multiplications. Understanding matrix multiplication’s shape rules, broadcast semantics, and algebraic properties helps avoid bugs and conceptual mistakes when designing or analyzing networks.
	- Algebraic properties: matrix multiplication is distributive, associative, but not generally commutative. However, vector dot product is commutative. 
	- matrices transform space (stretching, rotating, compressing) which is why some directions in input get amplified or suppressed, why some features become more salient, etc.

- Linear algebra concepts 
	- Linear independence, linear combination, column space, invertibility, singularity: 
	- For a matrix to be invertible, it must be square and have linearly independent columns (i.e. full rank). If columns are linearly dependent, the matrix is singular: inversion fails. That means some transformations collapse dimensions, lose information. This matters deeply in learning, generalization, invertibility, stability. 
	- Invertibility, rank, pseudoinverse: useful when thinking about expressivity, reconstructing signals, solving linear systems (e.g. in least-squares, linear regression), projections; helps understand when a transformation loses information (singular), or when there are infinite solutions / no unique solution.
	- Norms and distances (l2, matrix frobenius norm, distance between vectors): 
		- To measure the “size” or “length” of vectors, we use norms. This is vital in ML: for regularization, measuring distances, errors, and controlling stability. Norms are used everywhere in ML: loss functions, regularization, embeddings.
		- Norms and geometry: Many ML concepts hinge on distances, lengths, angles (e.g. regularization, similarity, orthogonality, normalization). Norms allow consistent quantitative reasoning about size, magnitude, and controlling overfitting.

- Matrix types
	- Identity matrix & inverse: The identity matrix leaves any vector unchanged when multiplied. The inverse of A lets you “undo” A. This formalism underlies solving linear systems, understanding linear transformations, etc.
		- Inverse & Pseudoinverse (Moore–Penrose Pseudoinverse): For non-square or singular matrices (where the usual inverse doesn’t exist), the pseudoinverse generalizes the inverse. This is critical for solving least-squares problems, underdetermined or overdetermined systems, and in training models when exact inversion isn’t feasible. 
	- Determinant (and volume / invertibility interpretation): The determinant of a square matrix measures how the linear transformation associated with the matrix scales volume (or area). If determinant is zero, the transformation collapses space along at least one dimension (i.e. the transformation is non-invertible, information lost). If determinant is one (or ±1), the transformation preserves volume (though may rotate or reflect). Understanding determinant gives insight into invertibility and volume distortion under transformations. The determinant is the volume scaling factor of the linear transformation
	- Symmetric: Many matrices in ML (e.g. covariance matrices, kernel matrices) are symmetric. 
	- Diagonal / diagonalizable: occurring often when parameters or features are independent or when scaling axes — much cheaper to store/compute.
	- Orthogonal matrices: rows (and columns) mutually orthonormal. Orthogonal matrices preserve lengths and angles; important for stability, transformations that don’t distort “geometry” of data.
	- Positive (semi-)definite matrices: These matrices often appear in optimization problems, covariance matrices, Hessians, etc. 

- Matrix eigen/singular value decompositions: 
	- Fundamental for understanding data covariance, PCA, dimensionality reduction, and for analyzing stability and conditioning of transformations, as in how a weight matrix in a network stretches/compresses different directions of input space; for interpreting how data is manipulated internally
	- Eigenvalues & Eigenvectors (Eigen-decomposition) — For a square matrix A, multiplication by A scales eigenvector v by λ
		- This reveals how A stretches/compresses space along different directions — essential for understanding linear transformations, dynamics, and in ML for e.g. spectral analysis, understanding covariance, stability, etc. 
		- Use in ML: covariance analysis, stability of dynamic systems, understanding transformations
	- Singular Value Decomposition (SVD) — More general than eigen-decomposition: every real matrix (not just square symmetric ones) can be factorized as A = U Σ V ⊤
		- Here, U and V are orthogonal matrices (left- and right-singular vectors), and Σ is diagonal with singular values. SVD helps understand how a matrix transforms space — especially for non-square/transformation between spaces of different dimensions — and is widely useful for e.g. dimensionality reduction, pseudoinverses, stability analysis. SVD is the core of PCA, whitening, pseudoinverse, low-rank approximation.