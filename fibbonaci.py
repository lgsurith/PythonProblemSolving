def fib(n):
    n1=0
    n2=1
    count=0
    if n<=0:
        print("Please enter a valid number")
    elif n==1:
        return(n1)
    elif n==2:
        return(n2)
    while count<=(n-3):
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
    return n3
for i in range(1,1000):
    print(fib(i))   



