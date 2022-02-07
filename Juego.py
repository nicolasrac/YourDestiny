import io

from Opcion import Opcion
from Escenario import Escenario
from Personaje import Personaje

#Iniciar los objetos
personaje = Personaje()
#Incialmente, el escenario está vacio, o no hay
escenarioActual = None
final = False
#Iniciamos escenarios como un diccionario vacío
escenarios = {}

#Iniciamos a leer el archivo de texto. Cambiamos el encoding para que salgan todos los signos del español.
with io.open('urdestiny.txt', 'r', encoding='utf8') as archivo:
    

#PAra empezar desde la linea 0
    archivo.seek(0)
    #Para converitr todo en una cadena de texto
    contenido = archivo. read()

 #Le pedimos a python que corte todo nuestro archivo txt en partes según el criterio que le pasamos 
    partes = contenido.split("#")

#Hacemos un bucle for que recorra toda el arreglo que quedó antes en "partes", para que automáticamente recorra las partes
    for p in range(len(partes)):

#Comprobación de errores para no leer archivos vacios
        if len(partes[p]) > 0:

#Acá separamos todo otra vez para tenerlo todo como queremos. Es decir, según el criterio del * y del |
            escenario = partes[p].split("*")
            #Le pasamos el indice 0 porque para python, el primer indice es 0. En nuestro caso, 0 es la descripción del escenario.
            partesEscenario = escenario[0].split("|")


#Ahora vamos a describir todo lo relacionado con las opciones del juego.
            opciones = []
#Hacemos exactamento lo mismo que hicimos con los escenarios, pero ahora enfocado a las opciones.
# La diferencia principal es que los escenarios se inicializan como diccionarios y la opciones como listas.
            for e in range(len(escenario)):

                if e > 0:
                    partesOpcion = escenario[e].split("|")
                    #Aquí lo que le estamos pidiendo a python es que cuando nos entregue una opción, nos entregue el indicie 0, que es el nombre de la opción.
                    #Y el indice 1, que es su descripción.
                    #El rstrip es para quitarle cualquier tipo de salto de linea, y así nos ahorramos errores.  
                    o = Opcion(partesOpcion[1].rstrip(), partesOpcion[0])
                    #Lo que estamos creando aquí es algo así como un historial, donde usamos append para llenar la lista que inicialmente estaba vacía.
                    opciones.append(o)

#Ya estamos ultimando detalles, entonces le pedimos a python que nos entregue la descripción, más las opciones
            e = Escenario (partesEscenario[1], opciones)

            #Aquí preguntamos si tenemos un cambio de supervivencia, porque hay veces que no lo tiene, por lo tanto es necesario hacernos cargo de esto.
            if 2 < len(partesEscenario):

                e.cambioSupervivencia = int(partesEscenario[2])
                #Esto lo hacemos para inicializar el juego, entoces e, guardará toda la informacion que necesitemos. 
                #Como vemos, el diccionario se va llenando, y esa es nuestra fuente de informacion.
            escenarios[partesEscenario[0]] = e

#Asignamos INICIO como nuestro escenario inicial, para no tener nungún problema
escenarioActual = escenarios['INICIO']

#Creamos un bucle infinito, para que el juego siempre corra a menos que nosotros digamos lo contrario
while not final:
    siguiente = escenarioActual.presentar(personaje)
    escenarioActual = escenarios[siguiente] 