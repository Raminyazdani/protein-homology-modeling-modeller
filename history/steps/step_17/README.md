# Protein Homology Modeling

**Comparative modeling and structure prediction using MODELLER**

**Stack:** Python, BioPython, MODELLER, PyMOL

## Overview

This project demonstrates protein homology modeling workflows, focusing on comparative modeling techniques to predict 3D protein structures from sequence data. The implementation uses MODELLER for structure generation and includes comparative analysis with Swiss-Model predictions.

## Setup / Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Install MODELLER (required for model generation):**
   - Register at https://salilab.org/modeller/
   - Download and install for your platform
   - Configure license key (free for academic use)

## How to Run

```bash
cd protein-homology-modeling-modeller
python build_model.py
python build_model_with_hydrogens.py
```
