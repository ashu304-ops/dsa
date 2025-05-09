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