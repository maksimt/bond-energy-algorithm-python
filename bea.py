# -*- coding: utf-8 -*-
import numpy as np

def BEA(S):
    """
    Order the columns of S to maximize the similarity between
        neighboring columns
    
    :param S - n*n similarity matrix
    """
    
    n = S.shape[0]
    O = [0] #order of the elements to maximize bond energy
    
    for i in range(1,n):
        
        n_pos = len(O)+1 #number of possible possitions to place i
        bondstr = np.zeros((n_pos,)) #value of placing i into each pos
        
        for p in range(n_pos):
            #p puts it between O[p-1] and O[p]
            
            #bond energy contributed from from O[p-1]---i
            if p>=1:
                bond_left = 2*S[O[p-1], i]
            else:
                bond_left = 0
            
            #bond energy contributed from i---O[p]
            if p<(n_pos-1):
                bond_right = 2*S[O[p], i]
            else:
                bond_right = 0
                
            #bond energy lost from O[p-1]---O[p]
            if p<(n_pos-1) and p>=1:
                bond_mid = 2*S[O[p-1], O[p]]
            else:
                bond_mid = 0
            
            bondstr[p] = bond_left + bond_right - bond_mid
        
        max_pos = np.argmax(bondstr)
        #_O = O[0:max_pos].append([i])
        #import pdb; pdb.set_trace()
        #O = np.vstack((_O,O[(max_pos-1):-1]))
        P=np.zeros((n_pos,))
        P[0:max_pos]=O[0:max_pos]
        P[max_pos]=i
        P[(max_pos+1):]=O[(max_pos):]
        O=P
    
    return O.astype(int)