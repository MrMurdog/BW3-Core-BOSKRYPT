from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

import base64

def UnpackMessage(packed_bytes):
    source = ""
    
    # Konvertiere jeden Byte in eine 8-Bit-binäre Zeichenkette und füge sie zu source hinzu
    for packed_byte in packed_bytes:
        text = bin(packed_byte)[2:].zfill(8)
        source += Reverse(text)
    
    # Teile source in 7-Bit-Blöcke auf
    chunks = [source[i:i+7] for i in range(0, len(source), 7)]
    
    result = ""
    
    # Konvertiere jeden 7-Bit-Block zurück in einen Char
    for chunk in chunks:
        reversed_chunk = Reverse(chunk)
        char_int = int(reversed_chunk, 2)
        result += chr(char_int)
    
    # Führe spezielle Ersetzungen durch
    if result is not None and result.startswith("ENCR"):
        result = result[4:].replace('@', '§').replace('[', 'Ä').replace('\\', 'Ö').replace(']', 'Ü').replace('{', 'ä').replace('|', 'ö').replace('}', 'ü').replace('~', 'ß')
        return result
    else:
        return None

def Reverse(text):
    return text[::-1]

def Decrypt(key, data):
  
    ## Umwandlung der Eingegebenen Daten in bytes
    
    key_bytes = bytes.fromhex(key)
    payload_bytes = base64.b64decode(data)
    
    ## extrahieren des IV/NONCE aus der Payload/Text
    
    iv = payload_bytes[:8]
    
    iv += b'\x00' * 8 # auffüllung mit Nullbytes um den minimalwert zu erreichen
  
    ## abtrennung des 'Text' Blocks von der Payload
    
    textblock = payload_bytes[8:]
    
    ## Verschlüsselungsobjekt erstellen
    
    cipher = Cipher(algorithms.AES(key_bytes), modes.CTR(iv), backend=default_backend())

    ## Verschlüsseler und Entschlüsseler instanziieren

    decryptor = cipher.decryptor()
    
    ## Entschlüsseln des 'Text' Blockes in 'RAW' bytes für die weiterverarbeitung
    
    rawtext = decryptor.update(textblock) + decryptor.finalize()

    ## Umwandlung der Raw Bytes in lesbaren Text ## Derzeit leider noch Fehlerhaft
    
    lets_magic = UnpackMessage(rawtext[5:])
    
    return lets_magic