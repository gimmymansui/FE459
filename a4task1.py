# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:02:44 2023

@author: JiaLin Sui suijs@bu.edu 

FE459 Computational Finance - a4task1
"""
from operator import add

def print_matrix(m, label = ' '):
    """prints matrix"""
    if label == ' ':
        print('[',end='')
        for i in range(len(m)):
            print(m[i])
    else: 
        print(label, " = ")
        print('[',end='')
        for i in range(len(m)):
            print(m[i])

def zeros(n, m = 0):
    if m == 0:
        m = n
    """creates matrix[n][m] of zeros """ 
    mat = [[0 for col in range(m)] for row in range (n)];
    return mat

def identity_matrix(n):
    """creates the square identity matrix of size n """
    mat = zeros(n,n)
    for i  in range(len(mat[0])):
        mat[i][i] = 1.00
    return mat

def transpose(M):
    """transposes matrix"""
    result = isinstance(M[0], list) #1d lists dont compute the same way so in the event that A[0] is not iterable, the function goes to assuming its 1
    if result:
        mat = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    else:
        mat = [[row for col in range(1)] for row in M]
    return mat

def swap_rows(M, src, dest):
    """swaps rows from source to destination"""
    temp = M[src]
    M[src] = M[dest]
    M[dest] = temp
    
    return M

def mult_row_scalar(M, row, scalar):
    """scalar multiply for a targeted row"""
    for i in range(len(M[row])):
        M[row][i] *= scalar
        
    return M

def add_row_into(M, src, dest):
    """ adds row to target location"""
    temp = []
    for i in range(len(M[src])):
        temp.append(M[src][i]+ M[dest][i])
    M[dest] = temp
    
    return M