from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd  # 新增pandas依赖

# 创建 EdgeOptions 对象，用于配置浏览器选项
edge_options = Options()
edge_options.add_argument('--ignore-certificate-errors')
edge_options.add_argument('--disable-extensions')
edge_options.add_argument('--no-sandbox')
edge_options.add_argument('--disable-gpu')

# 创建 Edge 浏览器驱动实例
driver = webdriver.Edge(options=edge_options)

url = 'https://report.iresearch.cn/'

# 打开指定 URL 的网页
driver.get(url)

try:
    data_list = []  # 用于保存字典数据
    wait = WebDriverWait(driver, 10)
    load_count = 0

    # 点击"加载更多"按钮10次
    while load_count < 11:
        try:
            load_more_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#loadbtn'))
            )
            load_more_btn.click()
            load_count += 1
            print(f"已点击加载更多 {load_count}/10 次")
            time.sleep(2)
            
        except Exception as e:
            print(f"点击加载更多失败: {e}")
            break

    print("等待内容加载完成...")
    time.sleep(3)
    
    # 定位所有目标元素
    elements = driver.find_elements(By.CSS_SELECTOR, 'li[id^="freport."]')
    print(f"共找到 {len(elements)} 个元素")

    found_links = []
    if elements:
        for elem in elements:
            try:
                # 提取元素信息
                title = elem.find_element(By.CSS_SELECTOR, 'h3').text.strip()  # 标题
                link = elem.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')  # 链接
                desc = elem.find_element(By.CSS_SELECTOR, 'p').text.strip() if elem.find_elements(By.CSS_SELECTOR, 'p') else ""  # 摘要
                tags = [tag.text for tag in elem.find_elements(By.CSS_SELECTOR, '.link a')]  # 标签
                timestamp = elem.find_element(By.CSS_SELECTOR, '.time span').text.strip()  # 时间戳

                found_links.append(link)

                # 构建字典
                data_dict = {
                    "标题": title,
                    "链接": link,
                    "描述": desc,
                    "标签": ", ".join(tags),
                    "时间": timestamp
                }
                data_list.append(data_dict)
                print(f"找到元素：{title[:30]}...")  
                
            except Exception as e:
                print(f"处理元素失败: {e}")
                continue

        # 将找到的链接信息保存到文件
        with open('found_links.txt', 'w', encoding='utf-8') as f:
            for link in found_links:
                f.write(link + '\n')
        print("已将找到的链接信息保存到 found_links.txt")

        # 将列表转换为DataFrame
        df = pd.DataFrame(data_list)
        
        # 保存为CSV文件（也可改为Excel等其他格式）
        df.to_csv('iresearch_reports.csv', encoding='utf-8-sig', index=False)
        print(f"\n成功保存 {len(data_list)} 条数据到 iresearch_reports.csv")

        # 打印DataFrame前5行（可选）
        print("\n数据预览：")
        print(df.head())

    else:
        print("未找到符合条件的元素。")

except Exception as e:
    print("定位元素失败：", e)
    with open('page_source.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    print("已保存页面源代码到 page_source.html")

finally:
    time.sleep(2)
    driver.quit()