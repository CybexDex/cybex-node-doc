## 行情查询相关操作
本文介绍如何查看赛贝交易所中的行情信息。

```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
ASSET_NAME = 'JADE.ETH'

instance = cybex.Cybex(NODE_URL)

# 创建两个资产对象
base = cybex.asset.Asset('JADE.ETH', cybex_instance = instance)
quote = cybex.asset.Asset('CYB', cybex_instance = instance)

# 创建市场对象
market = cybex.market.Market(base = base, quote = quote, cybex_instance = instance)

##### 最新tick #####
# 每次调用market对象的tick函数，会去链上查询最新的tick。
t = market.tick()

# 获取最新成交价格
print(float(t['latest']))

# 获取买1价
print(float(t['highestBid']))

# 获取卖1价
print(float(t['lowestAsk']))

# 获取最新价与24小时前的价格相比的涨跌幅
print(float(t['percentChange']))

# 获取24小时内的成交量
print(float(t['baseVolume']))
print(float(t['quoteVolume']))


##### 深度行情 #####
# 每次调用market对象的orderbook函数，会去链上查询最新的orderbook。
order_book = market.orderbook()

# 获取卖单队列
for ask_order in order_book['asks']:
    # 订单价格，为以base计价的quote的价值
    print(ask_order['price'])
    # 卖单中，出售quote资产的数量
    print(ask_order['quote'].amount)
    # 卖单中，收购base资产的数量
    print(ask_order['base'].amount)

# 获取买单队列
for bid_orders in order_book['bids']:
    # 订单价格，为以base计价的quote的价值
    print(ask_order['price'])
    # 买单中，收购quote资产的数量
    print(ask_order['quote'].amount)
    # 买单中，出售base资产的数量
    print(ask_order['base'].amount)
```
