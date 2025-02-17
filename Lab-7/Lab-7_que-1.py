dictionary1={10:'A',20:'B',30:'C',40:'D'}
dictionary2={50:'E',60:'F',70:'G',80:'H'}
dictionary3={90:'I',100:'J',110:'K',120:'L'}
print(f"Dictionary1: {dictionary1}")
print(f"Dictionary2: {dictionary2}")
print(f"Dictionary3: {dictionary3}")
dictionary4={**dictionary1, **dictionary2, **dictionary3}
print(f"Concatenated dictionary: {dictionary4}")