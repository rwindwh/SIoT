from mpython import *
import network
from umqtt.simple import MQTTClient
from machine import Timer
import ubinascii

my_wifi = wifi()
my_wifi.connectWiFi("make", "make2008")

mqtt = MQTTClient("xzr", "192.168.22.250", 1883, "siot", "dfrobot", keepalive=30)

try:
    mqtt.connect()
    print('Connected')
except:
    print('Disconnected')

def on_button_a_down(_):
    global pause
    mqtt.publish("yy/063", "0")

def on_button_b_down(_):
    global pause
    mqtt.publish("yy/063", "1")

def mqtt_topic_79792f303633(_msg):
    global pause
    oled.DispChar((str(_msg)), 0, 48, 1)
    oled.show()

button_a.irq(trigger=Pin.IRQ_FALLING, handler=on_button_a_down)

button_b.irq(trigger=Pin.IRQ_FALLING, handler=on_button_b_down)

def mqtt_callback(topic, msg):
    try:
        topic = topic.decode('utf-8', 'ignore')
        _msg = msg.decode('utf-8', 'ignore')
        eval('mqtt_topic_' + bytes.decode(ubinascii.hexlify(topic)) + '("' + _msg + '")')
    except: print((topic, msg))

mqtt.set_callback(mqtt_callback)

mqtt.subscribe("yy/063")

def timer14_tick(_):
    mqtt.ping()

tim14 = Timer(14)
tim14.init(period=20000, mode=Timer.PERIODIC, callback=timer14_tick)


oled.DispChar(my_wifi.sta.ifconfig()[0], 0, 0, 1)
oled.show()
oled.DispChar("mqtt-ok", 0, 16, 1)
oled.show()
while True:
    mqtt.wait_msg()
