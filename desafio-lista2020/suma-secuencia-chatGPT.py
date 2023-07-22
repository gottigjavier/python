import time

inicio = time.time()

ciclos = 0
no_hay_repeticiones = True
demasiadas_iteraciones = 500000

lista = [1, 2, 3]
conj_listas = {str(lista): sum(lista)}

while no_hay_repeticiones or ciclos > demasiadas_iteraciones:
    ciclos += 1
    nuevo_elemento = sum(lista) % 10000
    lista = [lista[1], lista[2], nuevo_elemento]
    conj_listas_str = str(lista)
    if conj_listas_str in conj_listas:
        no_hay_repeticiones = False
    else:
        conj_listas[conj_listas_str] = nuevo_elemento

tiempo_ejecucion = time.time() - inicio

if no_hay_repeticiones:
    print("No se encontraron repeticiones en el rango de búsqueda.")
else:
    ultima_repeticion = list(conj_listas.keys())[-1]
    print(f"La última repetición se encontró en la iteración {ciclos}: {ultima_repeticion}")
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.2f} segundos.")
