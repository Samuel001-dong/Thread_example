""""
写一个Bicycle(自行车)类
    有run(骑行)方法,调用时显示骑行里程km(骑行里程为传入的数字)
再写一个电动自行车类EBicycle继承Bicycle
    添加电池电量battery_level属性通过参数传入
    同时有两个方法:
        fill_charge(vol)用来充电,vol为电量
        run(km)方法用于骑行,每骑行10km消耗电量1度
            当电量耗尽时调用Bicycle的run方法骑行
通过传入的骑行里程数,显示骑行结果(就是当电量耗尽,需要你真正骑的里程数)
)
"""
import yaml


class Bicycle:
    @classmethod     # 可使调用run方法时不必输入self参数
    def run(self, km):
        print(f"骑行里程数:{km}km")


class EBicycle(Bicycle):
    battery_level: int

    def __init__(self, battery):      # 此方法在类实例化时即执行,所以类需要传入此参数
        self.battery_level = battery
        print(f"初始电量:{self.battery_level}度")

    def fill_charge(self, vol):
        self.battery_level += vol
        print(f"充电{vol}度")
        print(f"当前电量为{self.battery_level}度")

    def run(self, km):
        print(f"客户目标里程:{km}km")
        miles = km - self.battery_level*10
        if miles > 0:
            print("电量不够.....")
            print(f"电行里程数:{self.battery_level*10}km")
            Bicycle.run(miles)
        else:
            print("电量充足,不需要骑行")


with open("../Data/bicycle_data.yml", encoding='utf-8') as f:  # windows的默认编码格式是gbk,想要中文能识别需将编码格式改为utf-8
    data_all = yaml.safe_load(f)
print(data_all)
data = data_all['default']
print(data['env'])
e1 = EBicycle(data['battery'])
# # e1.fill_charge(5)
e1.run(data['km'])
