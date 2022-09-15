from itertools import permutations
import random
from copy import deepcopy
from turtle import back

# tier consists of some pairs (a,b), where a -> name and b-> group number, 0 means group A,
#  1 means B and 2 means C
tier1 = [("钱夫人",0),("莎拉公主",0)]
tier2 = [("宫本宝藏",2),("阿土伯",1)]
tier3 = [("沙隆巴斯",2),("孙小美",1)]
tier4 = [("金贝贝",0),("乌咪",2),("小丹尼",1),("糖糖",0)]
tiers = [tier1,tier2,tier3,tier4]

for i in range(4):
    random.shuffle(tiers[i])

group_d_cur = []
group_e_cur = []

group_d = []
group_e = []

group_d_participants = [0,0,0]
group_e_participants = [0,0,0]


flag = False

def valid_group():
    global group_d_participants,group_e_participants
    for i in range(3):
        if group_d_participants[i]>3 or group_e_participants[i] >3 or group_d_participants[i] <= 0 or group_e_participants[i] <= 0:
            return False
    return True




def backtracking(n):
    global group_d,group_e,group_d_cur,group_e_cur,group_d_participants,group_e_participants,flag
    if n==5:
        group_d = deepcopy(group_d_cur)
        group_e = deepcopy(group_e_cur)
        return
    if n<3:
        for x1,x2 in list(permutations(tiers[n])):
            group_d_cur.append(x1[0])
            group_d_participants[x1[1]] += 1
            group_e_cur.append(x2[0])
            group_e_participants[x2[1]] += 1
            backtracking(n+1)            
            group_d_cur.pop()
            group_e_cur.pop()
            group_d_participants[x1[1]] -= 1
            group_e_participants[x2[1]] -= 1

    else:
        perm = list(permutations(tier4))
        for x1,x2,x3,x4 in perm:
            group_d_participants[x1[1]] += 1
            group_d_participants[x2[1]] += 1
            group_e_participants[x3[1]] += 1
            group_e_participants[x4[1]] += 1
            if  valid_group():
                group_d_cur.append(x1[0])
                group_d_cur.append(x2[0])
                group_e_cur.append(x3[0])
                group_e_cur.append(x4[0])
                backtracking(5)
                group_d_cur.pop()
                group_d_cur.pop()
                group_e_cur.pop()
                group_e_cur.pop()
            group_d_participants[x1[1]] -= 1
            group_d_participants[x2[1]] -= 1
            group_e_participants[x3[1]] -= 1
            group_e_participants[x4[1]] -= 1
    return

backtracking(0)
random.shuffle(group_d)
random.shuffle(group_e)

print("D组: ")
print(*group_d,sep=',')
print("E组: ")
print(*group_e,sep=',')
