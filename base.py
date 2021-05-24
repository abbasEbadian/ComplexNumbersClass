from math import sin, cos
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        self.R  = self.r()

    def ip(self):
        if self.imag < 0:
            return  str(self.imag) + "j"
        if self.imag == 0:
            return ""
        else:
            p = str(self.imag)
            if self.imag == 1:
                p = ""
            if self.real == 0:
                return p + "j"
            else:
                return " + " + p + "j"
                
        
    def __add__(self, other):
        a = self.real + other.real
        b = self.imag + other.imag
        res = Complex(a, b)
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
        return f"{self.real or ''}{self.ip()}"
    
def euler(comp,  c):
    r = c * cos(comp.imag)
    i = c * sin(comp.imag) 
    return Complex(r, i) 

a = Complex(1, 1)
b = Complex(0, 2)
print("a: ", a)
print("b: ", b)
print("----------")
print("a+b: ", a + b)
print("a-b: ", a - b)
print("a*b: ", a * b)
print("a/b: ", a / b)
print("a^2: ", a**2)
print("a>b: ", a > b)
print("a<=b: ", a <= b)
print("euler(b, 2): ", euler(b, 2))
