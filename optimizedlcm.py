# lcm(a,b)* gcd(a,b)=a*b
# lcm(a,b)=a*b/gcd(a,b)

def optimizedlcm(a,b):
    lcm=a*b//gcd(a,b)
    return  lcm

def gcd(a,b):
    while(a!=0  and  b!=0):
        if  a>b:
            a=a%b
        else :
            b=b%a
    if  a!=0:
        return a
    else:
        return b

    
print(optimizedlcm(8,24))

# time complexity is O(log(max(a,b)))