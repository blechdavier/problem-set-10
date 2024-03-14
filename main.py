from sympy import Matrix, eye, pprint

print("Xavier Bradford")
print("Problem Set 10")
print("Linear Algebra")
print("Skipping 1e, 2d, 2e, 3b, 3e, 4e, and problem 8 here; they are done separately.")

inverses = [
    ("1a", Matrix([[1.0, -2.0, 1.0], [0.0, 2.0, 0.0], [-1.0, 0.0, 1.0]])),
    ("1b", Matrix([[1.0,1.0],[0.0,4.0]])),
    ("1c", Matrix([[2.0,-2.0,1.0],[0.0,2.0,0.0],[2.0,0.0,1.0]])),
    ("1d", Matrix([[2.0, 1.0, 0.0, 0.0], [0.0, 1.0, -2.0, 1.0], [0.0, 0.0, 2.0, 0.0], [0.0, 0.0, 0.0, 1.0]])),
    # skip e; it's done separately

    ("2a", Matrix([[1.0, 3.0, 0.0], [0.0, 4.0, 10.0], [9.0, 3.0, 0.0]])),
    ("2b", Matrix([[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]])),
    ("2c", Matrix([[1.0, 1.0, 1.0], [0.0, 1.0, 1.0], [-1.0, 0.0, 1.0]]))
    # skip d; it's done separately
    # skip e; it's done separately
]

determinants = [
    # 3acd
    ("3a", Matrix([[2.0, -1.0], [1.0, 1.0]])),
    # skip b; it's done separately
    ("3c", Matrix([[1.0, 1.0, 0.0], [1.0, 0.0, 1.0], [2.0, 1.0, 1.0]])),
    ("3d", Matrix([[1.0, -1.0, 4.0, 2.0], [0.0, 1.0, 0.0, 3.0], [0.0, 0.0, 2.0, 7.0], [-2.0, 3.0, 4.0, 6.0]])),
    # skip e; it's done separately

    # 4abcd
    ("4a", Matrix([[1.0, 0.0, 0.0, 0.0], [1.0, 1.0, 0.0, 0.0], [2.0, 0.0, 2.0, 0.0], [-2.0, 3.0, 4.0, 6.0]])),
    ("4b", Matrix([[0.0, 1.0, 0.0], [1.0, 0.0, -1.0], [0.0, 1.0, 1.0]])),
    ("4c", Matrix([[1.0, 1.0, 0.0, 1.0], [1.0, 2.0, 1.0, 1.0], [0.0, 0.0, 1.0, 3.0], [1.0, 1.0, 2.0, 7.0]])),
    ("4d", Matrix([[1.0, 0.0, 1.0], [2.0, 1.0, 1.0], [0.0, 1.0, 3.0]]))
    # skip e; it's done separately
]

"""Find the inverse of a square matrix using the augmented matrix method. This is the same method we use in class to compute by hand."""
def find_inverse(matrix):
    cols = matrix.shape[1]
    print("Finding the inverse of the matrix:")
    pprint(matrix)
    print("Augment the matrix by identity matrix:")
    aug = matrix.row_join(eye(matrix.shape[0]))
    pprint(aug)

    print("Put the augmented matrix into reduced row echelon form:");
    (rref, _pivots) = aug.rref()
    pprint(rref)

    # check if the left half of the augmented matrix is the identity matrix
    if rref[:, 0:cols] == eye(cols):
        print("The identity matrix is on the left half of the augmented matrix, so the inverse can be found on the right half:")
        pprint(rref[:, cols:])
    else:
        print("The matrix is not invertible because the left "+str()+" columns are not the identity matrix.")

"""Recursively calculate the determinant of a square matrix. This is the same algorithm we use in class to compute by hand."""
def determinant(matrix):
    print("Finding the determinant of the matrix by summing the results recursively:")
    pprint(matrix)
    if matrix.shape[0] == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    else:
        det = 0
        for i in range(matrix.shape[0]):
            det += ((-1) ** i) * matrix[0, i] * determinant(matrix.minorMatrix(0, i))
        return det

for (name, matrix) in inverses:
    print("Finding the inverse of matrix "+name+":")
    find_inverse(matrix)

for (name, matrix) in determinants:
    print("Finding the determinant of matrix "+name+":")
    det = determinant(matrix)
    if det == 0:
        print("The determinant is zero, so the matrix is not invertible.")
    else:
        print("The determinant is "+str(det)+", so the matrix is invertible.")
