import mqtt.*;
MQTTClient client;

class Adapter implements MQTTListener {
  void clientConnected() {
    println("client connected");
    client.subscribe("xzr/001");//要订阅的消息名称
  }
  void messageReceived(String topic, byte[] payload) {
    println("new message: " + topic + " - " + new String(payload));
  }
  void connectionLost() {
    println("connection lost");
  }
}
Adapter adapter;
void setup() {
  adapter = new Adapter();
  client = new MQTTClient(this, adapter);
  client.connect("mqtt://siot:dfrobot@127.0.0.1", "processing");//用户名为siotd；密码为frobot
}
void draw() {}
void keyPressed() {
  client.publish("xzr/001", "world");//给名称为"xzr/001"的topic发送消息"world"
}
