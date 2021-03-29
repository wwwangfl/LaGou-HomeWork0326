#定义一个英雄类，作为父类供作为其它英雄继承属性与方法
class Hero:
    """
    静态属性:
        hp 代表血量，
        power 代表攻击力
        name 代表英雄名称
        lines 代表英雄台词  
    """
    hp = 0
    power = 0
    name = ""
    lines = ""

    #每个英雄都有一个 fight 方法
    def figth(self,enemy_hp,enemy_power):
        #本英雄最终血量=本英雄血量-敌人攻击力
        final_hp = self.hp - enemy_power
        # 敌人最终血量=敌人英雄血量-本英雄攻击力
        enemy_final_hp = enemy_hp - self.power
        # 根据双方最终血量判断谁赢了
        if final_hp > enemy_final_hp:
            print(f"{self.name}赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("我们打平了")

    """
    每个英雄都一个speak_lines方法:
        调用speak_lines方法，不同的角色会打印（讲出）不同的台词"   
    """
    def speak_lines(self):
        print(f"{self.name} Speak：{self.lines}")