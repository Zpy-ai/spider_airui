# 基于selenium爬取艾瑞网报告


## 一、项目简介
该项目主要用于从艾瑞网爬取不付费的报告信息，标题、行业、作者、摘要和报告原件。

## 二、项目结构
```plaintext
spider_airui/
├─ utils/           # 工具模块目录
│  └─ config.py     # 配置文件
├─ main.py          # 主程序入口（核心爬取逻辑）
├─ load.py          # 链接处理与数据加载模块
├─ found_links.txt  # 爬取过程中发现的原始链接（临时存储）
├─ load_links.txt   # 生成的待下载链接列表
├─ iresearch_reports.csv # 最终爬取结果（csv格式）
├─ README.md        # 项目说明文档
└─ requirement.txt  # 依赖库清单
```


## 三、环境要求
1.本项目基于 Python 开发，运行前需确保已安装 Python 环境，项目依赖的 Python 库在requirement.txt中列出。

2.运行本项目需要安装对应版本的Edge驱动，详细参考blog：https://blog.csdn.net/2401_85252837/article/details/148436883?spm=1001.2014.3001.5501

## 四、使用指南
### 4.1 准备工作
1.安装依赖；

2.确保项目目录具有读写权限，以便程序生成和保存文件。

### 4.2 运行项目
1.在项目根目录下，运行main.py文件：

2.运行过程中，程序会在终端输出提取和生成链接的相关信息，如：


生成链接: https://report.iresearch.cn/include/ajax/user_ajax.ashx?reportid=12345&work=rdown&url=https%3A%2F%2Freport.iresearch.cn%2Freport%2F202505%2F12345.shtml
...

已保存生成的下载链接到 load_links.txt

### 4.3 查看结果

运行完成后，可在项目目录下查看生成的extracted_ids.txt和generated_links.txt文件，获取提取的数字 ID 和生成的新链接。

## 声明
本爬虫项目仅用于学习用途。严禁将本项目用于任何非法目的，包括但不限于恶意攻击网站、窃取用户隐私数据、破坏网站正常运营、商业侵权等行为。

用户在使用本项目时，需自行承担因使用不当或违反法律法规所引发的一切后果与责任。若因用户使用本项目导致任何第三方权益受损或违反法律规定，相关法律责任均由用户自行承担，与本项目开发者及维护者无关。

