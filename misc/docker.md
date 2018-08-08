# 获取 docker
download cybex-docker.zip
```
unzip cybex-docker.zip
```

# docker prepare config
* setup net for seed nodes
```
docker network create \
  --driver=bridge \
  --subnet=192.168.0.0/16 \
  --gateway=192.168.0.1 \
  br0
```
the start script shoule be changed to:
```
port=`expr $1  + 38090 `

docker run -it --cap-add=ALL --network=bridge -p $port:8080 -v  /etc/localtime:/etc/localtime:ro -v "/bigdata/home/sunqi/Docker//cybex-docker/mnt/data-dir$1":/data-dir -v /bigdata/home/sunqi/Docker/cybex-docker:/mnt  --name "node$1"  -h  "node$1"  witness_node:v2
```

# 简单启动 docker
* create image and check
```
tar -xf config.tar
cd cybex-docker/docker
./mk-image.sh
docker images
```
* start nodes
```
./start-witness-node.sh <node number>
```
单节点启动完成。
需要注意的是
<node number> should have a pair with cybex-docker/mnt/data-dir<node number>.

* stop and delete

leverage
```
docker ps -a
```
to get all the container ids.
```
docker stop <container id>
docker rm <container id>
```

# 修改配置
if you want to start a new chain, the first start node should be capable to generate A first block, so the param "enable-stale-production" should be set to "true" in data-dir<node-num>/config.ini.
```
enable-stale-production = true
```
The rest config.ini in other data-dir keep to be disabled.

# 再次启动
```
# host
./start-witness-node.sh <node number> 
# in-docker
exit
```
same cmd for other nodes starting...
You could see the start node generate blocks, several seconds later node-2 Got a block then generate a block, then node-3 Got the block genearated by node-2 and gen a new block.
A new chain has been started.
