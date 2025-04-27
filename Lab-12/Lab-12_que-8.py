class String:
    def __init__(self,data=""):
        self.data=data
    def __iadd__(self,other):
        self.data += other.data
        return self
    def toLower(self):
        return self.data.lower()
    def toUpper(self):
        return self.data.upper()
    def __str__(self):
        return self.data

s1 = String("Hello")
s2 = String("World")
s1+=s2
print(f"Concatenated string is {s1}")
print(f"String in lowercase is {s1.toLower()}")
print(f"String in uppercase is {s1.toUpper()}")