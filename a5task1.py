# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:53:59 2023

@author: JimmyMan
"""
    
    
def element_product(A, B):
    """ Returns Element wise multiplication """
    resultA = isinstance(A[0], list) #1d lists dont compute the same way so in the event that A[0] is not iterable, the function goes to assuming its 1
    resultB = isinstance(B[0], list)
    
    if resultA and resultB:
        assert len(A) == len(B) and len(A[0]) == len(B[0]), "Matrix Dimensions don't match"
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] *= B[i][j]
    else:
        for i in range(len(A)):
            A[i] *= B[i]
    return A    



class Bond:
    """Generates a bond object
    """
    def __init__(self, maturity_value, maturity_time, coupon_rate=0.0, coupon_frequency=2):
        """Constructor that takes the following:

        Args:
            maturity_value (float/int): $ value for maturity of the bond
            maturity_time (int): years until maturity
            coupon_rate (float, optional): coupon rate % as a decimal. Defaults to 0.
            coupon_frequency (int, optional): coupon payments per year. Defaults to 2.
        """
        self.__maturity_value = maturity_value
        self.__maturity_time = maturity_time
        self.__coupon_rate = coupon_rate
        self.__coupon_frequency = coupon_frequency
        self.__yield_to_maturity = coupon_rate
        self.__Bond_price = maturity_value
        self._Bond__pmt_times = self.cashflow_times()
        self.__cashflows = self.bond_cashflows()
        self.__discount_factors = self.discount_factors()
        self.__convexity = self.bond_convexity()
        self.__duration = self.bond_duration()


        
    def __repr__(self):
         '''return string representation'''
         s = f"${self.__maturity_value}-maturity {self.__maturity_time}-year {self.__coupon_rate*100}% bond, price=${self.__Bond_price}, ytm={self.__yield_to_maturity*100}% duration={self.__duration} convexity={self.__convexity}"
         return s
    
    def get_maturity_value(self):
        '''Returns maturity value of bond'''
        return self.__maturity_value
    
    def get_maturity_time(self):
        '''Returns years til maturity'''
        return self.__maturity_time

    def element_product(self, A, B):
        """ Returns Element wise multiplication """
        resultA = isinstance(A[0], list) #1d lists dont compute the same way so in the event that A[0] is not iterable, the function goes to assuming its 1
        resultB = isinstance(B[0], list)
        
        if resultA and resultB:
            assert len(A) == len(B) and len(A[0]) == len(B[0]), "Matrix Dimensions don't match"
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] *= B[i][j]
        else:
            for i in range(len(A)):
                A[i] *= B[i]
        return A
    

    def dot_product(self, B):
        """ Matrix multiplication """
        A = self.matrix
        B = B.matrix
        
        resultA = isinstance(A[0], list) #1d lists dont compute the same way so in the event that A[0] is not iterable, the function goes to assuming its 1
        resultB = isinstance(B[0], list)
        
        if resultA and resultB:
            assert len(A) == len(B[0]), "incompatible dimensions: cannot dot-product (" + str(len(A)) + "," + str(len(A[0])) + ") with (" + str(len(B)) +  "," + str(len(B[0])) + ")"
            dotMatrix = self.zeros(len(A), len(B[0]))
            
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        dotMatrix[i][j] += A[i][k]*B[k][j]
        else:
            dotMatrix = 0
            for i in range(len(A)):
                dotMatrix += A[i]*B[i]
        return dotMatrix

    def zeros(n, m = 0):
        """creates matrix[n][m] of zeros """ 
        if m == 0:
            m = n

        mat = [[0 for col in range(m)] for row in range (n)];
        return mat

    def get_cashflows(self):
        '''Returns cashflows of bond'''
        return self.__cashflows

    def get_coupon_amount(self):
        '''Returns coupon rate'''
        return self.__coupon_rate
    
    def get_coupon_rate(self):
        '''Returns coupon rate'''
        return self.__coupon_rate
    
    def get_coupon_frequency(self):
        '''Returns coupon payment frequency'''
        return self.__coupon_frequency
    
    def get_price(self):
        '''Returns price of bond'''
        return self.__Bond_price
    
    def get_yield_to_maturity(self):
        '''Returns ytm of bond'''
        return self.__yield_to_maturity

    def get_pmt_times(self):
        '''Returns payment times'''
        return self._Bond__pmt_times

    def get_discount_factors(self):
        '''Returns discount factors'''
        return self.__discount_factors
    
    def cashflow_times(self):
        """ computes cashflow times self.__coupon_frequency*self.__maturity_time, where self.__maturity_time is years til maturity and self.__coupon_frequency is coupon payments per year"""
        mat = [i+1 for i in range(self.__coupon_frequency*self.__maturity_time)];
        self._Bond__pmt_times = mat
        return mat

    def discount_factors(self):
        """computer discount factors given rate self.__yield_to_maturity, self.__maturity_time years til maturity and self.__coupon_frequency coupon payments per year"""
        vec = [1] #default is 1 to start the calculation
        [(vec.append((vec[-1])/((1+(self.__yield_to_maturity/self.__coupon_frequency))**(1)))) for i in range(self.__coupon_frequency) for j in range(self.__maturity_time)] # vec[-1] always gets the last element and sets that as the numerator
        vec.pop(0) # removing the first element
        self.__discount_factors = vec
        return vec

    def bond_cashflows(self):
        '''Calculates bond cashflows'''
        vec = [(self.__coupon_rate/self.__coupon_frequency)*self.__maturity_value for i in range((self.__maturity_time*self.__coupon_frequency)-1)]
        vec.append(((self.__coupon_rate/self.__coupon_frequency)*self.__maturity_value)+self.__maturity_value)#adds final element
        return vec
    
    def bond_price(self):
        """ returns bond price given self.__maturity_value maturity, self.__coupon_rate annual coupon, self.__maturity_time years til maturity, self.__coupon_frequency coupon payments per year, ytm annual yield to maturity"""
        df = self.discount_factors()
        cf = self.bond_cashflows()
        val = self.dot_product(df, cf)
        return val
    
    def bond_duration(self):
        """ returns bond duration given self.__maturity_value maturity, self.__coupon_rate annual coupon, self.__maturity_time years til maturity, self.__coupon_frequency coupon payments per year, ytm annual yield to maturity"""
        cf = self.bond_cashflows()
        df = self.discount_factors()
        T = self.cashflow_times()
        m = self.__coupon_frequency
        r = self.__yield_to_maturity

        B = self.__Bond_price
        temp = 0
        for t in range(T + 1):
            temp += (t*cf[t-1])/((1+r/m)^t)

        temp = temp*(1/B)
        temp = temp*(1/m)
        return temp

    def calculate_price(self):
        '''Calculates prices given a new yield to maturity'''
        self.__Bond_price = self.bond_price()

    def set_yield_to_maturity(self, new_ytm):
        """ Sets new yield to maturity value and then re-evaluates the price of the bond

        Args:
            new_ytm (float): percentage ytm as decimal
        """
        self.__yield_to_maturity = new_ytm
        self.calculate_price()
    
    def calculate_yield_to_maturity(self, accuracy = 0.0001):
        ''' Calculates new yield to maturity given new price'''
        x = len(str(accuracy).split(".")[1])
        C = self. __coupon_rate
        n = self.__coupon_frequency*self.__maturity_value
        fv = self.__maturity_time
        pv = self.__Bond_price
        temp = (C + (fv-pv)/n)/((fv+pv/2))
        self.__yield_to_maturity = temp

    def set_price(self, new_price):
        """ Sets new price of the bond and then re-evaluates the yield-to-maturity of the bond

        Args:
            new_price (int): new $ price of bond
        """
        self.__Bond_price = new_price
        self.calculate_yield_to_maturity()

    def bond_convexity(self):
        """Calculates bond convexity

        Returns:
            (float): convexity of the bond
        """
        df = self.discount_factors()
        cf = self.bond_cashflows()
        B = self.__Bond_price
        temp = 0
        for i in range(1, len(cf)+1):
           temp += df[i-1]*cf[i-1]*i*(i+1)
        temp = temp/(1+self.__yield_to_maturity/self.__coupon_frequency)**2
        convexity = (1/B)*temp*(1/((self.__coupon_frequency)**2))
        return convexity

    def get_duration(self):
        """Gets bond duration

        Returns:
            (float): value of bond duration
        """
        return self.__duration
    def get_convexity(self):
        """Gets bond convexity

        Returns:
            (float): value of bond convexity
        """
        return self.__convexity
