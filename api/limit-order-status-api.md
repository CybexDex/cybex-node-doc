# Limit Order Status API

limit_order_status API可以用来查看用户的历史订单状态。在区块链数据库中，订单被完全撮合或撤单后，节点会删除该订单的信息，用户只有在自己的账户操作历史中可以查看到这个订单的相关信息。此API可以向用户提供查询本人历史订单的接口。使用此API需要节点打开[历史订单插件](https://github.com/CybexDex/cybex-node-doc/blob/master/witness_node_startup.md#历史订单插件)，该插件会跟踪和记录订单信息，并供API查询。

## 订单结构  
字段名|类型|含义
---|---|---
order_id|订单id|订单在链上核心账本中的id
seller|账号id|挂单人
key:asset1|资产id|交易市场
key:asset2|资产id|
is_sell|bool|true表示出售asset1，false表示出售asset2
amount_to_sell|整数|下单时请求出售的资产数量
min_to_receive|整数|下单时请求购买的资产数量
sold|整数|已经出售的资产数量
received|整数|已经购得的资产数量
canceled|整数|撤单时尚未完全出售的资产数量
block_num|整数|创建订单的交易所在区块号
trx_in_blk|整数|创建订单的交易在区块中的交易编号
op_in_trx|整数|创建订单的操作在交易中的操作编号
create_time|时间戳|创建订单的区块的时间戳

## 历史订单状态
### get_limit_order_status
* 遍历账号的历史订单
* 参数: 账号id，遍历起始的订单id，最大返回记录条数
* 首次访问时，起始订单id可指定为1.7.0，节点会自动从最大符合要求的订单开始寻找。
```Bash
wscat -c wss://normal-hongkong.cybex.io
> {"method": "call", "params": [1, "limit_order_status", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_limit_order_status", ["1.2.100", "1.7.10000", 10]], "id": 2}
  < ...

```
* 返回结果为指定账号的，订单号小于等于指定订单id的订单结构数组

### get_market_limit_order_status
* 遍历某个交易对下，账号的历史订单
* 参数: 账号id，资产1的id，资产2的id，遍历起始的订单id，最大返回记录条数
* 首次访问时，起始订单id可指定为1.7.0，节点会自动从最大符合要求的订单开始寻找。
```Bash
wscat -c wss://normal-hongkong.cybex.io
> {"method": "call", "params": [1, "limit_order_status", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_market_limit_order_status", ["1.2.100", "1.3.0", "1.3.27", "1.7.10000", 10]], "id": 2}
  < ...
```
* 返回结果为指定账号在指定交易对下，订单号小于等于指定订单id的订单结构数组

### get_limit_order_id_by_time
* 根据时间查询订单号
* 参数: 时间戳
* 返回在用户指定时间戳之前的最大订单号，系统采用UTC时间格式
```Bash
wscat -c wss://normal-hongkong.cybex.io
> {"method": "call", "params": [1, "limit_order_status", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method":"call", "params": [2, "get_limit_order_id_by_time", ["2019-10-01T00:00:00"] ], "id": 2} 
  < ...
```
* 返回满足要求的最大订单id

## 当前订单状态
### get_opened_limit_order_status
* 查询账号的当前订单
* 当前订单未尚未完全撮合且尚未过期的订单
* 参数: 账号id
```Bash
wscat -c wss://normal-hongkong.cybex.io
> {"method": "call", "params": [1, "limit_order_status", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_opened_limit_order_status", ["1.2.100"]], "id": 2}
  < ...
```
* 返回指定账号的当前订单组成的订单结构数组

### get_opened_market_limit_order_status
* 查询账号在某个交易对下的当前订单
* 参数: 账号id，资产1的id，资产2的id
```Bash
wscat -c wss://normal-hongkong.cybex.io
> {"method": "call", "params": [1, "limit_order_status", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_opened_market_limit_order_status", ["1.2.100", "1.3.0", "1.3.27"]], "id": 2}
  < ...
```
* 返回指定账号在指定交易对下的订单结构数组


## 自定义交易对订单状态
通过设置交易对，可以使节点返回按交易对过滤后的订单信息，在一个websocket连接的生命周期内，用户可以设置若干自定义交易对，并通过api查询所有自定义交易对之内(或之外)的订单。
### add_filtered_market
* 设置自定义交易对
* 参数: 交易对数组
```Bash
wscat -c wss://normal-hongkong.cybex.io
> {"method": "call", "params": [1, "limit_order_status", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method":"call", "params": [2, "add_filtered_market", [[ ["1.3.0", "1.3.2"], ["1.3.2", "1.3.27"] ]] ], "id": 2} 
  < ...
```
* 无返回结果

### get_filtered_limit_order_status
* 使用自定义交易对过滤订单
* 参数: 账号id，遍历起始的订单id，最大返回记录条数，是否过滤交易对中的订单(true为获取交易对内的订单，false为获取交易对外的订单)
* 首次访问时，起始订单id可指定为1.7.0，节点会自动从最大符合要求的订单开始寻找。
```Bash
wscat -c wss://normal-hongkong.cybex.io
> {"method": "call", "params": [1, "limit_order_status", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method":"call", "params": [2, "add_filtered_market", [[ ["1.3.0", "1.3.2"], ["1.3.2", "1.3.27"] ]] ], "id": 2} 
  < ...
> {"method":"call", "params": [2, "get_filtered_limit_order_status", ["1.2.100", "1.7.10000", 100, true] ], "id": 3} 

```
* 返回订单结构数组

### clear_filtered_market
* 清空所有已设置的交易对
* 参数： 无
```Bash
wscat -c wss://normal-hongkong.cybex.io
> {"method": "call", "params": [1, "limit_order_status", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method":"call", "params": [2, "add_filtered_market", [[ ["1.3.0", "1.3.2"], ["1.3.2", "1.3.27"] ]] ], "id": 2} 
  < ...
> {"method":"call", "params": [2, "clear_filtered_market", [] ], "id": 3} 
  < ...
```

