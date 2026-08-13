from sympy import symbols, I, pi, sqrt, exp, cos, sin, Matrix, latex, simplify, expand, shape
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum.dagger import Dagger
from sympy.physics.quantum.state import Ket, Bra
from sympy.physics.quantum.operator import Operator



def generate_Vk_matrix_only(k_value):
    t_k = pi / k_value
    t_2_k = pi / (2 * k_value)

    Rk = cos(t_k)
    R_2_k = cos(t_2_k)
    Ik = sin(t_k)

    e_itk = exp(I * t_k)
    e_minus_itk = exp(-I * t_k)
    sqrt_Rk = sqrt(Rk)
    sqrt_Rk_plus_1 = sqrt(Rk + 1)
    e_minus_2_itk = exp(-I * t_2_k)
    e_2_itk = exp(I * t_2_k)

    Vk_matrix = Matrix([
    [ 1 / sqrt(2),                   0,                             sqrt_Rk,                                             e_itk / sqrt(2)       ],
    [ 1 / sqrt(2),                   0,                             -sqrt_Rk * e_minus_itk,                              e_minus_itk / sqrt(2) ],
    [ sqrt_Rk,                       0,                             e_minus_2_itk * Ik / (I * sqrt(2) * R_2_k),          -sqrt_Rk              ],
    [ 0,                             sqrt_Rk_plus_1,                0,                                                   0                     ]
])

    Vk_matrix_dagger = Matrix([
    [ 1 / sqrt(2),                   1 / sqrt(2),                    sqrt_Rk,                                            0              ],
    [ 0,                             0,                              0,                                                  sqrt_Rk_plus_1 ],
    [ sqrt_Rk,                       -sqrt_Rk * e_itk,               e_2_itk * Ik / (-I * sqrt(2) * R_2_k),              0              ],
    [ e_minus_itk / sqrt(2),         e_itk / sqrt(2),                -sqrt_Rk,                                           0              ]
])


    return Vk_matrix,Vk_matrix_dagger,Rk + 1

def tensor_power(matrix, times):
    result = matrix
    for _ in range(times - 1):
        result = TensorProduct(result, matrix)
    return result

k= 3

p_val = 3

Vk_matrix,dagger,norm_denom = generate_Vk_matrix_only(k)

normalized_Vkmatrix = (1/sqrt(norm_denom)) * Vk_matrix
normalized_dagger = (1/sqrt(norm_denom)) * dagger
Vk_tensor = tensor_power(normalized_Vkmatrix, p_val)
dim = Vk_tensor.shape[0]
one_party_dim = dim
print(dim)

vector_ket_full_zeroes = Matrix([1] + [0] * (one_party_dim - 1))
vector_ket_full_ones = Matrix([0]*(one_party_dim -1) + [1])
dimvect = vector_ket_full_zeroes.shape[0]
print(dimvect)
normalized_ket_full_zeroes = (1/sqrt(2)) * vector_ket_full_zeroes
normalized_ket_full_ones = (1/sqrt(2)) * vector_ket_full_ones
product_zeroes = Vk_tensor * normalized_ket_full_zeroes
product_ones = Vk_tensor * normalized_ket_full_ones
temp = simplify (product_zeroes) + simplify(product_ones)

latex_rows = []
for i, val in enumerate(temp):
    binary_str = format(i, '#0'+str(2*p_val+2)+'b')[2:]

    spaced_binary = '⟩\;|'.join(binary_str[j:j + 2] for j in range(0, len(binary_str), 2))

    odd_chars = binary_str[0::2]

    if len(set(odd_chars)) == 1:
        colored_prefix = f"\\textcolor{{red}}{{{spaced_binary}}}"
    else:
        colored_prefix = spaced_binary

    ket_label = "|" + colored_prefix + "⟩"
    val_str = latex(val)
    latex_rows.append(ket_label + f"& {val_str} \\\\")

latex_result_with_indices = (
    "\\begin{array}{r|l}\n"
    + "\n".join(latex_rows) +
    "\n\\end{array}"
)

latex_simplified = latex(simplify(temp,complex = True))

latex_expression = latex_result_with_indices

html_path = "../matrices/tensorvk/application/tkm12vk/Vk_tensor_applied_vector.html"
with open(html_path, "w") as f:
    f.write("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Vk Tensor Applied to |000...0⟩ + |111...1⟩ </title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script type="text/javascript" id="MathJax-script" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <style>
        body { font-family: sans-serif; padding: 2em; }
        .math-display { font-size: 1.2em; overflow-x: auto; }
    </style>
</head>
<body>
    <h2>Symbolic Application of $V_k^{\\otimes """ + str(p_val) + "}$ to $\\lvert 0\\cdots0 \\rangle$</h2>\n")
    f.write(f'<p class="math-display">\\[\n{latex_expression}\n\\]</p>\n')
    f.write("""
    <p>where \\( R_k = \\cos\\left(\\frac{\\pi}{k}\\right) \\), and \\( I_k = \\sin\\left(\\frac{\\pi}{k}\\right) \\)</p>
</body>
</html>
""")

print("Saved to:", html_path)


