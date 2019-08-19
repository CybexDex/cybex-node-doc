## 资产(1.3.X)
### 资产结构
```json
{
    "id": "1.3.2",
    "symbol": "JADE.ETH",
    "precision": 6,
    "issuer": "1.2.29",
    "options": {
        "max_supply": "1000000000000000",
        "market_fee_percent": 5,
        "max_market_fee": "1000000000000",
        "issuer_permissions": 79,
        "flags": 3,
        "core_exchange_rate": {
            "base": {
                "amount": 100000000,
                "asset_id": "1.3.0"
            },
            "quote": {
                "amount": 1000000,
                "asset_id": "1.3.2"
            }
        },
        "whitelist_authorities": [],
        "blacklist_authorities": [
            "1.2.40540"
        ],
        "whitelist_markets": [],
        "blacklist_markets": [],
        "description": "",
        "extensions": []
    },
    "dynamic_asset_data_id": "2.3.2"
}
```
### 字段含义
字段 | 类型 | 含义
---|---|---
id | 资产id | 资产id
symbol | 字符串 | 资产符号
precision | 整数 | 资产精度。资产的数量在链上以整数表示，除以10的精度次方，即为实际数量
issuer | 账号id | 资产当前发行人id
options:max_supply | 整数 | 资产最大供给量
options:market_fee_percent | 整数 | 资产在成交时需向发行人支付的交易手续费比例，默认分母为10000，整数5表示万分之5
options:max_market_fee | 整数 | 每笔成交收取的成交手续费上限
options:issuer_permissions | 整数 | 表示哪些权限位可以由发行人动态调整
options:flags | 整数 | 资产当前权限位，与issuer_permissions中的位一一对应，只有issuer_permissions中相应的位置位(设置为1)时，发行人可以动态调整该位对应的权限
options:core_exchange_rate | 价格 | 表示两种资产的兑换比例，其中之一为本资产，另一为核心资产CYB。当用户以本资产支付上链手续费时，会首先计算以CYB计价的手续费数额，乘以此比例，得到以本资产支付手续费时需要的数量。用户支付的本资产会进入手续费汇兑池，并从汇兑池中扣除相应的CYB用户代替用户支付链上手续费。
options:whitelist_authorities | 账号id数组 | 资产的白名单索引账户，若设置为非空，则只有被这些账户列为白名单的账户(参考账户部分whitelisted_accounts)才有权限持有该资产。
options:blacklist_authorities | 账号id数组 | 资产的黑名单索引账户，若某个账户被黑名单索引账户中的账户加入黑名单(参考账户部分blacklisted_accounts)，则该账户无权限持有该资产。
options:whitelist_markets | 资产id数组 | 若设置为非空，则持有本资产的用户只能下单求购该列表中的资产。
options:blacklist_markets | 资产id数组 | 若设置为非空，则持有本资产的用户不能下单求购列表中的资产。
options:description | 字符串 | 资产的描述字段
options:extensions | 数组 | 预留
dynamic_asset_data_id | id | 资产的动态统计对象id
