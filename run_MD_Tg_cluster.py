import os
import shutil


def insert_missing(file_to_insert_to, data_to_be_inserted):
    with open(file_to_insert_to, 'r') as inp:
        inplines = inp.readlines()
        for i, l in enumerate(inplines):
            if l.startswith('Atoms'):
                insert_position = i - 1
    
    with open(file_to_insert_to, 'w') as out:
        out.writelines(inplines[:insert_position])
        out.write('\n')
        out.write(data_to_be_inserted)
        out.writelines(inplines[insert_position:])


data_file = r'./Minimization/initial.data'

with open(data_file, 'r') as data:
    lines = data.readlines()
    for i, l in enumerate(lines):
        if l.startswith('Bond Coeffs'):
            start = i
        elif l.startswith('Atoms'):
            stop = i - 1

fragment = lines[start:stop]
missed_lines = ''.join(fragment)


# run minimization
#os.chdir(r'./Minimization')
# # https://docs.lammps.org/Run_windows.html
#os.system('mpirun -n 128 lmp -i input_min.lammps')
#shutil.copy(r'nvt300.data', r'./../nvt600/nvt300.data')

# # run nvt
#os.chdir(r'./../nvt600')
#insert_missing('nvt300.data', missed_lines)
#os.system('mpirun -n 128 lmp -i input_nvt600.lammps')
#shutil.copy(r'nvt600.data', r'./../npt600/npt600_50000/nvt600.data')
#shutil.copy(r'nvt600.data', r'./../npt600/npt600_44000/nvt600.data')
#shutil.copy(r'nvt600.data', r'./../npt600/npt600_38000/nvt600.data')
#shutil.copy(r'nvt600.data', r'./../npt600/npt600_32000/nvt600.data')
#shutil.copy(r'nvt600.data', r'./../npt600/npt600_26000/nvt600.data')
#shutil.copy(r'nvt600.data', r'./../npt600/npt600_20000/nvt600.data')
#shutil.copy(r'nvt600.data', r'./../npt600/npt600_14000/nvt600.data')
#shutil.copy(r'nvt600.data', r'./../npt600/npt600_8000/nvt600.data')


# # run npt600_50000
os.chdir(r'./npt600/npt600_50000') #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#insert_missing('nvt600.data', missed_lines)
#os.system('mpirun -n 12 lmp -i input_npt600.lammps')
shutil.copy(r'npt600_50000.data', r'./../../npt1atm/npt1atm_50000/npt600_50000.data')

# # run npt600_44000
os.chdir(r'./../npt600_44000')
insert_missing('nvt600.data', missed_lines)
os.system('mpirun -n 12 lmp -i input_npt600.lammps')
shutil.copy(r'npt600_44000.data', r'./../../npt1atm/npt1atm_44000/npt600_44000.data')

# # run npt600_38000
os.chdir(r'./../npt600_38000')
insert_missing('nvt600.data', missed_lines)
os.system('mpirun -n 12 lmp -i input_npt600.lammps')
shutil.copy(r'npt600_38000.data', r'./../../npt1atm/npt1atm_38000/npt600_38000.data')

# # run npt600_32000
os.chdir(r'./../npt600_32000')
insert_missing('nvt600.data', missed_lines)
os.system('mpirun -n 12 lmp -i input_npt600.lammps')
shutil.copy(r'npt600_32000.data', r'./../../npt1atm/npt1atm_32000/npt600_32000.data')

# # run npt600_26000
os.chdir(r'./../npt600_26000')
insert_missing('nvt600.data', missed_lines)
os.system('mpirun -n 12 lmp -i input_npt600.lammps')
shutil.copy(r'npt600_26000.data', r'./../../npt1atm/npt1atm_26000/npt600_26000.data')

# # run npt600_20000
os.chdir(r'./../npt600_20000')
insert_missing('nvt600.data', missed_lines)
os.system('mpirun -n 12 lmp -i input_npt600.lammps')
shutil.copy(r'npt600_20000.data', r'./../../npt1atm/npt1atm_20000/npt600_20000.data')

# # run npt600_14000
os.chdir(r'./../npt600_14000')
insert_missing('nvt600.data', missed_lines)
os.system('mpirun -n 12 lmp -i input_npt600.lammps')
shutil.copy(r'npt600_14000.data', r'./../../npt1atm/npt1atm_14000/npt600_14000.data')

# # run npt600_8000
os.chdir(r'./../npt600_8000')
insert_missing('nvt600.data', missed_lines)
os.system('mpirun -n 12 lmp -i input_npt600.lammps')
shutil.copy(r'npt600_8000.data', r'./../../npt1atm/npt1atm_8000/npt600_8000.data')

# run npt 1 atm
os.chdir(r'./../../npt1atm/npt1atm_50000')
insert_missing('npt600_50000.data', missed_lines)
os.system('mpirun -n 20 lmp -i input_npt_1atm.lammps')
shutil.copy(r'npt_1_50000.data', r'./../../Production/Prod_50000/npt_1_50000.data')

os.chdir(r'./../npt1atm_44000')
insert_missing('npt600_44000.data', missed_lines)
os.system('mpirun -n 20 lmp -i input_npt_1atm.lammps')
shutil.copy(r'npt_1_44000.data', r'./../../Production/Prod_44000/npt_1_44000.data')

os.chdir(r'./../npt1atm_38000')
insert_missing('npt600_38000.data', missed_lines)
os.system('mpirun -n 20 lmp -i input_npt_1atm.lammps')
shutil.copy(r'npt_1_38000.data', r'./../../Production/Prod_38000/npt_1_38000.data')

os.chdir(r'./../npt1atm_32000')
insert_missing('npt600_32000.data', missed_lines)
os.system('mpirun -n 20 lmp -i input_npt_1atm.lammps')
shutil.copy(r'npt_1_32000.data', r'./../../Production/Prod_32000/npt_1_32000.data')

os.chdir(r'./../npt1atm_26000')
insert_missing('npt600_26000.data', missed_lines)
os.system('mpirun -n 20 lmp -i input_npt_1atm.lammps')
shutil.copy(r'npt_1_26000.data', r'./../../Production/Prod_26000/npt_1_26000.data')

os.chdir(r'./../npt1atm_20000')
insert_missing('npt600_20000.data', missed_lines)
os.system('mpirun -n 20 lmp -i input_npt_1atm.lammps')
shutil.copy(r'npt_1_20000.data', r'./../../Production/Prod_20000/npt_1_20000.data')

os.chdir(r'./../npt1atm_14000')
insert_missing('npt600_14000.data', missed_lines)
os.system('mpirun -n 20 lmp -i input_npt_1atm.lammps')
shutil.copy(r'npt_1_14000.data', r'./../../Production/Prod_14000/npt_1_14000.data')

os.chdir(r'./../npt1atm_8000')
insert_missing('npt600_8000.data', missed_lines)
os.system('mpirun -n 20 lmp -i input_npt_1atm.lammps')
shutil.copy(r'npt_1_8000.data', r'./../../Production/Prod_8000/npt_1_8000.data')

# Production

os.chdir(r'./../../Production/Prod_8000')
insert_missing('npt_1_8000.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_prod.lammps')
shutil.copy(r'8000_1.data', r'./../../Cooling/Cool_8000_1/8000_1.data')
shutil.copy(r'8000_2.data', r'./../../Cooling/Cool_8000_2/8000_2.data')
shutil.copy(r'8000_3.data', r'./../../Cooling/Cool_8000_3/8000_3.data')
shutil.copy(r'8000_4.data', r'./../../Cooling/Cool_8000_4/8000_4.data')
shutil.copy(r'8000_5.data', r'./../../Cooling/Cool_8000_5/8000_5.data')

os.chdir(r'./../Prod_14000')
insert_missing('npt_1_14000.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_prod.lammps')
shutil.copy(r'14000_1.data', r'./../../Cooling/Cool_14000_1/14000_1.data')
shutil.copy(r'14000_2.data', r'./../../Cooling/Cool_14000_2/14000_2.data')
shutil.copy(r'14000_3.data', r'./../../Cooling/Cool_14000_3/14000_3.data')
shutil.copy(r'14000_4.data', r'./../../Cooling/Cool_14000_4/14000_4.data')
shutil.copy(r'14000_5.data', r'./../../Cooling/Cool_14000_5/14000_5.data')

os.chdir(r'./../Prod_20000')
insert_missing('npt_1_20000.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_prod.lammps')
shutil.copy(r'20000_1.data', r'./../../Cooling/Cool_20000_1/20000_1.data')
shutil.copy(r'20000_2.data', r'./../../Cooling/Cool_20000_2/20000_2.data')
shutil.copy(r'20000_3.data', r'./../../Cooling/Cool_20000_3/20000_3.data')
shutil.copy(r'20000_4.data', r'./../../Cooling/Cool_20000_4/20000_4.data')
shutil.copy(r'20000_5.data', r'./../../Cooling/Cool_20000_5/20000_5.data')

os.chdir(r'./../Prod_26000')
insert_missing('npt_1_26000.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_prod.lammps')
shutil.copy(r'26000_1.data', r'./../../Cooling/Cool_26000_1/26000_1.data')
shutil.copy(r'26000_2.data', r'./../../Cooling/Cool_26000_2/26000_2.data')
shutil.copy(r'26000_3.data', r'./../../Cooling/Cool_26000_3/26000_3.data')
shutil.copy(r'26000_4.data', r'./../../Cooling/Cool_26000_4/26000_4.data')
shutil.copy(r'26000_5.data', r'./../../Cooling/Cool_26000_5/26000_5.data')

os.chdir(r'./../Prod_32000')
insert_missing('npt_1_32000.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_prod.lammps')
shutil.copy(r'32000_1.data', r'./../../Cooling/Cool_32000_1/32000_1.data')
shutil.copy(r'32000_2.data', r'./../../Cooling/Cool_32000_2/32000_2.data')
shutil.copy(r'32000_3.data', r'./../../Cooling/Cool_32000_3/32000_3.data')
shutil.copy(r'32000_4.data', r'./../../Cooling/Cool_32000_4/32000_4.data')
shutil.copy(r'32000_5.data', r'./../../Cooling/Cool_32000_5/32000_5.data')

os.chdir(r'./../Prod_38000')
insert_missing('npt_1_38000.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_prod.lammps')
shutil.copy(r'38000_1.data', r'./../../Cooling/Cool_38000_1/38000_1.data')
shutil.copy(r'38000_2.data', r'./../../Cooling/Cool_38000_2/38000_2.data')
shutil.copy(r'38000_3.data', r'./../../Cooling/Cool_38000_3/38000_3.data')
shutil.copy(r'38000_4.data', r'./../../Cooling/Cool_38000_4/38000_4.data')
shutil.copy(r'38000_5.data', r'./../../Cooling/Cool_38000_5/38000_5.data')

os.chdir(r'./../Prod_44000')
insert_missing('npt_1_44000.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_prod.lammps')
shutil.copy(r'44000_1.data', r'./../../Cooling/Cool_44000_1/44000_1.data')
shutil.copy(r'44000_2.data', r'./../../Cooling/Cool_44000_2/44000_2.data')
shutil.copy(r'44000_3.data', r'./../../Cooling/Cool_44000_3/44000_3.data')
shutil.copy(r'44000_4.data', r'./../../Cooling/Cool_44000_4/44000_4.data')
shutil.copy(r'44000_5.data', r'./../../Cooling/Cool_44000_5/44000_5.data')

os.chdir(r'./../Prod_50000')
insert_missing('npt_1_50000.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_prod.lammps')
shutil.copy(r'50000_1.data', r'./../../Cooling/Cool_50000_1/50000_1.data')
shutil.copy(r'50000_2.data', r'./../../Cooling/Cool_50000_2/50000_2.data')
shutil.copy(r'50000_3.data', r'./../../Cooling/Cool_50000_3/50000_3.data')
shutil.copy(r'50000_4.data', r'./../../Cooling/Cool_50000_4/50000_4.data')
shutil.copy(r'50000_5.data', r'./../../Cooling/Cool_50000_5/50000_5.data')

# run cooling

os.chdir(r'./../../Cooling/Cool_8000_1')
insert_missing('8000_1.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_8000_2')
insert_missing('8000_2.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_8000_3')
insert_missing('8000_3.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_8000_4')
insert_missing('8000_4.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_8000_5')
insert_missing('8000_5.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_14000_1')
insert_missing('14000_1.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_14000_2')
insert_missing('14000_2.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_14000_3')
insert_missing('14000_3.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_14000_4')
insert_missing('14000_4.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_14000_5')
insert_missing('14000_5.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_20000_1')
insert_missing('20000_1.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_20000_2')
insert_missing('20000_2.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_20000_3')
insert_missing('20000_3.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_20000_4')
insert_missing('20000_4.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_20000_5')
insert_missing('20000_5.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_26000_1')
insert_missing('26000_1.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_26000_2')
insert_missing('26000_2.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_26000_3')
insert_missing('26000_3.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_26000_4')
insert_missing('26000_4.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_26000_5')
insert_missing('26000_5.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_32000_1')
insert_missing('32000_1.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_32000_2')
insert_missing('32000_2.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_32000_3')
insert_missing('32000_3.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_32000_4')
insert_missing('32000_4.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_32000_5')
insert_missing('32000_5.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_38000_1')
insert_missing('38000_1.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_38000_2')
insert_missing('38000_2.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_38000_3')
insert_missing('38000_3.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_38000_4')
insert_missing('38000_4.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_38000_5')
insert_missing('38000_5.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_44000_1')
insert_missing('44000_1.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_44000_2')
insert_missing('44000_2.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_44000_3')
insert_missing('44000_3.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_44000_4')
insert_missing('44000_4.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_44000_5')
insert_missing('44000_5.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_50000_1')
insert_missing('50000_1.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_50000_2')
insert_missing('50000_2.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_50000_3')
insert_missing('50000_3.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_50000_4')
insert_missing('50000_4.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

os.chdir(r'./../Cool_50000_5')
insert_missing('50000_5.data', missed_lines)
os.system('mpirun -n 128 lmp -i input_cooling.lammps')

