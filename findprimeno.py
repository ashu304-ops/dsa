def findprimeno(n):
    prime=[False]*(n+1)
    i=2
    while i*i<n:
        i+=1        
        if  prime[i]==False:
            j=i*i
            while  j<=n:
                prime[j]=True
                j+=i    
    for  i in range(2,n,1):
        if prime[i]==False:
            print(i)
print(findprimeno(50))