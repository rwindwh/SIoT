WebAPI
=========================


SIoT提供了一系列的WebAPI，供用户调用。

API列表：
------------
    - 发布消息
Http://[SIoT的IP]:8080/publish?topic=xzr/001&msg=on&iname=siot&ipwd=dfrobot

**说明**：发送topicid（主题）“xzr/001”发送内容为“on”的消息，其中“xzr”是项目id，“001”是设备id。

{"code":1,"msg":"数据已发送"}

 - 获取最新数据
Http://[SIoT的IP]:8080/lastmessage?topic=xzr/001&iname=siot&ipwd=dfrobot

**说明**：未通过测试

 - 获取消息列表
Http://[SIoT的IP]:8080/messages?topic=xzr/001&iname=siot&ipwd=dfrobot&pnum=1&psize=10&begin=2019-04-03&end=2019-04-05

**说明**：未通过测试

 - 清除消息
Http://[SIoT的IP]:8080/clearmsg?topic=xzr/001&iname=siot&ipwd=dfrobot

**说明**：未通过测试

 - 获取项目列表
Http://[SIoT的IP]:8080/projects?iname=siot&ipwd=dfrobot

**说明**：测试通过

"code":1,"data":[{"ID":"DFRobot","Description":"一个项目中包含多个设备\t","Created":1556265411},{"ID":"abc","Description":"","Created":1556939389},{"ID":"xzr","Description":"","Created":1556941184}],"msg":"成功"}

 - 更新项目
Http://[SIoT的IP]:8080/updateprj?pid=xzr&iname=siot&ipwd=dfrobot&desc=科学测量

**说明**：将名称为“xzr”的项目的备注修改为“科学测量”

{"code":1,"msg":"成功"}

 - 获取设备列表
Http://[SIoT的IP]:8080/devices?pid=xzr&iname=siot&ipwd=dfrobot

**说明**：返回项目名称为“xzr”的设备列表。

 - 更新设备
Http://[SIoT的IP]:8080/updatedev?pid=xzr&dname=001&iname=siot&ipwd=dfrobot&desc=台灯控制

**说明**：将项目名称为“xzr”，设备名称为“001”的设备，备注修改为“台灯控制”（发现BUG）

{"code":1,"msg":"成功"}

 - 删除设备
Http://[SIoT的IP]:8080/deldev?topic=xzr/001&iname=siot&ipwd=dfrobot

**说明**：未通过测试


返回数据格式说明：
------------------
{
   code = 1,
   message = "",
   data = {}
}
 **说明**：code等于1，表示成功。data中返回列表信息。