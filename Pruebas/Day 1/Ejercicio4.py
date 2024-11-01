#Ejercicio 4

def ingresar_palabra():
    frase = input("Ingrese una frase: ")
    print(frase)
    return frase

frase = ingresar_palabra()

def contar_vocales(frase):
    
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    frase_vocales = [letra for letra in frase if letra in vocales]
    return frase_vocales

vocales = contar_vocales(frase)

def conclusión(vocales):
    print("En la frase se a encontrado", len(vocales), "vocales", vocales)
 
conclusión(vocales)    