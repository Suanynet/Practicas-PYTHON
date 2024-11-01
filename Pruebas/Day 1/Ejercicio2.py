
#Ejercicio 1

def Welcome():
    
    Name = input("Ingrese su nombre: ")
    
    print("Bienvenido", Name)
    return Name

Name = Welcome()

def clasificar_edades():
    
    edad = float(input("Ingrese su edad: "))
    edad_obtenida = int(edad)
    
    return edad_obtenida

edad_obtenida = clasificar_edades()

#Ejercicio 1.2

def niño(edad_obtenida):
    if edad_obtenida < 13 :
        
        return print(Name, "Es un niño")
    
niño(edad_obtenida)

def adolecente(edad_obtenida):
    if edad_obtenida >= 13  and edad_obtenida < 18:
        
        return print(Name, "Es adolecente")

adolecente(edad_obtenida)

def adulto(edad_obtenida):
    if edad_obtenida >= 18 and edad_obtenida < 60:
        
        return print(Name, "Es adulto")

adulto(edad_obtenida)

def adulto_mayor(edad_obtenida):
    if edad_obtenida > 60 :
        
        return print(Name, "Es adulto mayor")
 
adulto_mayor(edad_obtenida)    