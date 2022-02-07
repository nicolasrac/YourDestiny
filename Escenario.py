import os
import time
import colorama
from colorama import Fore,Back,Style
colorama.init (autoreset=True)
import pyfiglet as pf 

#Aquí creamos las diferentes variables, las cuales van a ser determinantes para el desarrollo del juego.
class Escenario:
    def __init__(self, descripcion, opciones):
        self.descripcion = descripcion
        self.opciones = opciones
        self.cambioSupervivencia = 0

#Ajora vamos a definir la funcion que nos muestra en pantalla el juego.
    def presentar(self, personaje):
        #Salto de linea
        print('\n')
        #Nos muestra la vida actual
        print(personaje.obtenerEstado())
        #Nos muestra la descripcion del escenario
        print(self.descripcion)

        #Nos aseguramos que los cambios en supervivencia, se hagan y no solo sea la cadena.
        personaje.supervivencia += self.cambioSupervivencia


        #Acabamos el juego si el personaje muere

        if personaje.supervivencia <= 0: 
            time.sleep(2)
            print("\n.")
            time.sleep(1)
            print("\n.")
            time.sleep(1)
            print("\n.")
            time.sleep(2)

            print (pf.figlet_format("\nGAME OVER"))
            time.sleep(2)
            print(Fore.RED+"\nHas tomado una mala decisión y has muerto. Puedes intentarlo de nuevo.")
            personaje.supervivencia = 0
            time.sleep(3)
            print("El juego se reiniciará automáticamente en :\n3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(3)
            os.system ("clear")
            return 'INICIO'


        #Asignamos que pasa si alguien gana.
        
        elif personaje.supervivencia >= 1000:
            time.sleep(3)
            print("\n.")
            time.sleep(1)
            print("\n.")
            time.sleep(1)
            print("\n.")
            time.sleep(2)           
            print (pf.figlet_format("\n¡VICTORIA!"))
            time.sleep(2)
            print (Fore.YELLOW + "\nHas llegado a uno de los 9 finales positivos de destiny.")
            time.sleep(2)
            print ("De cualquier forma, te quedan finales por explorar.")
            time.sleep(2)
            print("Si quieres seguir jugando para descubrir cualquiera de los otros finales de Your Destiny...")
            time.sleep(3)
            print("...")
            time.sleep(2)
            print ("¡Solo di que sí! :)")
            time.sleep(2)
            print ("En caso de que ya hayas descubierto absolutamente todos los finales, o tengas otra cosa más productiva que hacer...")
            time.sleep(5)
            print ("Escribe cualquier otra cosa.")

            respuesta = input("¿Quieres seguir jugando Your Destiny?")
            if respuesta == "si" or "sí" or "SI" or "Sí" or "Si":
                print("¡Me alegra leer eso!\nFue una respuesta muy valiente de tu parte. Te deseo suerte en tu aventura.")
                time.sleep(4)
                print("El juego se reiniciará automáticamente en :")
                time.sleep(1)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                personaje.supervivencia = 0
                os.system ("clear")
                return 'INICIO'
            elif respuesta == "no" or "NO" or "nO":
                print ("Que tengas un buena vida. mi joven Padawan")
                time.sleep(2)
                print("¡Disfruta del mundo exterior!")
                time.sleep(10)
                os.system ("clear")
            
            else:
                print ("Que tengas un buena vida. mi joven Padawan")
                time.sleep(2)
                print("¡Disfruta del mundo exterior!")
                time.sleep(10)
                os.system ("clear")

#Presentamos la forma como se van a mostrar las opciones en pantalla
        for i in range(len(self.opciones)):
            print("[" + str(i) + "] " + self.opciones[i].descripcion)

#Hacemos un flag
        error = True

        while error:
            eleccion = input()

#Evitamos que lo que escribió el jugador sea algo diferente a numeros, porque eso sería arreglar otra cantidad de errores.
            if eleccion.isnumeric():
                #Convertimos la respuesta en un numero, porque lo que se recibía era una cadena
                eleccion = int(eleccion)

                if eleccion < len(self.opciones):
                    error = False

#Si escribe una opcion que no está dentro de lo que está, entonces, le decimos que se equivocó
            if error:
                print(Fore.RED +"¡Escribe el número de alguna de las opciones!")

#Acá acabamos la flag, y lo mandamos directamente al siguiente fragmento.
            if not error:
                return self.opciones[eleccion].siguienteFragmento

