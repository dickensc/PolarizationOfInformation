#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 07:28:09 2017

@author: charlesdickens
"""

"""
function:    LCS(), Longest Common Subsequence 

parameters:  Arr1:    Array 1
             Arr2:    Array 2
    
description: Given the two string arrays Arr1 and Arr2 LCS will return a list of the 
             longest common subsequences. To solve this problem we use 
             dynamic programming and memoization. 
"""
def LCS(Arr1, Arr2):
    
    #store lengths of Arr1 and Arr2
    n = len(Arr1)
    m = len(Arr2)
    
    #build n + 1 x m + 1 memoization table initializing every entry to 0
    MemTbl = [ [0 for x in range(m + 1)] for y in range(n + 1) ]
    
    #fill in memoization table bottom up, i.e., starting at 1st row and 
    #moving from 1st, to 2nd, ..., to (m+1)th column then to 2nd row and so on
    for i in xrange(n + 1):
        for j in xrange(m + 1):
            if i == 0 or j == 0:
                continue
            elif Arr1[i - 1] == Arr2[j - 1]:
                MemTbl[i][j] = (MemTbl[i-1][j-1] + 1)
            else:
                MemTbl[i][j] = max(MemTbl[i-1][j], MemTbl[i][j-1])
                
    #MemTbl[n][m] is the length of the longest common subsequence
    
    #lcs will store all the longest common subsequences
    #lcs = ['']
    
    #call recursive helper function
    #retrieveLCS(lcs, 0, MemTbl, n, m, Arr1, Arr2)
    
    return MemTbl[n][m]
    

"""
function:    retrieveLCS()

parameters:  lcs   :    list of longest common subsequences
             path  :    counts which path we are on while traversing MemTbl
             MemTbl:    Memoization table from LCS function
             k     :    Row Index
             l     :    Column Index
             Arr1    :    Array 1
             Arr2    :    Array 2
    
description: Given the two string arrays Arr1 and Arr2 LCS will return a list of the 
             longest common subsequences. To solve this problem we trace back the
             memoization table created in the LCS function.
"""
def retrieveLCS(lcs, path, MemTbl, k, l, Arr1, Arr2):
    
    #base case: at the first character of longest common subsequence
    if MemTbl[k][l] == 0:
        return
    #else if Arr1[k] = Arr2[l] append to lcs and recursively call function
    elif MemTbl[k][l] > MemTbl[k-1][l] and MemTbl[k][l] > MemTbl[k][l-1]:
        lcs[path] = Arr1[k-1] + " " + lcs[path]
        retrieveLCS(lcs, path, MemTbl, k-1, l-1, Arr1, Arr2)
    #follow diagonal path if there is one
    elif MemTbl[k][l] == MemTbl[k-1][l-1]:
        retrieveLCS(lcs, path, MemTbl, k-1, l-1, Arr1, Arr2)
    #else if there are 2 paths to take, add to the number of paths and
    #recursively follow both
    elif MemTbl[k][l] == MemTbl[k-1][l] and MemTbl[k][l] == MemTbl[k][l-1]:
        lcs.append(lcs[path])
        
        path = path + 1
        
        retrieveLCS(lcs, path, MemTbl, k, l-1, Arr1, Arr2)
        
        retrieveLCS(lcs, path - 1, MemTbl, k-1, l, Arr1, Arr2)
    #else if there is only 1 way to go follow that direction
    else:
        if MemTbl[k][l] == MemTbl[k-1][l]:
            retrieveLCS(lcs, path, MemTbl, k-1, l, Arr1, Arr2)
        if MemTbl[k][l] == MemTbl[k][l-1]:
            retrieveLCS(lcs, path, MemTbl, k, l-1, Arr1, Arr2)

        
        
        
    
    

    