def  lcm(a,b):
    res=max(a,b)

    while(True):
        if(res%a==0 and res%b==0):
            return res
            
        res+=1
print(lcm(2,5))

'''
a=2 ,b=5
res=5

5%2==0,5%5==0
6%2==0,6%5==0
10%2==0,10%5==0 ---true
res=10
'''