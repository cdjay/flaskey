# coding=utf-8
# 随机生成一副牌局
# 存储数组:P=筒,S=索,M=万.
# 筒=1-9,索=11-19,万=21-29.
# 字牌[东南西北白发中]分别对应[31,33,35,37,41,43,45]字牌无连续性,所以需要间隔.
# 四个方向:LEFT,RIGHT,UP,DOWN.自己:D,下家:R,对家:U,上家:L
# 每个方向分别有两组数据:1.打出的牌,2.吃碰杠区域.
# 自身手牌有两个区域.手牌+当前摸到的牌
# 整局游戏牌山数量为一个数组.

# -- 加载库 --
import random  # 随机模块


# -- 函数定义 --
# 摸牌模块
def PickStart(Hand):  # 开始配牌
    for i in range(0, 4):  # 一次4张
        Hand.append(MahjongList[0])  # 将牌山最前面的一张配牌传递给玩家
        del MahjongList[0]  # 将牌山最前面的一张牌删除
    Hand.sort()  # 排序
    return Hand


def Pick(Hand):  # 单张摸牌,
    for i in range(0, 1):  # 一次1张
        Hand.append(MahjongList[0])  # 将牌山最前面的一张配牌传递给玩家
        del MahjongList[0]  # 将牌山最前面的一张牌删除
    Hand.sort()  # 排序
    return Hand


# 主程序
print('---游戏开始---\n')

# 随机生成牌山
s=[1, 2, 3, 4, 5, 6, 7, 8, 9]*4                 #定义索
p=[11, 12, 13, 14, 15, 16, 17, 18,19]*4         #定义筒
m=[21, 22, 23, 24, 25, 26, 27, 28,29]*4         #定义万
z=[31,33,35,37,41,43,45]*4                      #定义东南西北白发中
MahjongList = s + p + m
MahjongList = random.sample(MahjongList, len(MahjongList))  # 打乱
print('[初始牌山', len(MahjongList), '张]')
print(MahjongList,'\n')

# 开始配牌
Hand_D = []  # 自己
Hand_R = []  # 下家
Hand_U = []  # 对家
Hand_L = []  # 上家
# 模拟真实摸牌过程,即4442模式
for i in range(3):  # 发三轮牌,每轮4张
    PickStart(Hand_D)
    PickStart(Hand_R)
    PickStart(Hand_U)
    PickStart(Hand_L)
# 第一轮摸牌,每人一张,庄家多一张.
for i in range(1):
    Pick(Hand_D)
    Pick(Hand_R)
    Pick(Hand_U)
    Pick(Hand_L)
    Pick(Hand_D)
# 配牌结束


# 输出测试
print('[配牌',len(Hand_D+Hand_L+Hand_R+Hand_U),'张]\n 自己 :', len(Hand_D), Hand_D)
print(' 下家 :', len(Hand_R), Hand_R)
print(' 对家 :', len(Hand_U), Hand_U)
print(' 上家 :', len(Hand_L), Hand_L)
print('\n[牌山剩余', len(MahjongList), '张]\n', MahjongList,'\n')
