from sympy import Matrix, sqrt, eye, simplify, latex, transpose


def create_v2(nb_machines):
    length = 2**nb_machines
    inner_ones = [1] * (length - 2)
    vec = [0] + inner_ones + [0]
    return Matrix(vec) / sqrt(length - 2)

n = 3
v1_raw = Matrix([1] * 2**n)
v2_raw = Matrix([0] + [1] * (2**n - 2) + [0])

v1_norm = sqrt(2**n)
v2_norm = sqrt(2**n - 2)

v1 = v1_raw / v1_norm
v2 = v2_raw / v2_norm


u = v1 - v2
u = u / u.norm()

I = eye(2**n)
A = simplify(I - 2 * u * u.T)
B = simplify(A * A)
C = simplify(A * v1)
D = simplify(A * v2)
E = simplify(A * transpose(A))
matrix_entries = "\\\\[1em]\n".join([
    " & ".join([latex(entry) for entry in row])
    for row in E.tolist()
])

latex_code = "\\begin{pmatrix}\n" + matrix_entries + "\n\\end{pmatrix}"

latex_file_path = "../matrices/unitary_matrix_A.tex"
with open(latex_file_path, "w") as f:
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{amsmath}\n")
    f.write("\\begin{document}\n")
    f.write("\\[\n")
    f.write("A = " + latex_code + "\n")
    f.write("\\]\n")
    f.write("\\end{document}")

print("Saved to:", latex_file_path)

