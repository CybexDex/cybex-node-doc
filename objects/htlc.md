## 哈希时间锁定HTLC(1.21.X)
哈希时间锁定为一种特殊的转账，账户A可以使用这种方式向账户B转账一定金额的任意资产。转账资产不会立刻进入目标账户，而是会被锁定在链上，锁定分为时间锁和哈希锁。发起人需要同时设置时间锁和哈希锁。哈希锁包含一个哈希后的字符串，只有使用原值提交解锁操作并且原值的哈希值与哈希锁中的字符串匹配时才能解锁。时间锁在区块时间到达设置时间后自动解锁。哈希锁解锁后，资产自动进入目标账户(账户B)。时间锁解锁后，资产自动退回来源账户(账户A)。不论哪一种解锁条件被触发，链上均会删除HTLC对象。
### HTLC结构
```json
{
    "id": "1.21.100",
    "transfer": {
        "from": "1.2.100",
        "to": "1.2.101",
        "amount": "10000000000",
        "asset_id": "1.3.0"
    },
    "conditions": {
        "hash_lock": {
            "preimage_hash": [
                2,
                "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            ],
            "preimage_size": 100
        },
        "time_lock": {
            "expiration": "2020-12-31T00:00:00"
        }
    }
}
```

### 字段含义
字段 | 类型 | 含义
---|---|---
id | htlc id | htlc id
transfer:from | 账号id | 锁定来源账号
transfer:to | 账号id | 锁定目标账号
transfer:amount | 整数 | 锁定金额
transfer:asset_id | 资产id | 锁定资产
conditions:hash_lock | 哈希锁 |
hash_lock:preimage_hash | 数组 | 第一个元素表示hash算法的类型，0为ripemd160，1为sha1，2为sha256，第二个元素表示哈希后的值
hash_lock:preimage_size | 整数 | 哈希原值的长度，只有符合该长度的原值，才被允许尝试解锁哈希锁
conditions:time_lock | 时间锁 |
time_lock:expiration | 时间戳 | 时间锁过期时间
