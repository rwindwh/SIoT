掌控板（mPython）
=================================


掌控板介绍
---------------------------------
  掌控板由虚谷计划组委会推出，是国内第一款专为编程教育而设计的开源硬件！为普及创客教育而生，反应一线Python编程教学需求，迎接普通高中新课改。
掌控板委托创客教育知名品牌Labplus盛思设计、制造与发行，历经十几轮次研究讨论，三次升级改版，是国内第一款专为编程教育而设计的开源硬件！
掌控板上集成了OLED显示屏、RGB灯、加速度计、麦克风、光线传感器、蜂鸣器、按键开关、触摸开关、金手指外部拓展接口，支持图形化及python代码编程，可实现智能机器人、创客智造作品等智能控制类应用。

利用掌控板上丰富的传感器，结合它小尺寸的特点还可以做很多智能穿戴、电子饰品等各种DIY作品应用。

掌控板地址：https://mpython.cn/mPython/index

掌控板的编程工具介绍
-------------------------------------------------

掌控板的编程工具很多，常用的有：

  - mPython X
  - Mind +
  - Mixly
  - BXY



掌控板的MQTT代码（基于Mind+）
---------------------------------------------------------
Mind+是一款基于Scratch3.0开发的青少年编程软件，让大家轻松体验创造的乐趣。

`网站：http://mindplus.cc/`

**代码说明：**

这段代码可以提供消息的发送和订阅功能，MQTT服务器既可以用EasyIot物联网，也可以用SIoT。
要实现功能，我们只需修改“发送消息”截图中的红框区域，设定相应的数据即可。

代码下载链接：mind+中自带范例。


**发送消息**

.. image:: ../image/linmiaoyan/Mind+Mqtt-02.png


**订阅消息**

.. image:: ../image/linmiaoyan/Mind+Mqtt-01.png

掌控板的MQTT代码（基于BXY）
-------------------------------------------------------

BXY是一款运行于Windows平台的MicroPython编程IDE，界面简洁，操作便利。BXY是浙教版普通高中信息技术教材的为众多micro:bit和掌控板爱好者提供了一个简洁实用的平台。

下载地址：http://docs.dfrobot.com.cn/bxy/

**代码说明：**

这个实验需要2个掌控板，一个发布光线数据一个订阅光线数据，MQTT服务器既可以用EasyIot物联网，也可以用SIoT。

**注意**：使用BXY下载下面的代码，还需要另外添加一个库文件Iot.py。本代码已经整合在BXY的范例中，将BXY升级到最新即可看到。

代码下载链接：https://github.com/vvlink/SIoT/tree/master/examples/%E6%8E%8C%E6%8E%A7%E6%9D%BF%E4%BB%A3%E7%A0%81/Bxy


**发送消息**

::

      # 功能：发布光线数据
      from mpython import light
      from Iot import Iot
      from umqtt.simple import MQTTClient
      from machine import Timer
      import machine
      import time
      import json
      import network

      WIFI_SSID = 'yourSSID'#替换成你的WIFI热点名称
      WIFI_PASSWORD = 'yourPASSWD'#替换成你的WIFI热点密码

      IOT_SERVER = "server address" #EASYIOT的服务器为iot.dfrobot.com.cn；Siot地址为用户搭建的服务器的ip地址，例如：192.168.0.100
      IOT_PORT = 1883
      IOT_ClientID = "your ClientID"#替换成你的ClientID，可为空
      IOT_UserName = "your UserName"#替换成你的UserName
      IOT_PassWord = "your PassWord"#替换成你的PassWord
      IOT_pubTopic = 'your PubTopic' #如果是siot，自定义的topic中需要添加"/"，例如:"abc/abc"

      myIot = Iot(IOT_SERVER, IOT_UserName, IOT_ClientID, IOT_PassWord)
      client = MQTTClient(myIot.client_id, myIot.mqttserver, port = IOT_PORT, user = myIot.username, password = myIot.password)

      tim1 = Timer(1)

      def connectWIFI():
        station = network.WLAN(network.STA_IF)
        station.active(True)
        station.connect(WIFI_SSID,WIFI_PASSWORD)
        while station.isconnected() == False:
          pass
        print('Connection successful')
        print(station.ifconfig())

      def restart():
        time.sleep(10)
        machine.reset()

      def check(_):
        try:
          msg = {}
          client.check_msg()
          msg["light"] = light.read()
          print(json.dumps(msg))
          client.publish(IOT_pubTopic,json.dumps(msg))
          lastTime = time.time()
        except OSError as e:
          tim1.deinit()
          restart()

      connectWIFI()
      client.connect()

      tim1.init(period=5000, mode=Timer.PERIODIC,callback=check)
      while True:
        pass


**订阅消息**

::
      # 功能：订阅光线数据
      from mpython import *
      from Iot import Iot
      from umqtt.simple import MQTTClient
      from machine import Timer
      from machine import Pin
      import machine
      import time
      import json
      import network

      WIFI_SSID = 'yourSSID'#替换成你的WIFI热点名称
      WIFI_PASSWORD = 'yourPASSWD'#替换成你的WIFI热点密码

      IOT_SERVER = "server address" #EASYIOT的服务器为iot.dfrobot.com.cn；Siot地址为用户搭建的服务器的ip地址，例如：192.168.0.100
      IOT_PORT = 1883
      IOT_ClientID = "your ClientID"#替换成你的ClientID，可为空
      IOT_UserName = "your UserName"#替换成你的UserName
      IOT_PassWord = "your PassWord"#替换成你的PassWord
      IOT_subTopic = 'your SubTopic' #如果是siot，自定义的topic中需要添加"/"，例如:"abc/abc"

      myIot = Iot(IOT_SERVER, IOT_UserName, IOT_ClientID, IOT_PassWord)
      client = MQTTClient(myIot.client_id, myIot.mqttserver, port = IOT_PORT, user = myIot.username, password = myIot.password)

      tim1 = Timer(1)

      def connectWIFI():
        station = network.WLAN(network.STA_IF)
        station.active(True)
        station.connect(WIFI_SSID,WIFI_PASSWORD)
        while station.isconnected() == False:
          pass
        print('Connection successful')
        print(station.ifconfig())

      def sub_cb(topic,msg):
        print((topic,msg))
        if topic == b'light':
          try:
            print(type(msg))
            print("msg=%s"%str(msg))
            light= json.loads(msg)["light"]
            oled.DispChar("接收到对方光强度",0,0)
            oled.DispChar("%s"%str(light),64,16)
            oled.show()
            oled.fill(0)
            v=light//16
            rgb[0] = (v,v,v)
            rgb[1] = (v,v,v)
            rgb[2] = (v,v,v)
            rgb.write()
          except:
            print("error msg:%s"%msg)
        else:
          print("other topic=%s msg=%s"%(topic,msg))

      def restart():
        time.sleep(10)
        machine.reset()

      def check(_):
        try:
          client.check_msg()
        except OSError as e:
          tim1.deinit()
          restart()

      oled.DispChar("正在连接网络...",0,0)
      oled.show()
      oled.fill(0)
      connectWIFI()

      client.set_callback(sub_cb)
      client.connect()
      client.subscribe(IOT_subTopic)

      tim1.init(period=1000, mode=Timer.PERIODIC,callback=check)

      while True:
        pass



掌控板的MQTT代码（基于mPythonX）
------------------------------------------------------

代码下载地址：https://github.com/vvlink/SIoT/tree/master/examples/%E6%8E%8C%E6%8E%A7%E6%9D%BF%E4%BB%A3%E7%A0%81/mPythonX/%E5%8F%91%E9%80%81%E6%B6%88%E6%81%AF

**发送消息**



**订阅消息**
