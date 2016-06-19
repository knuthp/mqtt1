import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("/message/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("wegtaymk", "ipQYk1CL74aU")
client.connect("m11.cloudmqtt.com", 19713, 60)

rc = 0
i = 0;
while rc == 0 and i < 10:
   rc = client.loop()
   client.publish("/message/t" + str(i),"M" + str(i))
   print "Iter " +  str(i)
   i = i + 1
   raw_input("Press Enter to continue...")
print("rc: " + str(rc))
