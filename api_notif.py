import json
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    payload = message.payload.decode().strip()
    if not payload:
        print("⚠ Message MQTT vide, ignoré.")
        return

    try:
        data = json.loads(payload)  # Essaie de parser le JSON
        print("📩 Notification reçue :", data)
    except json.JSONDecodeError:
        print(f"🔹 Message texte reçu : {payload}")  # Si ce n'est pas du JSON, affiche le texte brut

BROKER = "192.168.1.55"

client = mqtt.Client(client_id="PC_Listener", callback_api_version=1)
client.on_message = on_message

client.connect(BROKER, 1883)
client.subscribe("notifications")
client.loop_forever()
