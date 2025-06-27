# Protein Homology Modeling

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

## Outputs

- `modeller_model_default.pdb` - Homology model with default MODELLER parameters
- `modeller_model_hydrogen.pdb` - Model with explicit hydrogen atoms
- `swiss_model.pdb` - Comparative model from Swiss-Model web server
- Model quality assessment metrics (RMSD, DOPE scores)
- Structural alignment results
- Visualization-ready PDB files

## Reproducibility Notes

- MODELLER version may affect exact atomic coordinates
- Random seed in modeling can be set for reproducibility
- All file paths are relative to project root directory
- PDB files follow standard Protein Data Bank format (v3.3)
- Swiss-Model results obtained from https://swissmodel.expasy.org/

## Troubleshooting

**Common Issues:**

- **Import errors:** Install dependencies with `pip install biopython`
- **MODELLER not found:** 
  - Verify MODELLER installation
  - Check license key configuration
  - Ensure MODELLER Python bindings are in PYTHONPATH
- **PDB parsing errors:** 
  - Validate PDB file format using PDB validation tools
  - Check for missing residues or non-standard atom names
- **PyMOL unavailable:** Use alternative viewers:
  - ChimeraX (https://www.cgl.ucsf.edu/chimerax/)
  - VMD (https://www.ks.uiuc.edu/Research/vmd/)
  - Swiss-PdbViewer

**Path Issues:**
- Always run scripts from the project root directory
- Use relative paths for portability

## License & Attribution

- MODELLER requires free academic license (commercial licenses available)
- Swiss-Model provides web-based alternative modeling
- Model quality depends on template selection and sequence identity
- Typical pipeline: sequence alignment → model building → quality assessment → visualization
