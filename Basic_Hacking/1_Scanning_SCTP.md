<div class="page">

# HCreating an SCTP scanner

\

With SCAPY we can create a very simple SCTP port scanner.

It is only necessary to indicate the IP of the victim and it returns the list of
open ports

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

An example output is the following:

![](.../images/46-1.png)

The function sends a SCTP_INIT to ports 1..65535:

- Closed ports directly return a SCTP_ABORT
- Open ports respond with a SCTP_INIT_ACK, complete the
  4-way-handshake (with COOKIE_ECHO and COOKIE_ACK) and immediately release
  the connection with the sequence SHUTDOWN-SHUTDOWN_ACK-SHUTDOWN_COMPLETE,
  as shown in the screenshot with port 38412 (AMF/SCTP)

![](../images/46-2.png)

</div>