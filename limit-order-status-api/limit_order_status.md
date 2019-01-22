# limit_order_status

limit_order_status API可以用来查看用户的历史订单状态。在区块链数据库中，订单被完全撮合或撤单后，节点会删除该订单的信息，用户只有在自己的账户操作历史中可以查看到这个订单的相关信息。此API可以向用户提供查询本人历史订单的接口。使用此API需要节点打开limit_order_status插件，该插件会跟踪和记录订单信息，并供API查询。

#### 1. 打开limit_order_status_plugin
插件参数
```Bash
--order-status-timeout-sec 86400 # 表示跟踪记录86400秒之内的订单状态
--plugins "... limit_order_status" # plugins参数增加limit_order_status表示启动该插件
--api-access access.json # 编辑access.json文件，在allowed_apis中增加"limit_order_status_api"，表示打开该API
--ignore-accounts ignores.json # 编辑ignores.json文件，表示不跟踪某些账户的信息
# ignores.json格式为
# {"ignores":[ "1.2.XXXX", "1.2.XXXX", ... ]}
```

#### 2.登陆并获取limit_order_status_api
```json
{"method": "call", "params": [1, "limit_order_status", []], "id": $callid}
```

#### 3.查询用户的历史订单状态
此查询会返回指定用户的，订单号小于等于指定数值的订单，最多$limit条
```json
{
 "method": "call", 
 "params": [
    $limit_order_status_api_id,
    "get_limit_order_status",
    ["1.2.XXXXX", "1.7.XXXXXXX", $limit]
 ],
 "id": $callid 
}
```

#### 4.查询用户在某个交易市场的的历史订单状态
此查询会返回用户在某个交易市场上，订单号小于等于指定数值的订单，最多limit条
```json
{
 "method":"call",
 "params": [
    $limit_order_status_api_id,
    "get_market_limit_order_status",
    ["1.2.XXXXX", "1.3.X", "1.3.X", "1.7.XXXXX", $limit]
 ],
 "id": $callid
} 
```

#### 5.查询用户在途订单状态
此查询会返回用户所有在途订单，在途订单指尚未完全成交且未撤单的订单
```json
{
 "method":"call",
 "params": [
    $limit_order_status_api_id,
    "get_opened_limit_order_status",
    ["1.2.XXXXX"]
 ],
 "id": $callid
} 
```

#### 6.查询用户在某个交易市场的在途订单状态
此查询会返回用户在某个交易市场的所有在途订单
```json
{
 "method":"call",
 "params": [
    $limit_order_status_api_id,
    "get_opened_market_limit_order_status",
    ["1.2.XXXXX", "1.3.X", "1.3.X"]
 ],
 "id": $callid
} 
```

#### 7.用户自定义交易对查询
通过设置交易对，可以使节点返回按交易对过滤后的订单信息
##### 7.1 设置需要过滤的交易对
```json
{
 "method":"call",
 "params": [
    $limit_order_status_api_id,
    "set_filter_market",
    [[
        ["1.3.0", "1.3.2"],
        ["1.3.2", "1.3.27"]
    ]]
 ],
 "id": $callid
}
```

##### 7.2 查询过滤后的订单
```json
{
 "method": "call",
 "params": [
    $limit_order_status_api_id,
    "get_filtered_limit_order_status",
    [
      "1.2.xxxxx",
      "1.7.xxxxxxxx",
      $limit,
      true # true表示查询包含在过滤交易对中的订单， false表示查询不包含在过滤交易对中的订单
    ]
 ],
 "id": $callid
}
```

#### 8.查询结果
以上查询会以json格式返回，返回json格式转换为字典类型后，其result对象为数据列表，列表中每个元素格式如下
```json
{
    "id": "7.0.xxxxxx", # 对象id
    "order_id": "1.7.xxxxx", # 订单号
    "seller": "1.2.xxxxx", # 用户账号
    "key": {
        "asset1": "1.3.x", # 交易市场
        "asset2": "1.3.x"
    },
    "is_sell": true, # true表示此订单为出售asset1， false表示此订单为出售asset2
    "amount_to_sell": 100, # 下单时请求出售资产的数量
    "min_to_receive": 200, # 下单时希望获取资产的数量
    "sold": 50, # 已经出售的资产数量
    "received": 100, # 已经购得的资产数量
    "canceled": 50, # 撤单时尚未完全出售的资产数量
    "block_num": xxxxxx, # 创建订单的交易所在区块号
    "trx_in_blk": xx, # 创建订单的交易在区块中的交易编号
    "op_in_trx": xx, # 创建订单的操作在交易中的操作编号
    "create_time": "YYYY-mm-ddTHH:MM:SS" # 创建订单的交易所在区块的时间戳
}
```

#### 9.根据时间查询订单号
此查询会返回在用户指定时间戳之前的最大订单号，系统采用UTC时间格式
```json
{
 "method":"call",
 "params": [
    $limit_order_status_api_id,
    "get_limit_order_id_by_time",
    ["YYYY-mm-ddTHH:MM:SS"]
 ],
 "id": $callid
} 
```
