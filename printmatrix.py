import tkinter as tk
from sympy import symbols, I, pi, sqrt, exp, cos, sin, Matrix, simplify, kronecker_product, sstr


def generate_symbolic_Vk(k_sym):
    t_k = pi / k_sym
    Rk = cos(t_k)
    Ik = sin(t_k)

    e_itk = exp(I * t_k)
    e_minus_itk = exp(-I * t_k)

    sqrt_Rk = sqrt(Rk)
    sqrt_Rk_plus_1 = sqrt(Rk + 1)

    Vk_matrix = Matrix([
        [1 / sqrt(2),              0,                    sqrt_Rk,                      e_itk / sqrt(2)],
        [1 / sqrt(2),              0,           -sqrt_Rk * e_minus_itk,                e_minus_itk / sqrt(2)],
        [sqrt_Rk,                  0,   e_minus_itk * Ik / sqrt(2 * Rk),                -sqrt_Rk],
        [0,                sqrt_Rk_plus_1,               0,                                 0]
    ])

    return Vk_matrix, sqrt(Rk + 1)

def tensor_power(matrix, power):
    result = matrix
    for _ in range(power - 1):
        result = kronecker_product(result, matrix)
    return simplify(result)

def pretty_entry(expr):
    return sstr(expr, full_prec=False, order='none')

class MatrixViewer(tk.Tk):
    def __init__(self, matrix, cell_size=120):
        super().__init__()
        self.title("Symbolic Matrix Viewer")
        self.geometry("1000x700")

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.h_scroll = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.v_scroll = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.config(xscrollcommand=self.h_scroll.set, yscrollcommand=self.v_scroll.set,
                           scrollregion=(0, 0, 10000, 10000))

        self.bind_events()

        self.original_matrix = matrix
        self.zoom_factor = 1.0
        self.base_cell_size = cell_size
        self.draw_matrix()

    def bind_events(self):
        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind("<Button-4>", self.on_mouse_wheel)
        self.canvas.bind("<Button-5>", self.on_mouse_wheel)

    def on_mouse_wheel(self, event):
        direction = 1 if event.delta > 0 or event.num == 4 else -1
        factor = 1.1 if direction > 0 else 0.9
        self.zoom_factor *= factor
        self.zoom_factor = max(0.2, min(5.0, self.zoom_factor))
        self.draw_matrix()

    def draw_matrix(self):
        self.canvas.delete("all")
        cell_size = int(self.base_cell_size * self.zoom_factor)
        for i, row in enumerate(self.original_matrix):
            for j, expr in enumerate(row):
                x = j * cell_size
                y = i * cell_size
                self.canvas.create_rectangle(x, y, x + cell_size, y + cell_size, outline="black")
                self.canvas.create_text(
                    x + cell_size / 2,
                    y + cell_size / 2,
                    text=pretty_entry(expr),
                    font=("Courier", int(10 * self.zoom_factor)),
                    width=cell_size - 10
                )
        self.canvas.config(scrollregion=(0, 0, cell_size * len(self.original_matrix[0]),
                                         cell_size * len(self.original_matrix)))

if __name__ == "__main__":
    k = symbols('k', integer=True, positive=True)
    tensor_repeats = 2
    Vk, _ = generate_symbolic_Vk(k)
    Vk_tensor = tensor_power(Vk, tensor_repeats)
    rows = Vk_tensor.tolist()

    app = MatrixViewer(rows)
    app.mainloop()
