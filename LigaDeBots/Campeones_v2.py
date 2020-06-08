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
        print('La lista de items de ',self.nombre ,'es:',self.lista_items)

    def agregar_item(self,item):
        bolso_lleno = True
        for i in range(0,5):
            if(self.lista_items[i]=='0'):
                self.lista_items[i] = item
                bolso_lleno = False
                self.mostrar_items()
                break

        if(bolso_lleno):
            print('\n[!]El inventario esta lleno, tiene que vender un item: ')
            self.mostrar_items()
            item_vender = input('Indique posicion del item (1-6)>> ')
            self.lista_items[int(item_vender)-1] = '0'
            print("[+] Se vendio el item :)")
            self.agregar_item(item)

    def eliminar_item(item):
        for i in range(0,5):
            if(self.lista_items[i]==item):
                self.lista_items[i] = '0'
                #ganar oro
    def eliminar_item(posicion):
        self.lista_items[posicion-1] = '0'






def help():
   print('Add -c <champ> <vida> <energia/mana> <poder_habilidad> <armadura> <danio_basico>')
   print('Add -i <champ> <item>')



def main():

    campeones = ['','']
    index_champs = 0
    lista_index = {}


    entrada = input('>> ')
    while(entrada!="exit()"):
        secuencia = entrada.split(" ")
        secuencia.append('/x')

        if(secuencia[1]=='-c'):

            print('Agregando champ',secuencia[2])
            #Add -c <champ> <vida> <energia/mana> <poder_habilidad> <armadura> <danio_basico>
            champ = Campeon(secuencia[2],secuencia[3],secuencia[4],secuencia[5],secuencia[6],secuencia[7])
            campeones[index_champs] = champ
            lista_index.setdefault(secuencia[2],index_champs)
            index_champs += 1


        if(secuencia[1]=='-i'):
            # add -i <champ_index/name> <item>
            campeones[int(secuencia[2])].agregar_item(secuencia[3])

        if(secuencia[0]=='show'):
            print(lista_index)

        entrada = input('>> ')


main()



#http://docs.python.org.ar/tutorial/3/classes.html
