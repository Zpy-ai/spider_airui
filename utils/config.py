from selenium.webdriver.edge.options import Options



# 创建 EdgeOptions 对象，用于配置浏览器选项
class Config(object):

    @classmethod
    def EdgeOptions(cls):
        edge_options = Options()
        edge_options.add_argument('--ignore-certificate-errors')
        edge_options.add_argument('--disable-extensions')
        edge_options.add_argument('--no-sandbox')
        edge_options.add_argument('--disable-gpu')

        return edge_options
        