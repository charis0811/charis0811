# term class
class Term:
    def __init__(self,coefficient,power):
        self._coefficient=coefficient #  let variables to be private
        self._power=power

    def get_power(self):# use the method to access variable
        return self._power

    def get_coefficient(self):
        return self._coefficient
