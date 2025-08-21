# PdCrO2 Doping Magnetic Calculation

This repository contains comprehensive computational materials science calculations for studying the magnetic properties of PdCrO2 with vanadium doping using Special Quasirandom Structures (SQS) and advanced magnetic analysis techniques.

## Project Overview

The project investigates how vanadium doping affects the magnetic properties of PdCrO2 through:
1. **SQS Structure Generation**: Creating realistic doping configurations using ICET
2. **DFT Calculations**: Non-collinear magnetic calculations with spin-orbit coupling
3. **Magnetic Analysis**: Advanced magnetic moment analysis and visualization
4. **Electronic Structure**: Band structure and density of states analysis

## Repository Structure

```
PdCrO2_Doping_Magnetic_calculation/
├── magnetic_analysis/        # Advanced magnetic property analysis
│   ├── magmom.ipynb         # Magnetic moment calculation and analysis
│   ├── POSCAR               # Crystal structure for magnetic analysis
│   ├── MAGMOM.txt           # Magnetic moments data
│   ├── vesta.mcif           # MCIF file for VESTA visualization
│   ├── POSCAR_initial       # Initial structure
│   ├── MAGMOM_initial.txt   # Initial magnetic moments
│   ├── SELECTED_ATOMS_LIST  # Selected atoms for analysis
│   └── TRANSMAT             # Transformation matrix
├── sqs_generation/           # SQS structure generation
│   ├── icet.ipynb           # Main SQS generation notebook
│   ├── POSCAR               # Base structure for SQS generation
│   ├── POSCAR_SQS_V19_fixed.vasp  # SQS structure (19% V doping)
│   └── POSCAR_SQS_V50_fixed.vasp  # SQS structure (50% V doping)
├── dft_calculations/         # DFT calculation workflows
│   ├── doping/              # Doped system calculations
│   │   ├── PdCrO2_V30%_U_3/ # 30% V doping with U=3 eV
│   │   │   ├── scf/         # Self-consistent field calculation
│   │   │   ├── dos/         # Density of states calculation
│   │   │   └── band/        # Band structure calculation
│   │   ├── PdCrO2_V60%_U_3/ # 60% V doping with U=3 eV
│   │   └── PdCrO2_V90%_U_3/ # 90% V doping with U=3 eV
│   └── nodoping/            # Undoped system calculations
│       ├── scf_noncollinear/ # Non-collinear magnetic SCF
│       ├── dos_nonllinear/   # Non-linear DOS calculation
│       └── band_unfold/      # Band structure unfolding
└── README.md
```

## Key Features

### 🔬 Advanced Magnetic Analysis
- **Complex Magnetic Structure**: Implementation of 6-layer magnetic structure with 18 sublattices
- **Non-collinear Magnetism**: Full 3D magnetic moment calculations
- **VESTA Integration**: Direct export to MCIF format for visualization
- **Parameter Optimization**: Based on experimental data from Takatsu et al. (2014)

### 🏗️ SQS Structure Generation
- **ICET Framework**: Using state-of-the-art ICET library for SQS generation
- **Multiple Doping Levels**: 19%, 50%, 30%, 60%, 90% vanadium doping
- **Monte Carlo Optimization**: 50,000 steps for optimal structure generation
- **Cluster Expansion**: Advanced cluster space definition for accurate SQS

### ⚡ DFT Calculations
- **Non-collinear Magnetic**: Full spin-orbit coupling calculations
- **DFT+U Method**: U=3-4 eV for transition metals (Dudarev formulation)
- **High Precision**: 400 eV cutoff, 1e-6 convergence criteria
- **Parallel Optimization**: Optimized for Perlmutter supercomputer

## Current Status

### ✅ Completed
- **Magnetic Structure Analysis**: Complete 6-layer magnetic moment calculations
- **SQS Generation**: Multiple doping concentrations (19%, 30%, 50%, 60%, 90%)
- **DFT Workflows**: Full calculation setup for doped and undoped systems
- **VESTA Integration**: MCIF export for magnetic structure visualization
- **Parameter Optimization**: Based on experimental magnetic structure

### 🔄 In Progress
- Electronic structure analysis for doped systems
- Magnetic phase diagram construction
- High-throughput property screening

### 📋 Planned
- Machine learning for magnetic property prediction
- Advanced correlation effects analysis
- Experimental validation studies

## Quick Start

### 1. Magnetic Analysis

```bash
cd magnetic_analysis
jupyter lab magmom.ipynb
```

This opens the magnetic moment analysis notebook with:
- 6-layer magnetic structure calculations
- Parameter optimization based on experimental data
- Direct export to VESTA-compatible format

### 2. SQS Structure Generation

```bash
cd sqs_generation
jupyter lab icet.ipynb
```

Generate SQS structures for different doping concentrations using ICET.

### 3. DFT Calculations

```bash
cd dft_calculations/doping/PdCrO2_V30%_U_3/scf
sbatch submit_vasp6.4.3_cpu.slurm
```

Submit VASP calculations for doped systems.

## Technical Details

### Magnetic Structure Parameters
Based on Takatsu et al. (2014) Model 4:
- **6-layer structure** with alternating magnetic patterns
- **18 sublattices** (3 per layer × 6 layers)
- **Non-collinear moments** with 120° rotations
- **Layer-dependent parameters**: α_n, φ_n, γ_n, ξ_n

### DFT Calculation Parameters
- **VASP 6.4.3** with non-collinear magnetism
- **Spin-orbit coupling** enabled (LSORBIT = True)
- **DFT+U**: U=3-4 eV for Cr/V atoms
- **High precision**: 400 eV ENCUT, 1e-6 EDIFF
- **Parallelization**: 32 nodes × 8 cores on Perlmutter

### SQS Generation Features
- **Cluster expansion** with multiple cutoff radii
- **Monte Carlo optimization** with 50,000 steps
- **Target concentration control** for precise doping levels
- **Structure validation** and quality assessment

## Computational Resources

- **Supercomputer**: Perlmutter at NERSC
- **VASP Version**: 6.4.3
- **Parallelization**: 32 nodes × 8 cores per node
- **Memory**: Optimized for large magnetic supercells
- **Storage**: High-performance Lustre filesystem

## Dependencies

### Python Packages
```bash
pip install ase icet numpy pandas pymatgen jupyter
```

### External Software
- VASP 6.4.3 (licensed)
- VESTA (for visualization)
- SLURM (job scheduling)

## Complete Workflow

1. **Generate SQS structures** using `sqs_generation/icet.ipynb`
2. **Calculate magnetic moments** using `magnetic_analysis/magmom.ipynb`
3. **Set up DFT calculations** for each doping concentration
4. **Submit VASP jobs** using SLURM scripts
5. **Monitor calculations** with `squeue -u $USER`
6. **Analyze results** and extract magnetic properties
7. **Visualize structures** in VESTA using MCIF files

## Research Applications

This project enables:
- **Magnetic property engineering** through doping
- **Phase diagram construction** for PdCrO2-V systems
- **Electronic structure analysis** of doped delafossites
- **Magnetic frustration studies** in triangular lattices
- **High-throughput materials screening**

## Contributing

This is an active research project. For collaboration opportunities, please contact the author.

## References

- H. Takatsu, et al., Phys. Rev. B 89 (2014) 104408
- ICET: Inorganic Crystal Structure Enumeration Toolkit
- VASP: Vienna Ab initio Simulation Package

## Author

- **chamber523** - Principal investigator and developer

## License

This project is for research purposes. Please cite appropriately when using this code.