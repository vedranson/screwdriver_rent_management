# Arbeitsauftrag: Odoo Modul zur Schraubenzieher-Verwaltung

## Zwei neue Modelle:
- Schraubenziehzer
- Schraubenzieher-Typen

### Schraubenzieher:
- ID int (gewünschte Feldbezeichnung: id)
- Kontakt many2one (partner_id) required
- Verleihdatum date (start_date) required
- Rückgabedatum date (end_date)
- Typ many2one (screwdriver_type_id)
- Menge int (amount) required
- Status dropdown ["Geliehen", "Zurückgegeben", "Kaputt"] (state_id)

### Schraubenzieher-Typen:
- ID int (id)
- Name char (name)
- Name im alten System char (name_old_sys)
- Aktiv bool (active)

## Verknüpfung zu Kontakt:

Ein Kontakt kann jeweils Schraubenzieher ausleihen (1:n) 
-> neues Feld res.partner.screwdriver_ids
Ansicht: Neuer Reiter "Schraubenzieher" (notebook) im Kontaktmodul (res.partner)
mit Liste aller mit diesem Kontakt verknüpften Schraubenzieher, inklusive einem Button "Zeile hinzufügen" um einen neuen Schraubenzieher in der Liste anzulegen. Alle Felder des Schraubenziehers sowie der Name des Schraubenzieher-Typs sollten angezeigt werden.

## Tracking:

Bei Hinzufügen und Bearbeiten eines Schraubenziehers eines Kontakts sollen die gemachten Änderungen im Chatter getracked werden, damit man sieht wer wann was geändert oder neu angelegt hat.
