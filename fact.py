def fact(n):
    num=1
    if n<0:
        print("Please enter a valid number")
    elif n==0:
        return(num)
    while n>=1:
        num*=n
        n=n-1
    return num

print(fact(10000))  