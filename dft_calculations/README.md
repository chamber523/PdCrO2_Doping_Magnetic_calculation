# DFT Calculations Module

This module contains VASP input files and scripts for performing DFT calculations on PdCrO2 doping structures.

## Files

- `INCAR`: VASP input parameters for non-collinear magnetic calculations
- `KPOINTS`: K-point mesh configuration
- `POSCAR`: Crystal structure file (example)
- `submit_vasp6.4.3_cpu.slurm`: SLURM job submission script
- `README.md`: This file

## Calculation Setup

### 1. Input Files

#### INCAR Parameters
- **General**: Normal precision, 400 eV cutoff, 1e-7 convergence
- **Magnetic**: Non-collinear calculations with spin-orbit coupling
- **DFT+U**: U=4 eV for Cr atoms (Dudarev method)
- **Parallel**: Optimized for 32 nodes with 8 cores each

#### Key Features
- `LSORBIT = True`: Spin-orbit coupling enabled
- `LDAU = True`: DFT+U for Cr atoms
- `LDAUU = 0 4 0`: U=4 eV for Cr (second element)
- `MAGMOM`: Non-collinear magnetic moments for 18 Cr atoms

### 2. Workflow

1. **Generate SQS structures** using `sqs_generation/icet.ipynb`
2. **Replace POSCAR** with your SQS structure
3. **Update MAGMOM** in INCAR for your doping concentration
4. **Submit job** using the SLURM script

### 3. Job Submission

```bash
# Submit to SLURM queue
sbatch submit_vasp6.4.3_cpu.slurm

# Check job status
squeue -u $USER

# Monitor output
tail -f slurm-*.out
```

## Magnetic Moment Configuration

The INCAR contains magnetic moments for 18 Cr atoms in the supercell:
- Non-collinear magnetic moments (mx, my, mz)
- Based on spiral magnetic structure
- Compatible with SQS doping configurations

### Example MAGMOM format:
```
MAGMOM = 108*0.0 \
0.584587 0.351255 -0.731354 \
-0.697972 -0.674024 -0.241922 \
...
```

## Output Files

After calculation completion, you'll get:
- `OUTCAR`: Main output with energies and forces
- `CONTCAR`: Final relaxed structure
- `CHGCAR`: Charge density
- `DOSCAR`: Density of states
- `vasprun.xml`: XML format output for analysis

## Post-Processing

1. **Extract magnetic moments** from OUTCAR
2. **Convert to MCIF** using `magnetic_analysis/magmom_to_mcif.py`
3. **Visualize** in VESTA

## Integration with Other Modules

- **SQS Generation**: Use output POSCAR files as input
- **Magnetic Analysis**: Extract and analyze magnetic properties
- **Doping Studies**: Compare different doping concentrations

## Computational Resources

- **VASP Version**: 6.4.3
- **Nodes**: 32
- **Cores per node**: 8
- **Memory**: Optimized for Perlmutter supercomputer

## Tips

1. **Convergence**: Monitor EDIFF and forces for convergence
2. **Magnetic moments**: Check final magnetic moments in OUTCAR
3. **Structure**: Verify CONTCAR for structural changes
4. **Performance**: Adjust NPAR/KPAR based on your system

## Troubleshooting

- **Convergence issues**: Increase NELM or adjust mixing parameters
- **Memory problems**: Reduce NPAR or increase nodes
- **Magnetic ordering**: Check initial magnetic moments in INCAR 