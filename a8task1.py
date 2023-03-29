# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:38:10 2023

@author: suij2
"""
import math
from scipy.stats import norm

class BSMOption(object):
    '''An class that defines a option object'''

    def __init__(self, s, x, t, sigma, rf, div):
        """instantiates a new option object

        Args:
            s (float): the current price of the underlying asset
            x (float): the current strike price of the option
            t (float): the option maturity time in years
            sigma (float): the annualized standard deviation of returns
            rf (float): the annualized risk free rate of return
            div (float): the annualized dividend rate; assume continuous dividends rate
        """
        self._x = x 
        self._s = s 
        self._t = t 
        self._sigma = sigma 
        self._r = rf
        self._div = div
    
    def __repr__(self):
        '''returns string representation of the option'''
        s = f"s = ${self._x:.2f}, x = ${self._x:.2f}, t = {self._t:.2f} (years), sigma = {self._sigma:.3f}, rf = {self._r:.3f}, div = {self._div:.2f}"
        
        return s
    
    def getX(self):
        '''returns the strike price of the option'''
        return self._x
    
    def getS(self):
        '''returns the underlying stock price of the option'''
        return self._s
    
    def d1(self):
        '''returns d1 in the black-scholes model'''
        returnval = math.log(self._s/self._x) + (self._r - self._div + 0.5*self._sigma**2)*self._t
        return returnval/(self._sigma*self._t**0.5)
    
    def d2(self):
        '''returns d2 in the black-scholes model'''
        return self.d1() - self._sigma*self._t**0.5
    
    def setprice(self, s):
        '''sets the price of the underlying'''
        self._s = s
    
    def nprimed1(self):
        '''gives the normal pdf of d1'''
        return norm.pdf(self.nd1())
    
    def nd1(self):
        '''gives the normal cdf of d1'''
        return norm.cdf(self.d1())
    
    def nd2(self):
        '''gives the normal cdf of d2'''
        return norm.cdf(self.d2())
    
    def nnd2(self):
        '''returns the negative normal cdf of d2'''
        return norm.cdf(-self.d2())
    
    def nnd1(self):
        '''returns the negative normal cdf of d2'''
        return norm.cdf(-self.d1())
    
    def setsigma(self, sigma):
        '''sets a new sigma for the option'''
        self._sigma = sigma

    def value(self):
        '''for polymorphic purposes'''
        return 0
    
    def delta(self):
        '''for polymorphic purposes'''
        return 0

class BSMEuroCallOption(BSMOption):
    '''instantiates a call option using the parent BSMOption class'''
    def __init__(self, s, x, t, sigma, rf, div):
        '''instantiates a call option using the parent BSMOption class'''
        super().__init__(s, x, t, sigma, rf, div)
    
    def __repr__(self):
        '''gives string representation of object'''
        s = f"BSMEuroCallOption, value = ${self.value():.2f}, \n parameters = (${self._x:.2f}, x = ${self._x:.2f}, t = \
        {self._t:.2f} (years), sigma = {self._sigma:.3f}, rf = {self._r:.3f}, div = {self._div:.2f})"

        return s

    def delta(self):
        '''returns delta of object'''
        return math.exp(-self._div*self._t)*self.nd1()
    
    def vega(self):
        '''returns the vega of the call option'''
        return self.nprimed1()*self._s*math.sqrt(self._t)
    
    def value(self):
        '''returns the value of the call option'''
        returnValue = (self.nd1()*self._s*math.exp(-self._div*self._t))-(self._x*math.exp(-self._r*self._t)*self.nd2())
        return returnValue

    
class BSMEuroPutOption(BSMOption):
    
    def __init__(self, s, x, t, sigma, rf, div):
        '''instantiates a put option using the parent BSMOption class'''
        super().__init__(s, x, t, sigma, rf, div)
    
    def __repr__(self):
        '''gives string representation of put option'''
        s = f"BSMEuroPutOption, value = ${self.value():.2f}, \n parameters = (${self._x:.2f}, x = ${self._x:.2f}, t = \
        {self._t:.2f} (years), sigma = {self._sigma:.3f}, rf = {self._r:.3f}, div = {self._div:.2f})"

        return s
    
    def delta(self):
        '''returns the delta of the put option'''
        return -math.exp(-self._div*self._t)*self.nnd1()
    
    def vega(self):
        '''returns the vega of the put option'''
        return self.nprimed1()*self._s*math.sqrt(self._t)
    
    def value(self):
        '''returns the value of the option'''
        returnValue = self._x*math.exp(-self._r*self._t)*self.nnd2()-self._s*math.exp(self._div*(-self._t))*self.nnd1()
        return returnValue
    