# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:21:10 2021

@author: rudolf
"""

import pandas, os, copy
import numpy as np

def cdel(files):
    if type(files) != list:
        files = [files]
    for file in files:
        if os.path.exists(file):
            os.remove(file)

def readin(fname):
    f = open(fname, 'r', errors="ignore")
    content = f.read()
    return content

def replace_in_file2(fname, original, new):
    content = readin(fname)
    content = content.replace(original, new)
    with open(fname, 'w') as outfile:
        outfile.write(content)

charges = {"Na":0.0, "Qa":1.0, "Qd":-1.0, "N0":0.0,
           "P1":0.0, "P2":0.0, "P3":0.0, "P4":0.0, "P5":0.0,
           "SP1":0.0, "SP2":0.0, "SP3":0.0, "SP4":0.0, "SP5":0.0,
           "SC4":0.0, "SC5":0.0, 
           "C1":0.0, "C2":0.0, "C3":0.0, "C4":0.0, "C5":0.0}


SideChainCoords = {"AP00": np.array([[0.0, 0.2, 0.0]]),
                   "K000": np.array([[0.0, 0.15, 0.0],
                                     [0.0, 0.3, 0.0]]),
                   "Y000": np.array([[0.0, 0.2, 0.0],
                                     [0.2, 0.4, 0.0],
                                     [-0.2, 0.4, 0.0]]),
                   "FENR": np.array([[0.0, 0.2, 0.0],
                                     [-0.2, 0.2, 0.0],
                                     [-0.4, 0.3, 0.0],
                                    [-0.2, 0.4, 0.0],
                                    [0.0, 0.4, 0.0],
                                    [0.2, 0.3, 0.0]]),
                   "W000": np.array([[0.0, 0.2, 0.0],
                                     [0.2, 0.3, 0.0],
                                     [-0.2, 0.3, 0.0],
                                    [0.0, 0.4, 0.0]]),}

SideChainCoords["M000"] = copy.copy(SideChainCoords["AP00"])
SideChainCoords["M0A0"] = copy.copy(SideChainCoords["AP00"])
SideChainCoords["Q000"] = copy.copy(SideChainCoords["AP00"])
SideChainCoords["N000"] = copy.copy(SideChainCoords["AP00"])
SideChainCoords["E000"] = copy.copy(SideChainCoords["AP00"])
SideChainCoords["D000"] = copy.copy(SideChainCoords["AP00"])
SideChainCoords["S000"] = copy.copy(SideChainCoords["AP00"])
SideChainCoords["T000"] = copy.copy(SideChainCoords["AP00"])
SideChainCoords["SE00"] = copy.copy(SideChainCoords["AP00"])
SideChainCoords["FN00"] = copy.copy(SideChainCoords["Y000"])
SideChainCoords["F000"] = copy.copy(SideChainCoords["Y000"])
SideChainCoords["FE00"] = copy.copy(SideChainCoords["Y000"])
SideChainCoords["FE00"] = copy.copy(SideChainCoords["Y000"])
SideChainCoords["FP00"] = copy.copy(SideChainCoords["Y000"])
SideChainCoords["FER0"] = copy.copy(SideChainCoords["Y000"])
SideChainCoords["FES0"] = copy.copy(SideChainCoords["Y000"])
SideChainCoords["FEC3"] = copy.copy(SideChainCoords["Y000"])
SideChainCoords["FEC3"] = copy.copy(SideChainCoords["Y000"])
SideChainCoords["FENS"] = copy.copy(SideChainCoords["FENR"])
SideChainCoords["FMN0"] = copy.copy(SideChainCoords["FENR"])
SideChainCoords["WE00"] = copy.copy(SideChainCoords["W000"])
SideChainCoords["KE00"] = copy.copy(SideChainCoords["AP00"])
SideChainCoords["R000"] = copy.copy(SideChainCoords["K000"])
                                     
#print(SideChainCoords)


PseudoAtoms = {}



res_db = {"A000": [pandas.DataFrame([["BB", "Na"]], columns=["i", "type"]),
                   pandas.DataFrame(columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "AP00": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "C1"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "M000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "C5"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "M0A0": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "C5"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "Y000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "SC4"],
                                     ["SC2", "SC4"],
                                     ["SC3", "SP1"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500],
                                     [1, 2, 0.40, 2500],
                                     [2, 3, 0.40, 2500],
                                     [3, 1, 0.40, 2500]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "F000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "SC4"],
                                     ["SC2", "SC4"],
                                     ["SC3", "SC4"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500],
                                     [1, 2, 0.40, 2500],
                                     [2, 3, 0.40, 2500],
                                     [3, 1, 0.40, 2500]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "FEC3": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "SC4"],
                                     ["SC2", "SC4"],
                                     ["SC3", "SC5"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500],
                                     [1, 2, 0.40, 2500],
                                     [2, 3, 0.40, 2500],
                                     [3, 1, 0.40, 2500]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "FENR": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "SC4"],
                                     ["SC2", "SC4"],
                                     ["SC3", "SC4"],
                                     ["SC4", "SC4"],
                                     ["SC5", "SC4"],
                                     ["SC6", "SC4"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500],
                                     [1, 2, 0.40, 2500],
                                     [1, 6, 0.40, 2500],
                                     [2, 3, 0.40, 2500],
                                     [3, 4, 0.40, 2500],
                                     [4, 5, 0.40, 2500],
                                     [4, 6, 0.40, 2500],
                                     [5, 6, 0.40, 2500]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "W000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "SC4"],
                                     ["SC2", "SP1"],
                                     ["SC3", "SC4"],
                                     ["SC4", "SC4"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500],
                                     [1, 2, 0.40, 2500],
                                     [1, 3, 0.40, 2500],
                                     [2, 4, 0.40, 2500],
                                     [3, 4, 0.40, 2500]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "Q000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "P5"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.32, 5000]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "N000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "P4"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 5000]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "E000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "Qa"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 5000]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "D000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "Qa"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 7500]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "S000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "P1"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.25, 7500]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "T000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "P1"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.25, "Constraint"]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "SE00": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "P2"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.26, 5000]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "KE00": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "Qd"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.31, 5000]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "K000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "C3"],
                                     ["SC2", "Qd"],], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.31, "Constraint"],
                                     [1, 2, 0.33, 5000],], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "R000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "N0"],
                                     ["SC2", "Qd"],], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.31, "Constraint"],
                                     [1, 2, 0.33, 5000],], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],}



#Set the angles
res_db["AP00"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["M000"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["M0A0"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["Y000"][2].loc["BB-BB-SC1"] = [1,150,25]
res_db["F000"][2].loc["BB-BB-SC1"] = [1,150,25]
res_db["FEC3"][2].loc["BB-BB-SC1"] = [1,150,25]
res_db["FENR"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["W000"][2].loc["BB-BB-SC1"] = [1,150,25]
res_db["Q000"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["N000"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["E000"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["D000"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["S000"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["T000"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["SE00"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["KE00"][2].loc["BB-BB-SC1"] = [1,100,25]
res_db["K000"][2].loc["BB-BB-SC1"] = [1,180,25]
res_db["R000"][2].loc["BB-BB-SC1"] = [1,180,25]

# Set the dihedrals
res_db["Y000"][3].loc["BB-BB-SC1-SC2"] = [-1, 0, 1, 2, 0, 50]
res_db["F000"][3].loc["BB-BB-SC1-SC2"] = [-1, 0, 1, 2, 0, 50]
res_db["FEC3"][3].loc["BB-BB-SC1-SC2"] = [-1, 0, 1, 2, 0, 50]
res_db["FENR"][3].loc["BB-BB-SC1-SC2"] = [-1, 0, 1, 2, 0, 50]
res_db["FENR"][3].loc["SC1-SC2-SC3-SC4"] = [1, 2, 3, 4, 0, 200]
res_db["FENR"][3].loc["SC2-SC3-SC4-SC5"] = [2, 3, 4, 5, 0, 200]
res_db["FENR"][3].loc["SC3-SC4-SC5-SC6"] = [3, 4, 5, 6, 0, 200]
res_db["FENR"][3].loc["SC4-SC5-SC6-SC1"] = [4, 5, 6, 1, 0, 200]
res_db["FENR"][3].loc["SC5-SC6-SC1-SC2"] = [5, 6, 1, 2, 0, 200]
res_db["FENR"][3].loc["SC6-SC1-SC2-SC3"] = [6, 1, 2, 3, 0, 200]
res_db["W000"][3].loc["BB-BB-SC1-SC2"] = [-1, 0, 1, 2, 0, 50]
res_db["W000"][3].loc["SC1-SC2-SC3-SC4"] = [1, 2, 3, 4, 0, 200]
res_db["W000"][3].loc["SC2-SC3-SC4-SC1"] = [2, 3, 4, 1, 0, 200]
res_db["W000"][3].loc["SC3-SC4-SC1-SC2"] = [3, 4, 1, 2, 0, 200]
res_db["W000"][3].loc["SC4-SC1-SC2-SC3"] = [4, 1, 2, 3, 0, 200]


# Copy the same ones
#I don't have the necessary info to put in FE00 or FP00 or FER0 / make them any different
res_db["FN00"] = res_db["F000"]
res_db["FE00"] = res_db["F000"]
res_db["FP00"] = res_db["F000"]
res_db["FER0"] = res_db["F000"]
res_db["FES0"] = res_db["F000"]
res_db["FENS"] = res_db["FENR"]
res_db["FMN0"] = res_db["FENR"]
res_db["WE00"] = res_db["W000"]