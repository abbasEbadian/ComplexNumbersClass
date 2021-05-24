from math import sin, cos
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        self.R  = self.r()
        
    def __add__(self, other):
        res = Complex(self.real + other.real , self.imag + other.imag)
        return res
    
    def __sub__(self, other):
        res = Complex(self.real - other.real , self.imag - other.imag)
        return res
    
    def __mul__(self, other):
        a = self.real
        b = self.imag
        c = other.real
        d = other.imag
        r = a*c - b*d
        i = a*d + b*c
        res = Complex(r, i)
        return res
    
    def conjugate(self):
         return Complex(self.real, -1 * self.imag)

    def __truediv__(self, other):
        other_into_conjugate = other * other.conjugate()
        new = self * other.conjugate()
        return Complex(new.real/other_into_conjugate.real ,  new.imag/ (other_into_conjugate.real)) 
    
    def bar(self):
        return self.conjugate()
    
    def __pow__(self, power):
        a = self
        for i in range(1, power):
             a *= a
        return a
    
    def r(self):
        return (self.real ** 2 + self.imag **2 ) ** 0.5
    
    def __gt__(self, other):
        return self.R > other.R
    def __lt__(self, other):
        return self.R < other.R
    def __ge__(self, other):
        return self.R >= other.R
    def __le__(self, other):
        return self.R <= other.R
    def __eq__(self, other):
        return self.R == other.R
    def __ne__(self, other):
        return self.R != other.R
    
        
    def __repr__(self):
        op = " + "
        if not self.real:
            op = ""
            if self.imag < 0:
                op = " - "
        else:
            if self.imag < 0:
                op = " - "
        if self.imag == 1:
            self.imag = " "
        elif self.imag == 0:
            self.imag = ""
        else:
            self.imag = abs(self.imag)
        real = self.real or ''
        imag = self.imag
        return f"{real}{imag and op + str(imag)+ 'j'}"
    
def euler(comp,  c):
    r = c * cos(comp.imag)
    i = c * sin(comp.imag) 
    return Complex(r, i) 