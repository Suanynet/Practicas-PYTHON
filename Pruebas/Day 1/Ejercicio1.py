# Ejercicio 1

def welcome ():
    
    name = input("Ingrese nombre: ")
    
    print("Welcome", name)
    return name

name = welcome()

# Ejercicio 1.2

def promedio ():
    
    nota_1 = float(input("Ingrese nota 1: "))
    nota_2 = float(input("Ingrese nota 2: "))
    
    result = int(nota_1) + int(nota_2) / 2
    
    return result

result = promedio ()

# Ejercicio 1.3

def nota_final (name, result):
    
    print(name,"Promedio Obtenido", result)
    
nota_final(name, result)        