import random
import time


# 生成红球的方法
def createRed():
    # 有三个区间，每个红球落入区间的概率为1/3；
    # 骰点
    dice = random.randint(1, 3)
    if dice == 1:
        # 红球第一区间（1~11）
        r1 = random.randint(1, 11)
        return r1
    elif dice == 2:
        # 红球第二区间（12~22）
        r2 = random.randint(12, 22)
        return r2
    else:
        # 红球第三区间（12~22）
        r3 = random.randint(23, 33)
        return r3


# 产生红球组，调用生成红球的方法6次
def createReds():
    arr = []
    # 生成红球的概率值
    m1 = 0
    m2 = 0
    m3 = 0
    while True:
        tmp = createRed()
        if tmp not in arr:
            arr.append(tmp)

            # 根据tmp计算该组红球产生的概率
            if tmp in range(1, 12):  # 1~11之间
                m1 += 1
            elif tmp in range(12, 23):
                m2 += 1
            else:
                m3 += 1
        if len(arr) == 6:
            # 输出红球组
            return sorted(arr), m1, m2, m3


# 生成双色球函数
def createSSQ():
    wn = 0
    while True:
        wn += 1
        (reds, t1, t2, t3) = createReds()
        # 连号不能大于等于4
        if (reds[0] + 1 != reds[1] and reds[0] + 2 != reds[2] and reds[0] + 3 != reds[3]) and (
                                reds[1] + 1 != reds[2] and reds[1] + 2 != reds[3] and reds[1] + 3 != reds[4]) and (
                                reds[2] + 1 != reds[4] and reds[2] + 2 != reds[4] and reds[2] + 3 != reds[5]):
            ssq = [reds, [random.randint(1, 16)]]
            print(ssq)
            # print("执行次数：" + str(wn))
            # print("t1=" + str(t1) + "；t2=" + str(t2) + "；t3=" + str(t3))
            break


# 调用函数
# 生成5组
num = 0
sumX = 0
while True:
    num += 1
    now = int(time.time())  # 这是时间戳
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%H%M%S", timeArray)
    # for i in range(1, 6):
    ran1 = random.randint(1, int(otherStyleTime))
    ran2 = random.randint(1, int(otherStyleTime))
    if ran1 == ran2:
        sumX += 1
        createSSQ()
        # print(int(otherStyleTime))
        if sumX == 5:
            print(num)
            break
