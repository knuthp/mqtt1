# Example of using the MQTT client class to subscribe to a feed and print out
# any changes made to the feed.  Edit the variables below to configure the key,
# username, and feed to subscribe to for changes.

# Import standard python modules.
import sys
from node_status import CPU 

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient
from Adafruit_IO import Client
from time import sleep
from Adafruit_IO.client import Client


# Set to your Adafruit IO key & username below.
ADAFRUIT_IO_KEY      = 'facfa85eb7644973b7b309fd41087b99'
ADAFRUIT_IO_USERNAME = 'knuthp'  # See https://accounts.adafruit.com
                                                    # to find your username.

# Set to the ID of the feed to subscribe to for updates.
FEED_ID = 'node__lorkstation__status'

global status

# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print 'Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID)
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe(FEED_ID)

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print 'Disconnected from Adafruit IO!'
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print 'Feed {0} received new value: {1}'.format(feed_id, payload)
    client.status = payload
    printStatus(client)
    
    
def printStatus(status):
    print ('status={0}'.format(client.status))


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.status = 'OFF'

# Connect to the Adafruit IO server.
client.connect()

# Start a message loop that blocks forever waiting for MQTT messages to be
# received.  Note there are other options for running the event loop like doing
# so in a background thread--see the mqtt_client.py example to learn more.
client.loop_background()

cpu = CPU()
aio = Client(ADAFRUIT_IO_KEY)
client.status = aio.receive(FEED_ID).value
printStatus(client)
while True:
    if (client.status == 'ON'):
        client.publish('node__lorkstation__cpu', cpu.cpu_percent())
    sleep(10)