## Building a streaming application

Netflix & co, but also Whatsapp, Telegram, etc. All these are deployed in clouds, and use streaming techniques to move data from one place to another. Here, we will focus on [Apache Kafka](https://kafka.apache.org/), an open-source distributed event streaming platform. In brief, there are two roles: the producer (producing messages), and the consumer (polling messages).

### Installation

Let's first install our Kafka server in our VM. Connect to your VM, and clone the following repository:

```bash
git clone ...
```

Then you need to install Java 8:

```bash
cd streaming
./install_java9.sh

sudo su
echo "export JAVA_HOME=$(dirname $(dirname $(readlink -f $(type -P java))))" > /etc/profile.d/javahome.sh
exit
```

then run the installation script:

```bash
cd streaming
./install_kafka.sh --version 2.1.0
```

Modify the configuration of Zookeeper first (`config/zookeeper.properties`):

```
dataDir=/tmp/zookeeper

# the port at which the clients will connect
clientPort=<your ZOOKEEPER PORT>

# disable the per-ip limit on the number of connections since this is a non-production config
maxClientCnxns=60

# Disable the adminserver by default to avoid port conflicts.
# Set the port to something non-conflicting if choosing to enable this
admin.enableServer=false
server.1=<your IP>:23333:23334
```

Then modify the the server configuration (`config/server.properties`):

```
listeners=PLAINTEXT://<IP>:<PORT>

zookeeper.connect=<IP>:<ZOOKEEPER PORT>
```

Make sure the port `PORT` is open to the world!

and finally launch it:

```bash
cd streaming
./start_kafka.sh --version 2.1.0
```

You can check it runs correctly:

```bash
./ps aux | grep kafka
```

Once you have finished your work, do not forget to shut down the server:

```bash
cd streaming
./stop_kafka.sh --version 2.1.0
```

### Messaging

Anywhere (on your laptop, or VM, or...), produce message using:

```bash
python producer.py -ip $IP -port $PORT
```

And again, anywhere else, read those messages using:

```bash
python consumer.py -ip $IP -port $PORT
```

Youhou! Exercise: have fun by exploring the internals, and producing a real chat application.
