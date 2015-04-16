def dis(x1,y1,x2,y2):
    x = (x2-x1)**2
    y = (y2-y1)**2
    dist = (x + y)**0.5
    
    return dist

x1 = int(input("Dame el valor de x1: "))
y1 = int(input("Dame el valor de y1: "))
x2 = int(input("Dame el valor de x2: "))
y2 = int(input("Dame el valor de y2: "))

res = dis(x1,y1,x2,y2)
print("La distancia entre los dos puntos es de: "+str(res))
    
