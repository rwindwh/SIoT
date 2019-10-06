import threading
import paho.mqtt.client as mqtt
import time

class MqttClient:
    client = None
    timer = None

    def __init__(self, client_id, server, port=1883, user=None, password=None):
        self._host = server
        self._port = port
        self._user = user
        self._password = password
        self.client = mqtt.Client(client_id)
        self.client.on_connect = self._on_connect
        self.connected = False

    def connect(self):
        self.client.username_pw_set(self._user, self._password)
        self.client.connect(self._host, self._port, 60)

    def publish(self, topic, data):
        self.client.publish(str(topic), str(data))

    def check_msg(self, msg = ""):
        # thread.setDaemon(True)
        self.client.loop(1)
    
    def timer_sub_cb(self):
        self.check_msg()
        self.timer = threading.Timer(0.1, self.timer_sub_cb)
        self.timer.start()
    
    def subscribe(self, topic, cb):
        self.client.on_message  = cb
        self.client.subscribe(topic)
    
    def tim(self):
        self.timer = threading.Timer(1.0, self.timer_sub_cb)  
        self.timer.start()
    
    def _on_connect(self, client, userdata, flags, rc):
        #print("\nConnected with result code " + str(rc))
        self.connected = True
    
    def set_callback(self, cb):
        self.client.on_message = cb
    
    def getsubscribe(self, topic):
        self.client.subscribe(topic)

    def stop(self):
        self.client.disconnect()
        if self.timer != None:
            self.timer.cancel()