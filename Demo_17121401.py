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


# 生成篮球
def createBlue():
    # 有三个区间，每个红球落入区间的概率为1/3；
    # 骰点
    dice = random.randint(1, 16)
    if dice in range(1, 6):
        # 蓝球第一区间（1~5）
        b1 = random.randint(1, 5)
        return b1
    elif dice in range(6, 12):
        # 蓝球第二区间（6~11），蓝球无法均分，所以，中间多一个
        b2 = random.randint(6, 11)
        return b2
    else:
        # 蓝球第三区间（12~16）
        b3 = random.randint(12, 16)
        return b3


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
        blue = createBlue()
        # 连号不能大于等于4
        if (reds[0] + 1 != reds[1] and reds[0] + 2 != reds[2] and reds[0] + 3 != reds[3]) and (
                                reds[1] + 1 != reds[2] and reds[1] + 2 != reds[3] and reds[1] + 3 != reds[4]) and (
                                reds[2] + 1 != reds[4] and reds[2] + 2 != reds[4] and reds[2] + 3 != reds[5]):
            ssq = [reds, blue]
            # print("执行次数：" + str(wn))
            # print("t1=" + str(t1) + "；t2=" + str(t2) + "；t3=" + str(t3))
            return ssq, t1, t2, t3


def mainMethod():
    # 调用函数
    # 生成5组
    num = 0
    sumX = 0
    sumNum = 0
    while True:
        num += 1
        sumNum += 1
        now = int(time.time())  # 这是时间戳
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%H%M%S", timeArray)
        # 取当前时间的时分秒，产生两个随机数，做一个事件
        ran1 = random.randint(1, int(otherStyleTime))
        ran2 = random.randint(1, int(otherStyleTime))
        if ran1 == ran2:
            sumX += 1
            (ssq, t1, t2, t3) = createSSQ()
            print(ssq)
            print("区间发布：" + str(t1) + ":" + str(t2) + ":" + str(t3))
            print("触发时间：" + otherStyleTime)
            print("执行次数：" + str(num))
            num = 0  # 重新计数
            # print(int(otherStyleTime))
            if sumX == 5:
                print("总执行次数：" + str(sumNum))
                break


"""
    需要补充的
1、奇偶
2、AC
"""
#start = time.time()
mainMethod()
#end = time.time()
#print(end-start)



