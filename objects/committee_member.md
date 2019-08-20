## 理事会成员(1.5.X)
理事会成员是由用户创建的链上实体，从属于创建它的用户账户，每个用户账号至多创建一个理事会成员。理事会成员获取一定数量投票后，成为正式的理事会成员，可以参与链的管理。

### 理事会成员结构
```json
{
    "id": "1.5.1",
    "committee_member_account": "1.2.17",
    "vote_id": "0:12",
    "total_votes": "36647860903060",
    "url": ""
}
```

### 字段含义
字段 | 类型 | 含义
---|---|---
id|committee member id| committee member id
committee_member_account|账号id|该理事会成员所属的用户账号
vote_id|投票序号|其他账号投票此理事会成员时使用的投票号
total_votes|整数| 理事会成员当前得票数
url|字符串|理事会成员相关信息链接
