#Ejercicio3

def ingreso_numeros():
    
    lista_numeros = []
    
    pares = 0
    impares = 0
    
    for i in range(8):
        digitos = float(input("Ingrese un número: "))
        lista_numeros.append(int(digitos))
        print (lista_numeros)
        
        if lista_numeros[i] % 2 == 0:
            pares +=1
            print("Se encontraron", pares, "numeros pares")
            print("Se encontraron", impares, "numeros impares")
        else:
            if lista_numeros[i] % 2 != 0:
                impares +=1
                print("Se encontraron", pares, "numeros pares")
                print("Se encontraron", impares, "numeros impares")
            
ingreso_numeros()                      