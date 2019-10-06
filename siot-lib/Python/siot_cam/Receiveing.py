# coding= UTF-8
import sqlite3
import datetime
import json
import threading
import base64
import time
from flask import Flask, render_template, request
from simple import MqttClient

DATABASE = 'data/data.db'
app = Flask(__name__)
watering = 0

filepath = r'static\images'
filename = r"receive"    #参数调试，需要识别的图片路径里不能带有中文
SERVER = "192.168.0.102"	#MQTT服务器IP
CLIENT_ID = " "	#在SIoT上，CLIENT_ID可以留空
IOT_pubTopic = 'DFRobot/linmy'	#“topic”为“项目名称/设备名称”
IOT_UserName='siot'		#用户名
IOT_PassWord='dfrobot'	#密码
siot = MqttClient(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)

def sub_cb(client, userdata, msg):
    print("\nTopic:" + str(msg.topic) + " Message:" + str(msg.payload))
    #如果数据格式是监控数据,则接受服务器信息，并储存到数据库中
    if len(str(msg.payload))>500:
        #将JSON转化为字符串
        jsondata=msg.payload
        dictdata=json.loads(jsondata)
        base64_str=dictdata["base64"]
        #将字符串格式的"base64code"转化为bytes格式,但是数据中多了一个b"xxxx"，需要继续筛选最后成为单纯的bytes
        base64_byte=base64_str.encode(encoding="utf-8")[2:-1]
        imgdata = base64.b64decode(base64_byte)
        # 存入数据库
        db = sqlite3.connect(DATABASE)
        cur = db.cursor()
        #存入数据库之前要把b'iVBORw0KGg=' 数据格式中的b去掉,再转换单双引号
        dbbasecodein=dictdata["base64"][1:].replace("\'", '\"')
        #dbbasecodeout=('b'+dbbasecodein).replace("\"", '\'')
        cur.execute("INSERT INTO sensorlog(sensor1,base64,datatime) VALUES(%f,'%s','%s')"
                    % (float(dictdata["value"]), str(dbbasecodein), str(dictdata["time"])))
        db.commit()
        db.close()
        #本地存取图片
        file = open(filepath+ '/' + filename + str(dictdata["time"]) +'.jpg','wb')
        file.write(imgdata)
        file.close()

# 在浏览器窗口中显示数据
@app.route("/")
def hello():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    cur.execute("SELECT * FROM sensorlog")
    data = cur.fetchall()
    cur.close()
    db.close()
    temp1 = data[len(data) - 1]
    return render_template('index.html',
                           sensor1=temp1[1],
                           base64=temp1[2][:15],
                           filename=filename+temp1[3]+'.jpg',
                           datatime=temp1[3])

if __name__ == "__main__":
    siot.connect()
    siot.subscribe(IOT_pubTopic, sub_cb)
    siot.tim()
    app.run(host="0.0.0.0", port=5000, debug=True)
    try:
        while True:
            time.sleep(1)
            siot.check_msg()
    except:
        siot.stop()
        print("disconnect seccused")
