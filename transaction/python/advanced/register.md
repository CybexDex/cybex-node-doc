## 创建账户操作
终身会员用户可以在Cybex链上创建账户。Cybex链上账户权限可以分为账号权限和公钥权限。本文仅介绍常见的如何创建仅含公钥权限账户的操作。

#### 1.云账户和本地钱包账户
Cybex的网页客户端、App客户端支持云钱包登陆模式。云钱包和本地钱包都是保存私钥的方式，云钱包模式中，用户私钥由用户名+云密码衍生得到，在本地钱包模式中，用户私钥由钱包密码加密，保存在本地钱包文件中。  

#### 2.memo key
Memo key与账号的控制权无关，其含义是其他账号给该账号转账或发行资产，并需要添加附言时，参考该账号的memo key作为产生对称加密密钥的公钥。Cybex链并不要求memo中使用的目标公钥等于目标账户的memo key，通常，只是作为一种客户端间的约定，将目标账户的memo key作为memo中的目标公钥。  
通过Cybex网页端注册的账户，通常memo key设置为与活跃权限的公钥相同，方便用户查看memo。

#### 3.云密码计算公私钥
由于历史原因，Cybex的旧版网页钱包客户端注册的用户，使用以下方式计算的role为active公钥，被添加在账号的owner权限，使用以下方式计算的role为owner公钥，被添加在账号的active权限。对于使用云钱包解锁的用户来说，并不影响账号的正常使用。

```Python
from graphenebase.account import PasswordKey

active_password_key = PasswordKey('name', 'password', role = 'active')
active_private_key = active_password_key.get_private()
active_public_key = active_password_key.get_public()
print("Account active private key: ", str(active_private_key))
print("Account active public key: ", "CYB" + str(active_public_key)[3:])

owner_password_key = PasswordKey('name', 'password', role = 'owner')
owner_private_key = owner_password_key.get_private()
owner_public_key = owner_password_key.get_public()
print("Account owner private key: ", str(owner_private_key))
print("Account owner public key: ", "CYB" + str(owner_public_key)[3:])
```

#### 4.产生随机公私钥对
根据操作系统随机数产生随机私钥
```Python
from graphenebase.account import PrivateKey

random_priv_key = PrivateKey(prefix = 'CYB')
random_pub_key = random_priv_key.pubkey
print("Random private key: ", str(random_priv_key))

# cast pubkey to base58 format may generate
# a warning message due to unknown prefix 'CYB'
# just ignore it
print("Random public key: ", str(random_pub_key))
```

#### 5.根据指定的私钥计算公钥
```Python
from graphenebase.account import PrivateKey

# pass a Base58 format key
privkey = PrivateKey(wif = $BASE58_WIF, prefix = 'CYB')
pubkey = privkey.pubkey

# cast pubkey to base58 format may generate
# a warning message due to unknown prefix 'CYB'
# just ignore it
print("Public key: ", str(pubkey))
```

#### 6.使用公钥注册账户
注册账户需要支付一定的手续费，不同级别的帐户名需要支付的手续费不同。  
不含数字，且不含特殊字符(".", "-")，且含有aeiouy任一字母的帐户名，为高级帐户名，需要支付更多的上链手续费(具体费率以链上费率表为准)。
账号名长度必须大于等于1个字符，小于等于63字符。  
若账号名中含有"."，则以"."将账号名分割为若干段，每段必须满足: 1.以小写字母开头，2.以小写字母或数字结尾，3.只含小写字母、数字和"-"字符。  
若账号名中不含有"."，则视为以上条件中的一段，必须满足每段的要求。

注册账号需要填写注册人(registrar)和引荐人(referrer)，注册人为支付注册手续费的账户，必须是终身会员，引荐人为账号在链上的引荐账户，必须是终身会员。详情可参考[账号引荐机制](https://github.com/CybexDex/cybex-node-doc/wiki/%E4%BC%9A%E5%91%98%E7%AD%89%E7%BA%A7)。  

执行此操作前请确保已经将注册人的私钥添加进钱包。

```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

instance.create_account(
    account_name = $ACCOUNT_NAME
    registrar = $REGISTRAR_NAME,
    referrer = $REFERRER_NAME,
    referrer_percent = 0,
    owner_key = $OWNER_PUBKEY,
    active_key = $ACTIVE_PUBKEY,
    memo_key = $ACTIVE_PUBKEY,
    password = False
)
```
