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

------------------------------------------------------------------------------------------------------------------------------------------------------

# Élection Quantique - Outils Symboliques

## Présentation

Scripts Python pour le calcul formel de l'algorithme d'élection quantique de Tani-Kobayashi-Matsumoto (TKM12) utilisant SymPy.

## Fichiers

| Fichier | Description |
|---------|-------------|
| `Vk.py` | Génération de la matrice Vk avec paramètre symbolique k |
| `tensorVk.py` | Puissance tensorielle symbolique de Vk |
| `mult.py` | Application de Vk⊗p à l'état symétrique (|00...0⟩ + |11...1⟩)/√2 |
| `tkm12vk.py` | Analyse complète TKM12 avec coloriage des symétries |
| `tmk12safe.py` | Version simplifiée pour vérifications rapides |
| `braket.py` | Classe MatrixDefinedOperator personnalisée |
| `matrix.py` | Matrices de réflexion de Householder |
| `printmatrix.py` | Visualiseur de matrices Tkinter (zoom) |

## Utilisation Rapide

```bash
pip install sympy numpy
