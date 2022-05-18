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
