""""
pyyaml的使用示例
"""
import sys

import yaml
# yaml.safe_load()   # 将yaml格式转换为Python的对象
# yaml.safe_dump()


with open("./data.yml") as f:
    print(yaml.safe_load(f))
