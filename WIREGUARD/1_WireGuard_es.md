<div class="page">

# WireGuard

\

1.  ## ¿Qué es WireGuard?

WireGuard es un protocolo VPN moderno que opera en el **nivel de red
(capa 3)**. Está diseñado para ser:

- **Simple**: configuración minimalista.
- **Seguro**: usa criptografía moderna.
- **Rápido**: muy eficiente, incluso en dispositivos con pocos recursos.

1.  2\.

    ## 2. Protocolos y criptografía que utiliza

WireGuard no usa protocolos tradicionales como IPsec o TLS. En su lugar,
implementa su propio conjunto de protocolos criptográficos:

| Función                      | Algoritmo                          |
|------------------------------|------------------------------------|
| Intercambio de claves        | Curve25519 (clave pública/privada) |
| Cifrado de datos             | ChaCha20                           |
| Autenticación de datos       | Poly1305                           |
| Hashing                      | BLAKE2s                            |
| Derivación de claves         | HKDF (basado en BLAKE2s)           |
| Protección contra repetición | Recuento de paquetes + nonce       |

1.  3\.

    ## 3. Proceso de establecimiento del túnel

WireGuard no tiene un "handshake" complejo como IPsec o TLS. El proceso
es **muy eficiente** y se basa en el intercambio de claves públicas.

- **Configuración inicial**:
- Cada nodo tiene una **clave privada** y una **clave pública**.
- Se define una lista de **peers** con sus claves públicas y direcciones
  IP permitidas.

<!-- -->

- **Inicio de comunicación**:
- Cuando un nodo quiere enviar tráfico, envía un paquete cifrado usando
  la clave pública del peer.
- Si el peer no ha visto al otro recientemente, responde con un
  **handshake**.

<!-- -->

- **Handshake (cada 2 minutos o cuando es necesario)**:
- Se intercambian claves efímeras para derivar claves de sesión.
- Se usa **Curve25519 + HKDF** para derivar claves de cifrado.
- El handshake es **stateless** y muy rápido (~1 RTT).

<!-- -->

- **Transmisión de datos**:
- Los paquetes se cifran con **ChaCha20** y se autentican con
  **Poly1305**.
- Cada paquete incluye un **nonce** para evitar repeticiones.

<!-- -->

- **Keepalive**:
- Si no hay tráfico, se envía un paquete vacío cada 25 segundos
  (`PersistentKeepalive`) para mantener NAT abierto.

1.  4\.

    ## 4. ¿Qué transporta WireGuard?

WireGuard encapsula paquetes IP dentro de **UDP**. Por defecto usa el
puerto `51820/udp`, pero puede configurarse.

1.  5\.

    ## 5. Diferencias con IPsec y OpenVPN

| Característica | WireGuard | IPsec           | OpenVPN                        |
|----------------|-----------|-----------------|--------------------------------|
| Criptografía   | Moderna   | Variable        | Variable                       |
| Rendimiento    | Alto      | Medio           | Bajo                           |
| Configuración  | Simple    | Compleja        | Moderada                       |
| Protocolo base | UDP       | IPsec (ESP/IKE) | TCP/UDP                        |
| Kernel support | Sí        | Sí              | No (normalmente en user-space) |

1.  6\.

    ## 6. Configuración Base:

d[![](images/136-1.png)](https://www.zenarmor.com/docs/assets/images/figure-1-wireguardp2pvpntopology-452e7a073da12769cdd9e6530d5da284.png)

</div>
