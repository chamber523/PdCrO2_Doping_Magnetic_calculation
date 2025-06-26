#!/usr/bin/env python3
"""
Example workflow for PdCrO2 doping calculations

This script demonstrates the complete workflow from SQS generation
to DFT calculation setup.
"""

import os
import shutil
import subprocess
from pathlib import Path


def setup_calculation_directory(doping_fraction, base_dir="."):
    """
    Set up a calculation directory for a specific doping concentration.
    
    Parameters:
    -----------
    doping_fraction : float
        Vanadium doping fraction (0.0 to 1.0)
    base_dir : str
        Base directory for calculations
    """
    # Create calculation directory
    calc_dir = f"calc_V{int(doping_fraction*100):02d}"
    calc_path = Path(base_dir) / calc_dir
    
    if calc_path.exists():
        print(f"⚠️  Directory {calc_dir} already exists!")
        return calc_path
    
    calc_path.mkdir(parents=True, exist_ok=True)
    print(f"📁 Created calculation directory: {calc_dir}")
    
    # Copy VASP input files
    files_to_copy = ["INCAR", "KPOINTS", "POSCAR", "submit_vasp6.4.3_cpu.slurm"]
    
    for file in files_to_copy:
        src = Path(base_dir) / file
        dst = calc_path / file
        
        if src.exists():
            shutil.copy2(src, dst)
            print(f"   📄 Copied {file}")
        else:
            print(f"   ⚠️  {file} not found")
    
    # Generate appropriate INCAR for this doping concentration
    try:
        from generate_incar import create_incar_for_doping
        incar_file = create_incar_for_doping(doping_fraction, str(calc_path))
        
        # Rename to INCAR
        new_incar = calc_path / "INCAR"
        if new_incar.exists():
            new_incar.unlink()
        Path(incar_file).rename(new_incar)
        print(f"   🔧 Generated INCAR for {doping_fraction*100:.1f}% V doping")
        
    except ImportError:
        print("   ⚠️  Could not import generate_incar module")
    
    return calc_path


def create_sqs_structure_placeholder(calc_dir):
    """
    Create a placeholder for SQS structure.
    
    Parameters:
    -----------
    calc_dir : Path
        Calculation directory path
    """
    placeholder = calc_dir / "POSCAR_SQS_PLACEHOLDER.txt"
    
    content = """# Placeholder for SQS structure
# Replace this file with your SQS-generated POSCAR
# 
# To generate SQS structure:
# 1. Use sqs_generation/icet.ipynb
# 2. Set your doping concentration
# 3. Copy the generated POSCAR to this directory
# 4. Rename to POSCAR
#
# Example:
# cp ../sqs_generation/poscar_V30.txt POSCAR
"""
    
    with open(placeholder, 'w') as f:
        f.write(content)
    
    print(f"   📝 Created SQS placeholder in {calc_dir.name}")


def create_analysis_script(calc_dir):
    """
    Create a script to analyze calculation results.
    
    Parameters:
    -----------
    calc_dir : Path
        Calculation directory path
    """
    script_content = f"""#!/bin/bash
# Analysis script for {calc_dir.name}

echo "🔍 Analyzing {calc_dir.name} calculation..."

# Check if calculation completed
if [ -f "OUTCAR" ]; then
    echo "✅ OUTCAR found - calculation completed"
    
    # Extract total energy
    echo "📊 Total energy:"
    grep "free  energy   TOTEN" OUTCAR | tail -1
    
    # Extract magnetic moments
    echo "🧲 Magnetic moments:"
    grep -A 20 "magnetization (x)" OUTCAR | tail -20
    
    # Check convergence
    echo "🔄 Convergence check:"
    grep "reached required accuracy" OUTCAR
    
else
    echo "❌ OUTCAR not found - calculation may still be running"
    echo "Check job status with: squeue -u $USER"
fi

# Convert to MCIF if calculation completed
if [ -f "OUTCAR" ] && [ -f "../magnetic_analysis/magmom_to_mcif.py" ]; then
    echo "🔄 Converting to MCIF..."
    python ../magnetic_analysis/magmom_to_mcif.py OUTCAR
fi
"""
    
    script_path = calc_dir / "analyze_results.sh"
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    # Make executable
    os.chmod(script_path, 0o755)
    print(f"   📜 Created analysis script: analyze_results.sh")


def main():
    """Main workflow function."""
    print("🚀 PdCrO2 Doping Calculation Workflow")
    print("=" * 50)
    
    # Doping concentrations to set up
    doping_fractions = [0.1, 0.2, 0.3, 0.4, 0.5]
    
    print(f"\n📋 Setting up calculations for {len(doping_fractions)} doping concentrations...")
    
    for v_frac in doping_fractions:
        print(f"\n🔧 Setting up {v_frac*100:.1f}% V doping...")
        
        # Create calculation directory
        calc_dir = setup_calculation_directory(v_frac)
        
        # Create SQS placeholder
        create_sqs_structure_placeholder(calc_dir)
        
        # Create analysis script
        create_analysis_script(calc_dir)
    
    print(f"\n🎉 Workflow setup complete!")
    print("\n📋 Next steps:")
    print("1. Generate SQS structures using sqs_generation/icet.ipynb")
    print("2. Copy SQS POSCAR files to calculation directories")
    print("3. Submit calculations using sbatch submit_vasp6.4.3_cpu.slurm")
    print("4. Monitor progress with squeue -u $USER")
    print("5. Analyze results using analyze_results.sh")
    
    print("\n📁 Directory structure:")
    for v_frac in doping_fractions:
        calc_dir = f"calc_V{int(v_frac*100):02d}"
        print(f"   {calc_dir}/")
        print(f"     ├── INCAR (VASP parameters)")
        print(f"     ├── KPOINTS (k-point mesh)")
        print(f"     ├── POSCAR (structure - replace with SQS)")
        print(f"     ├── submit_vasp6.4.3_cpu.slurm (job script)")
        print(f"     ├── POSCAR_SQS_PLACEHOLDER.txt (instructions)")
        print(f"     └── analyze_results.sh (analysis script)")


if __name__ == "__main__":
    main() 