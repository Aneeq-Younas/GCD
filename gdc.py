
def GCD(a,b):
    c= a % b

    while c:
        a = b
        b = c
        c = a % b
    return b

print("Greatest Common Disivor of 15 and 18  is  :  ", GCD(15,18))
print("Greatest Common Disivor of 34 and 45  is  :  ", GCD(34,45))
print("Greatest Common Disivor of 7 and 18 is  :  ", GCD(7,18))





