## 资产相关操作
赛贝交易所的资产分为账户资产和地址相关资产。账户资产为账户名下的资产，用户可以在转账、买卖交易中使用。地址相关资产为与地址绑定的资产，例如锁定期资产。只有该地址对应的私钥持有者，才能申领对应的资产。申领后，资产等额转入账户名下，成为账户资产。


#### 1. 查询并申领锁定期资产
```Python
import cybex
from cybex import Account
from datetime import datetime, timedelta

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

account = Account('owner-account')

# 查询锁定期资产
# 仅当锁定期资产对应的公钥存在于账户的active或owner权限中时
# 可以使用此操作查询到锁定期资产
for bal in account.vesting_balances:
    policy = bal['vesting_policy']
    # 判断锁定期资产是否已经到期
    if (datetime.utcnow() >
        datetime.strptime(policy['begin_timestamp'], '%Y-%m-%dT%H:%M:%S') +
        timedelta(seconds = policy['vesting_duration_seconds'])):
        # 到期后可以申领锁定期资产
        instance.claim_balance(bal['id'])
    else:
        print('unclaimable ', bal['id'])
```
