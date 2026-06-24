<div class="page">

# WireGuard en routers Mikrotik

\

You have to do the installation in each part at the same time, or
create the private and public keys first... If we don't want to create them:

On Node 1 we create the Wireguard interface, without specifying a key
private:

<div class="codebox">

/interface wireguard add name=wg0 listen-port=51820

</div>

Now we can go to Winbox and copy the public key of node 1
(public_key_A).

On node 2 we repeat the process, but without specifying the port:

<div class="codebox">

/interface wireguard add name=wg0

</div>

We copy the public key of node 2 (public_key_B)

We return to node 1:

We create the virtual interface “wg0” on node 1

<div class="codebox">

/ip address add address=10.0.0.1/24 interface=wg0

</div>

We add the Peer, using B's public key:

<div class="codebox">

/interface wireguard peers add interface=wg0 public-key="public_key_B" allowed-address=10.0.0.2/32

</div>

Now on node 2:

We create the virtual interface "wg0":

<div class="codebox">

ip address add address=10.0.0.2/24 interface=wg0

</div>

And we add the Peer, using the public_key_A, as well as the
PUBLIC_IP_ROUTER_A:

<div class="codebox">

/interface wireguard peers add interface=wg0 public-key="public_key_A" allowed-address=10.0.0.1/32 endpoint-address=IP_PUBLICA_ROUTER_A endpoint-port=51820

</div>

It works perfectly!

</div>