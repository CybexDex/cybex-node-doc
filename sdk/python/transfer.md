## 转账相关操作
转账操作可用于将资产从一个账户转移到另一个账户或地址。在进行转账操作前，需要将转出账户的私钥提前加入Python库的本地钱包中，并解锁钱包。钱包相关操作详见[钱包操作](https://github.com/NebulaCybexDEX/cybex-node-doc/blob/master/transaction/python/wallet.md)

#### 1. 基本转账
基本转账操作用于将某资产从一个账户转移到另一个账户。收款账户可以立刻收到并使用这笔资产。同时，用户可以根据自身需要添加交易附言(memo)，该交易附言经过加密后发送到节点，只有发送方和收款方，使用对应的私钥才能解密。
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)
# 从from-account转10CYB到to-account，并带有附言memo string，
# 如果不需要填写附言，传入''作为附言字符串即可
instance.transfer('to-account', 10, 'CYB', 'memo string', 'from-account')
```

#### 2. 锁定期资产转账
锁定期资产为带有锁定期的资产，发送方发送锁定期资产后，相应资产立刻从发送方账户中扣除，在发送方指定的锁定时间到期后，接收方可以申领这笔锁定期资产。
锁定期资产与接收方的公钥关联，只有该公钥对应的私钥持有者，才能申领该锁定期资产。锁定期资产的申领操作详见[资产操作](https://github.com/NebulaCybexDEX/cybex-node-doc/blob/master/transaction/python/balance.md)
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# 获取收款账号的公钥
# 这里使用收款账号活跃权限的第一把公钥，使用者也可视情况选择其他公钥
account = cybex.account.Account('to-account', cybex_instance = instance)
to-account-pubkey = account['active']['key_auths'][0][0]

# 从from-account转10CYB到to-account，并锁定600秒
instance.transfer('to-account', 10, 'CYB', '', 'from-account', extensions = [[1, {
    'vesting_period': 600,
    'public_key': to-account-pubkey
}]])
```
