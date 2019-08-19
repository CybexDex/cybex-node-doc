# 节点启动方式
Cybex节点是单进程程序，用来承载Cybex链的分布式账本。账本根据用途分为核心账本和插件账本。核心账本记录区块链当前状态，是状态机演进的依据。每个节点维护一份相同的核心账本拷贝。插件账本依附于核心账本存在，不作为状态机演进的依据，当API访问的数据不能完全由核心账本提供时，通常由插件账本基于核心账本另行计算一份数据，供API访问者使用，不同的节点可以使用不同的插件及不同的插件启动参数，以根据需要提供不同的插件账本数据。举例来说，用户的余额、账户属性、资产属性，属于核心账本数据，若用户发起转账操作，需要核心账本验证并修改用户余额；订单簿也属于核心账本，当用户下单时，需要根据订单簿中的订单进行撮合。反之，行情K线、历史成交记录属于插件账本，他们的数据仅供API查询，并不作为任何操作的计算依据。

# 目录结构
以下为运行节点推荐的目录结构，用户可以根据需要自定义文件和目录的位置，并在命令行参数中作对应的更改。
```bash
working-directory
  ├── witness_node # 二进制可执行程序
  ├── genesis.json # 创世区块
  ├── access.json  # api访问配置文件(可选)
  └── data         # 数据目录
       ├── blockchain  # 区块和账本数据目录
       │     ├── database # 区块数据目录
       │     │     └── block_num_to_block # 区块数据目录
       │     │           ├── blocks # 区块文件
       │     │           └── index  # 区块索引文件
       │     ├── db_version # 账本数据库版本文件
       │     └── object_database # 对象数据库目录
       ├── config.ini # 主配置文件
       └── logs # 日志目录
             └── p2p # p2p日志目录
                  ├── p2p.log # 当前p2p日志
                  ├── p2p.log.20190101T000000 # 滚动的历史p2p日志
                  └── p2p.log.20190101T010000 # 滚动的历史p2p日志
```
# 节点插件
## 见证人插件
本插件是核心账本使用的插件，启动节点程序均应包含本插件。
### 插件名
witness
### 插件参数
* data-dir: 本节点数据目录，目录下至少需要包含config.ini文件
* p2p-endpoint: 本节点启动时绑定的p2p的ip和端口号
* seed-node: 本节点加入p2p网络时的种子节点
* seed-nodes: 本节点加入p2p网络时的备选种子节点
* rpc-endpoint: 本节点提供rpc服务的ip和端口号
* genesis-json: 创世区块文件
* plugins: 启动参数列表
* replay-blockchain: 重演节点账本，会重新执行区块中的所有交易
* resync-blockchain: 从p2p网络中重新同步所有区块数据，并重演节点账本
* api-access: 指定api访问控制配置json文件

### api访问控制配置文件
例子:
```bash
{
    "permission_map": [
        [
            "*",
            {
                "password_hash_b64": "*",
                "password_salt_b64": "*",
                "allowed_apis": [
                    "database_api",
                    "network_broadcast_api",
                    "history_api"
                ]
            }
        ]
    ]
}
```

### 命令行启动方式
```bash
./witness_node -d data/ --rpc-endpoint 0.0.0.0:8090 --seed-node 1.1.1.1:5000 --seed-nodes "[\"2.2.2.2:5000\",\"3.3.3.3:5000\"]" --genesis-json genesis.json --plugins "witness"
```

## 账号历史插件
本插件用来追溯账户的操作历史，当节点需要向客户端提供历史操作查询功能时，需打开本插件。
### 插件名
account_history
### 插件参数
* track-account: 账号id，可以指定多次，若指定了此参数，则节点只保留所有被指定账号的操作历史记录。
* partial-operations: 只保留指定数量的记录条数
* max-ops-per-account: 每个账号保留记录条数的最大数量

### 命令行启动方式
```bash
./witness_node -d data/ --rpc-endpoint 0.0.0.0:8090 --seed-node 1.1.1.1:5000 --seed-nodes "[\"2.2.2.2:5000\",\"3.3.3.3:5000\"]" --genesis-json genesis.json --plugins "witness account_history" --track-account "1.2.100" --track-account "1.2.200"
```

## 行情历史插件
本插件用来追溯交易对的行情、成交记录、最近成交价。
### 插件名
market_history
### 插件参数
* bucket-size: 记录k线的种类，以秒为单位，例如[60,300,3600]表示记录1分钟、5分钟和1小时K线
* history-per-size: 每种k线记录的最大条数，例如1000表示每个k线保留1000条
* max-order-his-records-per-market: 每个交易对可追溯的成交记录最大条目数
* max-order-his-seconds-per-market: 每个交易对可追溯的成交记录最大保留时间

### 命令行启动方式
```bash
./witness_node -d data/ --rpc-endpoint 0.0.0.0:8090 --seed-node 1.1.1.1:5000 --seed-nodes "[\"2.2.2.2:5000\",\"3.3.3.3:5000\"]" --genesis-json genesis.json --plugins "witness market_history" --bucket-size "[60,300,3600]" --history-per-size 1000 --max-order-his-records-per-market 10000 --max-order-his-seconds-per-market 259200
```

## 快照插件
本插件用来产生快照文件，需要在节点启动时指定快照的时间点或区块号，当达到指定的快照时间或区块时，节点会在当前运行目录生成一个指定名字的账本全量快照文件。若要产生当前时间之前某个区块或时间的快照，需要在命令行启动时指定--replay-blockchain参数。快照文件详情可参考[获取快照](https://github.com/CybexDex/cybex-node-doc/blob/master/%E8%8E%B7%E5%8F%96%E5%BF%AB%E7%85%A7%E6%96%B9%E6%B3%95.pdf)

### 插件名
snapshot
### 插件参数
* snapshot-at-block: 指定快照的区块
* snapshot-at-time: 指定快照的时间
* snapshot-to: 快照文件名

### 命令行启动方式
```bash
./witness_node -d data/ --rpc-endpoint 0.0.0.0:8090 --seed-node 1.1.1.1:5000 --seed-nodes "[\"2.2.2.2:5000\",\"3.3.3.3:5000\"]" --genesis-json genesis.json --plugins "witness snapshot" --snapshot-at-time "2020-01-01T00:00:00" --snapshot-to "20200101000000.snapshot"
```

## 币龄插件
币龄插件用于统计账号的币龄
### 插件名
token_age
### 插件参数
* track-asset: 统计的资产类型，若多次指定，则表示统计多个资产的币龄
* stat-period: 更新周期，以秒为单位
* aging-percent: 每次更新时，旧币龄的折旧因子,以10000为分母，即9000表示折旧为90%

### 命令行启动方式
```bash
./witness_node -d data/ --rpc-endpoint 0.0.0.0:8090 --seed-node 1.1.1.1:5000 --seed-nodes "[\"2.2.2.2:5000\",\"3.3.3.3:5000\"]" --genesis-json genesis.json --plugins "witness token_age" --track-asset "1.3.0" --stat-period 86400 --aging-percent 9750
```
