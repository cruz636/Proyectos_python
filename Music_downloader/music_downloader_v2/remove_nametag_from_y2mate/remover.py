#this program will remove the tag that y2mate add
# to the name when you download it
# Linux version

import os

def main():
    print( "Eliminando tag..")
    try:
        recorrer_directorio()
        print("Finalizado con exito!")
    except error:
        print("Ocurrio un error :(",error)

def recorrer_directorio():
    listar_canciones = os.listdir()

    for cancion in listar_canciones:
        if (cancion[:10] == "y2mate.com"):
            nombre_nuevo = cancion[12:]
            os.rename(cancion,nombre_nuevo)


main()
