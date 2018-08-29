## Python钱包相关操作
Python钱包是基于python库提供的钱包，在python钱包中，用户私钥被加密存储在本机的sqlite3文件数据库中，当用户需要发送交易时，pyton库从数据库中提取私钥，用来进行交易签名。

#### 1. 创建钱包
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'
instance = cybex.Cybex(NODE_URL)
instance.wallet.create(WALLET_PWD)
```

#### 2. 解锁钱包
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'
instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)
assert not instance.wallet.locked()
```

#### 3. 向钱包导入私钥
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'
PRIVATE_KEY = 'your-base58-formatted-private-key-here'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)
instance.wallet.addPrivateKey(PRIVATE_KEY)
```

#### 4. 查看钱包中的账户
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)
print(instance.wallet.getAccounts())
```

#### 5. 删除钱包中的私钥
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)
instance.wallet.removeAccount('account-to-be-removed')
```
