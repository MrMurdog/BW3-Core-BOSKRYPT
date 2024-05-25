# <center>BosKrypt1x</center> 
---

## Beschreibung
Mit diesem Modul ist es möglich mit Boskrypt verschlüsselte Narichten zu entschlüsseln.

## Unterstütze Alarmtypen
- Pocsag

## Resource
`BosKrypt1x`

## Konfiguration
Informationen zum Aufbau eines [BOSWatch Pakets](../develop/packet.md)

**Achtung:** Zahlen welche führende Nullen entahlten müssen in Anführungszeichen gesetzt werden Bsp. `'0012345'`

|Feld|Beschreibung|Default|
|----|------------|-------|
|bk_key|Angabe des Boskrypt Schlüssels, bzw auch mit Komma getrennt<br><br>Beispiel: <code>Schlüssel1,Schlüssel2,schlüsel3,...</code>||

**Beispiel:**
```yaml
- type: module
  res: BosKrypt1x
  config:
    - bk_key: key1,key2,key3,...
```

---
## Modul Abhängigkeiten
- keine

---
## Externe Abhängigkeiten
- BoskryptCLI im Modulordner
- Derzeit nur für ARM verfügbar

---
## Paket Modifikationen


---
## Zusätzliche Wildcards
- Von der Konfiguration abhängig
