## 锁定期资产(1.13.X)
Cybex具有多种锁定资产的方式，本文档的锁定期资产通常用来表示节点收益、worker收益、eto资产等。本对象保存的锁定期资产有两种锁定策略，分别是线性释放策略和CDD释放策略。

### 线性锁定期资产结构
线性锁定期资产结构的policy二元组，第一个元素为0。第二个元素为锁定明细。
```json
{
    "id": "1.13.0",
    "owner": "1.2.7",
    "balance": {
        "amount": "2968150706",
        "asset_id": "1.3.0"
    },
    "policy": [
        0,
        {
            "begin_timestamp": "1970-01-01T00:00:00",
            "vesting_cliff_seconds": 1566468000,
            "vesting_duration_seconds": 1566468000,
            "begin_balance": 20000
        }
    ]
}
```

### 字段含义
字段 | 类型 | 含义
---|---|---
id | 锁定期资产id | 锁定期资产id
owner | 账号id | 所属账户
balance | 资产数额 | 剩余未提取资产金额
begin_timestamp | 时间戳 | 锁定期开始时间
vesting_cliff_seconds | 整数 | 达到begin_timestamp + vesting_cliff_seconds后，锁定期资产开始线性释放
vesting_duration_seconds | 整数 | 达到begin_timestamp + vesting_duration_seconds后，锁定期资产释放完毕
begin_balance | 整数 | 释放前的金额


### CDD锁定期资产结构
CDD锁定期资产结构的policy二元组，第一个元素为1。第二个元素为锁定明细。
```json
{
    "id": "1.13.0",
    "owner": "1.2.7",
    "balance": {
        "amount": "2968150706",
        "asset_id": "1.3.0"
    },
    "policy": [
        1,
        {
            "vesting_seconds": 31536000,
            "start_claim": "1970-01-01T00:00:00",
            "coin_seconds_earned": "69977562899495967",
            "coin_seconds_earned_last_update": "2019-08-22T00:00:00"
        }
    ]
}
```
字段 | 类型 | 含义
---|---|---
id | 锁定期资产id | 锁定期资产id
owner | 账号id | 所属账户
balance | 资产数额 | 剩余未提取资产金额
vesting_seconds | 整数 | 锁定期开始时间
start_claim | 时间戳 | 可以开始提取的时间点
coin_seconds_earned | 整数 | 以币秒计的当前累计金额
coin_seconds_earned_last_update | 时间戳 | 币秒值上一次更新时间
