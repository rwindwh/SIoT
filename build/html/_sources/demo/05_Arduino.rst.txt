Arduino+OBloq
=========================

Arduino简介
---------------------
    Arduino是一款灵活便捷、易于上手的开源硬件，包含硬件部分（各种符合Arduino规范的电路板）和软件部分（一套整合的开发环境软件）两个部分。
    Arduino既可用来开发独立运作并具有互动性的电子产品，也可开发与PC相连的周边装置，同时能在运行时与PC上的软件进行交互。

OBloq模块简介
---------------------
    Arduino自身不能连接网络，但是借助于OBLOQ之类的扩展模块，Arduino也能轻松接入物联网。
    
    OBLOQ是一款基于ESP8266设计的串口转WIFI物联网模块，用以接收和发送物联网信息。模块尺寸紧凑，价格低，接口简单，即插即用，适用于3.3V~5V的控制系统。
    OBLOQ模块具备的两个基础功能：发送数据到物联网和接收物联网数据。即：
      1.Arduino读取温度传感器的数据，通过OBLOQ模块发送温度数据到物联网设备。
      
      2.物联网设备发送数据，OBLOQ接收数据并发送给Arduino,Arduino再通过串口显示接收的数据。
      
      OBloq模块通过wifi连接上网，收发数据。联网后，当检测到有最新版固件时，Obloq会自动升级。
      
      OBloq模块的购买链接：http://www.dfrobot.com.cn/goods-1577.html

    当OBloq处于正常工作时，Obloq上LED灯为绿色常亮，升级时为白色；当Obloq升级结束后，指示灯由白色变成红色，此时需要重启主控版，使得Obloq最新固件生效。
 其端口连接如下：

.. image:: ../image/zhangyu/05-Arduino-01.png

   


硬件连接
---------------------
将Arduino UNO主控板与OBloq模块结合，就等于搭建了一个智能设备。即：主控板 + 物联网模块 = 智能设备





参考代码
---------------------
一、Obloq发送消息

1.定义函数，导入库；

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-11.PNG

2.利用串口发送消息，并检查串口是否正常进行

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-12.PNG

3.连接WiFi，连接设备，利用串口返回设备相关状态

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-13.PNG

4.监听消息的接收，成功则串口返回。

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-14.PNG

5.创建发送消息设备凭据。

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-15.PNG

6.串口返回设备凭据的创建成功。

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-16.PNG

7.分隔存储字符串

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-17.PNG

8.处理串口消息

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-18.PNG

9.验证串口是否正常通信

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-19.PNG

10.根据不同状态发送不同命令，接收到传感器测得数据

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-20.PNG

11.接收消息

.. image:: ../image/zhangyu/ObloqSend/05-Arduino-21.PNG


二、Obloq接收信息

1.导入SoftwareSerial库，定义WiFi

.. image:: ../image/zhangyu/ObloqReceive/05-Arduino-21.png

2.通过串口发送消息

.. image:: ../image/zhangyu/ObloqReceive/05-Arduino-22.png

3.成功连接WiFi并返回代码

.. image:: ../image/zhangyu/ObloqReceive/05-Arduino-23.png

4.监听设备的设置与取消

.. image:: ../image/zhangyu/ObloqReceive/05-Arduino-24.png

5.消息发送通过串口显示

.. image:: ../image/zhangyu/ObloqReceive/5-6/05-Arduino-25.png

6.打印

.. image:: ../image/zhangyu/ObloqReceive/5-6/05-Arduino-26.png

7.销毁设备凭据

.. image:: ../image/zhangyu/ObloqReceive/05-Arduino-27.png

8.分隔字符串

.. image:: ../image/zhangyu/ObloqReceive/05-Arduino-28.png

9.处理串口数据

.. image:: ../image/zhangyu/ObloqReceive/9-10/05-Arduino-29.png



.. image:: ../image/zhangyu/ObloqReceive/9-10/05-Arduino-210.png

10.检验串口是否正常

.. image:: ../image/zhangyu/ObloqReceive/05-Arduino-211.png

11.接收信息字符串

.. image:: ../image/zhangyu/ObloqReceive/12-13/05-Arduino-212.png


.. image:: ../image/zhangyu/ObloqReceive/12-13/05-Arduino-213.png

