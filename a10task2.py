# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:04:20 2023

@author: suij2
"""
import numpy as np
import pandas as pd

def calc_portfolio_return(e, w):
    ''''calculate portfolio returns'''
    return float(np.dot(e, w.T))

def calc_portfolio_stdev(v, w):
    '''calculates portfolio std dev'''
    A = np.sqrt(np.dot(w, np.dot(v, w.T)))
    return A

def calc_global_min_variance_portfolio(v):

    n_assets = v.shape[0]
    ones = np.matrix(np.ones(n_assets)).reshape(1, -1)
    v_inv = np.linalg.inv(v)
    w = np.dot(ones, v_inv) / np.dot(ones, np.dot(v_inv, ones.T))
    return w

def calc_min_variance_portfolio(e, v, r):
    '''calculates local min variance portfolio'''
    n = e.size
    ones = np.ones((1, n))
    v_inv = np.linalg.inv(v)
    a = np.dot(np.dot(ones, v_inv), e.T).item()
    b = np.dot(np.dot(e, v_inv), e.T).item()
    c = np.dot(np.dot(ones, v_inv), ones.T).item()
    matA = np.matrix([[b,a],[a,c]])
    d = np.linalg.det(matA)
    temp = (b*ones - a*e)*v_inv
    g = np.dot(1/d,temp)
    temp2 = (c*e-a*ones)*v_inv
    h = np.dot(1/d,temp2)
    w_p =  g + h*r
    return w_p[0]

def calc_efficient_portfolios_stdev(e, v, rs):
    sigmas = np.zeros(len(rs))
    for i in range(len(rs)):
        r = rs[i]
        w = calc_min_variance_portfolio(e, v, r)
        sigma = calc_portfolio_stdev(v, w).item()
        sigmas[i] = sigma
        print(f"r = {r:.4f}, sigma = {sigma:.4f} w = {w}")
    return sigmas 


def get_stock_prices_from_csv_files(symbols):
    '''process each stock file using the a char vector of ticker names and return the stock prices'''
    for i, symbol in enumerate(symbols):
        filename = f"{symbol}.csv"
        df = pd.read_csv(filename)
        df = df[['Date', 'Adj Close']]
        df.set_index('Date', inplace=True)
        df.index = pd.to_datetime(df.index)
        df.columns = [symbol]
        if i == 0:
            result = df
        # otherwise, join the new data with the existing data using the stock symbol as the key
        else:
            result = result.join(df, how='outer')

    result = result.resample('M').ffill()

    return result



def get_stock_returns_from_csv_files(symbols):
    '''process each stock file using the a char vector of ticker names and return the stock returns'''
    for i, symbol in enumerate(symbols):
        filename = f"{symbol}.csv"
        df = pd.read_csv(filename)
        df = df[['Date', 'Adj Close']]
        df.set_index('Date', inplace=True)
        df.index = pd.to_datetime(df.index)
        df.columns = [symbol]
        returns = returns = df.pct_change().rename(columns={'Adj Close': symbol})
        if i == 0:
            result = returns
        # otherwise, join the new data with the existing data using the stock symbol as the key
        else:
            result = result.join(returns, how='outer')

    result = result.resample('M').ffill()

    return result


def get_covariance_matrix(returns: pd.DataFrame) -> pd.DataFrame:
    '''get covariance of matrices'''
    mean_returns = returns.mean()


    cov = {}
    for symbol in returns.columns:
        cov[symbol] = returns.cov()[symbol]

        for other_symbol in returns.columns:
            cov[symbol][other_symbol] -= mean_returns[symbol] * mean_returns[other_symbol]
        cov[symbol][symbol] = returns[symbol].var()

    cov = pd.DataFrame.from_dict(cov, orient='index')

    return cov



