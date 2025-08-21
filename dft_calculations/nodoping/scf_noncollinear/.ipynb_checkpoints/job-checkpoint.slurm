#!/bin/bash
#SBATCH -J test
#SBATCH -A m3578
#SBATCH -N 16             
#SBATCH -C cpu
#SBATCH -q regular
#SBATCH -t 12:00:00

module load vasp/6.4.3-cpu

export OMP_NUM_THREADS=1
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

free -mh
df -Th | grep shm

echo ""
cat INCAR
echo ""

echo "the start time is:" $(date) >> timing.log
DATE1=$(date +%s)

srun -n 16 -c 64 --cpu-bind=cores vasp_ncl   

DATE2=$(date +%s)
echo "the end time is:" $(date) >> timing.log

diff=$((DATE2-DATE1))
printf "TIME COST: %d DAYS %02d:%02d:%02d\n" \
  $((diff/86400)) $(((diff/3600)%24)) $(((diff/60)%60)) $(($diff %60)) \
  >> timing.log
