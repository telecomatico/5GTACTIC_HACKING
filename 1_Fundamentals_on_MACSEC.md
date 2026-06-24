## MACsec Fundamentals

### Purpose of the document
  
This document introduces the fundamentals of MACsec in a gradual way so that you understand what problem it solves, how it works at a high level, and in which scenarios it is useful within modern Ethernet networks and 5G transport environments. MACsec is defined by the IEEE 802.1AE standard and provides confidentiality, integrity, and source authenticity for traffic over Ethernet. 

The goal is not to replace a lab exercise, but to provide the minimum conceptual framework so that it becomes easier to configure, verify, and analyze a real deployment afterward. In particular, it is important to understand from the beginning that MACsec protects the Ethernet link at layer 2, while other solutions such as IPsec or WireGuard protect IP traffic at layer 3. 

### What MACsec is
  
MACsec, short for _Media Access Control Security_, is a security technology for Ethernet networks defined by IEEE 802.1AE. Its function is to protect Ethernet frames against eavesdropping, modification, and unauthorized insertion within the protected segment. 
In simple terms, MACsec adds security directly at the data link layer. This means protection is applied to Ethernet traffic between devices connected through a link or a specific Ethernet domain, without depending on higher-layer applications. 

### Security services it provides
  
MACsec offers three main capabilities:
- Confidentiality, through encryption of Ethernet frame payload. 
- Integrity, to detect unauthorized modifications during transport. 
- Source authenticity, to ensure that the frame originates from an authorized entity within the protected link.  
Additionally, MACsec is designed to operate with low overhead and is often supported in network hardware, making it attractive for high-performance links. This feature is especially relevant in Ethernet transport associated with mobile networks and backhaul or fronthaul environments. 

### What problem it solves
  
In an unprotected Ethernet network, an attacker with access to the medium or an intermediate device can observe traffic, attempt to modify it, or inject frames. MACsec reduces these risks when the goal is to protect the Ethernet link between two nodes or across a controlled domain.  
For this reason, MACsec fits very well when the main concern is not the application, but the transport. For example, it can be used to protect links between switches, routers, servers, virtualized functions, or radio access nodes connected via Ethernet.

### Where it fits in the layered model
  
A helpful way to understand MACsec is to position each technology by layers:

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

  
The practical consequence is important: MACsec does not automatically replace IPsec. In many designs, MACsec protects the physical or switched link, while IPsec protects a broader IP path between network functions.

### How it works at a high level
  
MACsec protects Ethernet frames through security associations and keys that allow traffic to be encrypted and authenticated. It is sufficient to retain the idea that there is a trust establishment process, followed by a frame protection process in each direction of the link. 
At a conceptual level, the flow can be explained as follows:
- Two Ethernet devices agree to participate in a protected domain.
- They authenticate and obtain cryptographic material, usually with the help of complementary access control and key management mechanisms.
- From that point on, link frames can be transmitted protected with MACsec. 
- The receiver validates integrity and authenticity before accepting traffic.
In many deployments, key negotiation and distribution rely on MKA and mechanisms based on 802.1X, although for a basic introduction it is enough to understand that MACsec requires a control plane to authenticate and manage keys, in addition to the data plane that protects frames.

### Link protection vs end-to-end protection
  
The most important difference to understand is that MACsec typically provides **link-level protection**, not end-to-end protection across an entire IP network. If traffic traverses multiple hops, it is necessary to decide on which links MACsec is enabled and where that protection ends. 
This has advantages and limitations. The advantage is usually excellent performance and transparency to upper layers; the limitation is that a packet may leave a protected link and enter another different segment, which requires careful trust domain design. 

### Advantages of MACsec
  
The main advantages for an initial understanding are:
- It operates at layer 2 and is transparent to IP protocols and higher-layer applications. 
- It can have low latency impact and high performance when hardware support exists. 
- It is especially suitable for protecting Ethernet infrastructure links, backhaul, and fronthaul. 
- It provides confidentiality and integrity without redesigning the application using the link. 

### Limitations of MACsec
  
It is also important to clearly present its limits:
- It is not the best option when end-to-end IP protection across large or heterogeneous networks is required. 
- It requires support on compatible Ethernet devices and ports. 
- In multi-hop topologies, it is necessary to plan which links are protected and how the chain of trust is maintained.
- It does not replace other security controls such as segmentation, access authentication, ACLs, or monitoring.

### Relationship with 5G and transport networks
  
Although MACsec is not a 5G-specific technology, its relevance in 5G comes from the extensive use of Ethernet in fronthaul, midhaul, and backhaul. Various technical works and documents present it as an efficient solution for protecting Ethernet transport in Open RAN and next-generation mobile networks.
From a teaching perspective, it can be said that if N2 or N3 traverse Ethernet infrastructure, MACsec can protect the **underlying Ethernet link** carrying those flows. In contrast, if the goal is to protect the IP path between 5G functions, IPsec or, in some labs and private networks, WireGuard are usually considered first. 

### Use cases
  
Some scenarios where MACsec makes a lot of sense are:
- Switch-to-switch links within a campus or data center. 
- Links between routers and Ethernet aggregation equipment. 
- Ethernet transport in mobile backhaul or fronthaul. 
- Environments requiring high speed with hardware-based protection.
An intuitive example for is the following: if two university buildings are connected by Ethernet fiber and it is necessary to prevent interception or alteration of traffic along that segment, MACsec is a very natural option. 

### Minimum concepts that you should retain
  
After reading, you should remember these key ideas:
- MACsec is Ethernet security at layer 2.
- It protects confidentiality, integrity, and source authenticity of frames. 
- It typically protects specific Ethernet links or segments, not the entire end-to-end IP path. 
- Its use is very appropriate in infrastructure, data centers, and mobile network transport. 
- It does not always compete with IPsec; often they complement each other. 

### Preparation for a practicla application
  
Before an effective deployment of MACsec, you should consider these questions:
- Which devices in the scenario support MACsec? 
- Which exact link needs to be protected?
- Where does the trust domain start and end? 
- How will it be verified that traffic is actually encrypted or authenticated?   
In practice, it is common to verify interfaces, enable protection on both ends, review operational status, and compare packet captures or counters before and after enabling MACsec. This practical work makes more sense once it is clearly understood that the goal is to protect Ethernet transport rather than a specific application. 
