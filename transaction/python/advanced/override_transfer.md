## 覆盖转账操作
资产的发行者在资产的覆盖转账旗标开启时，可以使用覆盖转账操作，将资产从拥有着A转移到账户B。

#### 1.发送覆盖转账操作
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# 资产发行人将资产从from-account转到to-account
# 目前暂不支持在覆盖转账操作中添加memo信息, 需要传入''作为memo字符串
instance.override_transfer('from-account', 'to-account', 10, 'asset-name', '', 'issuer')
```
