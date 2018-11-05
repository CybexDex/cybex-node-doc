## 创建资产操作
终身会员用户可以在Cybex链上创建资产。创建资产需要设置多个参数，参数的含义可以参考[创建资产](https://github.com/CybexDex/cybex-node-doc/wiki/%E6%90%AD%E5%BB%BACYBEX%E7%BD%91%E5%85%B3)

#### 1.创建资产
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# 创建一个普通资产

instance.create_asset(
    symbol = 'TEST', # 资产的符号
    precision = 6, # 资产的精度
    max_supply = 10000000, # 资产最大供给量，不含精度在内
    core_exchange_ratio = {'CYB': 1, 'TEST': 20}, # 资产手续费比例，1CYB换20TEST
    description = 'test description', # 资产的描述性质的文字，可以写中文

    ## 以下设置资产的发行人权限
    ## 资产发行人权限，是指资产在创建后，可以由发行人动态调整的权限
    ## 普通链上资产涉及以下4个发行人权限
    ## 如无特殊需求，建议全部设置为True
    charge_market_fee = True, # 发行人是否可以后期调整资产的charge_market_fee权限位
    white_list = True, # 发行人是否可以后期调整资产的white_list权限位
    override_authority = True, # 发行人是否可以后期调整资产的override_authority权限位
    transfer_restricted = True, # 发行人是否可以后期调整资产的transfer_restricted权限位
    
    is_prediction_market = False, # 预测市场资产，对于普通资产，设置位False
    account = 'owner1' # 资产创建人，必须是终身会员
)
```
