def fibonacci (): 
    n = eval(input("What term of the FIbonacci sequence are you trying to find?"))
    x=[0,1]
    for i in range(2,n):
        x.append(x[i-2]+x[i-1])
    print(x[n-1])
fibonacci ()