## 更新账户操作
警告！本文中的代码涉及更新账户权限相关功能，除非您清楚了解自己正在进行何种操作，否则请勿使用本文中代码对自己的账户进行测试。操作不当可能导致您丧失账号的控制权限。没有任何人可以为您恢复丢失的权限（包括赛贝）。  
建议使用测试账号进行开发测试。

## 账号权限体系
请参考[权限体系](https://github.com/CybexDex/cybex-node-doc/wiki/CYBEX%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C%EF%BC%88%E5%90%8D%E8%AF%8D%E8%A7%A3%E9%87%8A%EF%BC%89)

#### 1.更新账户active权限，添加一个账户多签
账号A原本为单签账号，只有一个公钥权限，active权限总权重为1，需要将账号B加入其active权限，总权重变为2，其中B的权限为1  
需要保证钱包中有A账号原有私钥。  
加入B的权限后，A账号的active权限变为多签权限，如果A没有自己账号owner权限，则无法单独通过active权限控制账号。
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# 传入的account-b需要是赛贝链上的账号名
instance.allow('account-b', weight = 1, permission = 'active', account = 'account-a', threshold = 2)
```

#### 2.更新账户active权限，添加一个公钥多签
账号A原本为单签账号，只有一个公钥权限，active权限总权重为1，需要将公钥pubkey-B加入其active权限，总权重变为2，其中pubkey-B的权限为1  
需要保证钱包中有A账号原有私钥。 
加入公钥B的权限后，A账号的active权限变为多签权限，如果A没有自己账号owner权限，则无法单独通过active权限控制账号。
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# 传入的pubkey-b需要是base58格式的公钥(CYB前缀)
instance.allow('pubkey-b', weight = 1, permission = 'active', account = 'account-a', threshold = 2)
```

#### 3.更新账户active权限，删除一个账号多签(钱包中的私钥足够更新账号的active权限的情况)
从账号A中删除账号B的账号多签，删除后active权限阈值设置为1
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# 传入的account-b需要是赛贝链上的账号名
instance.disallow('account-b', permission = 'active', account = 'account-a', threshold = 1)
```

#### 3.更新账户active权限，删除一个公钥多签(钱包中的私钥足够更新账号的active权限的情况)
从账号A中删除公钥B的公钥多签，删除后active权限阈值设置为1
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# 传入的pubkey-b需要是base58格式的公钥(CYB前缀)
instance.disallow('pubkey-b', permission = 'active', account = 'account-a', threshold = 1)
```

#### 4.使用proposal方式提议更新多签权限(钱包中的私钥不足以更新账号的active权限的情况)
若账号A更新多签后，失去独立控制自身账号的权限，则需要提交拟议交易，提议更新账号A的权限，需要多签各方批准。  
本例中使用账号proposer作为提议发起账号，需要有提议发起人的完全权限。
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

proposal = instance.new_proposal(proposer = 'proposer', proposal_expiration = 3600)
instance.disallow('pubkey-b', permission = 'active', account = 'account-a', threshold = 1, append_to = proposal)
proposal.broadcast()
```
