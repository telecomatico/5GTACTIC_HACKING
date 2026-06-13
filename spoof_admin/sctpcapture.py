
from scapy.all import *
from scapy.layers.sctp import SCTP
import sys
from pynput import keyboard
#import keyboard

captured_packets = []
n_packets = 1


def on_press(key):
    try:
        if key.char == 'oo':
            print("Tecla ESC presionada. Deteniendo captura...")
        return False # Detiene el listener
    except AttributeError:
        pass

def sctp_packet_callback(packet):
    global n_packets
    if SCTP in packet:
        captured_packets.append(packet)
        with open("captured_packets.txt", "a") as f:
            f.write(f"Captured SCTP packet: {packet.summary()}\n\n")
            """# Redirige la salida estándar a un fichero
            original_stdout = sys.stdout
            sys.stdout = f
            packet[SCTP].show()
            # Restaura la salida estándar
            sys.stdout = original_stdout
            """
            packet.pdfdump(f"sctp_packet{n_packets}.pdf")
            
            f.write(f"SCTP Chunk Type: {packet[SCTP].type}\n")
            f.write(f"SCTP Chunk Length: {packet[SCTP].len}\n")
            try:
                f.write(f"SCTP Chunk Data: {packet[SCTP].data}\n\n")
            except AttributeError:
                f.write("SCTP Chunk Data: NO HAY DATOS!!!\n\n")
                      
            n_packets = n_packets + 1
        print(f"Captured SCTP packet: {packet.summary()}")

# Captura los paquetes en la interfaz de red (por ejemplo, 'eth0')
print("\n... Capturando... ESC para detener el proceso...")

#with keyboard.Listener(on_press=on_press) as listener:
#    listener.join()
#while True:
    
sniff(iface="enp0s8", filter="sctp", prn=sctp_packet_callback, count=5) # Captura un paquete
    #if keyboard.is_pressed('esc'):
    #    print("Captura detenida.")
    #break

"""
# Reenvío
if captured_packets:
    send(captured_packets[0])
    print("Packet resent successfully!")
else:
    print("No packet captured to resend.")

# Modifica y reenvía:
"""
"""
if captured_packets:
    packet = captured_packets[0]
    
    # Modifica los campos del paquete
    packet[SCTP].chunk_type = 0x01 # Ejemplo: cambiar el tipo de chunk
    packet[SCTP].chunk_data = b"Nuevo contenido" # Ejemplo: cambiar los datos del chunk

    # Reenvía el paquete modificado
    send(packet)
    print("Packet modified and resent successfully!")
else:
    print("No packet captured to modify and resend.")
"""