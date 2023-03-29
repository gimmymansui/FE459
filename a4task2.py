# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:02:44 2023

@author: JiaLin Sui suijs@bu.edu 

FE459 Computational Finance - a4task2
"""

from a4task1 import *

def mult_scalar(M, s):
    """ Returns matrix times some scalar"""
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] *= s
    
    return M

def sub_matrices(A,B):
    """ Returns element wise substraction A - B """
    assert len(A) == len(B) and len(A[0]) == len(B[0]), "Matrix Dimensions don't match"
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] -= B[i][j]
    
    return A

def add_matrices(A, B):
    """ Returns Element wise addition """
    assert len(A) == len(B) and len(A[0]) == len(B[0]), "Matrix Dimensions don't match"
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    
    return A
        
    
    
def element_product(A, B):
    """ Returns Element wise multiplication """
    resultA = isinstance(A[0], list) #1d lists dont compute the same way so in the event that A[0] is not iterable, the function goes to assuming its 1
    resultB = isinstance(B[0], list)
    
    if resultA and resultB:
        assert len(A) == len(B) and len(A[0]) == len(B[0]), "Matrix Dimensions don't match"
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] *= B[i][j]
    else:
        for i in range(len(A)):
            A[i] *= B[i]
    return A    

def dot_product(A, B):
    """ Matrix multiplication """
    resultA = isinstance(A[0], list) #1d lists dont compute the same way so in the event that A[0] is not iterable, the function goes to assuming its 1
    resultB = isinstance(B[0], list)
    
    if resultA and resultB:
        assert len(A) == len(B[0]), "incompatible dimensions: cannot dot-product (" + str(len(A)) + "," + str(len(A[0])) + ") with (" + str(len(B)) +  "," + str(len(B[0])) + ")"
        dotMatrix = zeros(len(A), len(B[0]))
        
        for i in range(len(A)):
             for j in range(len(B[0])):
                for k in range(len(B)):
                    dotMatrix[i][j] += A[i][k]*B[k][j]
    else:
        dotMatrix = 0
        for i in range(len(A)):
            dotMatrix += A[i]*B[i]
    return dotMatrix
        
            

    