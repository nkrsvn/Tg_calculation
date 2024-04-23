import os
import shutil
import glob

T_npt = '600'
nsteps_npt = '50000'

T_npt_1atm = '650'
nsteps_npt_1atm = '100000'

nsteps_prod = '20000'

T_cool = '150'
nsteps_cool = '500000'


os.mkdir('./Minimization')

shutil.move("./input_min.lammps", "./Minimization/input_min.lammps")
shutil.move("./initial.data", "./Minimization/initial.data")


os.mkdir('./nvt600')

shutil.move("./input_nvt600.lammps", "./nvt600/input_nvt600.lammps")


os.mkdir('./npt600')

PRESSURE_LIST = range(8000, 56000, 6000)
for p in PRESSURE_LIST:
    os.mkdir(f'./npt600/npt600_{p}')


for folder in glob.glob('./npt600/npt600*/'):
    print(folder)
    pressure = folder.split('_', maxsplit=1)[-1].strip('//')
    # print(pressure)

    with open('./input_npt_template.lammps', 'r') as inp:
        content = inp.read()
        content = content.replace('$TTTEEEMMMPPP', T_npt)
        content = content.replace('$RRRUUUNNN', nsteps_npt)
        content = content.replace('$PPPREESSS', pressure)

    with open(folder + 'input_npt600.lammps', 'w') as out:
        out.write(content)
      

os.mkdir('./npt1atm')
for p in PRESSURE_LIST:
    os.mkdir(f'./npt1atm/npt1atm_{p}')

for folder in glob.glob('./npt1atm/npt1atm*/'):
    print(folder)
    pressure = folder.split('_', maxsplit=1)[-1].strip('//')
    # print(pressure)

    with open('./input_1atm_template.lammps', 'r') as inp:
        content = inp.read()
        content = content.replace('$TTTEEEMMMPPP', T_npt_1atm)
        content = content.replace('$RRRUUUNNN', nsteps_npt_1atm)
        content = content.replace('$PPPREESSS', pressure)

    with open(folder + 'input_npt_1atm.lammps', 'w') as out:
        out.write(content)
        

os.mkdir('./Production') 
for p in PRESSURE_LIST:
    os.mkdir(f'./Production/Prod_{p}')
    
for folder in glob.glob('./Production/Prod*/'):
    print(folder)
    pressure = folder.split('_', maxsplit=1)[-1].strip('//')
    # print(pressure)

    with open('./input_production_template.lammps', 'r') as inp:
        content = inp.read()
        content = content.replace('$TTTEEEMMMPPP', T_npt_1atm)
        content = content.replace('$RRRUUUNNN', nsteps_prod)
        content = content.replace('$PPPREESSS', pressure)

    with open(folder + 'input_prod.lammps', 'w') as out:
        out.write(content)
        

os.mkdir('./Cooling')
for p in PRESSURE_LIST:
    for i in range(1, 6):
        os.mkdir(f'./Cooling/Cool_{p}_{i}')
 
 
for folder in glob.glob('./Cooling/Cool*/'):
    print(folder)
    cooling_data = folder.split('_', maxsplit=1)[-1].strip('//')
    # print(cooling_data)

    with open('./input_cooling_template.lammps', 'r') as inp:
        content = inp.read()
        content = content.replace('$TTTEEEMMMPPP1', T_npt_1atm)
        content = content.replace('$TTTEEEMMMPPP2', T_cool)
        content = content.replace('$RRRUUUNNN', nsteps_cool)
        content = content.replace('$COOLING_DATA', cooling_data)

    with open(folder + 'input_cooling.lammps', 'w') as out:
        out.write(content)
        
