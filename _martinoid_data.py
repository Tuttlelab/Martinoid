# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:21:10 2021

@author: rudolf
"""

import pandas, os, copy
import numpy as np
import io, sys

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

charges = {"Na":0.0, "Qa":-1.0, "Qd":1.0, "N0":0.0, "Nda": 0.0,
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

def ParseData(res, typ):
    beads, bonds, angles, dihedrals, BB = readin(f"Data/{res}.csv").split("#"*60 + "\n")
    if typ.lower() == "beads":
        return pandas.read_csv(io.StringIO(beads), index_col=0)
    elif typ.lower() == "bonds":
        return pandas.read_csv(io.StringIO(bonds), index_col=0)
    elif typ.lower() == "angles":
        return pandas.read_csv(io.StringIO(angles), index_col=0)
    elif typ.lower() == "dihedrals":
        return pandas.read_csv(io.StringIO(dihedrals), index_col=0)
    elif typ.upper() == "BB":
        l, k = BB.split("[")[1].split("]")[0].split(",")
        l = float(l)
        k = float(k)
        return l, k
    else:
        print("Unknown data type:", typ)
        sys.exit()

if __name__ == "__main__":
    if not os.path.exists("Data"):
        os.mkdir("Data")
    
    for key in ["D000"]:
        print(key)
        a="""
        #beads, bonds, angles, dihedrals
        csv_content = ""
        for i in range(4):
            csv_content = csv_content + res_db[key][i].to_csv()
            csv_content = csv_content + "#"*60
            csv_content = csv_content + "\n"
        with open(f"Data/{key}.csv", 'w') as csv_out:
            csv_out.write(csv_content)
        #a="""
        
        beads = ParseData(key, "beads")
        bonds = ParseData(key, "bonds")
        angles = ParseData(key, "angles")
        dihedrals = ParseData(key, "dihedrals")
        BB = ParseData(key, "BB")
        
        print(BB)