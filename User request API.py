import requests

# Zielserver
host 'https://SRVTEST001/api/users'

# Anfrage an Server
response = requests.get(host)

# Verbindungsstatus
if response.status_code ==200:
    # JSON-Daten aus Request extrahieren
    user_data = response.json()

    # User analysieren und anschliessend Informationsausgabe
    for user in user_data:
        print(f"Benutzername: {user['username']}, E-Mail: {user['email']}")
    else:
        # Statusausgabe falls nicht erfolgreich
        print(f"Fehler: {response.status_code}")
        EncodingWarning
        