# Protein Homology Modeling with MODELLER

**Comparative modeling and structure prediction using MODELLER**

**Stack:** Python, BioPython, MODELLER, PyMOL

## Overview

This project demonstrates protein homology modeling workflows, focusing on comparative modeling techniques to predict 3D protein structures from sequence data. The implementation uses MODELLER for structure generation and includes comparative analysis with Swiss-Model predictions.

## Problem & Approach

**Problem:** Predict the 3D structure of a target protein using homology modeling techniques.

**Approach:**
- Identify suitable template structures based on sequence similarity
- Build homology models using MODELLER software
- Generate multiple models with different parameters (default and with explicit hydrogens)
- Compare models from different prediction methods (MODELLER vs. Swiss-Model)
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
├── modeller_model_default.pdb       # Generated homology model
├── modeller_model_hydrogen.pdb      # Model with explicit hydrogens
├── swiss_model.pdb                  # Swiss-Model prediction (for comparison)
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git exclusions
└── README.md                        # This file
```

## Setup / Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Install MODELLER (required for model generation):**
   - Register at https://salilab.org/modeller/
   - Download and install for your platform
   - Configure license key (free for academic use)

3. **Optional: Install PyMOL for visualization:**
   - Download from https://pymol.org/
   - Or use open-source version: `conda install -c conda-forge pymol-open-source`

## How to Run

1. **Navigate to project directory:**
```bash
cd protein-homology-modeling-modeller
```

2. **Run modeling scripts:**
```bash
python build_model.py
python build_model_with_hydrogens.py
```

3. **Visualize structures (optional):**
```bash
pymol modeller_model_default.pdb template.pdb
```

## Data / Inputs

**Input Files:**
- `target_sequence.fasta` - Target protein sequence in FASTA format
- `template.pdb` - Template structure in PDB format

**Data Location:** All input files are included in the project directory

## Outputs

- `modeller_model_default.pdb` - Homology model with default parameters
- `modeller_model_hydrogen.pdb` - Model with explicit hydrogen atoms
- `swiss_model.pdb` - Comparative model from Swiss-Model
- Model quality metrics (RMSD, DOPE scores)

## Troubleshooting

**Common Issues:**
- **MODELLER not found:** Verify installation and license key
- **Import errors:** Install dependencies with `pip install biopython`
- **Path Issues:** Always run scripts from the project root directory
