class Cifrado:
    
    def __init__(self, alfabeto, bienvenido):
 
        self.alfabeto = alfabeto
        self.bienvenido = bienvenido
        
         
    def saludar(self):
        print(f"Sea bienvenido al cifrado cesar, {self.bienvenido}")
    
    def cifrar(self):
        print(1)
        
            
    
    
    
def main():
    
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    usuario = input ("Ingrese su Nombre de Usuario: ")
    saludo = Cifrado(usuario, alfabeto)
    saludo.saludar()
    
    palabra = input("Ingrese el mensaje: ")
    texto_lista = list(palabra)
    
   
    posiciones = {
        
      0 : "z",
      1 : "a",
      2 : "b",
      3 : "c",
      4 : "d",
      5 : "e",
      6 : "f",
      7 : "g",
      8 : "h",
      9 : "i",
     10 : "j",
     11 : "k",
     12 : "l",
     13 : "m",
     14 : "n",
     15 : "ñ",
     16 : "o",
     17 : "p",
     18 : "q",
     19 : "r",
     20 : "s",
     21 : "t",
     22 : "u",
     23 : "v",
     24 : "w",
     25 : "x",
     26 : "y"
         
    }
    


main()


    