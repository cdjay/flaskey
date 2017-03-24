# 本模块判断距离听牌还有多少步骤(判断向听数)
# 加载配牌库
from pick import *

# Hand_D = [2, 2, 3, 3, 4, 4, 8, 8]  # 方便测试,此处暂时固定手牌,可注释
Hand_D = [1, 1, 1, 3, 3, 3, 8, 8]  # 方便测试,此处暂时固定手牌,可注释
print('[计算以下手牌胡牌组合] \n', Hand_D, '\n')  # 显示当前手牌

# 主程序R

# 以Hand_D数量为循环长度,计算[DD]的数量和位置
DD_pos = []  # 位置名称
DD_value = []  # 记录位置值名称
for i in range(len(Hand_D)):  # 循环手牌数量依次判断
    if i == len(Hand_D) - 1:  # 防止下标越界,循环到倒数第二张.
        break
    elif Hand_D[i] == Hand_D[i + 1]:  # 判断这张和下一张相同,构成DD形态
        DD_pos.append(i)  # 记录DD形态在Hand_D中的下标位置

# 将位置信息转换成具体值
Hand_temp = Hand_D.copy()  # 手牌暂存数组
for i in range(len(DD_pos)):  # 以位置数量循环
    DD_value.append(Hand_D[DD_pos[i]])  # 把位置对应的值append到DD_value里

# DD信息
# print('DD数量: [', len(DD_pos), ']')
# print('DD位置:', DD_pos)
# print('DD集合:', DD_value)
#

# 循环查找排除某个DD后,剩余的牌是否可构成面子(顺子:ABC,刻子:AAA)
print('[计算结果]')
Hand_Hu = [] # 牌型区
Hand_List = [] # 牌型组合列表
Hand_Hulist = [] # 可胡牌型的数量和位置
Hand_Ting = 0 # 向听数

def seekaaa(aaa,pailist):# 判断有无aaa形态,
    print('当前检查的是:',aaa)


def abc():# 判断有无abc形态
    pass

for i in range(len(DD_value)):
    print(seekaaa(Hand_temp[i],Hand_temp))
    Hand_temp.remove(DD_value[i])  # 移除第一个DD
    Hand_temp.remove(DD_value[i])  # 移除第二个DD
    print('DD为[%2s] %r' % (DD_value[i], Hand_temp))  # 按指定格式输出
    print('拆分结果', Hand_Hu)
    #结尾部分恢复原始数据便于下个循环
    Hand_temp = Hand_D.copy()
    Hand_Hu = []

if len(DD_value) < 1: print('\n---不可胡牌---')
