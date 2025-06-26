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
│   ├── generate_sqs_structures.py
│   ├── config.py
│   └── README.md
├── dft_calculations/         # DFT calculation scripts (to be added)
├── magnetic_analysis/        # Magnetic property analysis (to be added)
└── README.md
```

## Current Status

### ✅ Completed
- **SQS Structure Generation**: Complete implementation for generating Special Quasirandom Structures with vanadium doping concentrations from 10% to 90%

### 🔄 In Progress
- DFT calculation workflows
- Magnetic property analysis

### 📋 Planned
- Electronic structure analysis
- Magnetic moment calculations
- Phase diagram analysis

## Quick Start

### 1. SQS Structure Generation

```bash
cd sqs_generation
python generate_sqs_structures.py
```

This will generate POSCAR files for different V doping concentrations.

### 2. Configuration

Edit `sqs_generation/config.py` to customize:
- Doping concentrations
- Supercell parameters
- Monte Carlo optimization settings

## Requirements

- Python 3.7+
- ASE (Atomic Simulation Environment)
- ICET (Inorganic Crystal Structure Enumeration Toolkit)
- NumPy

## Installation

```bash
pip install ase icet numpy
```

## Contributing

This is a research project. Please contact the author for collaboration opportunities.

## Author

- **chamber523** - Initial work

## License

This project is for research purposes.