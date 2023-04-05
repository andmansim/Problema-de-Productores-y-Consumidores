# Problema-de-Productores-y-Consumidores

https://github.com/andmansim/Problema-de-Productores-y-Consumidores.git

```
from queue import Queue
from threading import Thread
import time

#creamos la cola que almacena los recursos
q = Queue(10)

#Creamos el productor
def productor(nombre):
    '''
    Añade los recursos que crea el productor a la cola
    '''
    contar = 1 
    while True:
        q.join()
        q.put(contar)
        print(f'{nombre} está produciendo el recurso {contar}')
        contar +=1
        
#Creamos el consumidor
def consumidor(nombre):    
    '''
    Coge un recurso de la cola
    '''
    contar = 1
    while True:
        a = q.get()
        print(f'El consumidor {nombre} está consumiendo el recurso {contar}')
        contar += 1
        q.task_done()
        time.sleep(1)
        
if __name__ == '__main__':
    '''
    Creamos los hilos de ambas funciones para que se ejecuten en paralelo
    '''
    t = Thread(target = productor, args = ('Productor', ))
    t1 = Thread(target = consumidor, args= ('Consumidor', ))
    t.start()
    t1.start()    


```
