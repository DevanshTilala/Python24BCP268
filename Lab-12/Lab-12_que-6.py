class Date:
    def __init__(self,date):
        self.day=date[0]
        self.month=date[1]
        self.year=date[2]
    def __eq__(self, other):
        if (self.day==other.day and self.month==other.month and self.year==other.year):
            return True
        else:
            return False

d1=Date([2,3,2025])
d2=Date([3,4,2025])
if(d1==d2):
    print("Both dates are same")
else:
    print("Both dates are different")