def fah_to_cel(F):
    C=(F-32)*(5/9)

    return C

fahrenheit=[32,-40,0,20,10]
celsius=[]

for i in fahrenheit:
    celsius.append(fah_to_cel(i))

print(celsius)