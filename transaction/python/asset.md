## 资产查询相关操作
赛贝交易所中的资产包含多个属性，本文介绍如何查看资产的这些属性。

```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
ASSET_NAME = 'JADE.ETH'

instance = cybex.Cybex(NODE_URL)
asset = cybex.asset.Asset(ASSET_NAME, cybex_instance = instance)

# 查看资产符号
print(asset.symbol)  # 'JADE.ETH'

# 查看资产id
# 资产id是资产在链上的唯一标识
print(asset["id"]) # '1.3.2'

# 查看资产精度
# 精度为6表示资产最多可以分割到小数点后6位
# 所有上链查询的数据均以整数表示，将小数点左移精度位即为实际数值
print(asset.precision) # 6

# 查看资产最大发行量
# 精度为6的资产，这里的max_supply即为 1000000000
print(asset["options"]["max_supply"]) # 1000000000000000

# 查看资产核心交换费率
# 该交换费率表示，当用户使用本资产作为手续费付费资产时，
# 将按照核心资产的手续费费率，根据此交换费率换算为付费资产向用户收取
# 例如用户转账，如以CYB支付手续费，根据费率表计算需支付0.01CYB，
# 如用户希望以JADE.ETH支付，根据JADE.ETH的交换费率表，CYB与JADE.ETH的
# 交换比例为1000:1，那么将向用户收取0.01/1000即0.00001JADE.ETH的手续费。
print(asset['options']['core_exchange_rate']) # {'base': {'amount': 100000000, 'asset_id': '1.3.0'}, 'quote': {'amount': 1000000, 'asset_id': '1.3.2'}}
```
