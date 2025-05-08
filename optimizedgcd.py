def optimizedgcd(a,b):
    while(a!=0  and  b!=0):
        if  a>b:
            a=a%b
        else :
            b=b%a
    if  a!=0:
        return a
    else:
        return b
print(optimizedgcd(15,20))
# time  complexity is best  as  log(min a,b)
'''
a,b=15,20
20>15---b=20%15=5
a=15,b=5
15>0 ---a=15%5=0
a=0,b=5
answer=0

'''
