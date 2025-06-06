from selenium import webdriver
from selenium.webdriver.edge.options import Options
import random
import time

# 创建 EdgeOptions 对象，用于配置浏览器选项
edge_options = Options()
# 添加参数忽略证书错误
edge_options.add_argument('--ignore-certificate-errors')
# 添加参数禁用扩展
edge_options.add_argument('--disable-extensions')
# 添加参数禁用沙盒模式
edge_options.add_argument('--no-sandbox')
# 添加参数禁用 GPU 加速
edge_options.add_argument('--disable-gpu')


# 创建 Edge 浏览器驱动实例
driver = webdriver.Edge(options=edge_options)

# 先访问站点基础页面（比如首页），让浏览器先有站点的基础上下文，再设置 Cookie 更有效
driver.get('https://report.iresearch.cn/')  # 替换为实际站点域名

# 逐个设置关键 Cookie ，这里示例写死值，实际要替换成你抓包拿到的真实值
cookies = [
    {'name': 'iRsUserType', 'value': '49'},
    {'name': 'iRsUserPhoto', 'value': '103a112a106a46a120a116a47a115a101a103a97a109a105a47a101a100a117a108a99a110a105a47a110a99a46a104a99a114a97a101a115a101a114a105a46a110a109a117a108a111a99a47a47a58a112a116a116a104'},  # 替换为完整真实值
    {'name': 'iRsUserPassword', 'value': '53a55a48a57a57a49a50a51a55a50a121a112a122'},
    {'name': 'iRsUserNick', 'value': ''},  # 补全真实值
    {'name': 'iRsUserRName', 'value': ''},
    {'name': 'iRsUserId', 'value': '51a55a48a54a57a54a49'},
    {'name': 'iRsUserGroup', 'value': '48'},
    {'name': 'iRsUserDate', 'value': '54a48a53a50a48a50'},
    {'name': 'iRsUserAccount', 'value': '109a111a99a46a113a113a64a53a55a48a57a57a49a50a51a55a50'},
    {'name': 'Hm_lvt_c33e4c1e69eca76a2e522c20e59773f6', 'value': '1748942804,1748947895,1749006115,1749097730'},
    {'name': 'Hm_lpvt_c33e4c1e69eca76a2e522c20e59773f6', 'value': '1749099415'},
    {'name': 'HMACCOUNT', 'value': '9DB3474109665891'},
    # 继续添加其他 iRs 开头等关键 Cookie 
]

for cookie in cookies:
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(f"设置 Cookie {cookie['name']} 失败：{e}")

# 重新加载页面，让设置的 Cookie 生效，尝试绕过登录
driver.refresh()
time.sleep(3)  # 等待页面加载


# 读取文件中的链接（假设链接文件为当前目录下的generated_links.txt）
def read_links():
    with open("generated_links.txt", "r", encoding="utf-8") as f:
        links = [line.strip() for line in f if line.strip()]
    return list(set(links))  # 去重处理

# 模拟浏览器遍历链接
def browse_links(links):

    try:
        for idx, link in enumerate(links, 1):
            try:
                driver.get(link)
                print(f"{idx}/{len(links)}正在访问：{link}")
                
                # 模拟真实用户行为
                time.sleep(random.uniform(3, 7))  # 随机停留3-7秒
                scroll_height = driver.execute_script("return document.body.scrollHeight")
                driver.execute_script(f"window.scrollTo(0, {random.randint(0, scroll_height)})")  # 随机滚动
                
                # 偶尔模拟刷新（增加随机性）
                if random.random() < 0.2:
                    driver.refresh()
                    time.sleep(2)
                
            except Exception as e:
                print(f"访问失败：{link} | 错误：{str(e)[:50]}...")
                continue  # 跳过当前链接
    
    finally:
        time.sleep(2)
        driver.quit()
        print("\n所有链接遍历完成！")

# 主程序入口
if __name__ == "__main__":
    links = read_links()
    if links:
        print(f"检测到 {len(links)} 个链接，开始遍历...")
        browse_links(links)
    else:
        print("未找到有效链接")