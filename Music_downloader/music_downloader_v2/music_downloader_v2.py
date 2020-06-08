import urllib.parse
import urllib.request

def main():
    try:
        #url = 'https://www.youtube.com/results?search_query=python2'
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        #req = urllib.request.Request(url,headers = headers)
        #resp = urllib.request.urlopen(req)
        #respData = resp.read(100)

        #print(respData)

        archivo_a_guardar = "archivo.jpg"
        req = urllib.request.Request("http://www.lawebdelprogramador.com/logolwp100x25.jpg",headers = headers)
        descarga2 = urllib.request.urlopen(req)
        fichero_a_guardar=open(archivo_a_guardar,'wb')
        fichero_a_guardar.write(descarga2.read())
        fichero_a_guardar.close()

        #saveFile = open('withHeaders.html','w')
        #saveFile.write(str(respData))
        #saveFile.close()

    except Exception as e:
        print(str(e))

main()
