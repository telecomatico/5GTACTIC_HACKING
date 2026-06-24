<div class="page">

# WireGuard

\

1. ## What is WireGuard?

WireGuard is a modern VPN protocol that operates at the **network level
(layer 3)**. It is designed to be:

- **Simple**: minimalist configuration.
- **Secure**: uses modern cryptography.
- **Fast**: very efficient, even on devices with few resources.

1. 2\.

    ## 2. Protocolos y criptografía que utiliza

WireGuard does not use traditional protocols such as IPsec or TLS. Instead,
implements its own set of cryptographic protocols:

| Function | Algorithm |
|----------------------------------|-----------------------------------|
| Key exchange | Curve25519 (public/private key) |
| Data encryption | ChaCha20 |
| Data authentication | Poly1305 |
| Hashing | BLAKE2s |
| Key derivation | HKDF (based on BLAKE2s) |
| Replay Protection | Packet count + nonce |

1. 3\.

    ## 3. Proceso de establecimiento del túnel

WireGuard does not have a complex handshake like IPsec or TLS. The process
It is **very efficient** and is based on public key exchange.

- **Initial configuration**:
- Each node has a **private key** and a **public key**.
- A list of **peers** is defined with their public keys and addresses
  Allowed IPs.

<!-- -->

- **Communication start**:
- When a node wants to send traffic, it sends an encrypted packet using
  the peer's public key.
- If the peer has not seen the other recently, respond with a
  **handshake**.

<!-- -->

- **Handshake (every 2 minutes or when necessary)**:
- Ephemeral keys are exchanged to derive session keys.
- **Curve25519 + HKDF** is used to derive encryption keys.
- The handshake is **stateless** and very fast (~1 RTT).

<!-- -->

- **Data transmission**:
- Packets are encrypted with **ChaCha20** and authenticated with
  **Poly1305**.
- Each package includes a **nonce** to avoid repetitions.

<!-- -->

- **Keepalive**:
- If there is no traffic, an empty packet is sent every 25 seconds
  (`PersistentKeepalive`) to keep NAT open.

1. 4\.

    ## 4. ¿Qué transporta WireGuard?

WireGuard encapsulates IP packets within **UDP**. By default it uses the
port `51820/udp`, but can be configured.

1. 5\.

    ## 5. Diferencias con IPsec y OpenVPN

| Feature | WireGuard | IPsec | OpenVPN |
|-----------------|--------|-----------------|--------------------------------|
| Cryptography | Modern | Variable | Variable |
| Performance | High | Medium | Low |
| Settings | Simple | Complex | Moderate |
| Base protocol | UDP | IPsec (ESP/IKE) | TCP/UDP |
| Kernel support | Yes | Yes | No (normally in user-space) |

1. 6\.

    ## 6. Configuración Base:

d[![](images/136-1.png)](https://www.zenarmor.com/docs/assets/images/figure-1-wireguardp2pvpntopology-452e7a073da12769cdd9e6530d5da284.png)

</div>