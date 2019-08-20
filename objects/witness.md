## 见证人(1.6.X)
见证人是由用户创建的链上实体，从属于创建它的用户账户，每个用户账号至多创建一个见证人。见证人获取一定数量投票后，成为活跃见证人，活跃见证人可以在DPOS共识算法下打包区块，并获取打包收益。

### 见证人结构
```json
{
    "id": "1.6.14",
    "witness_account": "1.2.43556",
    "last_aslot": 21522494,
    "signing_key": "CYB8FYdT6UH3HC8Q2Epw713jhkymocyrhfRnAHk8V2TwtKJKMU2wR",
    "pay_vb": "1.13.98",
    "vote_id": "1:41",
    "total_votes": "36630737598892",
    "url": "https://chainext.cn/about",
    "total_missed": 221,
    "last_confirmed_block_num": 15472913
}
```

### 字段含义
字段 | 类型 | 含义
---|---|---
id | witness id | witness id
witness_account | 账号id | 该见证人从属的用户账号
last_aslot | 整数 | 该见证人最近一次打包区块的slot序号
signing_key | 公钥 | 见证人签名区块的私钥对应的公钥
pay_vb | 锁定期id | 见证人领取报酬的账号id
vote_id | 投票序号 | 其他账号投票此见证人时使用的投票号
total_votes | 整数 | 见证人当前得票数
url | 字符串 | 见证人相关信息链接
total_missed | 整数 | 见证人遗漏出块数量
last_confirmed_block_num | 整数 | 见证人上次出块时进入不可逆区块的区块号
