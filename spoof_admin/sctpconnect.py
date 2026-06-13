import sctp
import socket

# Configura la dirección y el puerto del servidor
server_address = ('10.10.10.155', 38412)

# Crea un socket SCTP
sock = sctp.sctpsocket_tcp(socket.AF_INET)

# Conéctate al servidor
sock.connect(server_address)

print("Conectado al servidor SCTP")

# Envía datos al servidor
sock.sctp_send(b"Hola, servidor SCTP")

# Recibe datos del servidor
data = sock.recv(1024)
print(f"Datos recibidos: {data}")

# Cierra la conexión
sock.close()
