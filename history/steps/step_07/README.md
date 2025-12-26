# Protein Homology Modeling

**Comparative modeling and structure prediction using MODELLER**

**Stack:** Python, BioPython, MODELLER, PyMOL

## Overview

This project demonstrates protein homology modeling workflows, focusing on comparative modeling techniques to predict 3D protein structures from sequence data. The implementation uses MODELLER for structure generation.

## Problem & Approach

**Problem:** Predict the 3D structure of a target protein using homology modeling techniques.

**Approach:**
- Identify suitable template structures based on sequence similarity
- Build homology models using MODELLER software
- Generate multiple models with different parameters
- Perform structural quality assessment and validation

## Tech Stack

- **Python 3.x** - Core scripting language
- **BioPython** - Biological sequence and structure analysis
- **MODELLER** - Homology modeling software
- **PyMOL** - Molecular structure visualization

## Repository Structure

```
protein-homology-modeling-modeller/
├── build_model.py                   # Main modeling script (default parameters)
├── build_model_with_hydrogens.py    # Modeling script with explicit hydrogens
├── target_sequence.fasta            # Target protein sequence
├── template.pdb                     # Template structure
├── modeller_output.pdb              # Generated homology model (default)
├── modeller_hydrogen.pdb            # Model with explicit hydrogens
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git exclusions
└── README.md                        # This file
```

## Outputs

- `modeller_output.pdb` - Homology model with default MODELLER parameters
- `modeller_hydrogen.pdb` - Model with explicit hydrogen atoms
- Model quality assessment metrics (RMSD, DOPE scores)
