#!/usr/bin/env python3
"""
Example usage of magnetic moment to MCIF conversion

This script demonstrates how to use the magmom_to_mcif.py script
for converting magnetic moment data to MCIF format.
"""

from magmom_to_mcif import convert_magmom_to_mcif
import numpy as np


def create_sample_magmom_file(filename="MAGMOM.txt", n_atoms=100):
    """
    Create a sample magnetic moment file for testing.
    
    Parameters:
    -----------
    filename : str
        Output filename
    n_atoms : int
        Number of atoms (magnetic moments)
    """
    # Generate random magnetic moments (example data)
    magmoms = np.random.randn(n_atoms, 3) * 2.0  # Random moments around ±2 μB
    
    # Save to file
    np.savetxt(filename, magmoms, fmt='%.6f')
    print(f"Sample MAGMOM file created: {filename}")
    print(f"Shape: {magmoms.shape}")
    print(f"Mean magnitude: {np.linalg.norm(magmoms, axis=1).mean():.3f} μB")


def example_conversion():
    """Example of converting magnetic moments to MCIF."""
    print("=== Magnetic Moment to MCIF Conversion Example ===\n")
    
    # Example 1: Using default file names
    print("Example 1: Using default file names")
    print("Files needed: POSCAR, MAGMOM.txt")
    print("Output: vesta.mcif")
    print()
    
    # Example 2: Using custom file names
    print("Example 2: Using custom file names")
    try:
        convert_magmom_to_mcif(
            magmom_file="my_magmom.txt",
            poscar_file="my_structure.vasp", 
            mcif_file="my_output.mcif"
        )
    except FileNotFoundError:
        print("(This example would work if the files existed)")
    print()
    
    # Example 3: Command line usage
    print("Example 3: Command line usage")
    print("python magmom_to_mcif.py -m MAGMOM.txt -p POSCAR -o vesta.mcif")
    print("python magmom_to_mcif.py --magmom my_magmom.txt --poscar my_poscar --mcif output.mcif")
    print()


def check_requirements():
    """Check if required packages are available."""
    print("=== Requirements Check ===")
    
    try:
        import pymatgen
        print("✅ pymatgen: Available")
    except ImportError:
        print("❌ pymatgen: Not available (pip install pymatgen)")
    
    try:
        import numpy
        print("✅ numpy: Available")
    except ImportError:
        print("❌ numpy: Not available (pip install numpy)")
    
    print()


if __name__ == "__main__":
    check_requirements()
    example_conversion()
    
    # Uncomment to create a sample file
    # create_sample_magmom_file() 