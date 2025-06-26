"""
Configuration file for PdCrO2 SQS structure generation.

This file contains all the parameters needed for generating
Special Quasirandom Structures for doping calculations.
"""

# Input structure file
SUPERCELL_POSCAR = "POSCAR"

# Cluster expansion parameters
CUTOFFS = [8.0, 4.0]  # Angstroms

# Supercell information
CR_SITES = 18  # Total number of Cr sites in the supercell

# Doping concentrations (fractions between 0 and 1)
V_FRACTIONS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# Monte Carlo parameters
N_STEPS = 50000
RANDOM_SEED = 42

# Element order for POSCAR fixing
ELEMENT_ORDER = ['O', 'Cr', 'V', 'Pd']

# Output file naming
OUTPUT_PREFIX = "POSCAR_SQS_V"
OUTPUT_SUFFIX = ".vasp"

# Neighbor analysis cutoffs
NEIGHBOR_CUTOFFS = [4.0, 6.0, 8.0, 10.0] 