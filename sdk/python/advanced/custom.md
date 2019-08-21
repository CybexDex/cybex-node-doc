## 用户自定义操作
用户自定义操作允许用户发送一些自定义信息到区块链上。发送的信息可以包含
* 一个用户列表
* 一个无符号短整型数字[0,65535)
* 一段以ascii编码的文字
* [可选]用户自定义的将文字转为十六进制表示的函数

#### 1.发送自定义操作
```Python
import cybex

NODE_URL = 'ws://127.0.0.1:8090'
WALLET_PWD = '123456'

instance = cybex.Cybex(NODE_URL)
instance.wallet.unlock(WALLET_PWD)

# 用户列表填写包含用户名的list对象，如不需要，传入[]即可
# id为无符号短整型数字
# 用户定义文字需要以ascii编码，如需填入其他语言的文字，请自定义方法将其十六进制化，或将其以ascii编码后传入这个方法
# account为发送这个操作的账户
# 用户可以指定to_hex函数，如果不指定，将使用默认的to_hex函数，
# 默认to_hex函数会将输入字符串十六进制化，并前缀以ca1be4作为识别

data = 'customized data'
# 如果是中文字符串，可以通过以下方法编码，仅供参考
# import binascii
# data = binascii.hexlify(bytes('中文字符串', 'utf-8')).decode('ascii')

instance.custom(
                ['account1', 'account2'],
                12345,
                data,
                account = 'your-account'
               )
```

#### 2.解码字符串
通过查询链上的区块，获得交易中的十六进制编码的字符串后，可以通过以下方法解码，获得原字符串
```Python
import cybex
data = cybex.custom.convert_from_hex(hex_str)

# 如果是中文字符串，通过以下方法进一步解码
import binascii
binascii.unhexlify(data).decode('utf-8')
```
