import random
from math import hypot

import self as self

rand_num = random.uniform(-1, 1)
class Qualean:



    def __init__(self, number,rand_num=rand_num):
        if number==1 or number == 0 or number == -1:
            self.num = number
            self.rand_num= rand_num
            self.in_num = round(self.num * self.rand_num, 10)
        # self.imag_num = self.in_num * random.uniform(-1, 1)
        else:
            raise Exception("Must be in three possible real state (1,0,-1)")

    def __add__(self, other):
        global real_part, imag_part
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.in_num + other
            imag_part = self.rand_num + other.rand_num
        if isinstance(other, Qualean):
            real_part = self.in_num + other.in_num
            imag_part = self.rand_num + other.rand_num

        return self.__class__(real_part, imag_part)

    def __mul__(self, other):
        global real_part, imag_part
        if isinstance(other,float) or isinstance(other, int):
            real_part = self.in_num * other.in_num
            imag_part = self.rand_num * other.rand_num
        if isinstance(other,Qualean):
            real_part = self.in_num * other.in_num
            imag_part = self.rand_num * other.rand_num

        return self.__class__(real_part, imag_part)

    def __repr__(self):
        return '{self.__class__.__name__}({self.in_num}.format(self=self))'

    def __str__(self):
        return (f'{self.rand_num}')

    def __abs__(self):
        return hypot(self.in_num, self.rand_num)

    def __eq__(self, other):
        return (self.in_num == other.in_num) and (self.rand_num == other.rand_num)

    def __ne__(self, other):
        return (self.in_num != other.in_num) or (self.rand_num != other.rand_num)

    def __lt__(self, other):
        return (self.in_num, self.rand_num) < (other.in_num, other.rand_num)

    def __le__(self, other):
        return (self.in_num) <= (other.rand_num)

    def __bool__(self):
        return bool(self.in_num)

    def __sqrt__(self):
        return self.in_num.sqrt()


    def __and__(self, other):
        if not isinstance(other, Qualean):
            return False
        if self.in_num == 0 or other.in_num == 0:
            return False
        return True

    def __or__(self, other):
        if self.in_num != 0:
            return True
        if isinstance(other, Qualean) and other.in_num != 0:
            return True
        return False
