# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:27:16 2023

@author: suij2
"""

import math

def zeros(n, m = 0):
    if m == 0:
        m = n
    """creates matrix[n][m] of zeros """ 
    mat = [[0 for col in range(m)] for row in range (n)];
    return mat

def get_binomial_factors(sigma, rf, div, h):
    '''binomial factors given sigma, rf, div, h'''
    u = math.exp((rf-div)*h+sigma*math.sqrt(h))
    d = math.exp((rf-div)*h-sigma*math.sqrt(h))
    ans = (u, d)
    return ans
    
def get_risk_neutral_probability(sigma, rf, div, h):
    '''risk neutral probability given sigma, rf, div, h'''
    tuple = get_binomial_factors(sigma, rf, div, h)
    u = tuple[0]
    d = tuple[1]
    p = (math.exp((rf - div)*h)-d)/(u-d)
    return p 

def build_binomial_stock_price_tree(s, sigma, rf, div, T, n):
    '''Builds binomial tree given s, sigma, rf, div, T, n'''
    h = T/n
    tuple = get_binomial_factors(sigma, rf, div, h)
    u = tuple[0]
    d = tuple[1]
    tree = zeros(n+1)
    tree[0][0] = s
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j == 0:
                tree[j][i] = tree[j][i - 1] * u
            else:
                tree[j][i] = tree[j - 1][i - 1] * d
    return tree

def print_binomial_tree(tree):
    '''Prints binomial tree with 7 spaces left aligned'''
    max_digits_after_decimal = 2
    
    for i in range(len(tree)):
        for j in range(len(tree[0])):
            if j >= i :
                formatted_val = "{:<{}.{}f}".format(tree[i][j], 7, max_digits_after_decimal)
                print(formatted_val, end=' ')
            else:
                print(" "*(7), end=' ')
        print()