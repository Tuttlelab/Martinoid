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