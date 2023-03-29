# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:53:47 2023

@author: suij2
"""
import math

def mean(values):
    x = 0
    for i in range(len(values)):
        x += values[i]
    
    returnval = x/(len(values))
    return returnval
    

def variance(values):
    N = len(values)
    sum = 0
    for i in range(len(values)):
        sum += (values[i] - mean(values))**2
    returnval = (1/N)*sum
    return returnval
        
def stdev(values):
    return math.sqrt(variance(values))

def covariance(x, y):
    meanX = mean(x)
    meanY = mean(y)
    N = len(x)
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - meanX)*(y[i] - meanY)
    returnval = (1/N)*(sum)
    return returnval

def correlation(x, y):
    rootX = math.sqrt(variance(x))
    rootY = math.sqrt(variance(y))
    return (covariance(x, y))/(rootX*rootY)

def rsq(x, y):
    return (correlation(x,y))**2

def simple_regression(x, y):
    betaXY = (covariance(x, y))/variance(x)
    alphaXY = mean(y) - (betaXY * mean(x))
    return (alphaXY, betaXY)
def main():
    
    arr = [4,4,3,6,7]
    arr2 = [6,7,5,10,12]
    print(mean(arr),"\n")
    print(variance(arr),"\n")
    print(stdev(arr),"\n")
    print(covariance(arr, arr2),"\n")
    print(correlation(arr,arr2),"\n")
    print(rsq(arr,arr2),"\n")
    print(simple_regression(arr, arr2), "\n")
    
    z = simple_regression(arr, arr2)[0]
    print(z)
    return 0
    
main()

