from cmath import sqrt
from math import trunc
import time
import sys

print("Determinar si un numero es PRIMO o COMPUESTO")

invalido = True
is_primo = True

while invalido:
    try:
        # Acepta hasta 308 cifras en mi sistema!!
        n = int(input('Ingrese un numero: '))
        invalido = False 
    except:
        print('Algun dato no es valido. Intente nuevamente')

n_sqrt = trunc(abs(sqrt(n))) + 1
print("sqrt ", n_sqrt) 

print("Tamaño del dato de entrada asignado por el sistema: ",sys.getsizeof(n), " bytes, tipo: ", type(n))



tinicio=time.time()

for i in range(2,n_sqrt):
    if n % i == 0:
        is_primo = False
        break

if is_primo:
    print("El numero ", n , " es PRIMO")
else:
    print("El numero ", n , " es COMPUESTO")

tfinal=time.time()

tiempo_proceso = round(tfinal-tinicio,0)

print("\n El proceso demoró " + str(tiempo_proceso), " segundos.")