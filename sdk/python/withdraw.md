## 提现操作
提现操作可用于将资产从赛贝交易所提现到外部链。在进行提现操作前，需要将转出账户的私钥提前加入Python库的本地钱包中，并解锁钱包。钱包相关操作详见[钱包操作](https://github.com/NebulaCybexDEX/cybex-node-doc/blob/master/sdk/python/wallet.md)

#### 1. 网关
* Cybex链有多个网关可供用户提现，不同网关支持的资产类型不同。
* JADE前缀的资产为Cybex的官方资产，由赛贝官方网关提供充提服务，赛贝官方网关接入点是https://gateway.cybex.io/v1
* 若要使用其他网关进行提现或查询充值地址操作，请在对应函数后填写参数 gateway_url。
* 未填写gateway_url参数的调用，视为使用赛贝官方网关的服务。

#### 1. 提现
* 网关服务需要一定的手续费支持运行，其中需要执行一次Cybex内盘转账，该部分手续费您可选择使用CYB支付或ETH支付 
* 网关执行手续费将以您希望取出的目标资产支付，并从您提取金额中扣除 
* 请务必确认您的提币地址正确，一旦填写错误，您的提币将丢失 
* 所有出入金到账需要一定时限，请耐心等待 
* 提币操作请使用您的个人钱包地址, 提币到合约地址、交易所地址、ICO项目地址可能会发生合约执行失败，将导致转账失败，资产将退回到您的Cybex账户，处理时间较长，请您谅解。
* 提现EOS/PCX等资产时，如果需要在链上转账中填入附言，请使用to-account[memo]作为目标地址。如不需要填入附言，请使用to-account[]作为目标地址
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# 不同资产使用不同的目标地址作为提现地址
# asset-name为您希望提现的资产名字，请使用链上资产全名，如JADE.ETH
# withdraw-account-name为您在赛贝交易所的账号名
# 使用其他网关提现，按如下格式调用
# instance.withdraw(to_addr, 10, 'asset-name', 'withdraw-account-name', gateway_url = 'https://other-gateway/..')
instance.withdraw(to_addr, 10, 'asset-name', 'withdraw-account-name')
```

#### 2.获取充值地址
* 若查询EOS/PCX等资产的充值地址，会返回account_name[memo]格式的地址。
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# asset-name为您希望充值的资产名字，请使用链上资产全名，如JADE.ETH
# deposit-account-name为您在赛贝交易所的账号名
# 获取其他网关充值地址，按如下格式调用
# instance.get_deposit_address('asset-name', 'deposit-account-name'), gateway_url = 'https://gateway.candybull.io/v1')
print(instance.get_deposit_address('asset-name', 'deposit-account-name'))
```
