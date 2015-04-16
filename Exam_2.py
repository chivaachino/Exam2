def triangulo(SIZE):
    for n in range(1,SIZE+1):
        print("T"*n)
    for n in range(1,SIZE):
        s = SIZE-n
        print("T"*s)


SIZE = int(input("Dime el tamaño del triangulo: "))        
triangulo(SIZE)        
