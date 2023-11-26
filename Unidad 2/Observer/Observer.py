#clase publisher se encarga de actualizar o notificar a los subscriptores

class Publisher:

    # inicializar lista de observadores
    def __init__(self):
        self._observers = []

    def addSubscriber(self, newSubscriber):
        self._observers.append(newSubscriber)

    def removeSubscriber(self, subscriber):
        self._observers.remove(subscriber)

    def notifySubscribers(self, message):
        # enviar mensaje a todos los suscriptores en la lista
        for subscriber in self._observers:
            subscriber.update(message)