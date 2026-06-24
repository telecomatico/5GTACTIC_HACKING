<div class="page">

# Haciendo un escaner de SCTP

\

Con SCAPY podemos crear un scaner muy simple de puertos SCTP.

Solo es necesario indicar la IP de la víctima y devuelve la lista de
puertos abiertos

<div class="codebox">

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

</div>

Un ejemplo de salida es el siguiente:

![](../images/46-1.png)

La función manda un SCTP_INIT a los puertos 1..65535:

- Los puertos cerrados, devuelven directamente un SCTP_ABORT
- Los puertos abiertos responden con un SCTP_INIT_ACK, completa el
  4-way-handshake (con COOKIE_ECHO y COOKIE_ACK) e inmediatamente libera
  la conexión con la secuencia SHUTDOWN-SHUTDOWN_ACK-SHUTDOWN_COMPLETE,
  como se muestra en la captura con el puerto 38412 (AMF/SCTP)

![](../images/46-2.png)

</div>
