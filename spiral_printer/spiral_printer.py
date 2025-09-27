# -*- coding: utf-8 -*-
"""
Script Goal:
Given a NXM matrix, print its cell in spiral way.

Created on Tue May 29 10:39:50 2018
@author: Maya Galili
"""

import numpy as np

def spiralPrint(a) :
    
#   init vars
    N,M = a.shape  
    mat_sz = N*M
    i = 0 
    j = 0
    n=0
    m=0
    result = []
    
    while (mat_sz > 0):
        
#        go right
        for j in range(m,M) :
            result.append(a[i][j])
            mat_sz = mat_sz - 1;
        n=n+1

#        go down  
        if (mat_sz > 0):
            for i in range(n,N) :
                result.append(a[i][j])
                mat_sz = mat_sz - 1;    
            M=M-1   
        
#        go left
        if (mat_sz > 0):           
            for j in range(M-1,m-1,-1) :  
                result.append(a[i][j])
                mat_sz = mat_sz - 1           
            N=N-1 

#        go up     
        if (mat_sz > 0):            
            for i in range(N-1,n-1,-1) :         
                result.append(a[i][j])
                mat_sz = mat_sz - 1;   
            m=m+1
    
    return result


 
# Driver Code
a = np.array([
      [1, 2, 3, 4, 5, 6],
      [7, 8, 9, 10, 11, 12],
      [13, 14, 15, 16, 17, 18], 
      [19, 20, 21, 22, 23, 24]
      ])
       
result = spiralPrint(a)
print(" ".join(map(str, result)))