def  trailingzerosoffactorial(n):
    # 1/5  +1/25+1/125+1/625
    # 5 --0 example 5!=  1zero  ,10!=1*2*3*4*5*6*7*9*(5*2)=2 zeros
    # 10/5--2 zeros
    # 200/5 ---200/5+200/25+200/125+200/625  +....
    # 40+8+1+0=49  zeros
    # n=10 ,res=10/5=2 ,res=2 ,n=100 ,res=100/5=20 ,res=100/25=4, 20+4=24
    res=0
    powof5=5
    while(n>=powof5):
        res=res+(n//powof5)
        powof5=powof5*5
    return  res

print(trailingzerosoffactorial(200))


        