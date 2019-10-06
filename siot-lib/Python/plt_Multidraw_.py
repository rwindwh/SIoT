#本代码能够读取以特定格式上传到siot的数据，并将其对比图置于pylab所绘制的图表中
#数据需为以下字符串格式→    y1=5,y2=9,y3=3
from pylab import *
import threading
from simple import MqttClient
import time,random
import re

SERVER = "192.168.0.102"            #MQTT服务器IP
CLIENT_ID = ""                  #在SIoT上，CLIENT_ID可以留空
IOT_pubTopic  = 'xzr/001'       #“topic”为“项目名称/设备名称”
IOT_UserName ='siot'            #用户名
IOT_PassWord ='dfrobot'         #密码
rcParams['axes.unicode_minus'] = False  #pylab绘图参数
rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签

def sub_cb(client, userdata, msg):
    print("\nTopic:" + str(msg.topic) + " Message:" + str(msg.payload))
    #用正则表达式取出数字
    res=re.findall(r"\d+\.?\d*",str(msg.payload))
    print("senser",res[0],"value:",res[1])
    print("senser",res[2],"value:",res[3])
    print("senser",res[4],"value:",res[5])
    showplt(float(res[1]),float(res[3]),float(res[5])) #开始绘图



def showplt(val1,val2,val3):
    global x,y1,y2,y3,now
    plt.grid(True)
    plt.ion()
    x.append(now)
    now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))[-8:]
    y1.append(val1)
    y2.append(val2)
    y3.append(val3)
    #'-' solid line style '--' dashed line style '-.' dash-dot line style ':' dotted line style
    ax.plot(x,y1,'c-.')
    ax.plot(x,y2,'y-.')
    ax.plot(x,y3,'b-.')
    plt.pause(0.0001)

    #mac系统请删除下方的plt.ioff()语句
    plt.ioff()
    plt.show()


if __name__ == '__main__':
    global x,y1,y2,y3,i,fig, ax
    siot = MqttClient(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
    siot.connect()
    siot.set_callback(sub_cb)
    siot.getsubscribe(IOT_pubTopic)
    siot.tim()
    fig, ax= plt.subplots()
    plt.title('三列折线图 ') # 标题
    plt.xlabel('时间戳') # 横坐标标题
    plt.ylabel('数值') # 纵坐标标题
    now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))[-8:]
    x=[]
    y1=[]
    y2=[]
    y3=[]
    showplt(0,0,0)
    try:
      while True:
        time.sleep(1)
        siot.check_msg()
    except:
      siot.stop()
      print("disconnect seccused")


