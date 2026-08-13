# Quantum Election - Symbolic Tools

## Overview

Python scripts for symbolic computation of Tani-Kobayashi-Matsumoto (TKM12) quantum election algorithm using SymPy.

## Files

| File | Description |
|------|-------------|
| `Vk.py` | Generate Vk matrix with symbolic parameter k |
| `tensorVk.py` | Symbolic tensor power of Vk |
| `mult.py` | Apply Vk⊗p to symmetric state (|00...0⟩ + |11...1⟩)/√2 |
| `tkm12vk.py` | Full TKM12 analysis with symmetry coloring |
| `tmk12safe.py` | Simplified version for quick checks |
| `braket.py` | Custom MatrixDefinedOperator class |
| `matrix.py` | Householder reflection matrices |
| `printmatrix.py` | Tkinter GUI matrix viewer (zoom) |

## Quick Start

```bash
pip install sympy numpy
