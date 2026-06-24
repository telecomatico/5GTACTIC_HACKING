# 5GTACTIC_HACKING 🚀

Welcome to **5GTACTIC_HACKING**. This repository contains a collection of scripts, tools, and proof-of-concept (PoC) implementations designed to analyze, monitor, and test the security resilience of 5G Core (5GC) networks. 

The main focus of this laboratory environment is to inspect vulnerabilities within the **SCTP (Stream Control Transmission Protocol)** layer and the HTTP/2 service-based architectures using a virtualized deployment with **Free5GC**, **UERANSIM**, and **GNS3**.

---

## 🏗️ Topology & Environment Setup

This project is built around an advanced hybrid infrastructure combining virtual machines, Docker containers, and the host machine:

* **5G Core:** Free5GC deployed via Docker containers (`free5gc-compose`) running on the host machine.
* **RAN (gNB & UE):** Simulated via UERANSIM running inside the GNS3-VM environment.
* **Attacker (Insider Host):** The native Linux Host operating inside GNS3 through a dedicated virtual interface (`tap0` / bridge) to achieve maximum performance and direct access to raw sockets.

---

## 🛠️ Installation & Prerequisites

### 1. Host System Requirements
Before executing the scripts, install the required native dependencies to compile and handle SCTP traffic in your Ubuntu/Debian host:

```bash
sudo apt update
sudo apt install -y build-essential python3-dev libglib2.0-dev libsctp-dev
