# def dec_to_bin(num, decimal=[]):
#     if num==0:
#         return int(''.join(map(str, decimal[::-1])))
#     else:
#         decimal.append(num%2)
#         return dec_to_bin(num//2,decimal)
    
def dec_to_bin(num):
    if num == 0:
        return ""  
    return dec_to_bin(num // 2) + str(num % 2)

print(dec_to_bin(174))