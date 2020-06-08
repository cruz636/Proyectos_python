import os
import pafy
import sys

def iniciar():
    if len(sys.argv) == 1:
        main()
    if len(sys.argv) == 2:

        video = pafy.new(sys.argv[1])
        print "[+] Video name: ",video.title
        #porcentaje()
        best = video.getbest()
        print "[+] See the video here :) !\n"
        print(best.url)
        exit()


def logo():
    print("#"*34)
    print("# Free use mates! Author: P0rni #")
    print("#"*34)
    print("\n")

def main():
    logo()
    url = raw_input("[>] Youtube video url: ");
    while(url != "exit"):
        video = pafy.new(url)
        print("[+] Video name: ",video.title)
        #porcentaje()
        best = video.getbest()
        print("[+] See the video here :) !")
        print(best.url)

        url = raw_input("[>] Youtube video url: ");



iniciar()
