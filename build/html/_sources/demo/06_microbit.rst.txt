micro:bit+OBloq
===========================


micro:bit简介
-------------------------

    Micro:bit是由英国BBC公司所推出的面向青少年编程教育的微型计算机。Micro:bit电路板上集成了LED灯、两个可编程按钮、加速度传感器、磁力传感器以及蓝牙等常用设备，采用micro USB口供电，可外接电池盒，底部有多个环孔连接器，可用于控制外接设备。
    
    此外，Micro:bit拥有在线的编程网站（https://makecode.microbit.org/），可通过图形化的编程界面，以及支持python或Javascript等多种编程语言的软件进行编程，例如：BXY、Mind+等。
    
    micro:bit购买网址：http://www.dfrobot.com.cn/goods-1395.html
    

硬件连接
------------------------

.. image:: ../image/zhangyu/microbit相关代码/06-microbit-01.png

从左到右依次为：数据线、microbit、Micro:Mate多功能I/O扩展板（还有两个螺母）、OBLOQ物联网模块、LED模块。

.. image:: ../image/zhangyu/microbit相关代码/06-microbit-02.png

LED灯如图接在12号口。12号口高电平，LED灯亮；12号口低电平，LED灯灭。
    

使用MakeCode（Js代码）
---------------------------------

.. image:: ../image/zhangyu/microbit相关代码/06-microbit-03.png


.. image:: ../image/zhangyu/microbit相关代码/06-microbit-04.png


使用BXY（MicroPython代码）
------------------------------------------

 1、启动BXY，软件下载及df官方教程链接：http://docs.dfrobot.com.cn/bxy/
 
.. image:: ../image/zhangyu/microbit相关代码/06-microbit-05.png

 2、文件-示例-External-9.ObloqMqttSubTopic.py

.. image:: ../image/zhangyu/microbit相关代码/06-microbit-06.png

 3、简介

.. image:: ../image/zhangyu/microbit相关代码/06-microbit-07.png

 行2，导入obloq软件包,只需修改行6-行11内容为个人wifi,iot,topic信息。

.. image:: ../image/zhangyu/microbit相关代码/06-microbit-08.png

 4、修改程序

.. image:: ../image/zhangyu/microbit相关代码/06-microbit-09.png

修改完毕后，可载到板子运行。IOT模块指示灯由红-蓝-绿，表示接上wifi，micro:bit led点阵显示模块分配到的IP地址，表示程序运行成功。
