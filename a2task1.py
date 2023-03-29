# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:00:59 2023

@author: JiaLin Sui suijs@bu.edu 

FE459 Computational Finance - a2task1

"""

def cashflow_times(m,n):
    """ computes cashflow times m*n, where n is years til maturity and m is coupon payments per year"""
    mat = [i+1 for i in range(m*n)];
    return mat

def discount_factors(r, n, m):
    """computer discount factors given rate r, n years til maturity and m coupon payments per year"""
    vec = [1] #default is 1 to start the calculation
    [(vec.append((vec[-1])/((1+(r/m))**(1)))) for i in range(m) for j in range(n)] # vec[-1] always gets the last element and sets that as the numerator
    vec.pop(0) # removing the first element
    return vec

def bond_cashflows(fv, c, n, m):
    vec = [(c/m)*fv for i in range((n*m)-1)]
    vec.append(((c/m)*fv)+fv)#adds final element
    return vec

