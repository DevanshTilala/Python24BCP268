class complex_operations:
    def __init__(self,complex1,complex2):
        self.c1=complex1
        self.c2=complex2
    def comp_add(self):
        print(self.c1 + self.c2)
    def comp_sub(self):
        print(self.c1 - self.c2)
    def comp_multi(self):
        print(self.c1 * self.c2)
    def comp_div(self):
        print(self.c1 / self.c2)

a = complex(input("Enter a complex number(use j in imaginary): "))
b = complex(input("Enter a complex number(use j in imaginary): "))
c = complex_operations(a,b)
c.comp_add()
c.comp_sub()
c.comp_multi()
c.comp_div()