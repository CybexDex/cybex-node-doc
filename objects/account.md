## 账号(1.2.X)
### 权限结构
权限结构不是独立的数据库对象，而是内嵌于其他数据库对象中，表示该对象相关权限的结构。当权限结构内嵌于账号中时，表示账号的相关权限。  
以下为一个权限结构的内容
```bash
{
    "weight_threshold": 3, # 权限阈值，所有由账户/公钥提供的授权大于等于此阈值时，可以获取权限
    "account_auths": [ # 账号权限，表示该权限可以由其他账号授权获得
        [ "1.2.100", 2 ], # 每一条数据表示若获得该账号授权，则获取多少权重的权限
        [ "1.2.101", 1 ]  # 例如1.2.100授权提供权重2的权限值
    ],
    "key_auths": [ # 公钥权限，表示该权限可以由公钥对应的私钥签名授权
        [ "CYB6bCHU6sWD4estBBmpNeLMsuL3aZynrBLANGGg2MjELxzNJt45r", 1 ] # 表示该公钥对应的私钥若签名，则提供权重1的权限值
    ],
    "address_auths": [] # 仅创世文件中使用的权限，用以映射其他公链的权限
}
```
通常，用户的普通账户的active和owner权限中，account_auths为空数组，key_auths为包含1个权重1公钥的数组，且权限阈值为1，表示只需要一个私钥签名即可获取对应的权限。

### 账号结构
```json
{
  "id": "1.2.7",
  "membership_expiration_date": "1969-12-31T23:59:59",
  "registrar": "1.2.7",
  "referrer": "1.2.7",
  "lifetime_referrer": "1.2.7",
  "network_fee_percentage": 2000,
  "lifetime_referrer_fee_percentage": 8000,
  "referrer_rewards_percentage": 0,
  "name": "harley",
  "owner": {
    "weight_threshold": 1,
    "account_auths": [],
    "key_auths": [
        ["CYB8jM4e1z1xS63xxVhuperU1VvusQz8Ye8CrnTBigFUaErpigpPL", 1]
    ],
    "address_auths": []
  },
  "active": {
    "weight_threshold": 1,
    "account_auths": [],
    "key_auths": [
        ["CYB7UdEEgrFYAR4DfSi8svfUUzE2E2twSFqAx66LqmgxXJjk5h7LR", 1]
    ],
    "address_auths": []
  },
  "options": {
    "memo_key": "CYB7UdEEgrFYAR4DfSi8svfUUzE2E2twSFqAx66LqmgxXJjk5h7LR",
    "voting_account": "1.2.5",
    "num_witness": 0,
    "num_committee": 0,
    "votes": [],
    "extensions": []
  },
  "statistics": "2.6.7",
  "whitelisting_accounts": [],
  "blacklisting_accounts": [],
  "whitelisted_accounts": [],
  "blacklisted_accounts": [],
  "cashback_vb": "1.13.0",
  "owner_special_authority": [0, {}],
  "active_special_authority": [0, {}],
  "top_n_control_flags": 0
}
```
### 字段含义
字段 | 类型 | 含义
---|---|---
id | 账号id | 账号id
membership_expiration_date | 时间戳 | 会员超时时间，UTC -1表示终身会员，UTC 0表示非终身会员。
registrar| 账号id | 注册人，即注册该账号的账号。账号升级终身会员后，注册人变更为其自身。
referrer| 账号id | 引荐人，注册时填写的账号引荐人。账号升级成终身会员后，引荐人变更为其自身。
lifetime_referrer| 账号id | 终身会员引荐人，即注册时引荐人的终身会员引荐人。账号升级成终身会员后，终身会员引荐人变更为其自身。
network_fee_percentage| 整数 |用户支付的手续费中，由链收取的比例，以10000为分母，2000表示20%。
lifetime_referrer_fee_percentage| 整数 |用户支付的手续费中，由终身会员引荐人收取的比例，以10000为分母，3000表示30%。
referrer_rewards_percentage| 整数 |用户支付的手续费中，推荐人可以获取的分润比例，以10000为分母，0表示推荐人无分润。
name| 字符串 | 账号名
owner| 权限结构 | 账号所有者权限
active| 权限结构 | 账号活跃权限
options:memo_key| 公钥 | 其他用户需要在操作中向此用户发送附言时，此账号建议以这个公钥作为对称加密密钥生成算法中使用的公钥。
options:voting_account| 账号id | 当设置为1.2.5时，表示该账号的所有CYB均投票给votes字段中设置的项目，当设置为非1.2.5时，表示该账号的所有CYB均投票给所设置账号的投票项目。
options:num_witness| 整数 | 表示该账号投票了多少个打包人 
options:num_committee| 整数 | 表示该账号投票了多少理事会成员
options:votes| 数组 | 表示该账号具体投票情况
options:extensions| 数组 | 预留扩展字段
statistics| id | 该账号的统计对象id
whitelisting_accounts| 账号id数组 | 表示哪些账号将本账号列入白名单
blacklisting_accounts| 账号id数组 | 表示哪些账号将本账号列入黑名单
whitelisted_accounts| 账号id数组 | 表示本账号将哪些账号列入白名单
blacklisted_accounts| 账号id数组 | 表示本账号将哪些账号列入黑名单
owner_special_authority| 特殊权限结构 | 未使用
active_special_authority| 特殊权限结构 | 未使用
top_n_control_flags| 特殊权限标志位 | 未使用
