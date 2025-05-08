def  gcd(a,b):
    min=0
    if  a>b:
        min=b
    else:
        min=a
    for i in range(min,0,-1):
        if (a%i==0 and b%i==0):
            return i
# it  takes min(a,b)---worst case

print(gcd(17,13))

