# Quantum Election Algorithms - Symbolic Computation Tools

## English Version

### Overview

This repository contains a set of Python scripts for symbolic computation of quantum election algorithms, specifically analyzing the Tani-Kobayashi-Matsumoto (TKM12) quantum algorithm for leader election in anonymous rings. The code uses SymPy for symbolic mathematics and provides tools for matrix manipulation, tensor products, and visualisation of quantum states.

### Repository Structure

├── braket.py # Custom operator class for quantum computations
├── matrix.py # Matrix generation and unitary transformation utilities
├── mult.py # Tensor power and matrix application for Vk
├── printmatrix.py # GUI matrix viewer with zoom functionality
├── tensorVk.py # Symbolic tensor power generation for Vk
├── tkm12vk.py # Full TKM12 algorithm implementation with state coloring
├── tmk12safe.py # Simplified version of TKM12 application
└── Vk.py # Vk matrix generation with symbolic parameters
text


### Files Description

#### `braket.py`
Defines a custom `MatrixDefinedOperator` class that extends SymPy's `Operator` class. This allows direct matrix-operator applications to quantum states (kets). Includes the symbolic definition of the Vk matrix from the TKM12 paper.

**Key Features:**
- Custom operator class with matrix representation
- Automatic ket application with matrix multiplication
- Symbolic matrix representation of Vk

#### `matrix.py`
Generates unitary matrices for symmetry breaking in quantum election algorithms. Creates the matrix A = I - 2uu^T where u is the normalized difference between two basis states.

**Key Features:**
- Generation of v1 and v2 vectors (uniform and shifted)
- Householder reflection matrix construction
- LaTeX output generation

#### `mult.py`
Computes tensor powers of Vk and applies them to superposed initial states. Shows the effect of applying Vk^{\otimes p} to the state (|00...0⟩ + |11...1⟩)/√2.

**Key Features:**
- Tensor product computation
- Application to symmetric initial states
- HTML output with MathJax rendering

#### `printmatrix.py`
Interactive GUI matrix viewer built with Tkinter. Allows visual exploration of symbolic matrices with zoom functionality.

**Key Features:**
- Tkinter-based matrix display
- Mouse wheel zoom
- Symbolic entry rendering

#### `tensorVk.py`
Generates symbolic tensor powers of Vk with generic parameter k. Outputs LaTeX-formatted matrices for documentation.

**Key Features:**
- Symbolic tensor power computation
- LaTeX matrix generation
- HTML with MathJax output

#### `tkm12vk.py`
Full implementation of the TKM12 algorithm analysis. Applies Vk^{\otimes p} to the symmetric state and color-codes the coefficients based on symmetry breaking.

**Key Features:**
- Complete TKM12 matrix application
- Symmetry detection with red coloring
- Detailed coefficient listing

#### `tmk12safe.py`
Simplified version of `tkm12vk.py` without the advanced formatting. Useful for quick symbolic checks.

**Key Features:**
- Basic tensor application
- LaTeX output
- Lightweight implementation

#### `Vk.py`
Standalone Vk matrix generation with symbolic parameter k. Outputs LaTeX-formatted matrices.

**Key Features:**
- Symbolic Vk matrix definition
- Normalization factor extraction
- LaTeX export

### Installation

```bash
pip install sympy numpy

For GUI features (printmatrix.py), Tkinter is included with Python standard library.
Usage Examples

Generate Vk matrix:
python

from Vk import generate_Vk_matrix_only
k = 3
Vk, norm = generate_Vk_matrix_only(k)

Apply tensor power:
python

from mult import tensor_power, generate_Vk_matrix_only
Vk, norm = generate_Vk_matrix_only(3)
Vk_tensor = tensor_power(Vk, 2)

View matrix GUI:
bash

python printmatrix.py

Output

All scripts generate LaTeX-formatted matrices and HTML files with MathJax rendering for easy visualization in web browsers.
References

    Tani, S., Kobayashi, H., & Matsumoto, K. (2012). Exact quantum algorithms for the leader election problem. ACM Transactions on Computation Theory.
