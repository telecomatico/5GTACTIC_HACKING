## IPsec Fundamentals

### Purpose of the document
  
This document presents the fundamentals of IPsec in a clear and progressive way so that you understand what problem it solves, how it works at a general level, and why it is a particularly important technology in modern IP networks and in the transport of 5G interfaces. In the 3GPP ecosystem, the NDS/IP framework uses IPsec as a foundation to protect IP-based networks, which is why IPsec frequently appears when discussing security in interfaces such as N2 and N3.  
The goal is not to go into all cryptographic or signaling details, but to provide a sufficient conceptual foundation to later address a lab exercise. The main idea that should remain clear is that IPsec protects IP traffic at layer 3, unlike MACsec, which protects Ethernet links at layer 2.

### What IPsec is
  
IPsec, short for *Internet Protocol Security*, is a set of security mechanisms used to protect IP communications. Its design provides confidentiality, integrity, authentication, and protection against certain forms of packet replay in IP networks.  
Unlike solutions tied to a specific application, IPsec operates at the network layer. This allows it to protect IP traffic in a relatively transparent way for applications and many upper-layer protocols.

### Security services it provides
  
IPsec provides several fundamental services:
- Confidentiality, through encryption of IP traffic.
- Integrity, to detect modifications of packets during transport.
- Source authentication, to ensure that traffic comes from the expected entity.
- Protection against replay attacks, using sequence control mechanisms.  

In operator networks and critical infrastructures, this combination makes IPsec a well-established option when the goal is to protect IP paths between devices or network functions.

### What problem it solves
  
In an unprotected IP network, an attacker with visibility over the path can observe, modify, or attempt to inject packets. IPsec was specifically designed to reduce these risks when traffic traverses networks that cannot be considered fully trusted.  
For this reason, IPsec is suitable for inter-site links, operator networks, interconnection between virtualized functions, and many transport security scenarios for 4G and 5G. It is often presented as a reference solution for protecting IP segments of signaling and user traffic.

### Where it fits in the layered model
  
A useful way to explain IPsec is to compare it with other protection technologies:

<table>
<tr>
<th>Technology</th>
<th>Main layer</th>
<th>What it protects</th>
</tr>
<tr>
<td>MACsec</td>
<td>Layer 2 Ethernet</td>
<td>The Ethernet link or segment</td>
</tr>
<tr>
<td>IPsec</td>
<td>Layer 3 IP</td>
<td>IP traffic between endpoints or tunnels</td>
</tr>
<tr>
<td>WireGuard</td>
<td>Layer 3 IP</td>
<td>IP traffic between defined peers</td>
</tr>
</table>

  
The practical implication is that IPsec fits better than MACsec when the security problem lies in the **IP path** between two functions or two network domains, rather than just on a specific Ethernet link.

### Basic components of IPsec
  
For an introductory level, it is enough to present three ideas:
- **ESP** (*Encapsulating Security Payload*), which is commonly used as the main protocol to protect IP traffic.
- **Security Associations (SA)**, which define parameters and keys to protect traffic in a specific direction.
- **Key management and negotiation**, typically associated with IKE in real deployments, although at a first level it is enough to know that IPsec needs a mechanism to securely agree on cryptographic parameters.  

An important point is that a security association is usually unidirectional. This means that bidirectional communication typically requires separate associations for each traffic direction.

### How it works at a high level
  
IPsec operation can be explained simply in four steps:
- Two IP endpoints decide to protect their communications.
- They negotiate or establish security associations and keys.
- The sender encrypts and/or authenticates packets according to the configured policy.
- The receiver verifies integrity, authenticity and, if applicable, decrypts the content.  

From a teaching perspective, it is not necessary to go into the detail of all header fields or every IKE exchange in an initial session. It is more useful to understand the idea of a “secure IP tunnel between two endpoints.”

### Modes of operation: transport and tunnel
  
IPsec can be used in different modes, but for an introductory foundation it is especially useful to distinguish the **tunnel mode**. In this mode, an original IP packet is encapsulated inside another protected IP flow, which is very useful for inter-site networks, operator domains, or interconnection between functions.  
In teaching practice, tunnel mode is usually the most intuitive because it allows IPsec to be visualized as a “secure pipe” between two endpoints.

### Advantages of IPsec
  
The main advantages are:
- It protects IP traffic without depending on a single application.
- It is widely aligned with operator security frameworks and with 3GPP environments.
- It is suitable for protecting both signaling and user traffic over IP networks.
- It is a mature, well-known technology widely supported in network equipment and operating systems.

### Limitations of IPsec
  
It is also important to explain its limits and operational costs:
- It is usually more complex to configure and maintain than lightweight alternatives such as WireGuard.
- It may require more elaborate management of policies, keys, certificates, and security associations.
- Its operation may become more complex in scenarios with NAT, multiple administrative domains, or large heterogeneous deployments.
- It does not replace other security measures such as segmentation, system hardening, access control, and monitoring.

### Relationship with 5G and N2/N3
  
The relationship between IPsec and 5G is particularly relevant because N2 and N3 are interfaces that, in practice, rely on IP transport between network functions. N2 connects the gNB with the AMF for control signaling, while N3 connects the gNB with the UPF for user traffic.  
Since IPsec protects IP traffic, its use naturally fits when securing these paths between RAN and Core, especially if the transport network is not fully trusted.

From a teaching perspective:
- In **N2**, IPsec helps protect critical signaling between gNB and AMF.
- In **N3**, IPsec helps protect user traffic between gNB and UPF.
- In both cases, its use is associated with the IP path rather than the underlying Ethernet link.

### Simple comparison with MACsec and WireGuard

<table>
<tr>
<th>Technology</th>
<th>Simple idea</th>
<th>Main strength</th>
<th>Main limitation</th>
</tr>
<tr>
<td>MACsec</td>
<td>“Protects the Ethernet link”</td>
<td>Good performance at layer 2</td>
<td>Not end-to-end IP protection</td>
</tr>
<tr>
<td>IPsec</td>
<td>“Protects the IP path”</td>
<td>Strong alignment with operator and 3GPP frameworks</td>
<td>Higher operational complexity</td>
</tr>
<tr>
<td>WireGuard</td>
<td>“Lightweight IP VPN between peers”</td>
<td>Simplicity of deployment</td>
<td>Less tradition as a classical 3GPP mechanism</td>
</tr>
</table>

  
This comparison helps avoid a common mistake: assuming that all these technologies compete for exactly the same space. In reality, they often complement each other because they protect different layers and domains.

### Use cases
  
Some typical scenarios where IPsec is very useful are:
- Secure connection between sites over an untrusted IP network.
- Protection of transport between virtualized or distributed network functions.
- Security of signaling and user interfaces in 5G deployments.
- Interconnection between administrative domains where confidentiality and integrity of IP traffic are required.  

A useful example is to imagine two 5G nodes located in different data centers connected through an operator IP network. If it is necessary to ensure that neither signaling nor user traffic can be read or modified in transit, IPsec is a natural solution.

### Minimum concepts that you should remember
  
After reading, you should retain these key ideas:
- IPsec protects IP traffic at layer 3.
- It provides confidentiality, integrity, authentication, and replay protection.
- It uses security associations and key management mechanisms.
- It is especially suitable for protecting an IP path between endpoints.
- In 5G, its application to N2 and N3 is natural since they involve transport over IP.

### Preparation for a practical deployment
  
Before a practical deployment of IPsec, you should consider:
- Which IP endpoints need protection?
- What traffic should be included in the tunnel and what should remain outside?
- What authentication and key management mechanism will be used?
- How will it be verified that traffic is actually encrypted and authenticated?  

In a real lab, it is common to define policies, create tunnels or associations, enable cryptographic parameters, and validate connectivity, counters, and packet captures.
