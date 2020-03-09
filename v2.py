class Campeon():

    def __init__(self,nombre,vida,energia,p_habilidad,armadura,basico):
        self.nombre = nombre
        self.lista_items = ["0","0","0","0","0","0"]
        self.vida = vida
        self.energia = energia
        self.poder_habilidad = p_habilidad
        self.armadura = armadura
        self.ataque_basico = basico

   

    def mostrar_items(self):
        print('La lista de items es:',self.lista_items)

    def agregar_item(self,item):
        bolso_lleno = True
        for i in range(0,5):
            if(self.lista_items[i]=='0'):
                self.lista_items[i] = item
                bolso_lleno = False    
                self.mostrar_items()            
                break

        if(bolso_lleno):
            print('El inventario esta lleno, tiene que vender un item: ')
            self.mostrar_items()
            item_vender = input('Indique posicion del item (1-6)>> ')
            self.lista_items[int(item_vender)-1] = '0'
            self.agregar_item(item)





def help():
   print('Add -c <champ> <vida> <energia/mana> <poder_habilidad> <armadura> <danio_basico>')
   print('Add -i <champ> <item>')



def main():
    entrada = input('>> ')

    if(entrada.find('-c')):
        secuencia = entrada.split(" ")
        print('Agregando champ',secuencia[3])
        #Add -c <champ> <vida> <energia/mana> <poder_habilidad> <armadura> <danio_basico>
        champ = Campeon(secuencia[2],secuencia[3],secuencia[4],secuencia[5],secuencia[6],secuencia[7])
    #lista de campeones??

    if(entrada.find(-i)):
        secuencia = entrada.split(" ")
        champ.agregar_item(secuencia[2])


main()



#http://docs.python.org.ar/tutorial/3/classes.html
