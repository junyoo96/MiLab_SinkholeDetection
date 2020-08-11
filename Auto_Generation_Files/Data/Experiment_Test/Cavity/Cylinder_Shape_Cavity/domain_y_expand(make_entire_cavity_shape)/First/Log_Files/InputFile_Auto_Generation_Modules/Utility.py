from random import *
import sys
import decimal
from sympy import Symbol,solve

class Utility:
    def write_textfile(self,textfile):
        pass

    def random_sampling(self, min, max, user_defined_digits=-1):
        value = 0
        digits = 0

        min_digits = self.count_digits(min)
        max_digits = self.count_digits(max)

        if min_digits < max_digits:
            digits = max_digits
        else:
            digits = min_digits

        if user_defined_digits!=-1:
            digits=user_defined_digits

        tmp=uniform(min, max)
        tmp=float('{:.20f}'.format(tmp).rstrip('0'))
        value = round(tmp, digits)

        return value

    def count_digits(self,num):
        flag = False

        string = str(num)

        if "e" in string:
            string='{:.20f}'.format(num).rstrip('0')

        count = 0
        for char in string:
            if flag == True:
                count += 1
            if char == ".":
                flag = True
    

        return count

    def getXAxis(self,center_x, center_y, current_y, radius):
        x=Symbol('x')
        equation=x**2+(-2*center_x)*x+(center_x**2+current_y**2-(2*current_y*center_y)+center_y**2-radius**2)
        answer=solve(equation)

        x_axis=None
        if answer[0]<0:
            x_axis=-answer[0]
        else:
            x_axis=answer[0]

        return round(x_axis,4)