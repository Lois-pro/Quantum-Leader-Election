from sympy import symbols, Matrix, I, sqrt, exp


from sympy import Matrix, symbols, expand
from sympy.physics.quantum import Ket, Operator, Dagger
from sympy.physics.quantum.qapply import qapply
from sympy import Add, Mul
from sympy.physics.quantum.matrixutils import to_sympy
from sympy.physics.quantum.qubit import Qubit


from sympy.physics.quantum import Operator
from sympy.physics.quantum.matrixutils import to_sympy
from sympy import Add

class MatrixDefinedOperator(Operator):
    def __new__(cls, name, matrix, basis):
        obj = Operator.__new__(cls, name)
        obj.matrix = to_sympy(matrix)
        obj.basis = basis
        return obj

    def _apply_operator_Ket(self, ket):
        try:
            col = self.basis.index(ket)
        except ValueError:
            raise ValueError(f"Ket {ket} not in basis")

        result = sum(
            self.matrix[row, col] * self.basis[row]
            for row in range(len(self.basis))
            if self.matrix[row, col] != 0
        )
        return result

    def _apply_operator_Add(self, expr):
        return Add(*[qapply(self * arg, evaluate=True) for arg in expr.args])

    def _apply_operator_Mul(self, expr):
        scalar = 1
        state = None
        for arg in expr.args:
            if isinstance(arg, Ket):
                state = arg
            else:
                scalar *= arg
        if state is None:
            raise ValueError("No Ket found in expression")
        return scalar * qapply(self * state, evaluate=True)





R_k, t_k, R_2_k, Ik, R_k_plus_1 = symbols('R_k t_k R_2_k Ik R_k_plus_1', real=True)


e_itk = exp(I * t_k)
e_minus_itk = exp(-I * t_k)
e_minus_2_itk = exp(-2 * I * t_k)
sqrt_Rk = sqrt(R_k)
sqrt_Rk_plus_1 = sqrt(R_k_plus_1)


Vk_matrix = Matrix([
    [1 / sqrt(2),        0,               sqrt_Rk,                         e_itk / sqrt(2)],
    [1 / sqrt(2),        0,              -sqrt_Rk * e_minus_itk,          e_minus_itk / sqrt(2)],
    [sqrt_Rk,            0,     e_minus_2_itk * Ik / (I * sqrt(2) * R_2_k),     -sqrt_Rk],
    [0,           sqrt_Rk_plus_1,           0,                                  0]
])

from sympy.physics.quantum.qubit import Qubit


basis_kets_2q = [Qubit(f'{i:02b}') for i in range(4)]

Vk = MatrixDefinedOperator('Vk', Vk_matrix, basis_kets_2q)

from sympy import symbols, expand
from sympy.physics.quantum.qapply import qapply


a, b = symbols('a b')
psi = a * Qubit('00') + b * Qubit('01')

result = qapply(Vk * psi, evaluate=True)
print("Vk |ψ⟩ =")
print(expand(result))

