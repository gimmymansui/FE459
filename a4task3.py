# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:02:44 2023

@author: JiaLin Sui suijs@bu.edu 

FE459 Computational Finance - a4task1
"""
from a2task1 import cashflow_times, bond_cashflows, discount_factors # bond functions
from a4task1 import *
from a4task2 import *

def portfolio_return(weights, returns):
    """returns portfolio returns given two matrices"""
    rW = isinstance(weights[0], list)
    rR = isinstance(returns[0], list)
    if rW and rR:
        flattenweights = [item for sublist in weights for item in sublist]#turns out code only works for flattened lists.
        flattenreturns = [item for sublist in returns for item in sublist]#
        mat = dot_product(flattenreturns, flattenweights)
    else:
        mat = dot_product(returns, weights)
    return mat

def bond_price(fv, c, n, m, ytm):
    """ returns bond price given fv maturity, c annual coupon, n years til maturity, m coupon payments per year, ytm annual yield to maturity"""
    df = discount_factors(ytm, n, m)
    cf = bond_cashflows(fv, c, n, m)
    val = dot_product(df, cf)
    return val
   
def bond_duration(fv, c, n, m, ytm):
    """ returns bond duration given fv maturity, c annual coupon, n years til maturity, m coupon payments per year, ytm annual yield to maturity"""
    cf = bond_cashflows(fv, c, n, m)
    df = discount_factors(ytm, n, m)
    T = cashflow_times(m, n)
    
    B = bond_price(fv, c, n, m, ytm)
    
    temp = element_product(cf, df)
    temp = dot_product(temp, T)
    temp = temp/(B*m)
    return temp


def bond_convexity(fv, c, n, m, r):
    df = discount_factors(r,n,m)
    cf = bond_cashflows(fv,c,n,m)
    B = bond_price(fv, c, n, m, r)
    print(B)
    temp = 0
    for i in range(1, len(cf)+1):
       temp += df[i-1]*cf[i-1]*i*(i+1)
    temp = temp/(1+r/m)**2
    convexity = (1/B)*temp*(1/((m)**2))
    return convexity

def main():
    print(bond_convexity(5000, 0.05, 3, 2, 0.05))
    print(bond_duration(5000, 0.05, 3, 2, 0.05))
if __name__ == "__main__":
    main()