# PdCrO2 Doping Magnetic Calculation

This repository contains computational materials science calculations for studying the magnetic properties of PdCrO2 with vanadium doping using Special Quasirandom Structures (SQS).

## Project Overview

The project investigates how vanadium doping affects the magnetic properties of PdCrO2 through:
1. **SQS Structure Generation**: Creating realistic doping configurations
2. **DFT Calculations**: Electronic structure and magnetic properties
3. **Magnetic Analysis**: Understanding doping effects on magnetism

## Repository Structure

```
PdCrO2_Doping_Magnetic_calculation/
├── sqs_generation/           # SQS structure generation
│   ├── icet.ipynb           # Main SQS generation notebook
│   ├── generate_sqs_structures.py
│   ├── config.py
│   └── README.md
├── magnetic_analysis/        # Magnetic property analysis
│   ├── magmom_to_mcif.py    # Convert magnetic moments to MCIF
│   ├── magmom.ipynb         # Magnetic moment analysis notebook
│   ├── example_usage.py     # Usage examples
│   └── README.md
├── dft_calculations/         # DFT calculation setup and workflows
│   ├── INCAR                # VASP input parameters
│   ├── KPOINTS              # K-point mesh
│   ├── POSCAR               # Crystal structure
│   ├── submit_vasp6.4.3_cpu.slurm  # SLURM job script
│   ├── generate_incar.py    # Generate INCAR for different doping
│   ├── example_workflow.py  # Complete workflow example
│   └── README.md
└── README.md
```

## Current Status

### ✅ Completed
- **SQS Structure Generation**: Complete implementation for generating Special Quasirandom Structures with vanadium doping concentrations from 10% to 90%
- **Magnetic Analysis**: Tools for converting magnetic moments to MCIF format for VESTA visualization
- **DFT Calculations**: VASP input files and workflow scripts for non-collinear magnetic calculations

### 🔄 In Progress
- Advanced magnetic property analysis
- Electronic structure analysis

### 📋 Planned
- Phase diagram analysis
- High-throughput calculations

## Quick Start

### 1. SQS Structure Generation

```bash
cd sqs_generation
jupyter lab icet.ipynb
```

This will open the Jupyter notebook for generating SQS structures.

### 2. DFT Calculation Setup

```bash
cd dft_calculations
python example_workflow.py
```

This sets up calculation directories for different doping concentrations.

### 3. Magnetic Moment Analysis

```bash
cd magnetic_analysis
python magmom_to_mcif.py -m MAGMOM.txt -p POSCAR -o vesta.mcif
```

This converts magnetic moment data to MCIF format for VESTA visualization.

### 4. Configuration

Edit `sqs_generation/config.py` to customize:
- Doping concentrations
- Supercell parameters
- Monte Carlo optimization settings

## DFT Calculation Features

### VASP Parameters
- **Non-collinear magnetic calculations** with spin-orbit coupling
- **DFT+U** with U=4 eV for Cr atoms (Dudarev method)
- **Optimized for Perlmutter** supercomputer (32 nodes, 8 cores each)
- **High precision** with 400 eV cutoff and 1e-7 convergence

### Workflow Automation
- **Automatic INCAR generation** for different doping concentrations
- **SLURM job submission** scripts
- **Result analysis** scripts
- **Integration** with SQS generation and magnetic analysis

## Requirements

- Python 3.7+
- ASE (Atomic Simulation Environment)
- ICET (Inorganic Crystal Structure Enumeration Toolkit)
- NumPy
- pymatgen
- VASP 6.4.3 (for DFT calculations)

## Installation

```bash
pip install ase icet numpy pymatgen
```

## Complete Workflow

1. **Generate SQS structures** using `sqs_generation/icet.ipynb`
2. **Set up DFT calculations** using `dft_calculations/example_workflow.py`
3. **Copy SQS POSCAR files** to calculation directories
4. **Submit VASP jobs** using SLURM scripts
5. **Monitor calculations** with `squeue -u $USER`
6. **Extract magnetic moments** from OUTCAR
7. **Convert to MCIF** using `magnetic_analysis/magmom_to_mcif.py`
8. **Visualize** in VESTA or other crystallographic software

## Computational Resources

- **Supercomputer**: Perlmutter at NERSC
- **VASP Version**: 6.4.3
- **Parallelization**: 32 nodes × 8 cores
- **Memory**: Optimized for large supercells

## Contributing

This is a research project. Please contact the author for collaboration opportunities.

## Author

- **chamber523** - Initial work

## License

This project is for research purposes.