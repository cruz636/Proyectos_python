Req: Linux

goodbyeLenny.py es un script en python 3.x para inhabilitar la conexión de wifi de uno o todos los dispositivos de una red wifi. 
No es necesario estar conectado a la red wifi que se desea atacar ( o saber su contraseña) . El script envia cantidades industriales de
paquetes hacia los dispositivos elegidos con mensajes para que se desconecten.


Guia de Usuario:
Al iniciar el script, nuestra tarjeta de red se pondrá en modo monitor ( es necesario que soporte ponerse en este modo). Elegimos
la interfaz con la que deseamos trabajar. Luego nos mostrará las redes a las que podemos atacar. Debemos poner su BSSID, luego 
el canal ( CH ) . A continuación empezaremos a recoger paquetes que se envian en esa red, para identificar los dispositivos conectados.
Esperamos unos minutos y tocamos Ctrl+C para frenar la recopilación de información. Nos van a aparecer las MacAddress de los dispositivos,
y legimos nuestra víctima copiando su MACAddress (o ponemos 0 para atacar a todos los dispositivos). También hay que copiar la BSSID
de la red wifi ( en próximas versiones se automatizará esto). Una vez cargados todos esos datos, comenzamos el ataque. Para frenarlo,
tocamos nuevamente Ctrl+C, lo que también cambiará el modo de nuestra tarjeta de red nuevamente.
