

# sweetest

## 介绍

Sweetest 是一款小而美的自动化测试解决方案，同时支持 Web UI，Http 接口，DB 操作测试，Android/iOS App 测试，小程序测试，Windows GUI 测试，文件操作；由于开始只支持 Web UI 测试，名字取自 Selenium，Web UI，Excel，Element， Test 含义。
特点:

1.  简单快速，轻松上手
2.  无需编码能力
3.  在 Excel 中以文本编写测试用例
4.  维护成本低
5.  支持千、万级别的用例规模
6.  拥抱变化，支持敏捷

## 安装

### 环境要求

- 系统要求：Windows
- Python 版本：**3.6+**
- 浏览器：Chrome
- Chrome 驱动: [chromedriver](https://npm.taobao.org/mirrors/chromedriver) (需和 Chrome 版本匹配，并配置环境变量，[参考这里配置](https://segmentfault.com/a/1190000013940356))

### 安装 sweetest

```bash
pip install sweetest
```

### 升级 sweetest

```bash
pip install -U sweetest
```

### 快速体验

打开 cmd 命令窗口，切换到某个目录，如：D:\\Autotest

```bash
sweetest
cd sweetest_example
python start.py
```

![install](https://sweeter.io/docs/_snapshot/install.png)

OK，如果一切顺利的话，sweetest 已经跑起来了


目录	说明
element\	页面元素表目录
Baidu-Elements.xlsx	页面元素表，名称格式：project_name + "-Elements.xlsx"
junit\	junit格式测试结果目录
log\	自动化测试运行日志目录
report\	Excel 格式测试结果目录
snapshot\	错误截图目录
testcase\	测试用例目录
Baidu-TestCase.xlsx	测试用例，名称格式：project_name + "-TestCase.xlsx"
start.py	启动脚本，test = Autotest(project_name, sheet_name)
> 详细文档：https://sweeter.io/#/sweetest/
> github：https://github.com/tonglei100/sweetest








