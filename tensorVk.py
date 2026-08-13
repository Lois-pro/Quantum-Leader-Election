from sympy import symbols, I, pi, sqrt, exp, cos, sin, Matrix, latex
from sympy.physics.quantum import TensorProduct
from sympy import simplify


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
    [ 1 / sqrt(2),                   0,                             sqrt_Rk,                                             e_itk / sqrt(2)       ],
    [ 1 / sqrt(2),                   0,                             -sqrt_Rk * e_minus_itk,                              e_minus_itk / sqrt(2) ],
    [ sqrt_Rk,                       0,                             e_minus_2_itk * Ik / (I * sqrt(2) * R_2_k),          -sqrt_Rk              ],
    [ 0,                             sqrt_Rk_plus_1,                0,                                                   0                     ]
])

    return Vk_matrix, Rk + 1



def tensor_power(matrix, times):
    result = matrix
    for _ in range(times - 1):
        result = TensorProduct(result, matrix)
    return result


k = symbols('k', integer=True, positive=True)
#k = 3
p_val = 1

Vk_matrix, norm_denom = generate_Vk_matrix_only(k)
Vk_tensor = tensor_power(Vk_matrix, p_val)


matrix_entries = "\\\\[1.2ex]\n".join([
    " & ".join([latex(entry) for entry in row])
    for row in Vk_tensor.tolist()
])
latex_matrix = "\\begin{pmatrix}\n" + matrix_entries + "\n\\end{pmatrix}"
latex_norm = f"\\left( \\frac{{1}}{{\\sqrt{{{latex(norm_denom)}}}}} \\right)^{{{p_val}}}"

Vk_latex_full = f"{latex_norm} {latex_matrix}"

html_path = "../matrices/tensorvk/tensrovk_HTML/Vk_tensor_k_symbolic.html"
with open(html_path, "w") as f:
    f.write("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Symbolic Vk Tensor</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script type="text/javascript" id="MathJax-script" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <style>
        body { font-family: sans-serif; padding: 2em; }
        .math-display { font-size: 1.2em; }
    </style>
</head>
<body>
    <h2>Symbolic Tensor Power of V<sub>k</sub></h2>
    <p class="math-display">\\["""+
        """V_"""+str(k)+"""^{\\otimes """ + str(p_val) + "} = " + Vk_latex_full + """
    \\]</p>
    <p>where \\( R_k = \\cos\\left(\\frac{\\pi}{k}\\right) \\), and \\( I_k = \\sin\\left(\\frac{\\pi}{k}\\right) \\)</p>
</body>
</html>
""")

print("Saved to:", html_path)
