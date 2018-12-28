'''
请将数据文件email-Eu-core-temporal.csv和该运行文件放在同一文件夹下
运行完成后，可自行复制粘贴结果，稍作处理即可生成.csv文件
由于运行时间较长，本人已将运行后的结果放到result.csv中，请自行查看
@author:JeriYang
@time:2018
'''
DAY_INTERVAL = 86400   #时间戳对应的一天的时间间隔
MONTH_INTERVAL = 2678400  #一个月31天的时间间隔
MAX_TIMESTANP = 69459254  #数据中最大的时间戳
NODE_NUM = 1004 #最大节点数
import numpy as np
import csv    #需要加载numpy和csv两个包
import matplotlib.pyplot as plt
import time
###########读取csv文件吗，得到数据#################
def readFile(fileName):
    #csv_file=open('email-Eu-core-temporal.csv')         #打开文件
    csv_file=open(fileName)                    #打开文件
    csv_reader_lines = csv.reader(csv_file)    #用csv.reader读文件
    readData=[]
    for one_line in csv_reader_lines:
        mid = []
        for i in one_line:     #将字符串转换为int类型，方便后期处理
            mid.append(int(i))
        readData.append(mid)    #逐行将读到的文件存入python的列表
    u_v_t = np.array(readData)    #转为numpy，方便后期处理
    return u_v_t

############获取指定时间间隙的数据#############
def getTimeData(time_interval, u_v_t, start_time, begin_line):
    end_time = start_time + time_interval  # 结束时间
    ####筛选合适数据：
    if (start_time < MAX_TIMESTANP):  # 允许范围内
        while (u_v_t[begin_line][2] < start_time):
            begin_line += 1
    else:
        print("超出范围，程序异常");exit(0)
    print(begin_line)
    maxLine = begin_line  # 由开始行求截止行数
    if (end_time < MAX_TIMESTANP):  # 允许范围内
        while (u_v_t[maxLine][2] < end_time):
            maxLine += 1
    else:
        print("超出范围，程序异常");exit(0)
    print(maxLine)
    snapshot_u_v = u_v_t[begin_line:maxLine][:, [0, 1]]  # 取范围内的发送者合接受者
    return snapshot_u_v

#############按照时间间隔设置快照，并输出######################
total_x = []
total_y = []
u_v_t = readFile('email-Eu-core-temporal.csv')
time_interval = 10 * DAY_INTERVAL  # 设置时间间隔
for i in range(0, 50):
    start_time = i*time_interval        #开始时间
    begin_line = 0                      #开始行
    snapshot_u_v = getTimeData(time_interval, u_v_t, start_time, begin_line)
    # print(snapshot_u_v.shape)
    # print(snapshot_u_v[0])
    # print(snapshot_u_v[1])

    snapshot = np.zeros(shape =(NODE_NUM+1, NODE_NUM+1),dtype=int)  #定义快照986*986, 初始化全为0
    for i in snapshot_u_v:     #将出现过的人之间的关系全部设置为2，表示之间没有关系
        for j in range(0, NODE_NUM+1):
            snapshot[i[0]][j] = 2
            snapshot[i[1]][j] = 2
    #仍为0的行，则不用去管了
    for i in snapshot_u_v:   #朋友关系置为1, 生成快照
        snapshot[i[0]][i[1]] = 1
        snapshot[i[1]][i[0]] = 1

    print("求共同朋友：")
    #在快照中求还不是朋友的节点和共同朋友数量：
    notFriend = [] #四维数组用于保存未建立关系的两个人和共同朋友数量（x,y,z，0）其中x < y, z为共同朋友数量.0方便后期统计
    total = np.zeros(shape =(NODE_NUM+1),dtype=int)  #统计共同朋友数分别对应的人数，其中total[0]保存最大的朋友数（舍弃到共同朋友为0的数据）
    became_friend = np.zeros(shape =(NODE_NUM+1),dtype=int)  #统计变为朋友的人数，其中[0]保存人数，同上
    maxNum = 0
    for i in range(0,NODE_NUM+1):
        # if(i%100==0):
        #     print("加载中：{:.2f}%".format(i*100/NODE_NUM))
        if(snapshot[i][0] == 0): continue #此人未在快照中出现
        else:
            for j in range(0,NODE_NUM+1):
                if(snapshot[i][j] == 1 or i==j):continue  #两人为朋友或是自己
                else: #不是朋友时
                    if(i < j):  #求共同朋友
                        common_friend = 0
                        for k in range(0,NODE_NUM+1):
                            if(snapshot[i][k] == 1 and snapshot[j][k] == 1): common_friend += 1
                        if(common_friend != 0):
                            if(common_friend > maxNum): maxNum = common_friend
                            midList = [i,j,common_friend,0]
                            total[common_friend] +=1
                            notFriend.append(midList)
    total[0] = maxNum
    became_friend[0] = maxNum

    for i in range(1,total[0]+1):
        print(i,"个共同朋友的数量为：",total[i])

    #####下面求第二个时间段的快照，从而获得概率
    time_interval2 = MONTH_INTERVAL    #设置时间间隔2
    start_time2 = start_time + time_interval2   #开始时间2
    begin_line2 = 0
    ####筛选合适数据：
    print("获取下一个快照：")
    snapshot_u_v2 = getTimeData(time_interval2, u_v_t, start_time2, begin_line2)
    notFriend = np.array(notFriend)
    for u_v in snapshot_u_v2:
        if(u_v[0]>u_v[1]): u_v[0],u_v[1] = u_v[1],u_v[0]
        if(u_v[0] in notFriend[:, [0]] and u_v[1] in notFriend[:,[1]]):
            for not_friend in notFriend:
                if(u_v[0]==not_friend[0] and u_v[1] == not_friend[1]):
                    not_friend[3] = 1

    for not_friend in notFriend:
        if(not_friend[3] == 1):
            became_friend[not_friend[2]]+=1
    for i in range(1,became_friend[0]+1):
        print("有",i,"个共同朋友并成为朋友的数量为：",became_friend[i])

    #求概率
    print("求概率中：")
    x1 = []
    y1 = []
    for i in range(1, maxNum+1):
        x1.append(int(i))
        if(int(total[i]) == 0):
            y1.append(-1)
        else:
            y1.append(float(became_friend[i])/float(total[i]))
    print(x1)
    print(y1)
    total_x.append(x1)
    total_y.append(y1)


############输出结果############
print("x:")
num = 1
for i in total_x:
    print(num,"组数据x: ", i)
    num +=1
print("y:")
num = 1
for i in total_y:
    print(num, "组数据y: ", i)
    num += 1
