<div class="page">

# WireGuard y 5G

\

## ¿Dónde se puede usar WireGuard en Open5GS?

Open5GS is an implementation of the 4G/5G core that runs on
containers or services in Linux. WireGuard can be used to:

- Protect traffic between core functions (AMF, SMF, UPF, etc.) if
  They are distributed on different hosts.
- Ensure communication between gNB and UPF (N3 interface).
- Create secure tunnels between containers in virtualized environments or
  in the cloud.

## Ejemplo de integración

Suppose you have:

A container with gNB on a machine.

Another container with UPF on another machine.

Can:

1. Install WireGuard on both hosts.
2. Create a private network (e.g. 10.0.0.0/24) so that gNB and UPF
    communicate via internal IPs.
3. Configure WireGuard so that GTP-U traffic between gNB and UPF passes
    through the tunnel.

This is achieved by modifying the Open5GS configuration so that the UPF
listen on WireGuard private IP (10.0.0.2) and gNB send traffic
to that IP.

</div>