class time_operations:
    def __init__(self,hours,minutes,seconds):
        self.seconds=seconds
        self.minutes=minutes
        self.hours=hours
    def start_time(self):
        time=self.hours*3600 + self.minutes*60 + self.seconds
        return time
    def end_time(self):
        time=self.hours*3600 + self.minutes*60 + self.seconds
        return time
    def add(self,other):
        added_time= self.start_time() + other.end_time()
        self.hours=added_time//3600
        added_time-=(self.hours*3600)
        self.minutes=added_time//60
        added_time-=(self.minutes*60)
        self.seconds=added_time
        print(self.hours,self.minutes,self.seconds)
    def diff(self,other):
        added_time=abs(self.start_time() - other.end_time())
        self.hours=added_time//3600
        added_time-=(self.hours*3600)
        self.minutes=added_time//60
        added_time-=(self.minutes*60)
        self.seconds=added_time
        print(self.hours,self.minutes,self.seconds)
    def display(self):
        print(self.hours,self.minutes,self.seconds)

t1=time_operations(6,50,30)
t2=time_operations(8,10,31)
t1.display()
t2.display()
t1.add(t2)
t1.diff(t2)

# class Time:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#         self.normalize_time()

#     def normalize_time(self):
#         """Adjusts minutes and seconds to proper format."""
#         self.minutes += self.seconds // 60
#         self.seconds = self.seconds % 60
#         self.hours += self.minutes // 60
#         self.minutes = self.minutes % 60

#     def add(self, other):
#         return Time(self.hours + other.hours,
#                     self.minutes + other.minutes,
#                     self.seconds + other.seconds)

#     def subtract(self, other):
#         """Assumes first time is greater than second time."""
#         t1_seconds = self.to_seconds()
#         t2_seconds = other.to_seconds()
#         diff_seconds = abs(t1_seconds - t2_seconds)
#         return Time.from_seconds(diff_seconds)

#     def to_seconds(self):
#         return self.hours * 3600 + self.minutes * 60 + self.seconds

#     @staticmethod
#     def from_seconds(total_seconds):
#         hours = total_seconds // 3600
#         minutes = (total_seconds % 3600) // 60
#         seconds = total_seconds % 60
#         return Time(hours, minutes, seconds)

#     def display(self):
#         print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

# # Example usage
# print("Enter first time:")
# h1 = int(input("Hours: "))
# m1 = int(input("Minutes: "))
# s1 = int(input("Seconds: "))

# print("Enter second time:")
# h2 = int(input("Hours: "))
# m2 = int(input("Minutes: "))
# s2 = int(input("Seconds: "))

# t1 = Time(h1, m1, s1)
# t2 = Time(h2, m2, s2)

# print("\nFirst Time: ", end="")
# t1.display()
# print("Second Time: ", end="")
# t2.display()

# added_time = t1.add(t2)
# subtracted_time = t1.subtract(t2)

# print("\nAddition Result: ", end="")
# added_time.display()
# print("Subtraction Result: ", end="")
# subtracted_time.display()