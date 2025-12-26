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
├── modeller_model_default.pdb       # Generated homology model (default)
├── modeller_model_hydrogen.pdb      # Model with explicit hydrogens
├── swiss_model.pdb                  # Swiss-Model prediction (for comparison)
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git exclusions
└── README.md                        # This file
```

## Outputs

- `modeller_model_default.pdb` - Homology model with default MODELLER parameters
- `modeller_model_hydrogen.pdb` - Model with explicit hydrogen atoms
- `swiss_model.pdb` - Comparative model from Swiss-Model web server
- Model quality assessment metrics (RMSD, DOPE scores)

## Setup / Installation

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install biopython
```

2. **Install MODELLER (required for model generation):**
   - Register at https://salilab.org/modeller/
   - Download and install for your platform
   - Configure license key (free for academic use)
   - Follow platform-specific installation instructions

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
# Build homology model with default parameters
python build_model.py

# Build homology model with explicit hydrogen atoms
python build_model_with_hydrogens.py
```

3. **Visualize structures (optional):**
```bash
pymol modeller_model_default.pdb template.pdb
```

## Data / Inputs

**Input Files:**
- `target_sequence.fasta` - Target protein amino acid sequence in FASTA format
- `template.pdb` - Known template structure in PDB format (homologous protein)

**Data Source:** 
- Sequences from protein databases (UniProt/GenBank)
- Template structures from Protein Data Bank (PDB)

**Data Location:** All input files are included in the project directory
