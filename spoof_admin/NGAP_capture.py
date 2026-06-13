import ctypes
from scapy.all import sniff, SCTP, send 



# Cargar la biblioteca libngapcodec
ngapcodec = ctypes.CDLL("/usr/local/lib/ngapcodec/15.3.0/libngapcodec.so")

# Decodificar con libngapcodec
def decode_ngap(encoded_data):
    buffer = ctypes.create_string_buffer(encoded_data)
    decoded_data = ngapcodec.decode(buffer)
    return decoded_data

# Codificar con libngapcodec
def encode_ngap(decoded_data):
    buffer = ctypes.create_string_buffer(decoded_data)
    encoded_data = ngapcodec.encode(buffer)
    return encoded_data

# Capturamos y mostramos los SCTP
print("\nComienza la captura de SCTP")
packets = sniff(iface="enp0s8", filter="sctp", count=10)

for pkt in packets:
    if pkt.haslayer("SCTP"):
        pkt.show()

        # Extraer datos SCTP
        sctp_payload = packets[0]["SCTP"].payload.load

        if sctp_payload:
            # Decodificar con libngapcodeccd 
            ngap_decoded = decode_ngap(sctp_payload)
            print("\nMensaje NGAP decodificado:", ngap_decoded)

            # Modificar un campo NGAP (ejemplo: cambiar el tipo de mensaje)
            ngap_decoded.message_type = 2

            # Codificar con libngapcodec
            ngap_encoded = encode_ngap(ngap_decoded)
            print("\n\nMensaje NGAP decodificado:", ngap_decoded)

            # Crear un nuevo paquete SCTP con los datos modificados
            modified_pkt = SCTP() / ngap_encoded

            # Enviar el paquete modificado
            send(modified_pkt)
            print("Paquete NGAP modificado enviado.")
        else:
            print("\n\nNo hay datos!!!")