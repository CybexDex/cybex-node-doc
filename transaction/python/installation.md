## 运行环境
Cybex Python库支持Python3语言环境，建议用户使用virtualenv作为环境管理工具

## 安装Python库
Linux使用virtualenv运行PyCybex
```Bash
virtualenv --no-site-packages --python='PATH TO PYTHON3' venv
cd venv
source bin/activate
pip install PyCybex
```
Windows使用virtualenv运行PyCybex
```Bash
pip install virtualenv
virtualenv --no-site-packages venv
cd venv/Scripts
activate
pip install PyCybex
```
