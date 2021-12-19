# term class
class Term:
    def __init__(self,coefficient,power):
        self._coefficient=coefficient #  let variables to be private
        self._power=power

    def get_power(self):# use the method to access variable
        return self._power

    def get_coefficient(self):
        return self._coefficient

class Polynomial:
    def __init__(self,terms):
        # makes the variables private
        self._terms=terms 
        self._new_poly=dict()

    def __init__(self):
        ###
        return self._terms.__init__() # how many terms

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
        self._print_poly(self._new_poly)

    def get_poly(self):
        return self._terms
    def _print_poly(self,new_poly):
        print("Answer is:",end=" ")
        # return key-value pair
        for p,c in new_poly.items():
            if p==0:
                x=""
            else:
                x="x"
            if c>=1:
                plus="+"
            else:
                plus="-"
            print("{0}{1}{2}^{3}".format(plus,c,x,p),end=" ")            
    
##MAIN##
