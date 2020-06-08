#Va a estar desarrollado en Python 3
import sys
from pytube import YouTube

def main():

    if( len(sys.argv)>1):
        print("Bienvenido!")
        if(sys.argv[1]=='-v'):
            descargar(sys.argv[2])
            exit(0)
        if(sys.argv[1]=="-l"):
            print("Abriendo archivo  ",sys.argv[2])
            exit(0)
    if(len(sys.argv)==1):
        print("\nNo estas pasando bien los parametros!\n")
        print("python3 music_downloader.py -[opcion] [url o archivo.txt]")
        print("Opciones: ")
        print("-v: descarga una sola cancion que se le pasa por parametro")
        print("-l: descarga varias canciones de una lista que esta en un archivo .txt")

def descargar(url):
    video = YouTube(url)
    #print("[+] puntuacion del video: ",video.rating)
    try:
        print("[+] Descargando cancion")
        video.streams.last().download()

    except:
        print("[-] Error al descargar la cancion")
        print("Error inesperado:", sys.exc_info()[0])


#https://www.youtube.com/watch?v=12MkmNKRYu4



main()
