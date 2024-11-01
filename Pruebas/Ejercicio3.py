def Numero_Par (numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = filter(Numero_Par, numeros)

print(list(pares))

 
 
 #ejercicio 1.2
 
def Multiplicar(x):
 
  return x * 3

numbers = [1, 2, 3, 4, 5, 6]

resultado = map(Multiplicar, numbers)

resultado_lista = list(resultado)

print(resultado_lista)


# Ejercicio 1.3

def Mayusculas():
  
  return