from random import *
import sys

class Utility:
    def write_textfile(self,textfile):
        pass

    def random_sampling(self, min, max):
        value = 0
        digits = 0

        min_digits = self.count_digits(min)
        max_digits = self.count_digits(max)

        if min_digits < max_digits:
            digits = max_digits
        else:
            digits = min_digits

        value = round(uniform(min, max), digits)

        return value

    def count_digits(self,num):
        flag = False

        string = str(num)
        count = 0
        for char in string:
            if flag == True:
                count += 1
            if char == ".":
                flag = True

        return count