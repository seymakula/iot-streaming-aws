import time
import json
import random
from awscrt import mqtt
from awsiot import mqtt_connection_builder

ENDPOINT = "a1rim3gq9hoffc-ats.iot.eu-central-1.amazonaws.com"
CLIENT_ID = "iot-sensor-01"
TOPIC = "sensor/data"
CERT = "certs/device.pem.crt"
KEY = "certs/private.pem.key"
ROOT_CA = "certs/rootCA.pem"

mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=CERT,
    pri_key_filepath=KEY,
    ca_filepath=ROOT_CA,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=30
)

print("AWS IoT Core'a baglaniliyor...")
connect_future = mqtt_connection.connect()
connect_future.result()
print("Baglanti basarili!")

try:
    while True:
        payload = {
            "device_id": "sensor-01",
            "temperature": round(random.uniform(20.0, 35.0), 2),
            "humidity": round(random.uniform(40.0, 80.0), 2),
            "pressure": round(random.uniform(1000.0, 1020.0), 2),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        mqtt_connection.publish(
            topic=TOPIC,
            payload=json.dumps(payload),
            qos=mqtt.QoS.AT_LEAST_ONCE
        )
        print("Veri gonderildi:", payload)
        time.sleep(5)

except KeyboardInterrupt:
    print("Durduruldu.")
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
