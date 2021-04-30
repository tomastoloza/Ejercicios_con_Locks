import random
import threading
import time

from ColaFIFO import ColaFIFO

stack = ColaFIFO(10)


def prod(cola, sleep):
    while True:
        i = random.randint(1, 100)
        cola.insertar(i)
        print(f"Se insertó {i}\n")
        time.sleep(sleep)


def cons(cola, sleep):
    while True:
        i = random.randint(1, 100)
        cola.extraer()
        print(f"Se extrajo {i}\n")
        time.sleep(sleep)


p1 = threading.Thread(target=prod, args=(stack, 1))
c1 = threading.Thread(target=cons, args=(stack, 1))

if __name__ == '__main__':
    p1.start()
    c1.start()

# cuando la cola se quedó sin elementos para popear, Falló el hilo consumidor y dejó de ejecutarse por lo que solo
# funciona mientras que haya elementos para popear

# una vez implemetadas las verificaciones se observa estabilidad entre los hilos
