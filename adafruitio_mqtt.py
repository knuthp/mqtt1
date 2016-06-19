import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("knuthp/feed/#")

client = mqtt.Client()
client.on_connect = on_connect
client.username_pw_set("knuthp", "facfa85eb7644973b7b309fd41087b99")
client.connect("io.adafruit.com", 1883, 60)

rc = 0
i = 0;
while rc == 0 and i < 10:
   rc = client.loop()
   client.publish("knuthp/feeds/test", str(i))
   print "Iter " +  str(i)
   i = i + 1
   raw_input("Press Enter to continue...")
print("rc: " + str(rc))
