class Campeon():

    def __init__(self,nombre,lista):
        self.nombre = nombre
        self.lista_items = lista

    def vender_item(self,item):
        lista_items.remove(item)

    def agregar_item(self,item):
        agregado = False
        index = 0
        while(agregado != True and index < 7):
            if(self.lista_items(index)=="0"):
                self.lista_items.insert(index,item)
                agregado = True
            index = index + 1
        if(agregado == False):
            print("Debe vender un item para tener lugar")
            item_vender = raw_input("Elija un item para vender>> ")
            vender_item(self,item_vender)
            agregar_item(self,item)


        mostrar_items(self)


    def mostrar_items(self):
        print("La lista de items es la siguiente: ")
        print(self.lista_items)



Jugador1 = Campeon('Sejuani',["0","0","0","0","0","0"])


Jugador1.agregar_item("Espada de Doran")
