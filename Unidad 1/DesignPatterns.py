#adapter
#patron estructural adapter
#clase con interfaz no compatible con el cliente

class Adaptee:
    def __init__(self):
        pass

    def request_trans(self):
        return "Petición adaptada a la interface del cleinte"
    

#clase cliente
class Client:
    def __init__(self):
        pass

    def resquest(self):
        return "Petición del cliente (no compatible con la clase adaptada)"
    

#clase adaptadora
class Adapter(Client):
    def __init__(self, adaptee:Adaptee):
        self.adaptee = adaptee

    def resquest(self):
        return self.adaptee.resquest_trans()
    
#Ejemplo de implementación del adapter
pdata_reader = Client()
word_reader =Adaptee()

print(Adapter(word_reader).resquest)

######## Strategy #######

#clase que define una estrategia en general
class Strategy:
    def execute():
        pass

#Estrategias Concretas
class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Ejecutando estrategia concreta A:")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Ejecutando estrategia concreta B:")


#La clase Context es la que permite al cliente ejecutar la estrategia correspondiente:
class Context:
    def __init__(self, strategy:Strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.execute()

#Ejemplo de uso del patrón strategy:
strategyA = ConcreteStrategyA()
contexto_str1 = Context(strategyA)
result_str1 = contexto_str1.execute_strategy()

#Usando la estrategia B
strategyB = ConcreteStrategyB()
contexto_str2 = Context(strategyB)
result_str2 = contexto_str2.execute_strategy()