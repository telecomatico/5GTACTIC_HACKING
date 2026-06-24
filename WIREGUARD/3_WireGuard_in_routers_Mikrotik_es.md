<div class="page">

# WireGuard en routers Mikrotik

\

Hay que ir haciendo la instalación en cada parte al mismo tiempo, o
crear las claves privadas y públicas primero... Si no queremos crearlas:

En el Nodo 1 creamos el interface de Wireguard, sin especificar clave
privada:

<div class="codebox">

    /interface wireguard add name=wg0 listen-port=51820 

</div>

Ahora podemos ir a Winbox y copiar la clave pública del nodo 1
(clave_publica_A).

En el nodo 2 repetimos el proceso, pero sin especificar el puerto:

<div class="codebox">

    /interface wireguard add name=wg0

</div>

Copiamos la clave pública del nodo 2 (clave_publica_B)

Volvemos al nodo 1:

Creamos la interfaz virtual “wg0”en el nodo 1

<div class="codebox">

    /ip address add address=10.0.0.1/24 interface=wg0

</div>

Añadimos el Peer, usando la clave pública del B:

<div class="codebox">

    /interface wireguard peers add interface=wg0 public-key="clave_publica_B" allowed-address=10.0.0.2/32

</div>

Ahora en el nodo 2:

Creamos la interfaz virtual "wg0":

<div class="codebox">

    ip address add address=10.0.0.2/24 interface=wg0

</div>

Y añadimos el Peer, usando la clave_publica_A, así como la
IP_PUBLICA_ROUTER_A:

<div class="codebox">

    /interface wireguard peers add interface=wg0 public-key="clave_publica_A" allowed-address=10.0.0.1/32 endpoint-address=IP_PUBLICA_ROUTER_A endpoint-port=51820

</div>

Queda perfectamente funcionando!

</div>
