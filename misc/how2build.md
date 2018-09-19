## 源码编译cybex节点
### linux环境
* prepare dependencies
```
sudo apt-get update
sudo apt-get install autoconf cmake git libboost-all-dev libssl-dev
```

* download source code
```
git clone https://github.com/bitshares/bitshares-core.git
cd bitshares-core
git checkout <LATEST_RELEASE_TAG>
git submodule update --init --recursive
```

* build
```
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
make -j4
```
If the source code contains mongo plugin:

```
# MongoC lib for MongoCxx Lib
wget https://github.com/mongodb/mongo-c-driver/releases/download/1.10.2/mongo-c-driver-1.10.2.tar.gz
tar zxvf mongo-c-driver-1.10.2.tar.gz
cd mongo-c-driver-1.10.2
mkdir cmake-build
cd cmake-build
cmake -DENABLE_AUTOMATIC_INIT_AND_CLEANUP=OFF ..
make && sudo make install

# MongoCxx lib for MongoDB plugin in BitShares
git clone https://github.com/mongodb/mongo-cxx-driver.git --branch releases/v3.3 --depth 1
cd mongo-cxx-driver/build/
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=False -DCMAKE_INSTALL_PREFIX=/usr/local ..
sudo make EP_mnmlstc_core
make && sudo make install
```


### mac环境
1. get source code similar with linux
2. install openssl, boost via brew
```
brew install git
brew install openssl
brew install boost
brew install autoconf
```
3. build
```
mkdir biuld
cd build
cmake .. -DOPENSSL_ROOT_DIR=/usr/local/Cellar/openssl/1.0.2o_2/ -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j40
```
