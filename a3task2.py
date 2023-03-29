# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:45:54 2023

"""
from a3task1 import *
import csv

def calc_returns(prices):
    vectorCopy = prices[:]
    vectorR = []
    for i in range(1, len(vectorCopy)):
        price1 = vectorCopy[i]
        price2 = vectorCopy[i-1]
        r = ((price1)/(price2)) - 1
        vectorR.append(r)
    
    return vectorR
    
def process_stock_prices_csv(filename):

    data = csv.reader(open(filename, 'r'), delimiter=",")
    headers = next(data)
    adjValue = []
    for col in data:
        adjValue.append(col[5])
    
    floatValue = [float(i) for i in adjValue]
    type(floatValue[0])
    return floatValue

def stock_report(filenames):
    SPYprices = process_stock_prices_csv(filenames[3])
    SPYreturns = calc_returns(SPYprices)

    
    headings = ["Symbol:", "Mean:", "StDev:", "Covar:", "Correl:", "R-SQ:",  "Alpha:", "Beta:"]
    m = []
    st = []
    cov = []
    cor = []
    rsquare = []
    alpha = []
    beta = []
    for i in range(len(filenames)):
        stockprices = process_stock_prices_csv(filenames[i])
        returns = calc_returns(stockprices)

        m.append(mean(returns))
        st.append(stdev(returns))
        cov.append(covariance(returns, SPYreturns))
        cor.append(correlation(returns, SPYreturns))
        rsquare.append(rsq(returns, SPYreturns))
        alpha.append(simple_regression(SPYreturns, returns)[0])
        beta.append(simple_regression(SPYreturns, returns)[1])

    for i in range(len(filenames)):
        filenames[i] = filenames[i].removesuffix(".csv")
        
        
    
    count = 0
    
    print('{:10}'.format(headings[0 + count]),end = "")
    count += 1
    for j in range(len(filenames)):
        print('{:10}'.format(filenames[j]),end = "")
    
    print("\n")
    
    print('{:10}'.format(headings[0 + count]),end = "")
    count += 1
    for j in range(len(filenames)):
        rounded = round(m[j], 5)
        print('{:10}'.format(str(rounded)),end = "")
    
    print("\n")
    
    print('{:10}'.format(headings[0 + count]), end = "")
    count += 1
    for j in range(len(filenames)):
        rounded = round(st[j], 5)
        print('{:10}'.format(str(rounded)),end = "")
    
    print("\n")
    
    print('{:10}'.format(headings[0 + count]),end = "")
    count += 1
    for j in range(len(filenames)):
        rounded = round(cov[j], 5)
        print('{:10}'.format(str(rounded)),end = "")
    
    print("\n")
    
    print('{:10}'.format(headings[0 + count]),end = "" )
    count += 1
    for j in range(len(filenames)):
        rounded = round(cor[j], 5)
        print('{:10}'.format(str(rounded)), end = "")
    
    print("\n")
    
    print('{:10}'.format(headings[0 + count]),end = "")
    count += 1
    for j in range(len(filenames)):
        rounded = round(rsquare[j], 5)
        print('{:10}'.format(str(rounded)),end = "")
    
    print("\n")
    
    print('{:10}'.format(headings[0 + count]),end = "")
    count += 1
    for j in range(len(filenames)):
        rounded = round(alpha[j], 5)
        print('{:10}'.format(str(rounded)),end = "")
    
    print("\n")
    
    print('{:10}'.format(headings[0 + count]),end = "")
    count += 1
    for j in range(len(filenames)):
        rounded = round(beta[j], 5)
        print('{:10}'.format(str(rounded)),end = "")
    
    print("\n")
    
def main():

    
    filenames = ["TSLA.csv", "AAPL.csv", "GOOG.csv", "SPY.csv"]
    stock_report(filenames)
    return 0
    
main()
