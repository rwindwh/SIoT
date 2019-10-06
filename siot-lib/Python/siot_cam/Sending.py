# coding=utf-8
import cv2
import math
import base64
import json
import threading
import time
from simple import MqttClient


filepath = r"cache/sending.jpg"    #参数调试，需要识别的图片路径里不能带有中文
CLIENT_ID = ""
SERVER = "192.168.0.102"	#MQTT服务器IP
IOT_pubTopic = 'DFRobot/linmy'	#“topic”为“项目名称/设备名称”
IOT_UserName='siot'		#用户名
IOT_PassWord='dfrobot'	#密码

siot = MqttClient(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)

def sub_cb(client, userdata, msg):
  print("\nTopic:" + str(msg.topic) + " Message:" + str(msg.payload))

#摄像头取景
def get_pic():
    cap=cv2.VideoCapture(0)
    sucess,img=cap.read()
    #cv2.imshow("img",img)
    cv2.imwrite(filepath,img)
    #cv2.destroyAllWindows()
    cap.release()

#利用函数作画
def draw():
    img = cv2.imread(filepath)
    img = cv2.resize(img, (320,240), interpolation=cv2.INTER_AREA)
    high, width, _ = img.shape
    cv2.putText(img, 'temperature', (int(width*3/4-50),int(high*3/4-5)), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 1)
    cv2.rectangle(img,(int(width*3/4-40),int(high*3/4)),(int(width*3/4+100),int(high*3/4+25)),(0,0,255),1)
    cv2.putText(img, ('VALUE:' + str(value)), (int(width*3/4-40),int(high*3/4+20)), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 1)
    #cv2.imshow('img',img)
    cv2.imwrite(filepath,img)
    cv2.waitKey(0)


#图片→base64编码→json
def encode(value):
    with open(filepath, "rb") as f:
        base64_byte = base64.b64encode(f.read())
    #读取时间
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    dictdata={"value":value,"base64":str(base64_byte),"time":now}
    jsondata = json.dumps(dictdata)
    return jsondata

#在接收端进行解码
def decode():
    #将JSON转化为字符串
    dictdata=json.loads(jsondata)
    base64_str=dictdata["base64"]
    #将字符串格式的"base64"转化为bytes格式,但是数据中多了一个b"xxxx"，需要继续筛选
    base64_byte=base64_str.encode(encoding="utf-8")[2:-1]
    imgdata = base64.b64decode(base64_byte)
    file = open('photo1.jpg','wb')
    file.write(imgdata)
    file.close()

    
'''if 传感器数值发生变化,向服务器发送数值
    def sensor():

        return value'''
    
#向服务器发送信息

if __name__ == '__main__':
    siot.connect()
    siot.set_callback(sub_cb)
    siot.getsubscribe(IOT_pubTopic)
    siot.tim()
    try:
      while True:
        get_pic()
        value= 21#sensor()
        draw()
        jsondata = encode(value)
        siot.publish(IOT_pubTopic,jsondata)
        time.sleep(15) #隔多少秒发送一次
    except:
      siot.stop()
      print("disconnect seccused")

        
