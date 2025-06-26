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
│   ├── example_usage.py     # Usage examples
│   └── README.md
├── dft_calculations/         # DFT calculation scripts (to be added)
└── README.md
```

## Current Status

### ✅ Completed
- **SQS Structure Generation**: Complete implementation for generating Special Quasirandom Structures with vanadium doping concentrations from 10% to 90%
- **Magnetic Analysis**: Tools for converting magnetic moments to MCIF format for VESTA visualization

### 🔄 In Progress
- DFT calculation workflows
- Advanced magnetic property analysis

### 📋 Planned
- Electronic structure analysis
- Magnetic moment calculations
- Phase diagram analysis

## Quick Start

### 1. SQS Structure Generation

```bash
cd sqs_generation
jupyter lab icet.ipynb
```

This will open the Jupyter notebook for generating SQS structures.

### 2. Magnetic Moment Analysis

```bash
cd magnetic_analysis
python magmom_to_mcif.py -m MAGMOM.txt -p POSCAR -o vesta.mcif
```

This converts magnetic moment data to MCIF format for VESTA visualization.

### 3. Configuration

Edit `sqs_generation/config.py` to customize:
- Doping concentrations
- Supercell parameters
- Monte Carlo optimization settings

## Requirements

- Python 3.7+
- ASE (Atomic Simulation Environment)
- ICET (Inorganic Crystal Structure Enumeration Toolkit)
- NumPy
- pymatgen

## Installation

```bash
pip install ase icet numpy pymatgen
```

## Workflow

1. **Generate SQS structures** using the notebook in `sqs_generation/`
2. **Run DFT calculations** on the generated structures
3. **Extract magnetic moments** from VASP output
4. **Convert to MCIF** using `magnetic_analysis/magmom_to_mcif.py`
5. **Visualize** in VESTA or other crystallographic software

## Contributing

This is a research project. Please contact the author for collaboration opportunities.

## Author

- **chamber523** - Initial work

## License

This project is for research purposes.