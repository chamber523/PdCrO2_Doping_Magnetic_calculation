# SQS Structure Generation for PdCrO2 Doping

This directory contains scripts for generating Special Quasirandom Structures (SQS) for Pd(Cr,V)O2 doping calculations.

## Overview

The SQS method generates structures that mimic the random distribution of dopants (V) in the host material (PdCrO2) while maintaining periodicity for computational efficiency.

## Files

- `generate_sqs_structures.py`: Main script for generating SQS structures
- `config.py`: Configuration file with all parameters
- `README.md`: This file

## Requirements

```bash
pip install ase icet numpy
```

## Usage

### 1. Prepare your input structure

Make sure you have a `POSCAR` file with your supercell structure containing:
- Pd atoms
- Cr atoms (sites that will be doped with V)
- O atoms
- Optionally, some V atoms already present

### 2. Configure parameters

Edit `config.py` to set your desired parameters:
- `SUPERCELL_POSCAR`: Path to your input POSCAR file
- `CR_SITES`: Total number of Cr sites in your supercell
- `V_FRACTIONS`: List of V doping concentrations (0.0 to 1.0)
- `CUTOFFS`: Cluster expansion cutoff distances
- `N_STEPS`: Number of Monte Carlo steps for optimization

### 3. Run the script

```bash
python generate_sqs_structures.py
```

## Output

The script will generate:
1. **Neighbor analysis**: Shows number of neighbors at different cutoff distances
2. **SQS structures**: POSCAR files for each doping concentration:
   - `POSCAR_SQS_V10.vasp` (10% V doping)
   - `POSCAR_SQS_V20.vasp` (20% V doping)
   - `POSCAR_SQS_V30.vasp` (30% V doping)
   - ... and so on
3. **Fixed POSCAR files**: Cleaned up versions with proper element ordering

## Example Output

```
=== Neighbor Analysis ===
Neighbor analysis:
Cutoff = 4.0 Å → 有 1728 个邻居
Cutoff = 6.0 Å → 有 5508 个邻居
Cutoff = 8.0 Å → 有 14976 个邻居
Cutoff = 10.0 Å → 有 25956 个邻居

=== SQS Generation ===
Generating SQS for V concentration: 10.0% ...
SQS structure written to: POSCAR_SQS_V10.vasp
Generating SQS for V concentration: 20.0% ...
SQS structure written to: POSCAR_SQS_V20.vasp
...

=== Fixing POSCAR files ===
✅  Fixed POSCAR saved to POSCAR_SQS_V10_fixed.vasp
    Header : O Cr V Pd
    Counts : [144, 58, 14, 72]
...
```

## Parameters Explained

- **Cluster Space**: Defines the local environment around each atom
- **Cutoffs**: Maximum distance for considering atomic interactions
- **Monte Carlo Steps**: Number of optimization iterations
- **Target Concentrations**: Desired ratio of Cr:V at doping sites

## Next Steps

After generating SQS structures, you can:
1. Use them for DFT calculations
2. Perform magnetic property calculations
3. Analyze the effect of doping on electronic structure

## Troubleshooting

- **Memory issues**: Reduce `N_STEPS` or use smaller supercells
- **Poor convergence**: Increase `N_STEPS` or adjust `CUTOFFS`
- **Wrong element counts**: Check `CR_SITES` parameter matches your structure 