from timo import Timo
from police import Police


# 定义一个英雄工厂类
class HeroFactory:
    """
    简单工厂模式专门定义一个类来负责创建其他类型的英雄的实例
    """
    def create_hero(self, name):
        if name == "Timo":
            return Timo()
        elif name == "Police":
            return Police()
        else:
            # print(f"这个英雄:{name}不在英雄工厂")
            raise Exception(f"这个英雄:{name}不在英雄工厂")