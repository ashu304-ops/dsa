def countnoofdigit(n):
    count=0
    n=abs(n)
    while (n>0):
        n=n//10
        count+=1
    return count

print(countnoofdigit(-2546))
