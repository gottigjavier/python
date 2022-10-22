# Utilizar intérprete de Python 3.x o superior para salida por terminal. Sino pueden aparecer caracteres raros o lanzar errores de tipo charset="UTF-8"


numero_original = 58184241583791680
multiplicador_17cifras = 100000000000000000
divisor = 2017
resto_no_repetido = True
contador_iteraciones = 0
control_max_iter = 10000
resto = 0
resto_como_elem_lista = [resto]
lista_restos_str = str(resto_como_elem_lista)

def setResto():
    resto = 0
    return 

# Se traslada el resto previo 17 lugares hacia la izquierda y se le suma en número original
def agregarDividendoAlResto (p_resto, p_multiplicador_17cifras, p_numero_original):
    return (p_resto * p_multiplicador_17cifras) + p_numero_original

def newResto(p_resto_mas_numero_original, p_divisor):
    return p_resto_mas_numero_original % p_divisor

def agregarRestoaLista():
    return lista_restos_str + str(resto_como_elem_lista)


print("Este programa resuelve el desafío de encontrar el resto (residuo, módulo) \nde la división entre el número 58184241583791680 concatenado 58184241583791680 veces \n(casi 3.390.000.000.000.000.000.000.000.000.000.000 cifras) \ny el número 2017")


while resto_no_repetido:
    contador_iteraciones+=1
    resto_mas_numero_original = agregarDividendoAlResto(resto, multiplicador_17cifras, numero_original)
    resto = newResto(resto_mas_numero_original, divisor)
    resto_como_elem_lista = [resto]
    if str(resto_como_elem_lista) in lista_restos_str or contador_iteraciones > control_max_iter: # Se evalúa el contador para evitar un posible ciclo infinito
        resto_no_repetido = False
    else:
        lista_restos_str = agregarRestoaLista()

iteraciones_remanentes = numero_original % contador_iteraciones
setResto()


for i in range(0,iteraciones_remanentes):
    resto_mas_numero_original = agregarDividendoAlResto(resto, multiplicador_17cifras, numero_original)
    resto = newResto(resto_mas_numero_original, divisor)

print("\nEl Resto o Módulo final de la división es: ", resto)

print("\n Fin del Programa")