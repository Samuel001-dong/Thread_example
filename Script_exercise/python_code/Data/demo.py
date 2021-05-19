""""
pyyaml的使用示例
用于数据驱动存储数据
YAML 支持以下几种数据类型：
对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
纯量（scalars）：单个的、不可再分的值
"""
import sys

import yaml
# yaml.safe_load()   # 将yaml格式转换为Python的对象
# yaml.safe_dump()


with open("./data.yml") as f:
    print(yaml.safe_load(f))
