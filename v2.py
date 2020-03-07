class Campeon():

    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_items = ["0","0","0"]

    def vender_item(self,item):
        lista_items.remove(item)

    def mostrar_items(self):
        print("La lista de items es la siguiente: ")
        print(self.lista_items)


    def agregar_item(self,item):

        self.lista_items.append(item)

        self.mostrar_items()




Jugador1 = Campeon('Sejuani')


Jugador1.agregar_item("Espada de Doran")

#http://docs.python.org.ar/tutorial/3/classes.html
