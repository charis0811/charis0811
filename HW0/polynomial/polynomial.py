from Term import *

class Polynomial:
    def __init__(self,terms):
        # makes the variables private
        self._terms=terms 
        self._new_poly=dict()

    # first=first polynomial object
    # s_poly_object=second polynomial object
    def multiply(self,s_poly_object):
        for f_poly in range(0,self.__init__()):
            for s_poly in range(0,s_poly_object.__init__()):
                ###
                theNewPower=self.get_poly()[f_poly].get_power()+s_poly_object.get_poly()[s_poly].get_power() 
                theNewCoefficient=self.get_poly()[f_poly].get_coefficient()*s_poly_object.get_poly()[s_poly].get_coefficient() 
    
                if theNewPower not in self._new_poly:
                    # power is the key, coefficient is the value
                    # go ahead and add it
                    self._new_poly[theNewPower]=theNewCoefficient
                else:
                    # go to the dic to get the coefficient that already exist
                    # get():get the value of the specific key
                    # go ahead and update it
                    self._new_poly[theNewPower]=self._new_poly.get(theNewPower)+theNewCoefficient
        print(self._new_poly)

    def __init__(self):
        ###
        return self._terms.__init__() # how many terms

    def get_poly(self):
        return self._terms
    
poly1=Polynomial([Term(3,4),Term(2,2),Term(5,5)])
poly2=Polynomial([Term(3,4),Term(2,2)])

Polynomial.multiply(poly1,poly2)