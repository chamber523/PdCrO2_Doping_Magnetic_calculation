#!/usr/bin/env python3
"""
Magnetic Moment to MCIF Converter

This script converts magnetic moment data from a text file to MCIF format
for visualization in VESTA or other crystallographic software.

Author: chamber523
Date: 2024
"""

import argparse
import numpy as np
from pymatgen.core import Structure


def convert_magmom_to_mcif(magmom_file="MAGMOM.txt", poscar_file="POSCAR", 
                          mcif_file="vesta.mcif"):
    """
    Convert magnetic moments to MCIF format.
    
    Parameters:
    -----------
    magmom_file : str
        Path to the magnetic moment file (space-separated values)
    poscar_file : str
        Path to the POSCAR file
    mcif_file : str
        Output MCIF file path
    """
    # Read POSCAR structure
    structure = Structure.from_file(poscar_file)
    
    # Read magnetic moments
    mag_flat = np.fromstring(open(magmom_file).read(), sep=" ")
    magmoms = mag_flat.reshape(-1, 3)
    
    # Check if atom counts match
    if len(structure) != len(magmoms):
        raise ValueError(f"Atom count mismatch: POSCAR {len(structure)}, MAGMOM {len(magmoms)}")
    
    # Add magnetic moments to structure
    for i, site in enumerate(structure):
        site.properties["magmom"] = magmoms[i]
    
    # Write MCIF file
    structure.to(fmt="mcif", filename=mcif_file)
    print(f"MCIF written ➜ {mcif_file}")
    print(f"Structure: {structure.formula}")
    print(f"Atoms: {len(structure)}")
    print(f"Magnetic moments: {len(magmoms)}")


def main():
    """Main function with command line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Convert magnetic moments to MCIF format for VESTA visualization"
    )
    parser.add_argument("-m", "--magmom", default="MAGMOM.txt",
                       help="Input magnetic moment file (default: MAGMOM.txt)")
    parser.add_argument("-p", "--poscar", default="POSCAR",
                       help="Input POSCAR file (default: POSCAR)")
    parser.add_argument("-o", "--mcif", default="vesta.mcif",
                       help="Output MCIF file (default: vesta.mcif)")
    
    args, _ = parser.parse_known_args()  # Ignore -f for notebook compatibility
    
    try:
        convert_magmom_to_mcif(args.magmom, args.poscar, args.mcif)
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main() 