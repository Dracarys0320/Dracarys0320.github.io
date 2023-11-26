from Model import *
from View import *

class Controller:

#Recibe como parametros el modelo y la vist que está actualizada
    def __init__(this, model, view):
        this.model = model
        this.view = view

    def updateView(self):
        pass

    def updateModel(self):
        pass