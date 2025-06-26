#!/usr/bin/env python3
"""
PdCrO2 Doping SQS Structure Generation

This script generates Special Quasirandom Structures (SQS) for 
Pd(Cr,V)O2 doping calculations using the icet package.

Author: chamber523
Date: 2024
"""

import numpy as np
from ase import Atom
from ase.build import bulk
from ase.io import read, write
from ase.neighborlist import neighbor_list
from collections import Counter, defaultdict
import pathlib

from icet import ClusterSpace
from icet.tools.structure_generation import (generate_sqs,
                                             generate_sqs_from_supercells,
                                             generate_sqs_by_enumeration,
                                             generate_target_structure)
from icet.input_output.logging_tools import set_log_config


def analyze_neighbors(structure_file, cutoffs=[4.0, 6.0, 8.0, 10.0]):
    """
    Analyze the number of neighbors at different cutoff distances.
    
    Parameters:
    -----------
    structure_file : str
        Path to the POSCAR file
    cutoffs : list
        List of cutoff distances in Angstroms
    """
    structure = read(structure_file)
    
    print("Neighbor analysis:")
    for cutoff in cutoffs:
        i, j, d = neighbor_list('ijd', structure, cutoff)
        print(f"Cutoff = {cutoff} Å → 有 {len(d)} 个邻居")


def generate_sqs_batch(supercell_poscar, cutoffs, cr_sites, v_fractions, 
                      n_steps=50000, random_seed=42):
    """
    Batch generation of Pd(Cr,V)O2 SQS structures using a fixed supercell.

    Parameters:
    -----------
    supercell_poscar : str
        POSCAR file of the supercell.
    cutoffs : list
        List of cutoff radii for cluster expansion.
    cr_sites : int
        Total number of Cr sites in the supercell.
    v_fractions : list
        List of V doping fractions (between 0 and 1).
    n_steps : int
        Number of Monte Carlo steps for SQS generation.
    random_seed : int
        Random seed for reproducibility.
    """
    # Read supercell structure
    supercell_structure = read(supercell_poscar)

    # Define site-wise occupations
    chemical_symbols = []
    for atom in supercell_structure:
        if atom.symbol == 'Cr':
            chemical_symbols.append(['Cr', 'V'])  # allow substitution at Cr sites
        else:
            chemical_symbols.append([atom.symbol])  # fixed for other sites

    # Create ClusterSpace directly from the supercell
    cs = ClusterSpace(supercell_structure, cutoffs, chemical_symbols)

    # Use the provided supercell directly
    supercells = [supercell_structure]

    # Loop over all target V concentrations
    for v_fraction in v_fractions:
        v_count = round(cr_sites * v_fraction)
        cr_count = cr_sites - v_count
        vf = v_count / cr_sites
        cf = cr_count / cr_sites
        target_conc = {'Cr': cf, 'V': vf}

        print(f"Generating SQS for V concentration: {vf*100:.1f}% ...")

        sqs_structure = generate_sqs_from_supercells(
            cluster_space=cs,
            supercells=supercells,
            target_concentrations=target_conc,
            n_steps=n_steps,
            random_seed=random_seed
        )

        filename = f"POSCAR_SQS_V{int(vf*100)}.vasp"
        write(filename, sqs_structure)
        print(f"SQS structure written to: {filename}")


def fix_poscar(infile, outfile=None, order=None):
    """
    Rewrite a messy POSCAR so the element header is unique
    and the coordinate block is reordered accordingly.

    Parameters:
    -----------
    infile : str | Path
        Messy POSCAR / CONTCAR file
    outfile : str | None
        Output name; default adds '_fixed' suffix
    order : list[str] | None
        Desired element order, e.g. ['O','Cr','V','Pd'].
        If None → keep first-appearance order.
    """
    atoms = read(infile, format="vasp")
    symbols = atoms.get_chemical_symbols()

    # unique order
    seen = []
    for s in symbols:
        if s not in seen:
            seen.append(s)
    if order:
        # respect user order, then append leftovers
        order = list(order)
        uniq = [e for e in order if e in seen] + [e for e in seen if e not in order]
    else:
        uniq = seen

    # counts
    counts = Counter(symbols)
    nums = [counts[e] for e in uniq]

    # reorder atoms to match header
    buckets = defaultdict(list)
    for idx, s in enumerate(symbols):
        buckets[s].append(idx)
    new_idx = [i for elem in uniq for i in buckets[elem]]
    atoms = atoms[new_idx]          # ASE allows list indexing
    atoms.set_cell(atoms.get_cell())
    atoms.set_pbc(atoms.get_pbc())

    # write temporary file via ASE
    tmp = pathlib.Path(infile).with_suffix(".tmp")
    write(tmp, atoms, format="vasp", direct=True, vasp5=True, sort=False)

    # overwrite header manually
    with open(tmp, "r") as fin:
        lines = fin.readlines()
    lines[5] = " ".join(uniq) + "\n"
    lines[6] = " ".join(str(n) for n in nums) + "\n"

    if outfile is None:
        p = pathlib.Path(infile)
        outfile = p.with_name(p.stem + "_fixed" + p.suffix)
    with open(outfile, "w") as fout:
        fout.writelines(lines)
    tmp.unlink()  # remove temp file

    print("✅  Fixed POSCAR saved to", outfile)
    print("    Header :", " ".join(uniq))
    print("    Counts :", nums)


def main():
    """Main function to run SQS generation."""
    set_log_config(level='INFO')

    # Input supercell file (make sure this includes all elements: Pd, Cr, V, O)
    supercell_poscar = "POSCAR"

    # Cluster expansion cutoffs (adjust if necessary)
    cutoffs = [8.0, 4.0]

    # Total number of Cr sites in the supercell
    cr_sites = 18

    # Target V doping fractions
    v_fractions = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    # Analyze neighbors first
    print("=== Neighbor Analysis ===")
    analyze_neighbors(supercell_poscar)
    print()

    # Generate SQS structures
    print("=== SQS Generation ===")
    generate_sqs_batch(supercell_poscar, cutoffs, cr_sites, v_fractions)
    print()

    # Fix POSCAR files (optional)
    print("=== Fixing POSCAR files ===")
    for v_frac in v_fractions:
        vf = int(v_frac * 100)
        filename = f"POSCAR_SQS_V{vf}.vasp"
        if pathlib.Path(filename).exists():
            fix_poscar(filename, order=['O', 'Cr', 'V', 'Pd'])


if __name__ == "__main__":
    main() 