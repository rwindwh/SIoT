互动媒体之龙舟竞赛
=====================================

基于SIoT和和掌控板，可以设计一些多人竞赛的游戏，然后借助Mind+实时呈现出来。

**案例作者：张喻，林淼焱 **

程序描述：
--------------------


.. image:: ../image/linmiaoyan/。。。.png


原理介绍
-----------------
本案例分为两个终端，分别为划手1（player1）和划手2（player2）。player1端和player2端通过连接同一物联网平台MQTT（siot）进行数据的交换，从而实现联机比拼的功能。


准备工作
-----------------

1.运行SIoT

.. image:: ../image/linmiaoyan/。。。.png

2.运行Mind+1.5.5及以上的版本

  mind+下载地址：http://mindplus.cc

*本教程使用的是Mind+1.5.5版本软件


操作步骤
-----------

1.运行mind+，选择右上角“实时模式”，点击左下角“扩展”，添加”网络服务”中的“MQTT”。

.. image:: ../image/linmiaoyan/Mind+danmu-01.png

.. image:: ../image/linmiaoyan/Mind+danmu-02.png

2.编写代码。

1）在终端1的“背景”中写如下程序。

.. image:: ../image/example/06_subtitles_1.png

并修改MQTT服务器相关的参数

  **说明**：Topic设置为“xzr/001”（项目ID/名称）

2）给角色1选择多个造型。

3）在角色1中写如下代码。

.. image:: ../image/example/06_subtitles_2.png

4）复制出4个角色，修改代码。

5）如果想要确认客户端与服务器间的通讯是否正常，可以在变量中为“消息数量”打勾，实时查看数据的传输情况。

参考代码
---------------

代码下载地址：https://github.com/vvlink/SIoT/tree/master/examples/Mind%2B



运行界面：

.. image:: ../image/linmiaoyan/。。。.png

视频演示：

https://github.com/vvlink/SIoT/blob/master/source/image/linmiaoyan/。。。

拓展思考
-----------------

利用这一作品原理，可以制作一些集体互动的大型游戏。
