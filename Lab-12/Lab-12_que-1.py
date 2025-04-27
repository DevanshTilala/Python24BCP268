class complex_operations:
    def __init__(self,complex1,complex2):
        self.c1=complex1
        self.c2=complex2
    def __add__(self):
        return self.c1 + self.c2
    def __sub__(self):
        return self.c1 - self.c2
    def __mul__(self):
        return self.c1 * self.c2
    def ___truediv__(self):
        return self.c1 / self.c2

a = complex(input("Enter a complex number(use j in imaginary): "))
b = complex(input("Enter a complex number(use j in imaginary): "))
c = complex_operations(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# class Complex:
#     def __init__(self, r = 0.0, i = 0.0):
#         self.real = r
#         self.imag = i
#     def __add__(self,other):
#         z = Complex()
#         z.real = self.real + other.real
#         z.imag = self.imag + other.imag
#         return z
#     def __sub__(self,other):
#         z = Complex()
#         z.real = self.real - other.real
#         z.imag = self.imag - other.imag
#         return z
#     def __mul__(self, other):
#         return Complex(self.real * other.real - self.imag * other.imag,
#                        self.real * other.imag + self.imag * other.real)

#     def __truediv__(self, other):
#         denominator = other.real**2 + other.imag**2
#         return Complex((self.real * other.real + self.imag * other.imag) / denominator,
#                        (self.imag * other.real - self.real * other.imag) / denominator)
#     def display(self):
#         print(self.real, self.imag)

# c1 = Complex(1.1,0.2)
# c2 = Complex(2.2,0.4)
# c3 = c1 + c2
# c3.display()
# c4 = c1 - c2
# c4.display()