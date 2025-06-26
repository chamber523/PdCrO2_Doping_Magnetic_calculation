# Magnetic Analysis Module

This module contains tools for analyzing and visualizing magnetic properties of materials, specifically for PdCrO2 doping studies.

## Files

- `magmom_to_mcif.py`: Main script for converting magnetic moments to MCIF format
- `example_usage.py`: Example usage and testing scripts
- `README.md`: This file

## Magnetic Moment to MCIF Converter

The `magmom_to_mcif.py` script converts magnetic moment data from a text file to MCIF format for visualization in VESTA or other crystallographic software.

### Requirements

```bash
pip install pymatgen numpy
```

### Input Files

1. **POSCAR file**: Crystal structure file (VASP format)
2. **MAGMOM.txt**: Magnetic moment data file with space-separated values
   - Format: Each line contains 3 values (mx, my, mz) for each atom
   - Example:
     ```
     1.5 0.0 0.0
     -1.2 0.3 0.1
     0.8 -0.5 0.2
     ...
     ```

### Usage

#### Command Line

```bash
# Using default file names
python magmom_to_mcif.py

# Using custom file names
python magmom_to_mcif.py -m my_magmom.txt -p my_poscar -o output.mcif

# With long options
python magmom_to_mcif.py --magmom MAGMOM.txt --poscar POSCAR --mcif vesta.mcif
```

#### Python Script

```python
from magmom_to_mcif import convert_magmom_to_mcif

# Convert using default files
convert_magmom_to_mcif()

# Convert using custom files
convert_magmom_to_mcif(
    magmom_file="my_magmom.txt",
    poscar_file="my_structure.vasp",
    mcif_file="output.mcif"
)
```

### Output

The script generates a MCIF file that can be opened in:
- VESTA
- Jmol
- Other crystallographic visualization software

### Example Workflow

1. **Generate SQS structures** (from `sqs_generation/`)
2. **Run DFT calculations** with magnetic moments
3. **Extract magnetic moments** from VASP output
4. **Convert to MCIF** using this script
5. **Visualize** in VESTA

### Error Handling

The script includes error handling for:
- File not found errors
- Atom count mismatches between POSCAR and MAGMOM files
- Invalid data formats

### Testing

Run the example script to test the functionality:

```bash
python example_usage.py
```

This will check requirements and show usage examples.

## Integration with SQS Generation

This module works seamlessly with the SQS structures generated in the `sqs_generation/` module:

1. Use SQS-generated POSCAR files as input
2. Extract magnetic moments from DFT calculations
3. Convert to MCIF for visualization
4. Analyze doping effects on magnetic properties

## Next Steps

- Add magnetic moment analysis functions
- Integrate with DFT calculation workflows
- Add magnetic property plotting tools 