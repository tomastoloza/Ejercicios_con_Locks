import threading


class ColaFIFO:

    def __init__(self, max_size):
        self.max_size = max_size
        self.elementos = []
        self.lock = threading.Lock()

    def insertar(self, dato):
        # self.lock.acquire()
        # try:
        if len(self.elementos) > self.max_size:
            print("max stack size reached\n")
        self.elementos.append(dato)
        return dato

    # finally:
    #     self.lock.release()

    def extraer(self):
        # self.lock.acquire()
        # try:
        if len(self.elementos) > 0:
            return self.elementos.pop(0)
        else:
            print("no elements to pop\n")
        # finally:
        #     self.lock.release()

    def ultimo(self):
        return self.elementos[-1]

    def primero(self):
        return self.elementos[0]

    def cola_vacia(self):
        return len(self.elementos) == 0

    def cantidad_elementos(self):
        return len(self.elementos)
