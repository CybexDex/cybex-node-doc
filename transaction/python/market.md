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

##### 获取K线 #####
# 赛贝是一个全球部署的去中心化交易所，系统使用UTC时间，
# 获取K线需要使用UTC时间
# 以下例子获取开始时间在UTC时间2018-08-31日，5:59:00到6:01:00之间的3600秒k线，
# 将会返回UTC时间2018-08-31 06:00:00的小时K线
from datetime import datetime
start = datetime.strptime('2018-08-31 05:59:00', '%Y-%m-%d %H:%M:%S')
end = datetime.strptime('2018-08-31 06:01:00', '%Y-%m-%d %H:%M:%S')

# 返回一个kline的序列，所有开始时间在start到end之间的K线
# 如果在某个时间段内没有成交，则对应的K线不存在，也不会返回。
kline_arr = market.get_market_history(3600, start, end)
kline = kline_arr[0]

# 开盘价格
print(float(kline['openPrice']))
# 收盘价格
print(float(kline['closePrice']))
# 最高价格
print(float(kline['highPrice']))
# 最低价格
print(float(kline['lowPrice']))

# 开盘成交中，base资产的数量
openBase = kline['openBaseVolume'] / 10 ** kline['openBaseVolume'].asset['precision']
print(openBase.asset['symbol'], float(openBase))

# 开盘成交中，quote资产的数量
openQuote = kline['openQuoteVolume'] / 10 ** kline['openQuoteVolume'].asset['precision']
print(openQuote.asset['symbol'], float(openQuote))

# 依上例可获取openBase, openQuote, closeBase, closeQuote, highBase, highQuote, lowBase, lowQuote
```
