#Es sencillo todo esta comenta para un mejor
#Este codigo lo hice por que falte a mi trabajo y queria descansar
#No es el mejor codigo pero es funcional 
#Luis Miguel de los Santos Sanches,  2024












#Librerias necesarias
from random import choice
import time
import pyfiglet
from termcolor import colored
from Tiempos import Cuenta_regresiva

#Lista de paises
lista_paises_capitales = [
    ["republica dominicana", "santo domingo"],
    ["puerto rico", "san juan"],
    ["estados unidos", "washington d.c."],
    ["mexico", "ciudad de mexico"],
    ["argentina", "buenos aires"],
    ["espana", "madrid"],
    ["francia", "paris"],
    ["alemania", "berlin"],
    ["italia", "roma"],
    ["brasil", "brasilia"],
    ["chile", "santiago"],
    ["colombia", "bogota"],
    ["canada", "ottawa"],
    ["peru", "lima"],
    ["venezuela", "caracas"],
    ["reino unido", "londres"],
    ["china", "pekin"],
    ["japon", "tokio"],
    ["india", "nueva delhi"],
    ["rusia", "moscu"],
    ["australia", "canberra"],
    ["sudafrica", "pretoria"],
    ["egipto", "el cairo"],
    ["turquia", "ankara"],
    ["grecia", "atenas"],
    ["portugal", "lisboa"],
    ["corea del sur", "seul"],
    ["corea del norte", "pionyang"],
    ["filipinas", "manila"],
    ["tailandia", "bangkok"],
    ["nueva zelanda", "wellington"],
    ["suecia", "estocolmo"],
    ["noruega", "oslo"],
    ["finlandia", "helsinki"],
    ["dinamarca", "copenhague"],
    ["paises bajos", "amsterdam"],
    ["belgica", "bruselas"],
    ["suiza", "berna"],
    ["austria", "viena"],
    ["irlanda", "dublin"],
    ["polonia", "varsovia"],
    ["hungria", "budapest"],
    ["ucrania", "kiev"],
    ["kazajistan", "nursultan"]
]



#Validacion
juangando = True
Bienvenida = "Aprende las capitales"

Bienvenida = pyfiglet.figlet_format(Bienvenida)
Bienvenida = colored(Bienvenida ,"yellow")
print(Bienvenida)


#Boton para detener el juego
print("Pulsa 1 para detecner el juego")


#Bucle del juego
while juangando:
    




    #Obten las lista de pases y capilaes
    pais_capital = choice(lista_paises_capitales)
    #Preguntar al usuario

    Cuenta_regresiva()
    usurio = input(colored(f"Capita de {pais_capital[0]}: ", "blue"))
    

    
    

    #Validar la respuesta y la pasamos a minusculas para  evitar errores
    if usurio.lower() == pais_capital[1]:
        print("bien  hecho")




    #si la validacion es negativa o la repuesta lo es
    else:
        print(colored(f"Mal, era  {pais_capital[1]}", "red"))


        #Esto cierra el juego si pierde si quieres inplementarlo solo le quitas el (#)
        #juangando = False

     #Cierra el juego
    if usurio =="1":
        print(colored("Saliendo......", "red"))
        time.sleep(2)
        break


    #Por si lo quieres agregar

    #if usurio == " ":
        print(colored("Hoy hasido un placer jugar con ustedes", "green"))