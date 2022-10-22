# Utilizar intérprete de Python 3.x o superior para salida por terminal. Sino pueden aparecer caracteres raros o lanzar errores de tipo charset="UTF-8"
import time
from io import open

tinicio=time.time()

ciclos=0
no_hay_repeticiones=True
demasiadas_iteraciones=500000
posision_final=2020202020202020
lista=[1,2,3]
conj_listas=str(lista)

def resetLista():
    lista=[1,2,3]
    conj_listas=str(lista)

def sumar (lista):
    return (lista[0]+lista[1]+lista[2]) % 10000 # Se utilizan solo los 4 últimos dígitos

def ordenar (lista):
    lista[0]= lista[1]
    lista[1]= lista[2]
    lista[2]= nuevo_elemento
    return lista

def archivar(conj_listas):
    archivo=open("salida_lista.txt", "w")
    archivo.write("Comienzo del bloque que se repite 16291951775 veces cada 124000 iteraciones \n")
    archivo.write(conj_listas)
    archivo.write("\n Final del bloque que se repite \n \n \n")
    archivo.close() 


def agregar(conj_listas):
    conj_listas= conj_listas+str(lista) # Para que se incluya la última tríada
    archivo=open("salida_lista.txt", "r+")
    archivo.seek(len(archivo.read()))
    archivo.write("Comienzo de la lista remanente \n")
    archivo.write(conj_listas)
    archivo.write("\n Fin de las listas")
    archivo.close()

print("Este algoritmo da solución al siguiente problema:\nUna computadora comienza imprimiendo los números 1, 2 y 3. \nLuego continúa imprimiendo sin parar la suma de los últimos 3 números que imprimió: 6, 11, 20, 37, 68, ... \n¿Cuales son los últimos 4 dígitos del número impreso en la posición 2020202020202020? \nPor ejemplo, en la posición 30, está impreso el número 45152016 que termina en 2016.\n\n")

print("Solución ---> Comienzo \n\n")

print("Debido a la gran cantidad de datos, con la tecnología actual es imposible correr la secuencia completa porque podría demorar miles de años. \nSí es muy posible que la secuencia se repita.\nDependiendo de su equipo esto puede tardar un par de minutos.\n")
print("Si no se encuentran repeticiones en un lapso aceptable el programa se detendrá y se podrá elegir extender el rango de búsqueda.\n")
print("-- Buscando repeticiones -- Espere -->\n")


while no_hay_repeticiones or ciclos>demasiadas_iteraciones: # La segunda condición es una proteccion por si no se hallan repeticiones 
    ciclos+=1
    nuevo_elemento= sumar(lista)
    lista = ordenar(lista)
    if str(lista) in conj_listas: # Buscando si se repite la lista
        no_hay_repeticiones=False
    else:
        conj_listas= conj_listas+str(lista) # Actualiza el conjunto de listas




ciclos_remanentes = posision_final % ciclos
cant_repeticiones= (posision_final-ciclos_remanentes)//ciclos

# Si encuentra repeticiones antes de un lapso prudete entrará en el siguiente if, sino ira al elif en el final del código mostrando un mensaje para extender el rango de búqueda de repeticiones. 

if not no_hay_repeticiones:
    print("\nSe encontró que el ciclo se repite "+ str(cant_repeticiones)+ " veces cada "+ str(ciclos)+ " iteraciones\n") 
    print("El bloque repetido sigue siendo demasiado grande para presentarlo por pantalla\npor lo que se guardó en el archivo salida_lista.txt en este mismo directorio\n")
    print("\nContinuando con el ciclo no repetido...")
    
    # Una vez encotrado el bloque que se repite, se lo guarda, se descartan los próximos bloques repetidos, se resetea la lista a [1,2,3] y se sigue hasta el final de la secuencia. 
    
    archivar(conj_listas)
    resetLista()

    for i in range(3,ciclos_remanentes): # Arranca en 3 porque las tres primeras posiciones estan ocupadas por los elementos de la lista --> [1,2,3]
        ciclos+=1
        nuevo_elemento= sumar(lista)
        lista = ordenar(lista)
        conj_listas= conj_listas+str(lista)

    agregar(conj_listas) # Se agrega el bloque final que no se repite

    print("\nLos cuatro últimos dígitos de la nuevo_elemento en la posición " + str(posision_final) + "\nson: ", nuevo_elemento)

    print("\nEl boque final de agregó al archivo salida_lista.txt \n")

    tfinal=time.time()

    tiempo_proceso = round(tfinal-tinicio,0)

    print("\n El proceso demoró " + str(tiempo_proceso), " segundos.")

    print(" Fin del programa.")
elif ciclos>demasiadas_iteraciones:
    print("\nNo se encontraron repeticiones en " + str(demasiadas_iteraciones) + " repeticiones.\nPuede extender la búqueda cambiando el valor de la variable < demasiadas_iteraciones > en el archivo fuente del programa")