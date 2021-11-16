# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:22:22 2021

@author: avtei
"""
from _martinoid_data import *
import matplotlib.pyplot as plt
import numpy as np
import pandas, sys, time
from ase import Atoms
from ase.constraints import Hookean
from ase.calculators.lj import LennardJones
from ase.constraints import FixInternals
from ase.optimize import BFGS, FIRE
from ase.optimize.minimahopping import MinimaHopping
from ase.optimize.minimahopping import MHPlot
#import MDAnalysis as mda
import mdtraj
import warnings
warnings.filterwarnings("ignore")



np.random.seed(int(time.time()))
DEBUG = True
#seq = ["FENR", "A000", "Y000", "AP00", "M000", "M0A0", "FN00", "F000", "WE00"]
#seq = ["AP00", "Y000"]
seq = ["W000", "FENR", "FENR", "FENR", "FENR", "T000", "N000", "K000"]


SS = {"straight":{"Angle_deg":161, "Angle_FC":25, 
                  "Dihedral_deg":180, "Dihedral_FC":180 },
      "helix":{"Angle_deg":96, "Angle_FC":700, 
                  "Dihedral_deg":-120, "Dihedral_FC":400 }}
SS_type = "helix"
SS = SS[SS_type]

beads = pandas.DataFrame(columns=["i", "type", "residue", "resname"])
bonds = pandas.DataFrame(columns=["i", "j", "L", "k"], dtype=np.float64)
constraints = pandas.DataFrame(columns=["i", "j", "L"], dtype=np.float64)
angles = pandas.DataFrame(columns=["i", "j", "k", "angle", "FC", "comment"])
dihedrals = pandas.DataFrame(columns=["i", "j", "k", "h", "dihedral", "FC", "comment"])


side_chain_angles_template = pandas.DataFrame(columns=["j", "angle", "FC"])
side_chain_angles_template.loc["BB-BB-SC1"] = [0,0,0]

side_chain_dihedrals_template = pandas.DataFrame(columns=["i", "j", "k", "h", "dihedral", "FC"])
#side_chain_dihedrals_template.loc["BB-BB-SC1-SC2"] = [-2, -1, 0, 1, 0, 0]







residue_n = 0
for seq_i, s in enumerate(seq):
    # Append new beads
    last_i = beads.index.shape[0]
    new_beads = res_db[s][0].copy()
    new_index = np.array(new_beads.index) + last_i
    new_beads = new_beads.set_index(new_index)
    new_beads["residue"] = [residue_n]*new_beads.shape[0]
    new_beads["resname"] = [s]*new_beads.shape[0]
    beads = pandas.concat((beads, new_beads))
    
    #Make BB-BB bond
    if np.where(beads["i"]=="BB")[0].shape[0] >= 2:
        bond = np.where(beads["i"]=="BB")[0][-2:]
        bonds.loc[bonds.index.shape[0]] = [bond[0], bond[1], 0.35, 1250]

     #Make BB-BB-BB Angle
    if np.where(beads["i"]=="BB")[0].shape[0] >= 3:
        BB = np.where(beads["i"]=="BB")[0][-3:]
        angles.loc[angles.index.shape[0]] = [BB[0], BB[1], BB[2], SS["Angle_deg"], SS["Angle_FC"], "BB-BB-BB_"+SS_type]

        
    #Make BB-BB-BB-BB dihedral
    if np.where(beads["i"]=="BB")[0].shape[0] >= 4:
        BB = np.where(beads["i"]=="BB")[0][-4:]
        dihedrals.loc[angles.index.shape[0]] = [BB[0], BB[1], BB[2], BB[3], SS["Dihedral_deg"], SS["Dihedral_FC"], "BB-BB-BB-BB_"+SS_type]

    # make side-chain  bonds
    new_bonds = res_db[s][1].copy()
    #new_index = np.array(new_bonds.index) + bonds.index.max() + 1
    #new_bonds = new_bonds.set_index(new_index)
    new_bonds["i"] += last_i
    new_bonds["j"] += last_i
    for bond in new_bonds.index:
        isConstraint = str(new_bonds.loc[bond]["k"])
        if "constraint" in isConstraint.lower():
            constraints.loc[constraints.index.shape[0]] = new_bonds.loc[bond][list("ijL")]
        else:
            bonds.loc[bonds.index.shape[0]] = new_bonds.loc[bond]
        print(bond)
    #bonds = pandas.concat((bonds, new_bonds))
    
    # make BB - side-chain angles
    if beads[beads["i"] == "BB"].shape[0] >= 2 and s != "A000":
        new_angles = res_db[s][2].copy()
        new_angles["j"] += last_i
        BB_i, BB_j = np.where(beads["i"]=="BB")[0][-2:]
        SC1 = new_angles.loc["BB-BB-SC1"]["j"]
        Angle = new_angles.loc["BB-BB-SC1"]["angle"]
        FC = new_angles.loc["BB-BB-SC1"]["FC"]
        angles.loc[angles.index.shape[0]] = [BB_i, BB_j, SC1, Angle, FC, "BB-BB-SC1"]

        
    if res_db[s][3].shape[0] > 0:
        new_dihedrals = res_db[s][3].copy()
        #BB-BB-SC1-SC2
        if beads[beads["i"] == "BB"].shape[0] >= 2:
            new_dihedrals.at["BB-BB-SC1-SC2", "k"] += last_i
            new_dihedrals.at["BB-BB-SC1-SC2", "h"] += last_i
            BB_i, BB_j = np.where(beads["i"]=="BB")[0][-2:]
            SC1 = new_dihedrals.loc["BB-BB-SC1-SC2"]["k"]
            SC2 = new_dihedrals.loc["BB-BB-SC1-SC2"]["h"]
            dihedral = new_dihedrals.loc["BB-BB-SC1-SC2"]["dihedral"]
            FC = new_dihedrals.loc["BB-BB-SC1-SC2"]["FC"]
            comment = "BB-BB-SC1-SC2"
            dihedrals.loc[dihedrals.index.shape[0]] = [BB_i, BB_j, SC1, SC2, dihedral, FC, comment]
        new_dihedrals = new_dihedrals.drop(["BB-BB-SC1-SC2"])
        if new_dihedrals.shape[0] > 0:
            new_dihedrals[["i", "j", "k", "h"]] += last_i
            for row in new_dihedrals.iterrows():
                comment = row[0]
                index = np.random.random()
                while index in dihedrals.index:
                    index = np.random.random()
                dihedrals.loc[np.random.random()] = list(row[1].values) + [comment]
                #print(s, dihedrals.shape)

    residue_n += 1

    
bonds["i"] = bonds["i"].astype(np.uint64) 
bonds["j"] = bonds["j"].astype(np.uint64) 

print("Setting N-ter and C-ter to charged")

beads.at[beads[beads["i"] == "BB"].index[0], "type"] = "Qd"
beads.at[beads[beads["i"] == "BB"].index[-1], "type"] = "Nda"

    
print("Beads:")
print(beads)

print("Bonds:")
print(bonds)

print("Angles:")
print(angles)

print("Dihedrals:")
print(dihedrals)


print("\n\nWriting to Peptoid.gro")
# MDAnalysis
a="""
U = mda.Universe.empty(beads.shape[0],
                         n_residues=len(seq),
                         atom_resindex=beads["residue"].values,
                         residue_segindex=np.arange(len(seq)),
                         trajectory=True) # necessary for adding coordinates
gro = U.select_atoms("all")
coords = np.array([[0.0, 0.0, 0.0]])
coords_beads = ["BB"]
index = 1
sign = 1
while index <= beads["i"][1:].shape[0]:
    bead = beads.at[index, "i"]
    print("index:", index, beads.at[index, "resname"])
    new_pos = coords[np.where(np.array(coords_beads) == "BB")[0][-1]].copy()
    #new_pos[2] = np.random.random()/10
    if bead == "BB":
        new_pos[0] += 0.4
        new_pos[1] = 0
        coords = np.vstack((coords, new_pos))
        coords_beads.append("BB")
        if sign == 1:
            sign = -1
        else:
            sign = 1
    else:
        SC_i = int(beads.at[index, "i"][-1])-1
        #print("SideChainCoords:", SideChainCoords[beads.at[index, "resname"]], SC_i)
        new_side_chain = SideChainCoords[beads.at[index, "resname"]] + new_pos
        new_side_chain[:,1]*=sign
        coords = np.vstack((coords, new_side_chain[SC_i]))
        coords_beads += ["SC"] 
    index += 1
    

coords = np.array(coords)
coords *= 10
print(coords)    
gro.positions = coords
gro.write("Peptoid.gro")
#"""

#MDTraj
template = mdtraj.core.topology.Topology()

coords = np.array([[0.0, 0.0, 0.0]])
coords_beads = ["BB"]

index = 0
sign = 1

while index <= beads["i"][1:].shape[0]:
    bead = beads.at[index, "i"]
    print("index:", index, beads.at[index, "resname"])
    new_pos = coords[np.where(np.array(coords_beads) == "BB")[0][-1]].copy()
    new_pos[2] = np.random.random()/10
    if bead == "BB":
        current_chain = template.add_chain()
        res = template.add_residue("W1000", current_chain)
        template.add_atom("BB", mdtraj.core.element.carbon, res)
        new_pos[0] += 0.4
        new_pos[1] = 0
        if index > 0:
            coords = np.vstack((coords, new_pos))
            coords_beads.append("BB")
        if sign == 1:
            sign = -1
        else:
            sign = 1
    else:
        SC_i = int(beads.at[index, "i"][-1])-1
        template.add_atom(f"SC{SC_i}", mdtraj.core.element.carbon, res)
        #print("SideChainCoords:", SideChainCoords[beads.at[index, "resname"]], SC_i)
        new_side_chain = SideChainCoords[beads.at[index, "resname"]] + new_pos
        new_side_chain[:,1]*=sign
        coords = np.vstack((coords, new_side_chain[SC_i]))
        coords_beads += ["SC"] 
    index += 1

print(template.to_dataframe())
traj = mdtraj.Trajectory(coords, template)
traj.save_pdb("Peptoid.pdb")


#replace_in_file2("Peptoid.gro", "   0.00000   0.00000   0.00000", "  15.00000  15.00000  15.00000")
local_i = 0
if DEBUG:
    for i in range(beads.shape[0]):
        if beads.at[i, "i"] == "BB":
            c = "blue"
        else:
            c = "red"
            
        if beads.at[i, "i"] == "BB":
            local_i = 0
        
        plt.scatter([coords[i,0]], [coords[i,1]], color=c)
        plt.text(coords[i,0], coords[i,1], str(local_i))
        local_i += 1


print("Writing to Peptoid.itp")
itp = open("Peptoid.itp", 'w')
NAME = "Peptoid"
itp.write(f"""[ moleculetype ]
; Name         Exclusions
{NAME}   1\n
""")

itp.write("[ atoms ]\n")

for bead in beads.index:
    i = bead+1
    typ = beads.at[bead, "type"]
    B = beads.at[bead, "i"]
    resname = beads.at[bead, "resname"]
    resnum = beads.at[bead, "residue"] + 1
    charge = charges[typ]
    itp.write(f"\t{i}\t{typ}\t{resnum}\t{resname}\t{B}\t {i}  {charge} ; \n")

itp.write("\n[ bonds ]\n")

for bond in bonds.index:
    i = int(bonds.at[bond, "i"]+1)
    j = int(bonds.at[bond, "j"]+1)
    L = bonds.at[bond, "L"]
    k = bonds.at[bond, "k"]
    b1 = beads.at[i-1, "i"]
    b2 = beads.at[j-1, "i"]
    itp.write(f"\t{i}\t{j}\t1\t{L}\t\t{k} ; {b1}-{b2}\n")
    
itp.write("\n[ constraints ]\n")

for constraint in constraints.index:
    i = int(constraints.at[constraint, "i"]+1)
    j = int(constraints.at[constraint, "j"]+1)
    L = constraints.at[constraint, "L"]
    b1 = beads.at[i-1, "i"]
    b2 = beads.at[j-1, "i"]
    itp.write(f"\t{i}\t{j}\t1\t{L} ; {b1}-{b2}\n")

itp.write("\n[ angles ]\n")
for angle in angles.index:
    i = angles.at[angle, "i"]+1
    j = angles.at[angle, "j"]+1
    k = angles.at[angle, "k"]+1
    Angle = angles.at[angle, "angle"]
    FC = angles.at[angle, "FC"]
    comment = angles.at[angle, "comment"]
    itp.write(f"\t{i}\t{j}\t{k}\t2\t{Angle}\t{FC} ; {comment}\n")
    
    
if dihedrals.shape[0] > 0:
    itp.write("\n[ dihedrals ]\n")
    for dihe in dihedrals.index:
        i = dihedrals.at[dihe, "i"]+1
        j = dihedrals.at[dihe, "j"]+1
        k = dihedrals.at[dihe, "k"]+1
        h = dihedrals.at[dihe, "h"]+1
        dihedral = dihedrals.at[dihe, "dihedral"]
        FC = dihedrals.at[dihe, "FC"]
        comment = dihedrals.at[dihe, "comment"]
        itp.write(f"\t{i}\t{j}\t{k}\t{h}\t2\t{dihedral}\t{FC} ; {comment} \n")
    
itp.close()


print("\n")
print("rm *#*")
print("gmx editconf -f Peptoid.pdb -o Peptoid.gro -c -box 15 15 15")
print("rm *tpr*")
print("gmx grompp -f min.mdp -p topol.top -o Peptoid_min -c Peptoid.gro -maxwarn 1")
print("gmx mdrun -v  -ntomp 4 -deffnm Peptoid_min")
#print("gmx grompp -f Eq.mdp -p topol.top -o Peptoid_Eq -c Peptoid_min.gro -maxwarn 1")
#print("gmx mdrun -v  -ntomp 4 -deffnm Peptoid_Eq")
print("")


a="""
mol = Atoms(symbols=["C"]*beads.shape[0], positions=coords)

constraints = []
for bond in bonds.iterrows():
    bond = bond[1]
    c = Hookean(a1 = int(bond["i"]), a2 = int(bond["j"]), rt=0.94, k=2.)
    constraints.append(c)

angle_indices1 = [0, 1, 5]
#anglecombo_indices1 = [[, 180.0], [1, 5, 7, 180.0]]
#angle1 = [mol.get_angle(*angle_indices1), angle_indices1]
angle1 = [0, angle_indices1]

constraints.append( FixInternals(angles_deg = [angle1], epsilon=0.000000000000000000000001) )

mol.set_constraint(constraints)


mol.calc = LennardJones(sigma=6.0, epsilon=6.0)
#mol.calc = LennardJones()
cdel(["pep.pdb", "hop.log"])
mol.write("pep.pdb")
#opt = BFGS(mol)
#opt.run(fmax = 0.05, steps=1000)
#mol.write("pep.pdb", append=True)

hop = MinimaHopping(mol,
                    Ediff0=2.5,
                    T0=4000.)
hop(totalsteps=5)

"""