__author__ = 'garvit'

class fraction:

    def __init__(self, top, bottom):
        if bottom < 0:
            top = top * -1
            bottom = bottom * -1
        self.num = int(top)
        self.den = int(bottom)

    def __str__(self):
        gcd = self.gcd(self.num, self.den)
        self.num = int(self.num / gcd)
        self.den = int(self.den / gcd)
        return str(self.num) + "/" + str(self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        return fraction(newnum,newden)

    def gcd(self, m,n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

    def __eq__(self, other):
        if(self.num == other.num and self.den == other.den):
            return True
        return  False