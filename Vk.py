from sympy import symbols, I, pi, sqrt, exp, cos, sin, Matrix, latex, simplify


def generate_Vk_matrix_only(k_value):
    t_k = pi / k_value
    t_2_k = pi / (2*k_value)

    Rk = cos(t_k)
    R_2_k = cos(t_2_k)
    Ik = sin(t_k)

    e_itk = exp(I * t_k)
    e_minus_itk = exp(-I * t_k)
    sqrt_Rk = sqrt(Rk)
    sqrt_Rk_plus_1 = sqrt(Rk + 1)
    e_minus_2_itk = exp(-I * t_2_k)

    Vk_matrix = Matrix([
        [1 / sqrt(2), 0, sqrt_Rk, e_itk / sqrt(2)],
        [1 / sqrt(2), 0, -sqrt_Rk * e_minus_itk, e_minus_itk / sqrt(2)],
        [sqrt_Rk, 0, e_minus_2_itk * Ik / (I * sqrt(2) * R_2_k), -sqrt_Rk],
        [0, sqrt_Rk_plus_1, 0, 0]
    ])

    return Vk_matrix, Rk + 1


#k = 5
k = symbols('k', integer=True, positive=True)

Vk_matrix, norm_denom = generate_Vk_matrix_only(k)

matrix_entries = "\\\\[1.5ex]\n".join([
    " & ".join([latex(entry) for entry in row])
    for row in Vk_matrix.tolist()
])

Vk_latex_matrix = "\\begin{pmatrix}\n" + matrix_entries + "\n\\end{pmatrix}"
Vk_latex_full = f"\\frac{{1}}{{\\sqrt{{{latex(norm_denom)}}}}} {Vk_latex_matrix}"

latex_file_path = "../matrices/vk/Vk_extracted_norm.tex"
with open(latex_file_path, "w") as f:
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{amsmath}\n")
    f.write("\\begin{document}\n")
    f.write("\\[\n")
    f.write(f"V_"+ "{"+ "k=" +str(k)+"}" + "= " + Vk_latex_full + "\n")
    f.write("\\]\n")
    f.write("where $R_k = \\cos\\left(\\frac{\\pi}{k}\\right)$ and $I_k = \\sin\\left(\\frac{\\pi}{k}\\right)$.\n")
    f.write("\\end{document}")

print("Saved to:", latex_file_path)
