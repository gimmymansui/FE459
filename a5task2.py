from a5task1 import *

class BondPortfolio:
    """ Class called BondPortfolio that stores individual bonds in a list
    """
    def __init__(self):
        """Creates a new BondPortfolio
        """
        self.__list = []
        self._BondPortfolio__value = self.get_value()
        self.__yield_to_maturity = self.get_yield_to_maturity()
        self.__duration = self.get_duration()
        self.__convexity = self.get_convexity()
    
    def __repr__(self):
        '''String representation of object'''
        if len(self.__list) == 0:
            s = f"BondPortfolio contains {len(self.__list)} bonds: \n "
        
        s = f"BondPortfolio contains {len(self.__list)} bonds: \n "
        #\n Portfolio value: ${self.__yield_to_maturity}\n Portfolio duration: ${self.__duration}\n Portfolio convexity: ${self.__convexity}"
            
        return s

    def add_bond(self, b):
        """
        Args:
            b (Bond): Adds the chosen bond into BondPortfolio
        """
        self.__list.append(b)
    
    def rem_bond(self, b):
        """
        Args:
            b (Bond): Remove the chosen bond in BondPortfolio
        """
        self.__list.remove(b)
    
    def get_value(self):
        """

        Returns:
            _float_ : returns total value of the portfolio
        """
        temp = 0
        for i in range(len(self.__list)):
            temp += self.__list[i].get_price()
        
        self._BondPortfolio__value = temp
        return temp
    
    def get_yield_to_maturity(self):
        """

        Returns:
            _float_ : average ytm of the portfolio
        """
        portfolioValue = self.get_value()
        averageYTM = 0
        for i in range(len(self.__list)):
            averageYTM += ((self.__list[i].get_price()/portfolioValue)*self.__list[i].get_coupon_rate())

        self.__yield_to_maturity = averageYTM
        return averageYTM
    
    def get_duration(self):
        """

        Returns:
           _float_ : average duration of the portfolio
        """
        portfolioValue = self.get_value()
        averageDuration = 0
        for i in range(len(self.__list)):
            averageDuration += ((self.__list[i].get_price()/portfolioValue)*self.__list[i].get_duration())

        self.__duration = averageDuration
        return averageDuration

    def get_convexity(self):
        """

        Returns:
           _float_ : average convexity of the portfolio
        """
        portfolioValue = self.get_value()
        averageConvexity = 0
        for i in range(len(self.__list)):
            averageConvexity += ((self.__list[i].get_price()/portfolioValue)*self.__list[i].get_convexity())

        self.__convexity = averageConvexity
        return averageConvexity

    def shift_ytm(self, delta_ytm):
        """
        Shifts ytm by delta_ytm
        """
        for i in range(len(self.__list)):
            nytm = self.__list[i].get_yield_to_maturity() + delta_ytm
            self.__list[i].set_yield_to_maturity(nytm)