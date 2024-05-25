import subprocess

def FormatKeys(wert):

    array = array = [item.strip() for item in wert.split(',')]

    return array

def Decrypt(keys, message):

    for key in keys:
        try:
            # Setze den Befehl zusammen
            command = ["./CLI/BoskryptCLI", key, message]
            
            # Führe den Befehl aus und fange die Ausgabe ab
            result = subprocess.run(command, capture_output=True, text=True)
            
            # Überprüfe die Ausgabe
            if result.stdout.strip():  # Wenn die Ausgabe nicht leer ist
                return result.stdout.strip()
        except Exception as e:
            # Optional: Fehlerbehandlung, falls der Befehl fehlschlägt
            return(f"Fehler bei der Ausführung von {command}: {e}")

    # Wenn keine der Ausführungen eine Ausgabe hatte
    return 'KeineEntschlüsselung'