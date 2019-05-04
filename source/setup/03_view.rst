
界面简介
=========================
SIoT既可以作为教师教学物联网课程的教学支持平台，也可以作为学生物联网作品的支持平台。
当你下载完成之后就可以运行相应的软件啦。  

下载地址：https://github.com/vvlink/SIoT/tree/master/software

登录Web页面
--------------------
如果你是Windows用户，请运行SIot_win.exe。类似的，如果你是Linux用户，请运行SIoT_linux，如果你是Mac用户，请运行SIoT_mac。
启动软件后请不要关闭这个黑窗口，它将维持你的计算机（电脑）作为MQTT服务器。  
  
  
.. image:: https://github.com/vvlink/SIoT/blob/master/source/image/eason/setup.PNG    

打开浏览器，输入：http://localhost:8080 或者 http://127.0.0.1:8080 进行登录     

.. image:: https://github.com/vvlink/SIoT/blob/master/source/image/eason/login.PNG    

用户名（usr）为：df_admin     

密码（pwd）为：dfrobot  



查看项目
-----------------
登录成功之后，默认界面就是查看项目界面，你也可以通过点击上方菜单栏的“项目列表”访问。   

.. image:: https://github.com/vvlink/SIoT/blob/master/source/image/eason/list_html.PNG

地址：http://localhost:8080/html/

查看设备
-----------------
通过通过点击上方菜单栏的“设备列表”访问。

.. image:: https://github.com/vvlink/SIoT/blob/master/source/image/eason/devices.PNG

地址：http://localhost:8080/html/devices.html


查看数据
-----------------
在“设备列表”界面找到需要查看的设备，在操作这一栏中点击“查看消息”访问。

.. image:: https://github.com/vvlink/SIoT/blob/master/source/image/eason/topicMsg.PNG

地址：http://localhost:8080/html/messages.html?topic=PROGRAM_ID/TOPIC_ID

请把PROGRAM_ID替换成自己的项目名，把TOPIC_ID替换成自己的消息名。

发送消息
-------------------
通过通过点击上方菜单栏的“发送消息”访问。

.. image:: https://github.com/vvlink/SIoT/blob/master/source/image/eason/SendMsg.PNG

地址：http://localhost:8080/html/sendMsg.html
