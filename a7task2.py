# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:04:15 2023

@author: suij2
"""

from a7task1 import *
import math

from decimal import Decimal, getcontext

def build_euro_call_value_tree(s, x, sigma, rf, div, T, n):
    '''Builds binomial tree of option values given s, x, sigma, rf, div, T, n'''
    h = T/n
    p = get_risk_neutral_probability(sigma, rf, div, h)
    u = get_binomial_factors(sigma, rf, div, h)[0]
    d = get_binomial_factors(sigma, rf, div, h)[1]
    stock_tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)
    option_tree = zeros(n+1)
    for j in range(len(option_tree[0])):
        option_tree[j][n] = max(0, stock_tree[j][n] - x)
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            option_tree[j][i] = math.exp(-rf*h)*(p*option_tree[j][i+1] + (1-p)*option_tree[j+1][i+1])
    return option_tree

"""
def build_euro_call_value_tree(s, x, sigma, rf, div, T, n):
    '''Builds a binomial call option pricing tree using the underlying stock tree'''
    h = T/n
    tuple = get_binomial_factors(sigma, rf, div, h)
    p = get_risk_neutral_probability(sigma, rf, div, h)
    u = tuple[0]
    d = tuple[1]
    stock_tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)
    option_tree = zeros(n+1)
    for i in range(n, -1, -1):
        for j in range(i + 1):
            if i == n:
                option_tree[j][i] = max(0, stock_tree[j][i] - x)
            else:
                option_tree[j][i] = (1 / (1 + rf*h)) * (p * option_tree[j][i+1] + (1 - p) * option_tree[j+1][i+1])
    
    return option_tree

"""

def euro_call_value(s, x, sigma, rf, div, T, n):
    '''Calculates the value of a European call option using the binomial pricing model'''
    option_tree = build_euro_call_value_tree(s, x, sigma, rf, div, T, n)
    return option_tree[0][0]

def build_euro_put_value_tree(s, x, sigma, rf, div, T, n):
    '''Builds a binomial put option pricing tree using the underlying stock tree'''
    h = T/n
    p = get_risk_neutral_probability(sigma, rf, div, h)
    u = get_binomial_factors(sigma, rf, div, h)[0]
    d = get_binomial_factors(sigma, rf, div, h)[1]
    stock_tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)
    option_tree = zeros(n+1)
    for j in range(len(option_tree[0])):
        option_tree[j][n] = max(0, x - stock_tree[j][n])
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            option_tree[j][i] = math.exp(-rf*h)*(p*option_tree[j][i+1] + (1-p)*option_tree[j+1][i+1])
    return option_tree

def euro_put_value(s, x, sigma, rf, div, T, n):
    '''Calculates the value of a European put option using the binomial pricing model'''
    option_tree = build_euro_put_value_tree(s, x, sigma, rf, div, T, n)
    return option_tree[0][0]

def build_amer_put_value_tree(s, x, sigma, rf, div, T, n):
    '''Builds binomial tree for American put option given s, x, sigma, rf, div, T, n'''
    h = T/n
    p = get_risk_neutral_probability(sigma, rf, div, h)
    u = get_binomial_factors(sigma, rf, div, h)[0]
    d = get_binomial_factors(sigma, rf, div, h)[1]
    stock_tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)
    option_tree = zeros(n+1)
    for j in range(len(option_tree[0])):
        option_tree[j][n] = max(0, x - stock_tree[j][n])
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            exercise_value = max(0, x - stock_tree[j][i])
            continuation_value = math.exp(-rf*h)*(p*option_tree[j][i+1] + (1-p)*option_tree[j+1][i+1])
            option_tree[j][i] = max(exercise_value, continuation_value)
    return option_tree

def amer_put_value(s, x, sigma, rf, div, T, n):
    '''Calculates the value of a American put option using the binomial pricing model'''
    option_tree = build_amer_put_value_tree(s, x, sigma, rf, div, T, n)
    return option_tree[0][0]

"""
def build_amer_put_value_tree(s, x, sigma, rf, div, T, n):
    '''Builds a binomial American put option pricing tree using the underlying stock tree'''

    h = T/n
    tuple = get_binomial_factors(sigma, rf, div, h)
    p = get_risk_neutral_probability(sigma, rf, div, h)
    u = tuple[0]
    d = tuple[1]
    stock_tree = build_binomial_stock_price_tree(s, sigma, rf, div, T, n)
    option_tree = zeros(n+1)
    for j in range(n, -1, -1):
        for i in range(j + 1):
            if j == n:
                option_tree[i][j] = max(0, x - stock_tree[i][j])
            else:
                exercise_value = max(0, x - stock_tree[i][j])
                option_value = (1 / (1 + rf * h)) * (p * option_tree[i+1][j+1] + (1 - p) * option_tree[i][j+1])
                option_tree[i][j] = max(exercise_value, option_value)
    return option_tree
"""
