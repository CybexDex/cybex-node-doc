## 如何运行cybex节点

假设你的binary built 完备
* Step1. download gensis.json & config.ini

If you want to connect to TEST chain
```
wget https://github.com/NebulaCybexDEX/how-to-run-cybex-node/raw/master/bin/witness_node -O bin/witness_node
wget https://github.com/NebulaCybexDEX/how-to-run-cybex-node/raw/master/bin/cli_wallet -O bin/cli_wallet
wget https://raw.githubusercontent.com/NebulaCybexDEX/how-to-run-cybex-node/master/testchain/genesis.json -O genesis.json
wget https://raw.githubusercontent.com/NebulaCybexDEX/how-to-run-cybex-node/master/testchain/config.ini -O data/config.ini
```
If you want to connect to MAIN chain

```
wget https://github.com/NebulaCybexDEX/how-to-run-cybex-node/raw/master/bin/witness_node -O bin/witness_node
wget https://github.com/NebulaCybexDEX/how-to-run-cybex-node/raw/master/bin/cli_wallet -O bin/cli_wallet
wget https://raw.githubusercontent.com/NebulaCybexDEX/how-to-run-cybex-node/master/mainchain/genesis.json -O genesis.json
wget https://raw.githubusercontent.com/NebulaCybexDEX/how-to-run-cybex-node/master/mainchain/config.ini -O data/config.ini
```
* Step2. 启动witness_node连接到链

```
./bin/witness_node -d data --genesis-json genesis.json --max-ops-per-account 500 --resync-blockchain --replay-blockchain
```



### 各组件基础连接拓扑
1. Trusted Full Node
* extern: internet access required （需要连接P2P网络）
* intern: 192.168.0.100 （rpc interface address）
* port: 8090 （rpc interface port）
* example:
```./programs/witness_node/witness_node --rpc-endpoint="192.168.0.100:8090"```
2. Wallet
* extern: no internet access required
* intern: 192.168.0.102
* port:8092
* example:```./programs/cli_wallet/cli_wallet --server-rpc-endpoint="ws://192.168.0.100:8090"  --rpc-http-endpoint="192.168.0.102:8092"```

3. delayed full node
* will need the IP address and port of the p2p-endpoint from the trusted full node
* the number of blocks(getting from trusted full node) should be delayed
* RPC/Websocket port (rpc interface to the local network) needed too
* example:```./programs/delayed_node/delayed_node --trusted-node="192.168.0.100:8090"                                     --delay-block-count=10   --rpc-endpoint="192.168.0.101:8090"  --seed-nodes "[]" ```


### 搭建测试链 HOW2
* fork  testnet code base
```
git clone https://github.com/bitshares/bitshares-core.git bitshares-core-testnet
cd bitshares-core-testnet/
git checkout testnet
```
* 配置
1. blockchain 参数配置在
```
vim libraries/chain/include/graphene/chain/config.hpp
```
2. 默认种子节点列表hard code 在 libraries/app/application.cpp
```
 167       vector<string> seeds = {
 168                "seed.testnet.bitshares.eu:1776",   // BitShares Europe
 169                "176.9.148.19:16543",               // Uptick.rocks
 170                "31.171.251.20:1776",               // @Taconator
 171                "23.92.53.25:11010",                // sahkan
 172                "139.162.242.253:1700",             // rnglab
 173       };

```

* 编译安装
```
$ mkdir build
$ cd build
$ cmake ..
$ make -j4
```
* 生成genesis.json文件  
```
$ mkdir -p genesis
$ programs/witness_node/witness_node --create-genesis-json genesis/my-genesis.json
$ vim genesis/my-genesis.json
```
 my-genesis.json  决定了初始的网络状态，修改相关配置可以定制
1. chian id（即初始状态的hash码），若要同步某个已存链，需要配置相同的id；
2. 账户的名称和公钥
3. 初始的见证者（账号和签名钥匙）
4. 资产及其初始的分布
* Including Genesis into the binaries
```
$ make clean
$ find . -name "CMakeCache.txt" | xargs rm -f
$ find . -name "CMakeFiles" | xargs rm -Rf
$ cmake -DGRAPHENE_EGENESIS_JSON="$(pwd)/genesis.json" .
```
或者将
```
set(GRAPHENE_EGENESIS_JSON "${CMAKE_CURRENT_SOURCE_DIR}/genesis.json" )
```
添加进CMakeFile.txt

* 配置config.ini文件
```
$ mkdir -p data/testnet
$ vim data/testnet/config.ini
```
example:
```
witness-id = "1.6.1"
witness-id = "1.6.2"
witness-id = "1.6.3"
witness-id = "1.6.4"
witness-id = "1.6.5"
witness-id = "1.6.6"
witness-id = "1.6.7"
witness-id = "1.6.8"
witness-id = "1.6.9"
witness-id = "1.6.10"
# For each witness, add pubkey and private key:
private-key = ["GPH6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV","5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"]
private-key = [<pubkey>,<privkey>]
private-key = [<pubkey>,<privkey>]
private-key = [<pubkey>,<privkey>]
private-key = [<pubkey>,<privkey>]
private-key = [<pubkey>,<privkey>]
private-key = [<pubkey>,<privkey>]
private-key = [<pubkey>,<privkey>]
private-key = [<pubkey>,<privkey>]
private-key = [<pubkey>,<privkey>]
private-key = [<pubkey>,<privkey>]
```
private key用于sign blocks。通常来说见证者在不同的节点上，测试链为了简化可以让不同的见证者共享一个节点。
rpc-endpoint 连接 wallet（cli 或者web）；p2p-endpoint，internet 接入点，亦可作为seed node。
#### 使用cli_wallet初始化链
* import batch
```
>>> import_accounts <path to exported json> <password of wallet you exported from>
>>> import_account_keys /path/to/keys.json <my_password> <my_account_name> <my_account_name>
>>> import_balance <my_account_name> ["*"] true
```

* import one by one 
```
>>> import_balance <my_account_name> ["*"] true
```
* verify
```
>>> list_account_balances <my_account_name>
```

### 使用delay node
delayed full node 连接信任节点。信任节点即通常的全节点与P2P 网络相连接，可以认为是 delayed node 的proxy。delayed 节点会delay block直到这些block 变成irrreversible。根据出块速度和见证者规模会导致几分钟的延迟。
example：
```
./programs/delayed_node/delayed_node --trusted-node="192.168.0.100:8090" --rpc-endpoint="192.168.0.101:8090" -d delayed_node -s "0.0.0.0:0"  --p2p-endpoint="0.0.0.0:0" --seed-nodes "[]"
```
note: 信任节点应该在delayed节点之前启动
``
