#Sum of Digits / Digital Root
def digital_root(n):#bige but not easy to understand though maybe reflect pythonic
    #return n if n<10 else digital_root(sum([int(a) for a in str(n)]))
    return n%9 or n and 9 
            
print(digital_root(999999999999))