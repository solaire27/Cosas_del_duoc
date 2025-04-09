variable_entera = 23
variable_decimal= 3.6
variable_texto= "si"
variable_booleana= True

resultado_suma = variable_entera + variable_decimal 
comparacion= (variable_entera>variable_decimal)

nombre_usuario = input("Por favor, ingresa tu nombre: ")
print("Hola, " + nombre_usuario + " sas")

if variable_booleana:
    print("what the fuck is bool")
elif resultado_suma < 10:
    print("La suma es menor que 10.")
else:
    print("Ninguna de las condiciones anteriores se cumple.")

lista_numeros = [1, 2, 3, 4, 5]
tupla_colores = ("rojo", "verde", "azul")
diccionario_edades = {"Juanito": 25, "Maríata": 30, "Carlosito": 22}
conjunto_elementos = {1, 2, 3, 4, 5}

def saluo(nombre):
    return "Hola, " + nombre

saludar = saluo("estudiante")

try:
    division = 0/0
except ZeroDivisionError:
    print("what")
finally: 
    print("si")
    
with open("archivo.txt", "w") as archivo:
    archivo.write("spam!")
    
import random
print(random.randint(1,9))

class Desclasao():
    def __init__(self,atributo):
        self.atributo= atributo
    def mostrar_atributo(self):
        print("el valor es ", self.atributo)

longitud_cadena = len("paralelepipedo")
mayusculas = "holas".upper()
minusculas = "AAAAAAA".lower()
reemplazo = "python es si".replace("si", "increíble")
print(mayusculas, minusculas, reemplazo)