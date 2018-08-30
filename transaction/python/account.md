## 账户相关操作
本文介绍如何查看赛贝交易所中，账户相关的信息。

```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
ACCOUNT_NAME = 'nathan'

instance = cybex.Cybex(NODE_URL)
account = cybex.account.Account(ACCOUNT_NAME, cybex_instance = instance)

# 查看账户名
print(account.name)

# 查看账户id
print(account["id"])

# 查看账户在链上活跃权限对应的公钥
print(account['active']['key_auths'])

# 查看账户在链上账户权限对应的公钥
print(account['owner']['key_auths'])

# 查看账户余额
for bal in account.balances:
    # 资产名
    print(bal.asset.symbol)
    # 资产id
    print(bal.asset["id"])
    # 资产数量
    print(bal.amount) # 不含精度的浮点数
    
# 查看账户当前挂单
# 这里获得的base和quote，并不一定是用户挂单时在Market对象中指定的base和quote，
# base为在该订单中用户愿意付出的资产
# quote为在该订单中用户期望获得的资产
# 例如，
# 1.用户在交易市场中，期望以0.02 JADE.ETH/JADE.EOS的价格购买10个JADE.EOS，
#   则base为JADE.ETH, quote为JADE.EOS，price为0.02
# 2.用户在交易市场中，期望以0.02 JADE.ETH/JADE.EOS的价格卖出10个JADE.EOS，
#   则base为JADE.EOS，quote为JADE.ETH，price为50
for order in account.openorders:
    # 出售的资产名
    print(order['base'].symbol)
    # 出售的资产数量
    print(order['base'].amount)
    # 期望获得的资产名
    print(order['quote'].symbol)
    # 期望获得的资产数量
    print(order['quote'].amount)
    # 以base计价的quote的价格
    print(order['price'])
```
