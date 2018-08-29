## 报单相关操作
报单操作可以向赛贝去中心化交易所发送订单。在赛贝中，一个交易市场由两种资产组成，用户报单即提交订单，付出一些资产A，期望获得一些资产B的行为。
为了方便用户理解，赛贝交易所的常用客户端没有采用资产交换的方式来表示订单和价格，而是采用与传统交易所相似的价格+数量的方式，Python库也使用这种模式报单，本demo会同时在注释中说明报单的实际资产交换值。
报单操作前，需要将报单账户的私钥提前加入Python库的本地钱包中，并解锁钱包。钱包操作详见[钱包操作](https://github.com/NebulaCybexDEX/cybex-node-doc/blob/master/transaction/python/wallet.md)
赛贝交易所的资产由瑶池(JADE)托管，所有由瑶池托管的资产以JADE.作为资产前缀，比如以太坊的资产名为JADE.ETH，此外还有JADE.EOS, JADE.BTC, JADE.USDT等。赛贝的网页前端为了照顾用户使用习惯，在显示时去除了JADE前缀，在使用Python库时，资产名需要加JADE.前缀。

#### 1. 买卖单
```Python
import cybex
from cybex import Market, Asset, Account

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

asset1 = Asset('CYB')
asset2 = Asset('JADE.ETH')
m = Market(base = asset1, quote = asset2,
    cybex_instance = self.instance)

# 下面的buy操作表示:
# 以1000的单价购买1个asset2，交易超时时间为3600秒
# 计价单位为Market对象中的base资产, 实际资产交换情况为：
# 希望付出1000个CYB，希望至少获得1个JADE.ETH
# 用户下单时，账户中会立刻扣除1000个CYB，如果账户中CYB不足，会造成下单失败
# 订单若超过3600秒还未完全撮合完成，则将剩余的订单自动撤销
m.buy(1000, 1, 3600, killfill = False, account = 'seller-account')

# 下面的sell操作表示:
# 以1200的单价出售一个asset2，交易超时时间为3600秒
# 计价单位为Market对象中的base资产, 实际资产交换情况为：
# 希望付出1个JADE.ETH，希望至少获得1200个CYB
# 用户下单时，账户中会立刻扣除1个JADE.ETH，如果账户中JADE.ETH不足，会造成下单失败
# 订单若超过3600秒还未完全撮合完成，则将剩余的订单自动撤销
m.sell(1200, 1, 3600, killfill = False, account = 'seller-account')
```

#### 2. FOK单
FOK即fill or kill，当且仅当该订单可以被立刻完全撮合时，才撮合该订单。
在上例中，若killfill为True，表示该订单是FOK单.例如：
```Python
m.sell(1200, 1, 3600, killfill = True, account = 'seller-account')
```
