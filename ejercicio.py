from queue import Queue
from threading import Thread
import time

#creamos la cola que almacena los recursos
q = Queue(10)
def productor(nombre):
    contar= 1
    while True:
        q.join()
        q.put(contar)
        print(f'{nombre} está produciendo el recurso {contar}')
        contar +=1
