from modeller import *
from modeller.automodel import *
import os

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(__file__)
    
    # Set up MODELLER environment
    env = Environ()
    
    # File paths
    template_pdb_path = os.path.join(script_dir, "template.pdb")
    target_sequence_fasta_path = os.path.join(script_dir,"target_sequence.fasta")
    
    # Read template and target sequence
    aln = Alignment(env)
    mdl = Model(env, file=template_pdb_path)
    aln.append_model(mdl, align_codes='template')
    
    print("Alignment setup complete")

if __name__ == "__main__":
    main()
