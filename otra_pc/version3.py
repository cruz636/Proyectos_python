from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import os

global private_key
global public_key

global userId
#el userId nos va a servir para guardar nuestras llaves publica y privada
userId = input("Ingrese su nombre de sesion: ")

def crearLlavePrivada():
	#creamos llave privada 
	private_key = rsa.generate_private_key(
		public_exponent = 65537,
		key_size=2048,
		backend = default_backend()
	)

	#guardamos la llave en un fichero.pem

	pem = private_key.private_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PrivateFormat.PKCS8,
		encryption_algorithm=serialization.NoEncryption()
		)

	with open('private_key_'+userId+'.pem', "wb") as pem_out:
		pem_out.write(pem)
	print("[+] Llave privada guardada con exito!")
	print("Nombre: private_key_"+userId+".pem")
	cargarLlavePrivada("private_key_"+userId)
	

def cargarLlavePrivada(nombreFichero):
	global private_key
	#leemos fichero.pem con la llave privada guardada

	with open(nombreFichero+'.pem','rb') as key_file:
		private_key = serialization.load_pem_private_key(
			key_file.read(),
			password = None,
			backend=default_backend()
		)

	print("Llave privada cargada con exito!")

	#cargamos la llave publica de la llave privada
	public_key = private_key.public_key()
	
	#guardamos la llave publica en un archivo "public_key_[userId].pem"
	pem = public_key.public_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PublicFormat.SubjectPublicKeyInfo
		)
	
	with open("public_key_"+userId+".pem", "wb") as pem_out:
		pem_out.write(pem)
	print("[+] Llave publica guardada con exito!")
	


def cargarLlavePublica():
	#cargamos llave publica con la que vamos a cifrar
	global pubKey
	nombreFichero = input("ingrese la llave publica (sin la extencion) : ")
	pubKey = load_pem_public_key(open(nombreFichero+'.pem','rb').read(),default_backend())


def cifrarTexto(plainText):
	global userId
	#lo pasamos a binario al texto plano
	plainText = plainText.encode()
	#ciframos el texto
	cipherText = pubKey.encrypt(
		plainText,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA1()),
			algorithm=hashes.SHA1(),
			label=None
			)
		)
	print("Texto cifrado! ")
	print("Guardandolo en fichero cifrado"+userId+".txt")
	with open('cifrado'+userId+'.txt','wb') as w:
		w.write(cipherText)
	print("Fichero guardado!")


def desencriptarTexto(textCipherFile):
	global private_key
	#abrimos archivo con texto cifrado
	with open(textCipherFile,'rb') as w:
		textoCifrado = w.read()
	#desciframos el texto
	plainText = private_key.decrypt(
		textoCifrado,
		padding.OAEP(
			mgf = padding.MGF1(algorithm=hashes.SHA1()),
			algorithm = hashes.SHA1(),
			label = None
			)
		)

	print('Texto desencriptado: \n')
	print(plainText.decode())


def main():
	
	global pubKey
	global userId
	os.system('cls')
	print('#'*(len(userId)+13))
	print('  UserId: '+ userId)
	print('#'*(len(userId)+13)+'\n')
	print('1- Cargar llave privada.')
	print('2- Crear llave privada.')
	print('3- Cifrar texto con llave publica.')
	print('4- Descifrar texto con llave privada.')
	print('0- SALIR')

	opc = input("\nElija una opcion:")
	opc = int(opc)
	if(opc==1):
		nombreFichero = input("Ingrese el nombre del fichero ( sin la extencion): ")
		cargarLlavePrivada(nombreFichero)
	if(opc==2):
		crearLlavePrivada()
	if(opc==3):
		cargarLlavePublica()
		plainText = input("Texto para encriptar con llave publica>> ")
		cifrarTexto(plainText)
	if(opc==4):
		nombreFichero = input("ingrese el nombre del fichero cifrado (sin la extencion): ")
		desencriptarTexto(nombreFichero+'.txt')		

	if(opc==0):
		exit()

	input('\n\nPresione ENTER para continuar >>')
	main()

if __name__ == '__main__':
	main()
