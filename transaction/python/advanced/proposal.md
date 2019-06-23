## 创建拟议交易操作
任意一个账户可以提议一个拟议交易(proposal)。拟议交易可以包含多个独立操作。当某账户发起一个拟议交易上链后，节点会自动根据拟议交易中的所有操作，计算该拟议交易需要的权限集合。
例如：用户A可以发起一个拟议交易，包含两个操作：1.从B帐号向C帐号转账1CYB，2.从D帐号向E帐号转账1CYB。该拟议交易发上链后，节点自动计算出，该交易需要B和D的权限。通过查询B和D的拟议交易(使用B和D的帐号id，调用get_proposed_transactions api)，可以看到该拟议交易。此时，用户B和D可以批准该拟议交易，当用户B和D批准后，该拟议交易中的两个操作会被原子执行，即两笔转账同时发生(若由于某些原因，某笔转账不能被执行，则两笔转账会同时失败。)。若拟议交易执行失败，该拟议交易会存留于链上，直到拟议交易过期。在拟议交易过期的时间点，节点会再次尝试执行拟议交易，若继续失败，则从链上删除拟议交易。

#### 1.创建拟议交易
以下演示如何用Python库完成上面的创建拟议交易操作
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

proposal = instance.new_proposal(proposer = 'account-a', proposal_expiration = 3600)
instance.transfer('C', 1, 'CYB', '', account = 'B', append_to = proposal)
instance.transfer('E', 1, 'CYB', '', account = 'D', append_to = proposal)
proposal.broadcast()
```

#### 2.查询和本账号相关的拟议交易
以下演示如何用Python库查询和某个帐号相关的拟议交易
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'

instance = cybex.Cybex(NODE_URL)

account = cybex.Account('B', cybex_instance = instance)

proposals = instance.rpc.get_proposed_transactions(account['id'])

for proposal in proposals:
    print(proposal['id'], proposal)
```

#### 3.同意一个拟议操作
帐号B通过查询操作查询到本账号相关的拟议交易后，获取其id字段，使用approveproposal操作，批准该拟议交易
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

instance.approveproposal([proposal_id], account = 'B', approver = 'B')
```
