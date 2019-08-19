# Database API
## 通用
### get_objects
* 通过object id获取节点对象数据库中的对象  
* 参数: [object-id1, object-id2,...]  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_objects", "params": [["1.2.0", "1.3.0"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_objects", [["1.2.0", "1.3.0"]]], "id": 2}
  < ...
```
* 返回结果的"result"字段为数组，每个元素对应查询中相应位置的对象。  

## 账户
### get_accounts
* 通过账号id批量查询账号  
* 参数：[account-id1, account-id2,...]  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_accounts", "params": [["1.2.0", "1.2.1"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_accounts", [["1.2.0", "1.2.1"]]], "id": 2}
  < ...
```
* 返回[账号结构](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/account.md)  

### get_full_accounts
* 通过账号名查询多个账号全量信息，包含[基础信息](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/account.md)、[持仓](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/account_balance.md)、[挂单](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/limit_order.md)、[哈希时间锁资产](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/htlc.md)等  
* 参数: [账号名数组], 0  
* 第一个参数为账号名数组，第二个参数为是否订阅账号活动，默认填0
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_full_accounts", "params": [["harley", "sun"], 0], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_full_accounts", [["harley", "sun"], 0]], "id": 2}
  < ...
```
* 返回数组，每个元素为二元组，二元组内容为[账号名,全量账号结构]

### get_account_by_name
* 通过账号名查询账号[基础信息](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/account.md)  
* 参数: 账号名
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_account_by_name", "params": ["harley"], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_account_by_name", ["harley"]], "id": 2}
  < ...
```
* 返回[账号结构](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/account.md)

### get_account_references
* 若账号A以账号多签的形式参与了账号B某个权限的多签，则称账号B引用了账号A。本API可以查看哪些账号引用了账号A。  
* 参数:  被引用账号id
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_account_references", "params": ["1.2.6"], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_account_references", ["1.2.6"]], "id": 2}
  < ...
```
* 返回引用该账号的账号id列表

### lookup_account_names
* 通过账号名批量查询账号  
* 参数: 账号名列表
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "lookup_account_names", "params": [["harley", "sun"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "lookup_account_names", [["harley", "sun"]]], "id": 2}
  < ...
```
* 返回[账号结构](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/account.md)列表

### lookup_accounts
* 链上账号名按字典序排序后，返回大于等于指定账号名的账号名和id列表。  
* 参数: 起始字符串,返回记录条数(最大1000)
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "lookup_accounts", "params": ["harley", 100], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "lookup_accounts", ["harley", 100]], "id": 2}
  < ...
```
* 返回数组，每个元素为二元组，内容为[账号名,账号id]

### get_account_count
* 查询链上账户数量  
* 参数: 无  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_account_count", "params": [], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_account_count", []], "id": 2}
  < ...
```
* 返回整数

## 资产
### get_assets
* 使用资产id批量查询资产  
* 参数: 资产id数组  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_assets", "params": [["1.3.0", "1.3.1", "1.3.2"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_assets", [["1.3.0", "1.3.1", "1.3.2"]]], "id": 2}
  < ...
```
* 返回[资产结构](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/asset.md)数组

### list_assets
* 链上资产名按字典序排序后，返回大于等于给定资产名的资产列表  
* 参数: 资产名,返回记录条数(最大100)  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "list_assets", "params": ["JADE", 10], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "list_assets", ["JADE", 10]], "id": 2}
  < ...
```
* 返回[资产结构](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/asset.md)数组

### lookup_asset_symbols
* 使用资产名批量查询资产  
* 参数: 资产名列表
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "lookup_asset_symbols", "params": [["JADE.EOS", "JADE.BTC"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "lookup_asset_symbols", [["JADE.EOS", "JADE.BTC"]]], "id": 2}
  < ...
```
* 返回[资产结构](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/asset.md)数组

## 行情
### get_limit_orders
* 查询链上订单簿中的订单  
* 参数: 资产1 id,资产2 id,订单数量N  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_limit_orders", "params": ["1.3.0", "1.3.2", 10], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_limit_orders", ["1.3.0", "1.3.2", 10]], "id": 2}
  < ...
```
* 返回[订单结构](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/limit_order.md)数组，数组分为两部分，分别是出售资产1求购资产2的订单，求购资产1出售资产2的订单。在每部分中，价格更优的排在前，可参考[排序规则](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/limit_order.md)。每部分最多返回N个订单。

### get_ticker
* 查询最新行情。使用此API需要被访问节点开启[行情历史](https://github.com/CybexDex/cybex-node-doc/blob/master/witness_node_startup.md)插件。  
* 参数: 资产1的id或资产1的符号,资产2的id或资产2的符号  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_ticker", "params": ["1.3.27", "1.3.0"], "id": 1}' https://hongkong.cybex.io
```
或
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_ticker", "params": ["JADE.USDT", "CYB"], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_ticker", ["1.3.27", "1.3.0"]], "id": 2}
  < ...
```
* 返回ticker结构，字段如下  

字段名|类型|含义
---|---|---
time|时间戳|当前时间(0时区)
base|资产id或名字|请求中资产1，也是返回结果中的计价资产
quote|资产id或名字|请求中资产2，也是返回结果中的被计价资产
latest|浮点数|最新成交价，以base资产计价
lowest_ask|浮点数|卖1价
highest_bid|浮点数|买1价
percent_change|浮点数|最新成交价与24小时前最后一笔成交价相比，百分比的波动幅度(例如1表示波动1%)，正数表示最新成交价较高，负数则反之。
base_volume|浮点数|最近24小时内base资产的成交额
quote_volume|浮点数|最近24小时内quote资产的成交额

### get_24_volume
* 查询最近24小时交易量  
* 参数: 资产1的id或资产1的符号,资产2的id或资产2的符号  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_24_volume", "params": ["JADE.USDT", "CYB"], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_24_volume", ["JADE.USDT", "CYB"]], "id": 2}
  < ...
```
* 返回24小时成交量结构，字段如下  

字段名|类型|含义
---|---|---
time|时间戳|当前时间(0时区)
base|资产id或名字|请求中资产1
quote|资产id或名字|请求中资产2
base_volume|浮点数|最近24小时内base资产的成交额
quote_volume|浮点数|最近24小时内quote资产的成交额

### get_order_book
* 查询链上订单簿中的订单(结果顺序同get_limit_orders)，结果以用户可读形式表示。  
* 参数: 资产1的id或资产1的符号,资产2的id或资产2的符号,每个方向返回记录条数  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_order_book", "params": ["JADE.USDT", "CYB", 10], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_order_book", ["JADE.USDT", "CYB", 10]], "id": 2}
  < ...
```
* 返回结果字段如下  

字段名|类型|含义
---|---|---
base|资产id|计价资产，即资产1
quote|资产id|被计价资产，即资产2
asks|数组|卖单队列，出售quote资产的订单，价格低的卖单排在前
bids|数组|买单队列，求购quote资产的订单，价格高的买单排在前
每个订单:price|浮点数|以base计价的订单价格
每个订单:base|浮点数|base资产尚未成交的数量
每个订单:quote|浮点数|quote资产尚未成交的数量

### get_trade_history
* 查询指定交易对的历史成交记录。使用此API需要被访问节点开启[行情历史](https://github.com/CybexDex/cybex-node-doc/blob/master/witness_node_startup.md)插件。  
* 参数: 资产1的id或资产1的符号，资产2的id或资产2的符号，开始时间，结束时间，最大返回记录条数。  
* 参数含义: 返回资产1和资产2的历史成交，从小于等于开始时间的第一条成交记录开始，按时间倒序取成交记录，直到获取到结束时间的成交记录或记录条数达到最大值。  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_trade_history", "params": ["CYB", "JADE.USDT", "2020-01-01T00:00:00", "2019-01-01T00:00:00", 30], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_trade_history", ["CYB", "JADE.USDT", "2020-01-01T00:00:00", "2019-01-01T00:00:00", 30]], "id": 2}
  < ...
```
* 返回结果字段如下  

字段名|类型|含义
---|---|---
sequence|整数|节点的成交编号
date|时间戳|成交时间
price|浮点数|以资产1计价的成交价
amount|浮点数|成交中资产2转移的数量
value|浮点数|成交中资产1转移的数量
side1_account_id|账号id|成交中maker一方的账号id
side2_account_id|账号id|成交中taker一方的账号id
  
### get_trade_history_by_sequence
* 使用上面的get_trade_history查询成交记录时，如果同一时刻有多个成交记录，会导致很难完全遍历，此时，可以使用本api对成交记录进行遍历。使用此API需要被访问节点开启[行情历史](https://github.com/CybexDex/cybex-node-doc/blob/master/witness_node_startup.md)插件。本API与get_trade_history的区别在于遍历的开始时间被替换成遍历的开始id号。  
* 参数: 资产1的id或资产1的符号，资产2的id或资产2的符号，开始id，结束时间，最大返回记录条数。  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_trade_history_by_sequence", "params": ["JADE.USDT", "CYB", 1000000, "2019-01-01T00:00:00", 100], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_trade_history_by_sequence", ["JADE.USDT", "CYB", 1000000, "2019-01-01T00:00:00", 100]], "id": 2}
  < ...
```
* 返回结果字段同get_trade_history。

## 权限和验证
### get_transaction_hex
* 使用交易体的json表示，获取交易序列化后的字节流（16进制表示）。这里的序列化后的字节流是包含签名字段的，因此不能作为客户端签名使用的字节流。  
* 参数: 交易体的json表示。  
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_transaction_hex", "params": [{"ref_block_num":42369,"ref_block_prefix":556684788,"expiration":"2019-08-19T05:13:05","operations":[[1,{"fee":{"amount":55,"asset_id":"1.3.0"},"seller":"1.2.37633","amount_to_sell":{"amount":23376,"asset_id":"1.3.4"},"min_to_receive":{"amount":87235,"asset_id":"1.3.27"},"expiration":"2019-08-19T05:15:35","fill_or_kill":false,"extensions":[]}]],"extensions":[],"signatures":["207adcd427ec30695a6c66506ae893eeae0c25cce70a4f2c68ddb6db0e2423115e05e3fa72a9ac30080aeddf7d8ad15e901fa4bf8f519bd6db64ea5cee28b1d7d4"],"operation_results":[[1,"1.7.787045780"]]}], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_transaction_hex", [{"ref_block_num":42369,"ref_block_prefix":556684788,"expiration":"2019-08-19T05:13:05","operations":[[1,{"fee":{"amount":55,"asset_id":"1.3.0"},"seller":"1.2.37633","amount_to_sell":{"amount":23376,"asset_id":"1.3.4"},"min_to_receive":{"amount":87235,"asset_id":"1.3.27"},"expiration":"2019-08-19T05:15:35","fill_or_kill":false,"extensions":[]}]],"extensions":[],"signatures":["207adcd427ec30695a6c66506ae893eeae0c25cce70a4f2c68ddb6db0e2423115e05e3fa72a9ac30080aeddf7d8ad15e901fa4bf8f519bd6db64ea5cee28b1d7d4"],"operation_results":[[1,"1.7.787045780"]]}]], "id": 2}
  < ...
```
### get_required_signatures
* 当客户端不知道一个交易需要由哪些私钥签名时，可以通过此api查询。
* 参数: 未签名的交易体，客户端已经持有的私钥对应的公钥列表
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_required_signatures", "params": [{"ref_block_num":12775,"ref_block_prefix":2748496443,"expiration":"2019-07-24T02:15:39","operations":[[0,{"fee":{"amount":100,"asset_id":"1.3.0"},"from":"1.2.100","to":"1.2.200","amount":{"asset_id": "1.3.0", "amount": 100000},"extensions":[]}]],"extensions":[],"signatures":[],"operation_results":[[1,"1.19.7639802"]]}, ["CYB5vujBXLBcDB1ae4Cb1phJk6NiSX73PRSxtHHsYVKYF13t1UWLY", "CYB6bCHU6sWD4estBBmpNeLMsuL3aZynrBLANGGg2MjELxzNJt45r"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_required_signatures", [{"ref_block_num":12775,"ref_block_prefix":2748496443,"expiration":"2019-07-24T02:15:39","operations":[[0,{"fee":{"amount":100,"asset_id":"1.3.0"},"from":"1.2.100","to":"1.2.200","amount":{"asset_id": "1.3.0", "amount": 100000},"extensions":[]}]],"extensions":[],"signatures":[],"operation_results":[[1,"1.19.7639802"]]}, ["CYB5vujBXLBcDB1ae4Cb1phJk6NiSX73PRSxtHHsYVKYF13t1UWLY", "CYB6bCHU6sWD4estBBmpNeLMsuL3aZynrBLANGGg2MjELxzNJt45r"]]], "id": 2}
  < ...
```
* 结果为需要签名的私钥对应的公钥列表。若传入的交易体已经包含了签名，则返回仍然需要签名的私钥对应的公钥。
