def superpower(num1,num2):
    res = 1
    pot = 1
	while(pot<num2+1):
		res = res * num1
		pot = pot +1 
		

    
num1 = int(input("Dame el numero que deseas elevar a una potencia: "))
num2 = int(input("¿A cual potencia lo quieres elevar? "))
final = superpower(num1,num2)
print("El resultado es: "+str(final))


