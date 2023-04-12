# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:27:48 2023

@author: suij2
"""
import numpy as np

def bond_price(times, cashflows, rate):
    'calculates bond prices'
    pv_factors = 1 / (1 + rate)**np.array(times)
    present_values = np.array(cashflows) * pv_factors
    return np.sum(present_values)

def bootstrap(cashflows, prices):
    '''calculates the bootstrap '''
    CF = np.matrix(cashflows)
    P = np.matrix(prices).T
    return CF.I*P

def bond_duration(times, cashflows, rate):
    '''calculates bond duration'''
    C = np.array(cashflows)
    print(C)
    t = np.matrix(times)
    d = np.matrix([1 / (1 + rate)**t for t in times])
    B = bond_price(times, cashflows, rate)
    print(d.transpose())
    temp = (1/B)*t
    t2 = np.multiply(temp, C)
    return t2*d.T