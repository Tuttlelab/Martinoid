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

charges = {"Na":0.0, "Qa":1.0, "Qd":-1.0, "N0":0.0, "Nda": 0.0,
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


beads = pandas.DataFrame(columns=["i", "type", "residue", "resname"])
bonds = pandas.DataFrame(columns=["i", "j", "L", "k"], dtype=np.float64)
constraints = pandas.DataFrame(columns=["i", "j", "L"], dtype=np.float64)
angles = pandas.DataFrame(columns=["i", "j", "k", "angle", "FC", "comment"])
dihedrals = pandas.DataFrame(columns=["i", "j", "k", "h", "dihedral", "FC", "comment"])


side_chain_angles_template = pandas.DataFrame(columns=["j", "angle", "FC"])
side_chain_angles_template.loc["BB-BB-SC1"] = [0,0,0]

side_chain_dihedrals_template = pandas.DataFrame(columns=["i", "j", "k", "h", "dihedral", "FC"])
#side_chain_dihedrals_template.loc["BB-BB-SC1-SC2"] = [-2, -1, 0, 1, 0, 0]




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
                                     [1, 2, 0.40, "Constraint"],
                                     [2, 3, 0.40, "Constraint"],
                                     [3, 1, 0.40, "Constraint"]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "F000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "SC4"],
                                     ["SC2", "SC4"],
                                     ["SC3", "SC4"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500],
                                     [1, 2, 0.40, "Constraint"],
                                     [2, 3, 0.40, "Constraint"],
                                     [3, 1, 0.40, "Constraint"]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "FEC3": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "SC4"],
                                     ["SC2", "SC4"],
                                     ["SC3", "SC5"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500],
                                     [1, 2, 0.40, "Constraint"],
                                     [2, 3, 0.40, "Constraint"],
                                     [3, 1, 0.40, "Constraint"]], columns=["i", "j", "L", "k"]), 
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
                                     [1, 2, 0.40, "Constraint"],
                                     [1, 6, 0.40, "Constraint"],
                                     [2, 3, 0.40, "Constraint"],
                                     [3, 4, 0.40, "Constraint"],
                                     [4, 5, 0.40, "Constraint"],
                                     [4, 6, 0.40, "Constraint"],
                                     [5, 6, 0.40, "Constraint"]], columns=["i", "j", "L", "k"]), 
                   side_chain_angles_template.copy(), 
                   side_chain_dihedrals_template.copy()],
          "W000": [pandas.DataFrame([["BB", "Na"],
                                     ["SC1", "SC4"],
                                     ["SC2", "SP1"],
                                     ["SC3", "SC4"],
                                     ["SC4", "SC4"]], columns=["i", "type"]),
                   pandas.DataFrame([[0, 1, 0.40, 2500],
                                     [1, 2, 0.40, "Constraint"],
                                     [1, 3, 0.40, "Constraint"],
                                     [2, 4, 0.40, "Constraint"],
                                     [3, 4, 0.40, "Constraint"]], columns=["i", "j", "L", "k"]), 
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


TPB_quotes = ["Beauty is in the eye when you hold her.",
              "For the Gooder of Us All.",
              "Good things come to those at the gate.",
              "It's all water under the fridge.",
              "It's better to have a gun and need it than to not have a gun and not need it.",
              "Just remember Lahey, what comes around is all around.",
              "Lucy, I will make you have an eternity test if I have to.",
              "One man's garbage is another man person's good un-garbage.",
              "Do you have a search warranty?",
              "So, I'm going to do what the old man used to always say. 'Let guy bonds be guy bonds.",
              "The thing is, in order to stop breakin' the law is we gotta break the law just for a couple of minutes, and then we're gonna be done, retired.",
              "I'd like to make a request under the People's Freedom of Choices and Voices Act to be able to smoke an' swear in your courtroom.",
              "A lot of people might say I'm stupid; I don't know; I don't think I am. I'm probably smarter than that, I mean. This thing here's smarter than me, I guess, but it has a battery.",
              "When you're growing up, you gotta do illegal things once in a while, have a bit of fun and maturinate into a better person.",
              "I mean, nobody wants to admit they ate nine cans of ravioli, but I did. I'm ashamed of myself. The first can doesn't count, then you get to the second and third, fourth and fifth I think I burnt with the blowtorch, and then I just kept eatin'.",
              "I've met cats and dogs smarter than Trevor and Cory. In fact, most cats and dogs are smarter than Trevor and Cory.",
              "Thing with me is that... I am smart. And I'm self-smarted basically by myself.",
              "How can a peanut kill someone? It's not even a person.",
              "Why are you dressed up as a bumblebee for? And why do you look like Indianapolis Jones?",
              "Let the liquor do the thinkin', bud.",
              "Listen, I was unaware that I had an appointment with you fine people today. As it turns out I have another engagement: I plan to get drunk!",
              "Nice disguise, Bubs. You might be able to fool the FBI, but you can't fool the FB-Me.",
              "Randy, I've decided to lay off the food for a bit, and go on the booze.",
              "I'm sober enough to know what I'm doing, and drunk enough to really enjoy it.",
              "Boys, when the cops get here, tell them I won't resist. I'll be in my shed hyperventilating.",
              "Boys, my legs are all jankity-janked.",
              "My rhymes and mic are like a corporate merger, they go together like Randy's gut and cheeseburger.",
              "I spin more rhymes than a Lazy Susan, and I'm innocent until my guilt is proven."]