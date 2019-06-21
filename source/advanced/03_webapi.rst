WebAPI
=========================


SIoT提供了一系列的WebAPI，供用户调用。一些不支持MQTT的编程语言，如VB，也可以通过这种形式和SIoT进行互动。

API列表：
-----------------
    - 发布消息
    Http://[SIoT的IP]:8080/publish?topic=xzr/001&msg=on&iname=siot&ipwd=dfrobot

    **说明**：向topicid（主题）“xzr/001”发送内容为“on”的消息，其中“xzr”是项目id，“001”是设备id。

    返回数据：{"code":1,"msg":"数据已发送"}

    - 获取最新数据

    Http://[SIoT的IP]:8080/lastmessage?topic=xzr/001&iname=siot&ipwd=dfrobot

    **说明**：获取topicid（主题）“xzr/001”的最新一条消息
    
    返回数据：{"code":1,"data":[{"ID":27,"Topic":"xzr/001","Content":"11","Created":"2019-06-06 11:55:39"}],"msg":"成功"}

    - 获取消息列表

    Http://[SIoT的IP]:8080/topic=xzr/001&iname=siot&ipwd=dfrobot&pnum=1&psize=10&begin=2019-04-03+00%3A00%3A00&end=2019-06-07+00%3A00%3A00

    **说明**：
    
    返回数据：{"code":1,"data":[{"ID":26,"Topic":"xzr/001","Content":"10","Created":"2019-06-06 11:55:33"},{"ID":27,"Topic":"xzr/001","Content":"11","Created":"2019-06-06 11:55:39"}],"msg":"成功"}

    - 清除消息

    Http://[SIoT的IP]:8080/clearmsg?topic=xzr/001&iname=siot&ipwd=dfrobot

    **说明**：删除topicid（主题）“xzr/001”的所有消息
    
   返回数据：{"code":1,"data":4,"msg":"成功清空消息"}

    - 获取项目列表

    Http://[SIoT的IP]:8080/projects?iname=siot&ipwd=dfrobot

    **说明**：

    返回数据："code":1,"data":[{"ID":"DFRobot","Description":"一个项目中包含多个设备\t","Created":1556265411},{"ID":"abc","Description":"","Created":1556939389},{"ID":"xzr","Description":"","Created":1556941184}],"msg":"成功"}

     - 更新项目

    Http://[SIoT的IP]:8080/updateprj?pid=xzr&iname=siot&ipwd=dfrobot&desc=科学测量

    **说明**：将名称为“xzr”的项目的备注修改为“科学测量”

   返回数据： {"code":1,"msg":"成功"}

    - 获取设备列表

    Http://[SIoT的IP]:8080/devices?pid=xzr&iname=siot&ipwd=dfrobot

    **说明**：返回项目名称为“xzr”的设备列表。

    - 更新设备

    Http://[SIoT的IP]:8080/updatedev?pid=xzr&dname=001&iname=siot&ipwd=dfrobot&desc=台灯控制

    **说明**：将项目名称为“xzr”，设备名称为“001”的设备，备注修改为“台灯控制”（发现BUG）

    {"code":1,"msg":"成功"}

     - 删除设备

    Http://[SIoT的IP]:8080/deldev?topic=xzr/001&iname=siot&ipwd=dfrobot

    **说明**：
    
    返回数据：{"code":1,"msg":"删除成功"}


返回数据的通用格式说明：
-----------------------------------
{
   code = 1,
   message = "",
   data = {}
}
 **说明**：code等于1，表示成功。data中返回列表信息。
 
