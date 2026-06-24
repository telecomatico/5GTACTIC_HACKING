## WireGuard Fundamentals

### Purpose of the document
  
This document introduces the fundamentals of WireGuard so that you understand what problem it solves, how it works at a high level, and why it has become a very attractive option in laboratories, private networks, and some modern 5G and Open RAN scenarios. Recent studies evaluate it as a lightweight solution to protect traffic in private 5G networks and compare its use with traditional alternatives such as IPsec.   
The goal is to provide a sufficient conceptual foundation so that, in a later document, you can configure tunnels, exchange keys, verify connectivity, and understand which traffic is being protected. The most important idea is that WireGuard protects IP traffic at layer 3, with a simpler and lighter design than IPsec. 

### What WireGuard is
  
WireGuard is a modern VPN tunneling technology designed to protect IP communications in a simple and efficient way. In recent literature on private networks and Open RAN, it is presented as a lightweight alternative for securing IP transport with lower operational complexity than IPsec.   
From a practical point of view, WireGuard creates a secure tunnel between defined peers using public and private keys. This tunnel can carry encrypted and authenticated IP traffic between the configured endpoints. 

### Security services it provides
  
WireGuard provides, functionally, the security services expected from a modern layer 3 VPN:
- Confidentiality of IP traffic through encryption. 
- Packet integrity to detect unauthorized modifications.
- Authentication between peers based on cryptographic keys. 
- Simplicity of configuration, thanks to the use of a fixed cryptographic suite and a reduced operational model compared to other alternatives. 
This combination makes WireGuard especially attractive in environments where ease of deployment, lightweight operation, and operational clarity are priorities. 

### What problem it solves
  
When two systems exchange IP traffic through a network that is not fully trusted, there is a risk of interception, modification, or impersonation. WireGuard is used to create an encrypted channel between these endpoints in order to protect traffic along the path.  
This makes it useful in private networks, laboratories, virtualized infrastructures, Linux environments, and some non-public 5G or Open RAN scenarios. A recent study on a real industrial 5G network evaluates WireGuard precisely as a lightweight solution for protecting relevant communications in that context. 

### Where it fits in the layered model
  
A layer-based comparison helps clarify its position:

<table>
<tr>
<th>  
Technology
</th>
<th>  
Main layer
</th>
<th>  
What it protects
</th>
</tr>
<tr>
<td>  
MACsec
</td>
<td>  
Layer 2 Ethernet 
</td>
<td>  
The Ethernet link or segment 
</td>
</tr>
<tr>
<td>  
IPsec
</td>
<td>  
Layer 3 IP 
</td>
<td>  
IP traffic between endpoints or tunnels 
</td>
</tr>
<tr>
<td>  
WireGuard
</td>
<td>  
Layer 3 IP 
</td>
<td>  
IP traffic between defined peers 
</td>
</tr>
</table>

  
The essential idea is that WireGuard does not directly protect the Ethernet link, but rather the IP traffic flowing between configured endpoints. Therefore, it is more naturally compared with IPsec than with MACsec. 

### How it works at a high level
  
WireGuard can be explained very simply using four ideas:
- Each endpoint has a private key and a public key. 
- Each peer knows the public key of the other endpoint. 
- Tunnel IP addresses are defined, along with which prefixes or networks should be sent through that tunnel. 
- Allowed traffic flows encrypted and authenticated between both endpoints. 

This model is very intuitive because it avoids much of the complexity found in other VPNs. For an introductory explanation, it is sufficient to understand that WireGuard behaves like a secure virtual network interface between peers that recognize each other cryptographically. 

### Basic concepts that you should understand
  
In an introductory approach, the most important concepts are:
- **Peer**: each endpoint participating in the tunnel. 
- **Public and private keys**: cryptographic material that identifies and authenticates each endpoint. \
- **WireGuard interface**: virtual interface through which protected traffic flows. 
- **Allowed IPs**: networks or addresses that will be sent to the corresponding peer through the tunnel. 
- **Endpoint**: IP address and port of the remote endpoint.  

For lab work, the **Allowed IPs** concept is particularly important, because it determines which traffic actually enters the tunnel and to which peer it is routed. 

### Advantages of WireGuard
  
The advantages most valued by technics and administrators include:
- Simpler configuration than IPsec in many scenarios. 
- Lower operational complexity, by reducing the number of cryptographic and signaling decisions required. 
- Good suitability for Linux environments, virtualization, containers, and laboratories. 
- Growing interest in private networks and Open RAN as a lightweight alternative for protecting IP transport.  

In a real industrial 5G network, WireGuard has been used to encrypt traffic associated with N3 and to authenticate communications related to N2 between gNB and AMF, showing performance results comparable to IPsec along with easier configuration. 

### Limitations of WireGuard
  
Its limitations should also be clearly explained:
- It is not the traditional reference mechanism within the 3GPP NDS/IP framework, where IPsec has stronger standardization. 
- It may face organizational barriers in large operators where processes and tools are already centered around IPsec. 
- Its simplicity does not eliminate the need for proper design of addressing, routing, segmentation, and access control. 
- It does not replace other network security measures. 

### Relationship with 5G, N2 and N3
  
WireGuard is not part of the traditional family of 3GPP mechanisms historically used for IP network protection, but its lightweight nature has attracted interest in private 5G and Open RAN scenarios. Recent research explicitly evaluates it as an alternative for protecting N3 and part of the internal communications of the 5G Core or radio access. 

In 5G, N2 connects the gNB with the AMF for control signaling, while N3 connects the gNB with the UPF for user traffic. Since these are IP-based paths, WireGuard can be used as a lightweight tunnel to protect these flows when operational conditions allow it.  

A simple way to explain it in class is:
- In **N2**, WireGuard can help secure signaling between gNB and AMF in private networks or testing environments. 
- In **N3**, WireGuard can encrypt user traffic between gNB and UPF. 
- Its main advantage in these cases is the simplicity of deployment compared to IPsec. 

### Simple comparison with MACsec and IPsec

<table>
<tr>
<th>  
Technology
</th>
<th>  
Simple idea
</th>
<th>  
Main strength
</th>
<th>  
Main limitation
</th>
</tr>
<tr>
<td>  
MACsec
</td>
<td>  
“Protects the Ethernet link” 
</td>
<td>  
Good performance at layer 2 
</td>
<td>  
Does not by itself protect a broader IP path 
</td>
</tr>
<tr>
<td>  
IPsec
</td>
<td>  
“Protects the IP path with a mature solution” 
</td>
<td>  
Highly aligned with operator frameworks and 3GPP
</td>
<td>  
Higher operational complexity
</td>
</tr>
<tr>
<td>  
WireGuard
</td>
<td>  
“Protects the IP path with a lightweight VPN” 
</td>
<td>  
Simplicity and agile deployment 
</td>\
<td>  
Less normative tradition in classical 3GPP 
</td>
</tr>
</table>

  
This comparison helps to understand that WireGuard should not be presented as a universal replacement, but rather as a particularly useful option when simplicity, deployment speed, and operational clarity are prioritized. 

### Use cases
  
Some scenarios where WireGuard is especially useful include:
- Teaching and research labs on secure IP networking. 
- Private 5G networks or campus environments. 
- Linux-based infrastructures and virtualized systems. 
- Lightweight protection of interconnections between network functions or distributed nodes. 

An intuitive example is to imagine a software-based gNB and a 5G Core deployed on two Linux servers connected through an intermediate IP network. If simple and fast encryption of traffic between them is required for testing or training purposes, WireGuard can be a very suitable solution.

### Minimum concepts that you should remember
  
After reading, you should retain:
- WireGuard protects IP traffic at layer 3. 
- It uses a peer-based model with public/private keys. 
- It defines which traffic enters the tunnel using routes or _Allowed IPs_. 
- It is often simpler to deploy than IPsec in many scenarios. 
- In 5G, it is particularly attractive in labs, private networks, and some Open RAN contexts. 

### Preparation for a practical deployment
  
Before a practical deployment of WireGuard, you should be clear about:
- Which endpoints will act as peers. 
- What public and private keys each endpoint will have. 
- What IP addresses will be assigned to the tunnel. 
- Which networks or prefixes will be included in _Allowed IPs_. 
- How to verify that traffic actually flows through the tunnel and not through the normal route. 

In a real lab, the usual steps include generating keys, creating the WireGuard interface, defining the remote peer, assigning tunnel addresses, and validating connectivity, routing, and packet captures. This process is much easier to understand once it is clear that WireGuard creates a secure layer 3 virtual interface between endpoints authenticated by keys. 

