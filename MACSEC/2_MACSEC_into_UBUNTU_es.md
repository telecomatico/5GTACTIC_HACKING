<div class="page">

# MACSEC en UBUNTU

\

(fuente principal: [MACsec Explained and Configuration Example - Learn
Duty](https://learnduty.com/network-techs/macsec-explained-and-configuration-example/))

MACsec (estándar IEEE 802.1AE) es un estándar de seguridad de red que
opera en la Capa 2 (capa MAC) y define la confidencialidad e integridad
de los datos sin conexión para protocolos independientes del acceso al
medio.

Es similar a la trama Ethernet, pero incluye campos adicionales:

![](../images/50-1.png)

El campo MACsec Ethertype tiene una longitud de 2 bytes, al igual que el
campo Ethertype normal. Su valor es 0x88e5 para indicar que se trata de
una trama MACsec:

- • <span style="indent:1;">• ICV: El ICV proporciona la comprobación de
  integridad de la trama y suele tener una longitud de 8 a 16 bytes,
  dependiendo del conjunto de cifrado. Las tramas que no coinciden con
  el ICV esperado se descartan en el puerto.</span>
- <span style="indent:1;">SecTAG: La etiqueta de seguridad tiene una
  longitud de 8 a 16 bytes e identifica la clave SAK que se utilizará
  para la trama. Con la codificación SCI (Identificador de Canal
  Seguro), la etiqueta de seguridad tiene una longitud de 16 bytes; sin
  codificación, tiene una longitud de 8 bytes. TCI/AN: El tercer octeto
  corresponde al campo de Información de Control de Etiqueta
  (TCI)/Número de Asociación. El TCI designa el número de versión de
  MACsec si se utilizan únicamente la confidencialidad o la
  integridad.</span>
- <span style="indent:1;">SL: El cuarto octeto corresponde a la longitud
  corta, que corresponde a la longitud de los datos cifrados.</span>
- <span style="indent:1;">PN: Los octetos del 5 al 8 representan el
  número de paquete y se utilizan para la protección contra la
  reproducción y la construcción del vector de inicialización (junto con
  el identificador de canal seguro \[SCI\]).</span>
- <span style="indent:1;">SCI: Los octetos del 9 al 16 representan el
  identificador de canal seguro. Cada asociación de conectividad (CA) es
  un puerto virtual, y a cada puerto virtual se le asigna un
  identificador de canal seguro, que es la concatenación de la dirección
  MAC de la interfaz física y un ID de puerto de 16 bits.</span>

## Terminología MACsec

- • <span style="indent:1;">• MKA (Acuerdo de Clave MACsec): protocolo
  de acuerdo de claves para descubrir pares MACsec y negociar claves.
  Representa el protocolo de control entre pares MACsec.</span>
- <span style="indent:1;">CA (Asociación de Conectividad): relación de
  seguridad establecida y mantenida por protocolos de acuerdo de claves
  (MKA). La clave de cifrado utilizada por los participantes de la CA se
  denomina CAK (clave de asociación de conectividad).</span>
- <span style="indent:1;">CAK (Clave de Asociación de Conectividad):
  clave primaria de larga duración utilizada para generar todas las
  demás claves utilizadas para MACsec.</span>

<span style="indent:1;"></span>

<span style="indent:1;"></span>

<span style="indent:2;">Tras generar la CAK, se obtienen dos
claves:</span>

- • <span style="indent:3;">• Clave de Cifrado de Clave (KEK): clave
  para proteger y cifrar las claves MACsec (cifrar la SAK).</span>
- <span style="indent:3;">Clave de Conexión de Integridad (ICK): clave
  para comprobar la integridad de cada MKPDU enviada entre dos pares. Se
  etiqueta en cada trama de datos/control para demostrar que la trama
  proviene de un par autorizado.</span>
- <span style="indent:1;">CKN (Nombre de Clave CAK): se utiliza para
  configurar el valor de la clave o CAK. Solo se permiten hasta 64
  caracteres hexadecimales. El CKN identifica el CAK.</span>

MACsec es compatible con los kernels de Linux a partir de la versión
4.6.

Para comprobar la versión del kernel:

<div class="codebox">

    uname -r

</div>

Para ver si ese kernel soporta MACSEC:

<div class="codebox">

    grep -i macsec /boot/config-6.6.11_1 

</div>

<span style="color:#0a0a0a;"></span>

<span style="color:#0a0a0a;">Si devuelve CONFIG_MACSEC=m</span>, el
kernel es más que suficiente.

ATAJO: Para comprobar si el módulo MACsec está disponible también es
posible utilizando el comando modprobe, intentando cargar el módulo
MACsec. Si el módulo se carga sin errores, el kernel soporta MACsec.

<div class="codebox">

    sudo modprobe macsec

</div>

Para verificar que el módulo está cargado:

<div class="codebox">

    lsmod | grep macsec

</div>

## Herramientas asociadas

El paquete macsec-tools incluye varias herramientas útiles para
configurar y gestionar MACsec en sistemas Linux.

<div class="codebox">

    sudo apt-get install macsec-tools

</div>

Aquí tienes una lista de algunas de las herramientas principales que
puedes encontrar en este paquete 1:

- • <span style="indent:1;">• macsec: Utilidad principal para configurar
  y gestionar interfaces MACsec.</span>
- <span style="indent:1;">ip macsec: Comando de la herramienta ip que
  permite añadir, modificar y eliminar configuraciones MACsec en
  interfaces de red.</span>
- <span style="indent:1;">wpa_supplicant: Aunque no es parte directa de
  macsec-tools, se utiliza frecuentemente en combinación con MACsec para
  gestionar la autenticación y el cifrado.</span>

Estas herramientas te permiten configurar la seguridad de capa 2 en tus
interfaces de red, asegurando que la comunicación entre tus máquinas
virtuales esté cifrada y autenticada.

</div>
