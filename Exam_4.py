def fib(y):
    x=0
    z=0
    f=0
    while(x<y):
        x=x+1
        z=z+x
    
    return z
    
     
y = int(input("Dame un numero entero positivo para obtener la serie fibonacci: "))
res = fib(y)
print(res)
