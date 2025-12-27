from modeller import *
from modeller.automodel import *
import os

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(__file__)
    
    # Set up MODELLER environment
    env = Environ()
    
    print("MODELLER environment initialized")

if __name__ == "__main__":
    main()
