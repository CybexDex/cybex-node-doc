## 提现操作
提现操作可用于将资产从赛贝交易所提现到外部链。在进行提现操作前，需要将转出账户的私钥提前加入Python库的本地钱包中，并解锁钱包。钱包相关操作详见[钱包操作](https://github.com/NebulaCybexDEX/cybex-node-doc/blob/master/sdk/python/wallet.md)

#### 1. 提现
* 瑶池（Jadepool）作为Cybex推荐的网关将为您提供这一服务 
* 网关服务需要一定的手续费支持运行，其中需要执行一次Cybex内盘转账，该部分手续费您可选择使用CYB支付或ETH支付 
* 网关执行手续费将以您希望取出的目标资产支付，并从您提取金额中扣除 
* 请务必确认您的提币地址正确，一旦填写错误，您的提币将丢失 
* 所有出入金到账需要一定时限，请耐心等待 
* 提币操作请使用您的个人钱包地址, 提币到合约地址、交易所地址、ICO项目地址可能会发生合约执行失败，将导致转账失败，资产将退回到您的Cybex账户，处理时间较长，请您谅解。
* 目前支持提现的币种有
JADE.ETH  JADE.BTC  JADE.LTC  JADE.EOS  JADE.USDT
JADE.MT   JADE.SNT  JADE.PAY  JADE.GET  JADE.MVP
JADE.DPY  JADE.MVP  JADE.LHT  JADE.INK  JADE.BAT
JADE.OMG  JADE.NAS  JADE.KNC  JADE.MAD  JADE.TCT
JADE.GNT  JADE.GNX
* 提现EOS时，如果需要在链上转账中填入附言，请使用to-account[memo]作为目标地址。如不需要填入附言，请使用to-account[]作为目标地址
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# 不同资产使用不同的目标地址作为提现地址
# asset-name为您希望提现的资产名字，请使用JADE.作为资产前缀，如JADE.ETH
# withdraw-account-name为您在赛贝交易所的账号名
instance.withdraw(to_addr, 10, 'asset-name', 'withdraw-account-name')
```
