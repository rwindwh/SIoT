from mpython import *
import network
from umqtt.simple import MQTTClient

#基于mpythonx编写
#发现中文发送会部分文字显示不全，不知道是SIoT原因还是mpythonx的原因


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
    mqtt.publish("yy/063", "你好A")

def on_button_b_down(_):
    global pause
    mqtt.publish("yy/063", "你好B")

button_a.irq(trigger=Pin.IRQ_FALLING, handler=on_button_a_down)

button_b.irq(trigger=Pin.IRQ_FALLING, handler=on_button_b_down)


oled.DispChar(my_wifi.sta.ifconfig()[0], 0, 0, 1)
oled.show()
oled.DispChar("mqtt-ok", 0, 16, 1)
oled.show()
