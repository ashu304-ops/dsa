'''
def checkprime(n):
    for i in range(2,n//2 +1):
        if  n%i==0:
            return True
        else:
            return False
if checkprime(7)==True:
    print('it  is a  not prime  number')
else :
    print('it  is  a prime number')

# time  compleixty is  O(n/2)
'''
def checkprime(n):
    if n==1:
        return False
    elif  n%2==0  or  n%3==0:
        return  False
    else :
        i=5
        while i*i<n:
            i+=1
            if  n%i==0 or n%(i+2)==0:
                return False 
    return True

if checkprime(14)==True:
    print('it  is  a  prime number')
else :
    print('it is not  prime  number')   
