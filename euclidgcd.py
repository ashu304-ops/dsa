def  euclidgcd(a,b):
    # solve it  by  euclead approach
    while(a!=b):
        if a>b:
            a=a-b
        else:
            b=b-a
    return a 

print(euclidgcd(35,70))