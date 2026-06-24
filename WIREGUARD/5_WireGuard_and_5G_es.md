<div class="page">

# WireGuard y 5G

\

## ¿Dónde se puede usar WireGuard en Open5GS?

Open5GS es una implementación del core 4G/5G que corre sobre
contenedores o servicios en Linux. WireGuard puede usarse para:

- Proteger el tráfico entre funciones del core (AMF, SMF, UPF, etc.) si
  están distribuidas en diferentes hosts.
- Asegurar la comunicación entre gNB y UPF (interfaz N3).
- Crear túneles seguros entre contenedores en entornos virtualizados o
  en la nube.

## Ejemplo de integración

Supongamos que tienes:

Un contenedor con gNB en una máquina.

Otro contenedor con UPF en otra máquina.

Puedes:

1.  Instalar WireGuard en ambos hosts.
2.  Crear una red privada (por ejemplo, 10.0.0.0/24) para que gNB y UPF
    se comuniquen por IPs internas.
3.  Configurar WireGuard para que el tráfico GTP-U entre gNB y UPF pase
    por el túnel.

Esto se logra modificando la configuración de Open5GS para que el UPF
escuche en la IP privada de WireGuard (10.0.0.2) y el gNB envíe tráfico
a esa IP.

</div>
