from mqtt.simple import MQTTClient
d = dht.DHT22(machine.Pin(14))

ssid = 'xxxxxxx'
pasword = 'yyyyyyy'
    msg = json.dumps({
      'ID':CONFIG['CLIENT_ID'],
      'temperature':d.temperature(),
      'humidity':d.humidity()