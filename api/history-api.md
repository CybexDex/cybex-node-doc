# History API
## 查询账号操作历史
* 查询账号操作历史需要节点打开[账号历史插件](https://github.com/CybexDex/cybex-node-doc/blob/master/witness_node_startup.md#账号历史插件)
* 用户的每一个操作对应节点上的一个历史操作id，历史操作id为"1.11.X"的格式，其中X为序号。序号越大的操作对应发生时间越晚。
* 用户的操作可以分为两类，一是用户签名并主动发起的交易中包含的操作，二是虚拟操作。虚拟操作由节点在一定条件下触发，用于表示某些执行结果。例如，用户发送订单需要用户签名，将下单操作包含在某个交易中，并主动发送到链上，属于第一类操作；订单上链后，若与其他订单发生撮合，节点会生成一个虚拟的撮合操作，该操作与用户的下单操作并无一一对应关系，也不需要用户签名，只是用来表示一次撮合的结果。账号历史api可以同时查询两类操作。

### get_account_history
* 通过账号id查询账号操作历史
* 参数: 账号id, 终止id，返回记录条数，起始id。  
* 参数中需要起始id大于终止id，节点从起始id开始，倒序遍历该账号所有操作历史，直到满足返回记录条数要求或达到终止id。返回记录条数最大为100。若无法在一次请求中获取全部记录，下一次调用时可以使用前一次调用中最后一条记录的id，将其中的序号减一，作为下一次调用的起始id。第一次调用时，由于无法确定起始id，可以填写"1.11.0"，节点自动查找当前链上的最大id作为起始id。
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "history", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_account_history", ["1.2.0", "1.11.0", 10, "1.11.0"]], "id": 2}
  < ...
```
* 返回结果为操作历史列表，列表中每一项的字段内容如下  

字段名|类型|含义
---|---|---
id|历史操作id|"1.11.X"形式的历史操作id
block_num|整数|操作所在的区块号，若操作为虚拟操作，则为触发该操作的区块号
trx_in_block|整数|交易在区块中的序号
op_in_trx|整数|操作在交易中的序号
op|json|操作对象

### get_account_history_operations
* 查询账号指定操作类型的操作历史
* 参数: 账号id，操作编号，起始id，终止id，返回记录条数
* 常用操作编号：转账->0，下单->1，撤单->2，成交(虚拟)->4。编号规则与get_account_history相同。
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "history", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_account_history_operations", ["1.2.0", 0, "1.11.0", "1.11.0", 10]], "id": 2}
  < ...
```
* 返回结果与get_account_history相同。

### get_account_history_by_operations
* 以账号自身操作顺序为编号，获取指定数量的、指定操作的操作历史
* 参数: 账号id，操作编号列表，起始记录号，记录条数
* 常用操作编号：转账->0，下单->1，撤单->2，成交(虚拟)->4。操作编号列表留空表示获取所有操作。
* 例如，账号依次执行了10个操作，分别为 转账1，转账2，下单3，成交4，下单5，撤单6，转账7，下单8，撤单9，撤单10。若操作编号指定为 [转账，成交]，起始序号为0，记录条数为5，则返回[转账1，转账2，成交4]。若操作编号指定为 [转账，撤单]，起始序号为5，记录条数为5，则返回[撤单6，转账7，撤单9，撤单10]。
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "history", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_account_history_by_operations", ["1.2.100", [0, 1], 0, 20]], "id": 2}
  < ...
```

* 返回结果中，total_count表示返回记录的条数，operation_history_objs为操作记录的列表，列表中每一项同get_account_history。

### get_relative_account_history
* 以账号自身操作顺序为编号，获取指定数量的操作历史
* 参数: 账号id，终止id，记录条数，起始id
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "history", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_relative_account_history", ["1.2.100", 100, 5, 105]], "id": 2}
  < ...
```
* 返回结果同get_account_history。


## 查询行情历史
* 查询历史行情需要节点打开[行情历史插件](https://github.com/CybexDex/cybex-node-doc/blob/master/witness_node_startup.md)

### get_market_history_buckets
* 获取节点可提供的K线种类。
* 参数: 无
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "history", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_market_history_buckets", []], "id": 2}
  < ...
```
* 返回结果为数组，每一项表示节点支持的K线种类，以秒为单位，例如结果中包含3600表名节点支持1小时K线查询。

### get_market_history
* 获取某个交易对的K线
* 参数: 资产1的id，资产2的id，k线种类，起始时间，终止时间。
* 每个K线都有其统计起始时间(open time)，api返回open time大于等于起始时间，且小于终止时间的K线，因此，起始时间和终止之间不一定需要可以被K线的秒数整除。例如，k线种类86400，起始时间2019-05-01T00:00:00，终止时间2019-05-01T00:00:01，可以用于查询2019-05-01T00:00:00为open time的日K线。
* 节点限制最多每次返回200条记录。
* 若某k线时间范围内不存在任何成交记录，则k线不存在。
* k线中的所有价格均为成交中maker一方的下单价，而不是成交中实际交换的资产数量。例如用户A于17:50下单，使用100CYB交换0.1ETH，用户B于17:55下单购买了用户A出售的部分CYB，此时，用户A的订单剩余50CYB待出售，下单价格仍是100CYB/0.1ETH。用户C于18:01下单购买了用户A的剩余CYB，且为CYB对ETH在18:00后的第一笔成交，则18:00开始的，CYB:ETH的一小时K线中，开盘价为100CYB/0.1ETH，乘以资产精度后，base=CYB, quote=ETH, open_base = 10000000, open_quote=100000。
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "history", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_market_history", ["1.3.0", "1.3.27", 86400, "2019-05-01T00:00:00", "2019-05-10T00:00:01"]], "id": 2}
  < ...
```
* 返回结果字段  

字段名|类型|含义
---|---|---
key:base|资产id|base资产，后续所有价格中的base资产均为本资产
key:quote|资产id|quote资产，后续所有价格中的quote资产均为本资产
key:seconds|整数|k线种类，例如3600表示1小时k线
key:open|时间戳|k线的时间段
high_base|数量|最高价
high_quote|数量|
low_base|数量|最低价
low_quote|数量|
open_base|数量|开盘价
open_quote|数量|
close_base|数量|收盘价
close_quote|数量

### get_fill_order_history
* 获取某个交易对的成交历史
* 参数: 资产1的id，资产2的id，记录条数
* 成交记录成对出现，分别关联到成交双方的账号，使用is_maker字段来区分撮合中先下单者。
* Websocket请求例子
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "history", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method": "call", "params": [2, "get_fill_order_history", ["1.3.0", "1.3.2", 10]], "id": 2}
  < ...
```
* 返回结果字段  

字段名|类型|含义
---|---|---
key:base|资产id|撮合中一方资产，为id较小者
key:quote|资产id|撮合中另一方资产，为id较大者
key:sequence|整数|序号
time|时间戳|撮合发生的时间
op:order_id|订单id|本次撮合中涉及到的订单
op:account_id|账号id|本次撮合中涉及到的账号
op:pays|资产数量|本账号在本次撮合中支付给对手方的资产
op:receives|资产数量|本账号在本次撮合中从对手方获取的资产
op:fill_price|资产价格|本次撮合的价格
op:is_maker|bool|本订单在本次撮合中是否扮演maker角色

