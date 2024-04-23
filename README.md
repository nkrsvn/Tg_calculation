# Tg_calculation

Scripts for polymers glass transition temperature calculation using lammps.

1. Put file initial.data with geometry of the polymer and parameters of the force field in the main directory together with all of these scripts.
   
3. Edit temperatures and duration of calculations in the script.py:

  T_npt - temperature of calculation at elevated temperature and pressure
  nsteps_npt - steps number of calculation at elevated temperature and pressure
  T_npt_1atm - temperature of calculation at elevated temperature and atmospheric pressure
  nsteps_npt_1atm - steps number of calculation at elevated temperature and atmospheric pressure
  nsteps_prod - steps number between samplings at production run
  T_cool - temperature of the end of annealing
  nsteps_cool - steps number of annealing
  
2. Run script.py - it creates all needed directories and fills the templates.
   Calculations will be in the order: Minimization - nvt at 300 K - nvt at 600 K - npt at high temperature that you've chosen and pressures 8000, 12000, 20000, 26000, 32000, 38000, 44000 and 50000 atm - npt at high temperature and 1 atm - production run - cooling (annealing) till the T_cool you've chosen.
   
4. Run run_MD_Tg_cluster.py - it runs the calculations.

5. Run Tg_analysis.ipynb, choosing the right pressure - it processes the results of the calculations, makes graph and gives you Tg value.
