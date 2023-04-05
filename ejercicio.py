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

def consumidor(nombre):    
    contar = 1
    while True:
        a = q.get()
        print(f'El consumidor {nombre} está consumiendo el recurso {contar}')
        contar += 1
        q.task_done()
        time.sleep(1)
        
if __name__ == '__main__':
    t = Thread(target = productor, args = 'Patata')
    t1 = Thread(target = consumidor, args= 'Xiao')
    t.start()
    t1.start()    
