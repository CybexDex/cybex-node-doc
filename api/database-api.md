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

### get_account_token_age
* 查询账户币龄，需要被访问节点打开[币龄插件](https://github.com/CybexDex/cybex-node-doc/blob/master/witness_node_startup.md#币龄插件)
* 参数: 账号id
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_account_token_age", "params": ["1.2.100"], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_account_token_age", ["1.2.100"]], "id": 2}
  < ...
```
* 返回列表，列表为节点配置的所有币种的币龄，其中CYB的币龄在获取到数据的基础上，除以40再除以100000即为前端显示的币龄。


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

## 持仓
持仓API返回的持仓数量仅包含[账户持仓](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/account_balance.md)部分，不包含订单中冻结的资产、锁定期资产、哈希锁定资产等。
### get_account_balances
* 根据账号id查询账号持仓
* 参数: 账号id，资产id列表
* 若资产id列表为空，则返回账号所有持仓资产列表。
* Http请求例子
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_account_balances", "params": ["1.2.3", ["1.3.0", "1.3.2"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_account_balances", ["1.2.3", ["1.3.0", "1.3.2"]]], "id": 2}
  < ...
```
* 返回数组，数组中的每个元素是二元组，分别为[资产id,持仓数量]

### get_named_account_balances
* 根据账号名查询账号持仓
* 参数: 账号名，资产id列表
* 若资产id列表为空，则返回账号所有持仓资产列表。
* Http请求例子
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_named_account_balances", "params": ["null-account", ["1.3.0", "1.3.2"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_named_account_balances", ["null-account", ["1.3.0", "1.3.2"]]], "id": 2}
  < ...
```
* 返回数组，数组中的每个元素是二元组，分别为[资产id,持仓数量]

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
* 查询最新行情。使用此API需要被访问节点开启[行情历史插件](https://github.com/CybexDex/cybex-node-doc/blob/master/witness_node_startup.md#行情历史插件)。  
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
* 查询指定交易对的历史成交记录。使用此API需要被访问节点开启[行情历史插件](https://github.com/CybexDex/cybex-node-doc/blob/master/witness_node_startup.md#行情历史插件)。  
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
* 使用上面的get_trade_history查询成交记录时，如果同一时刻有多个成交记录，会导致很难完全遍历，此时，可以使用本api对成交记录进行遍历。使用此API需要被访问节点开启[行情历史插件](https://github.com/CybexDex/cybex-node-doc/blob/master/witness_node_startup.md#行情历史插件)。本API与get_trade_history的区别在于遍历的开始时间被替换成遍历的开始id号。  
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

### get_potential_signatures
* 查询可能签名交易的公钥
* 参数: 未签名的交易体
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_potential_signatures", "params": [{"ref_block_num":12775,"ref_block_prefix":2748496443,"expiration":"2019-07-24T02:15:39","operations":[[0,{"fee":{"amount":100,"asset_id":"1.3.0"},"from":"1.2.100","to":"1.2.200","amount":{"asset_id": "1.3.0", "amount": 100000},"extensions":[]}]],"extensions":[],"signatures":[]}], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_potential_signatures", [{"ref_block_num":12775,"ref_block_prefix":2748496443,"expiration":"2019-07-24T02:15:39","operations":[[0,{"fee":{"amount":100,"asset_id":"1.3.0"},"from":"1.2.100","to":"1.2.200","amount":{"asset_id": "1.3.0", "amount": 100000},"extensions":[]}]],"extensions":[],"signatures":[]}]], "id": 2}
  < ...
```
* 返回公钥列表，列表中的每个公钥均为可能签名交易的公钥。对于普通单私钥账户，只需要返回公钥中任意一个对应的私钥签名即可。对于多签账户，使用哪些私钥签名需要结合账号权限设置进行判断。

### verify_authority
* 验证交易签名权限是否满足
* 参数: 签名后的交易体
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "verify_authority", "params": [{"ref_block_num":12775,"ref_block_prefix":2748496443,"expiration":"2019-07-24T02:15:39","operations":[[56,{"fee":{"amount":100,"asset_id":"1.3.0"},"from":"1.2.100","to":"1.2.200","amount":{"asset_id": "1.3.0", "amount": 100000},"extensions":[]}]],"extensions":[],"signatures":["1f1820116d748f266a345f5d6b6ab3e28921395624f21af0509d9c98fb27fca24c344a5062d441ef3b4f8107319a0b9cdb977fa6c7ba589c07926c87f1eb0cdc44"]}], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "verify_authority", [{"ref_block_num":12775,"ref_block_prefix":2748496443,"expiration":"2019-07-24T02:15:39","operations":[[56,{"fee":{"amount":100,"asset_id":"1.3.0"},"from":"1.2.100","to":"1.2.200","amount":{"asset_id": "1.3.0", "amount": 100000},"extensions":[]}]],"extensions":[],"signatures":["1f1820116d748f266a345f5d6b6ab3e28921395624f21af0509d9c98fb27fca24c344a5062d441ef3b4f8107319a0b9cdb977fa6c7ba589c07926c87f1eb0cdc44"]}]], "id": 2}
  < ...
```
* 若满足要求，则返回true，否则，api返回异常。

### validate_transaction
* 验证交易是否能上链。与verify_authority不同的是，validate_transaction不仅验证签名是否满足要求，还验证执行交易需要的条件是否满足，例如转账操作的余额是否足够、下单是否满足fok条件，交易体是否重复等。全节点接受请求后，会基于其当前状态执行一遍交易，并获取交易执行结果。执行完后会恢复现场到执行前状态。
* 参数: 签名后的交易体
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "validate_transaction", "params": [{"ref_block_num":12775,"ref_block_prefix":2748496443,"expiration":"2019-07-24T02:15:39","operations":[[0,{"fee":{"amount":100,"asset_id":"1.3.0"},"from":"1.2.100","to":"1.2.200","amount":{"asset_id": "1.3.0", "amount": 100000},"extensions":[]}]],"extensions":[],"signatures":["1f1820116d748f266a345f5d6b6ab3e28921395624f21af0509d9c98fb27fca24c344a5062d441ef3b4f8107319a0b9cdb977fa6c7ba589c07926c87f1eb0cdc44"]}], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "validate_transaction", [{"ref_block_num":12775,"ref_block_prefix":2748496443,"expiration":"2019-07-24T02:15:39","operations":[[0,{"fee":{"amount":100,"asset_id":"1.3.0"},"from":"1.2.100","to":"1.2.200","amount":{"asset_id": "1.3.0", "amount": 100000},"extensions":[]}]],"extensions":[],"signatures":["1f1820116d748f266a345f5d6b6ab3e28921395624f21af0509d9c98fb27fca24c344a5062d441ef3b4f8107319a0b9cdb977fa6c7ba589c07926c87f1eb0cdc44"]}]], "id": 2}
  < ...
```
* 若交易可以执行，则返回执行结果，否则，api返回异常。

### get_required_fees
* 获取操作所需要的最低手续费。
* 参数: 操作列表，手续费资产
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_required_fees", "params": [[[0,{"fee":{"amount":0,"asset_id":"1.3.0"},"from":"1.2.100","to":"1.2.200","amount":{"asset_id": "1.3.0", "amount": 100000},"extensions":[]}]], "1.3.27"], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_required_fees", [[[0,{"fee":{"amount":0,"asset_id":"1.3.0"},"from":"1.2.100","to":"1.2.200","amount":{"asset_id": "1.3.0", "amount": 100000},"extensions":[]}]], "1.3.27"]], "id": 2}
  < ...
```
* 返回手续费金额列表，列表中每一项对应参数的操作列表中的项。
## 公钥
### get_key_references
* 获取某个公钥所有关联的账户，当公钥同时出现在账户的active和owner权限中时，会返回两次相同的账号id。
* 参数: 公钥列表
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_key_references", "params": [["CYB79urmnmMH5GKxxRXNhxRfMsEgqodHCrnxK6HxzpSA1F3J7MKDE"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_key_references", [["CYB79urmnmMH5GKxxRXNhxRfMsEgqodHCrnxK6HxzpSA1F3J7MKDE"]]], "id": 2}
  < ...
```
* 返回结果为数组，数组中的每一项对应参数中的一个公钥的引用账号列表。

### is_public_key_registered
* 判断公钥是否已经被注册
* 参数: 公钥
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "is_public_key_registered", "params": ["CYB79urmnmMH5GKxxRXNhxRfMsEgqodHCrnxK6HxzpSA1F3J7MKDE"], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "is_public_key_registered", ["CYB79urmnmMH5GKxxRXNhxRfMsEgqodHCrnxK6HxzpSA1F3J7MKDE"]], "id": 2}
  < ...
```
* 返回true或false

## 拟议交易
### get_proposed_transactions
* 获取某个账号需要批准的拟议交易。
* 参数: 账号id
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_proposed_transactions", "params": ["1.2.0"], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_proposed_transactions", ["1.2.0"]], "id": 2}
  < ...
```
* proposal列表

## 区块和交易
### get_block_header
* 使用区块号获取区块头结构
* 参数: 区块号
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_block_header", "params": [100000], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_block_header", [100000]], "id": 2}
  < ...
```
* 返回结果字段如下

字段名|类型|含义
---|---|---
previous|字符串|前一个区块的id
timestamp|时间戳|区块打包时间
witness|打包人id|打包人
transaction_merkle_root|哈希值|交易体的merkle哈希值

### get_block_header_batch
* 使用区块号批量获取多个区块头信息
* 参数: 区块号列表
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_block_header_batch", "params": [[100, 1000, 10000]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_block_header_batch", [[100, 1000, 10000]]], "id": 2}
  < ...
```
* 返回结果为区块头信息列表，列表中的每一项是一个二元组，为[区块号,区块头],其中区块头字段同get_block。

### get_block
* 使用区块号获取区块信息
* 参数: 区块号
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_block", "params": [100000], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_block", [100000]], "id": 2}
  < ...
```
* 返回结果字段如下

字段名|类型|含义
---|---|---
previous|字符串|前一个区块的id
timestamp|时间戳|区块打包时间
witness|打包人id|打包人
transaction_merkle_root|哈希值|交易体的merkle哈希值
witness_signature|哈希值|打包人区块签名
transactions|数组|区块中包含的交易数组

### get_transaction
* 使用区块号和交易号获取某个交易。对于已经打包完成的区块，区块号和交易号是交易的唯一索引。
* 参数:  区块号，交易号
* Http请求例子
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_transaction", "params": [1000000, 1], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_transaction", [10000000, 1]], "id": 2}
  < ...
```
* 返回交易体

## 见证人
### get_witnesses
* 批量查询见证人信息
* 参数: 见证人id列表
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_witnesses", "params": [["1.6.1", "1.6.2"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_witnesses", [["1.6.1", "1.6.2"]]], "id": 2}
  < ...
```
* 返回[见证人](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/witness.md)数组

### get_witness_by_account
* 查询账号创建的见证人
* 参数: 账号id
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_witness_by_account", "params": ["1.2.7"], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_witness_by_account", ["1.2.7"]], "id": 2}
  < ...
```
* 返回[见证人](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/witness.md)结构

### lookup_witness_accounts
* 字典序列出打包人账号
* 参数: 起始字符串，数量
* 在节点所有已创建的打包人中，按创建账号的账号名排序，获取大于等于起始字符串的给定数量个打包人的id。
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "lookup_witness_accounts", "params": ["a", 10], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "lookup_witness_accounts", ["a", 10]], "id": 2}
  < ...
```
* 返回数组，每个元素是一个二元组，分别为[账号名,打包人id]

### get_witness_count
* 获取见证人数量
* 包含活跃见证人和非活跃见证人
* 参数: 无
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_witness_count", "params": [], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_witness_count", []], "id": 2}
  < ...
```

## 理事会成员
### get_committee_members
* 批量查询理事会成员信息
* 参数: 理事会成员id列表
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_committee_members", "params": [["1.5.1", "1.5.2"]], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_committee_members", [["1.5.1", "1.5.2"]]], "id": 2}
  < ...
```
* 返回[理事会成员](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/committee_member.md)数组

### get_committee_member_by_account
* 查询账号创建的理事会成员
* 参数: 账号id
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_committee_member_by_account", "params": ["1.2.7"], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_committee_member_by_account", ["1.2.7"]], "id": 2}
  < ...
```
* 返回[理事会成员](https://github.com/CybexDex/cybex-node-doc/blob/master/objects/committee_member.md)结构

### lookup_committee_member_accounts
* 字段序列出理事会成员账号
* 参数: 起始字符串，数量
* 在节点所有已创建的理事会成员中，按创建账号的账号名排序，获取大于等于起始字符串的给定数量个理事会成员的id。
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "lookup_committee_member_accounts", "params": ["a", 10], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "lookup_committee_member_accounts", ["a", 10]], "id": 2}
  < ...
```
* 返回数组，每个元素是一个二元组，分别为[账号名,理事会成员id]

### get_committee_count
* 获取理事会成员数量
* 包含活跃理事会成员和非活跃理事会成员
* 参数: 无
* 参数:
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_committee_count", "params": [], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_committee_count", []], "id": 2}
  < ...
```

## 全局参数
### get_chain_properties
* 获取链的不可变参数，不可变参数由创世区块文件指定，在链的生命周期中不可被改变。
* 参数: 无
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_chain_properties", "params": [], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_chain_properties", []], "id": 2}
  < ...
```
### get_global_properties
* 获取链的可变参数，可变参数可以由理事会成员通过投票进行调整
* 参数: 无
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_global_properties", "params": [], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_global_properties", []], "id": 2}
  < ...
```
### get_config
* 获取链的静态参数，静态参数在代码中指定，通常用于限制一些交易中的变量，如帐户名长度，资产名称长度等。
* 参数: 无
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_config", "params": [], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_config", []], "id": 2}
  < ...
```
### get_chain_id
* 获取链的id
* 参数: 无
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_chain_id", "params": [], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_chain_id", []], "id": 2}
  < ...
```
### get_dynamic_global_properties
* 获取链的动态参数，动态参数通常跟随最新区块变动，如最新区块高度、最新区块打包人等
* 参数: 无
* Http请求例子  
```Bash
curl --data '{"jsonrpc": "2.0", "method": "get_dynamic_global_properties", "params": [], "id": 1}' https://hongkong.cybex.io
```
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "database", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_dynamic_global_properties", []], "id": 2}
  < ...
```
* 返回结果字段如下  

字段名|类型|含义
---|---|---
head_block_number|整数|最新区块高度
head_block_id|哈希值|最新区块id
time|时间戳|最新区块时间
current_witness|打包人id|最新区块的打包人
next_maintenance_time|时间戳|下一次维护时间
last_budget_time|时间戳|上一次维护结束时间
witness_budget|整数|本维护期内尚未分配的打包人收益
accounts_registered_this_interval|整数|本维护期内新注册账户数量
recently_missed_count|整数|当前节点当前未收到的区块数量
current_aslot|整数|从创世区块的时间开始的block槽数量
dynamic_flags|整数|当前仅使用最低位，当进入维护状态时，置最低位为1
last_irreversible_block_num|整数|当前不可逆区块高度
