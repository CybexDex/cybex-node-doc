# Network Broadcast API
Network Broadcast API用于在区块链上广播交易。在交易被广播之前，需要先进行签名，签名后的交易通过本API发送到节点。节点接收交易后，首先基于本地状态机进行检查，若交易检查通过，会在P2P网络上广播交易。交易被打包进区块后，会随区块被广播回本节点。

## 广播交易
### broadcast_transaction
* 请求节点广播交易，若节点检查通过，则在交易被广播后立刻返回结果。
* 若节点检查交易失败，会返回异常
* 参数: 签名后的交易json
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "network_broadcast", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method":"call", "params": [2, "broadcast_transaction", [{"method":"call", "params": [2, "broadcast_transaction", [{"extensions": [], "ref_block_prefix": 3294169051, "signatures": ["1f7e466e4b23fd6a85f6d9f214c05718966e942f9a8b6fcf29015a92176c65958134d7e689076977bd74b17f161b1d216ebf55222b5f09d9b282eb55829852f501"], "expiration": "2019-08-20T05:02:57", "ref_block_num": 5115, "operations": [[0, {"amount": {"amount": 10000, "asset_id": "1.3.0"}, "extensions": [], "from": "1.2.38759", "fee": {"amount": 1000, "asset_id": "1.3.0"}, "to": "1.2.38305"}]]}] ], "id": 2}] ], "id": 2} 
  < {"id":2,"jsonrpc":"2.0","result":null}
```
* 若成功广播，则返回result:null。
 
### broadcast_transaction_with_callback
* 请求节点广播交易，并在交易被打包后主动回调客户端。
* 发送交易时需要附带回调id，若节点检查通过，立刻返回结果，并在交易被打包后使用回调id回调客户端。
* 参数: 回调id，签名后的交易json
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "network_broadcast", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method":"call", "params": [2, "broadcast_transaction_with_callback", [100, {"expiration": "2019-08-20T05:10:34", "ref_block_prefix": 4146358936, "extensions": [], "ref_block_num": 5267, "signatures": ["205e300139615f32a9ba793930379f71746547e9e352e429707fe7cacd56e868bf1fe479f2b8d9667c48122b880199cdec1fdccc57c093218b6ad932b37d612141"], "operations": [[0, {"from": "1.2.38759", "extensions": [], "fee": {"asset_id": "1.3.0", "amount": 1000}, "amount": {"asset_id": "1.3.0", "amount": 10000}, "to": "1.2.38305"}]]}] ], "id": 2} 
  < {"id":2,"jsonrpc":"2.0","result":null}
  < {"method":"notice","params":[100,[{"id":"a0dca958449191b1b721ac33825813d1f76777d0","block_num":15471784,"trx_num":26,"trx":{"ref_block_num":5267,"ref_block_prefix":4146358936,"expiration":"2019-08-20T05:10:34","operations":[[0,{"fee":{"amount":1000,"asset_id":"1.3.0"},"from":"1.2.38759","to":"1.2.38305","amount":{"amount":10000,"asset_id":"1.3.0"},"extensions":[]}]],"extensions":[],"signatures":["205e300139615f32a9ba793930379f71746547e9e352e429707fe7cacd56e868bf1fe479f2b8d9667c48122b880199cdec1fdccc57c093218b6ad932b37d612141"],"operation_results":[[0,{}]]}}]]}
```
* 操作包含两个返回结果，第一个{"id":2,"jsonrpc":"2.0","result":null}在节点广播后立刻返回，表示节点已经接受并广播了此交易。第二个{"method":"notice",...}返回为交易被打包后的返回，通常需要等待0-3秒，网络拥堵时可能等待更长时间(视p2p节点拥堵情况而定)。params中100表示设置的回调id。

### broadcast_transaction_synchronous
* 请求节点广播交易，并同步等待打包结果。
* 参数: 签名后的交易json
```Bash
wscat -c wss://hongkong.cybex.io
> {"method": "call", "params": [1, "network_broadcast", []], "id": 1}
  < {"id":1,"jsonrpc":"2.0","result":2}
> {"method":"call", "params": [2, "broadcast_transaction_synchronous", [{"expiration": "2019-08-20T05:16:01", "signatures": ["1f291b9fc7091c9eb1cf93f6ab1b97f24545fb626337083831a091ae19892834c51f09899a93a2165a3804288bf75a302186a4f9911494471b3b831d51b052f0a4"], "operations": [[0, {"amount": {"amount": 10000, "asset_id": "1.3.0"}, "fee": {"amount": 1000, "asset_id": "1.3.0"}, "from": "1.2.38759", "to": "1.2.38305", "extensions": []}]], "ref_block_num": 5374, "ref_block_prefix": 721999338, "extensions": []}] ], "id": 2} 
  < {"id":2,"jsonrpc":"2.0","result":{"id":"049c88a0473b98af3a93e5a365e6f62c22af6c97","block_num":15471889,"trx_num":1,"trx":{"ref_block_num":5374,"ref_block_prefix":721999338,"expiration":"2019-08-20T05:16:01","operations":[[0,{"fee":{"amount":1000,"asset_id":"1.3.0"},"from":"1.2.38759","to":"1.2.38305","amount":{"amount":10000,"asset_id":"1.3.0"},"extensions":[]}]],"extensions":[],"signatures":["1f291b9fc7091c9eb1cf93f6ab1b97f24545fb626337083831a091ae19892834c51f09899a93a2165a3804288bf75a302186a4f9911494471b3b831d51b052f0a4"],"operation_results":[[0,{}]]}}}
```
* 在交易被打包后才会收到返回结果，并包含了交易被打包的区块号、交易号和交易执行结果等信息。
