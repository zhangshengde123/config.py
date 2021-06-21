from sweetest import Autotest
import sys


# 项目名称，和测试用例、页面元素表文件名称中的项目名称必须一致
plan_name = 'Suda_Mall'

# 单 sheet 页面模式
sheet_name = 'comb'

# sheet 页面匹配模式，仅支持结尾带*
#sheet_name = 'TestCase*'

# sheet 页面列表模式
#sheet_name = ['TestCase', 'test']


# 环境配置信息
# Chrome
#desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome'}
# Chrome 模拟移动浏览器
desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome', 'mobile_emulation': {"deviceName": "iPhone X"}}
# headless
#desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome', 'headless': True}
# 设置全局截图
#desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome', 'snapshot': True}
# 指定 driver 路径
#desired_caps = {'platformName': 'Desktop', 'browserName': 'Chrome', 'executable_path': 'D:\drivers\chromedriver.exe'}
server_url = ''

# 初始化自动化实例
sweet = Autotest(plan_name, sheet_name, desired_caps, server_url)

# 按条件执行,支持筛选的属性有：'id', 'title', 'designer', 'priority'
#sweet.fliter(priority='H')
#sweet.fliter(id='ADDR_001')

# 执行自动化测试
sweet.plan()


# Web 测试报告
#sweet.report(r'D:\report')

# 如果是集成到 CI/CD，则给出退出码
#sys.exit(sweet.code)
