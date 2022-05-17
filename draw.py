#!/usr/bin/python

import random
import copy
import sys
import datetime
from group_config import *
#fifa 2017 October ranking: https://www.fifa.com/fifa-world-ranking/ranking-table/men/rank/id11976/
# pot = [[['Russia', 0, 65], ['Germany', 0, 1], ['Brazil', 2, 2], ['Portugal', 0, 3], ['Argentina', 2, 4], ['Belgium', 0, 5], ['Poland', 0, 6], ['France', 0, 7]],
# [['Spain', 0, 8], ['Peru', 2, 10], ['Switzerland', 0, 11], ['England', 0, 12], ['Colombia', 2, 13], ['Mexico', 4, 16], ['Uruguay', 2, 17], ['Croatia', 0, 18]],
# [['Denmark', 0, 19], ['Iceland', 0, 21], ['Costa Rica', 4, 22], ['Sweden', 0, 25], ['Tunisia', 3, 28], ['Egypt', 3, 30], ['Senegal', 3, 32], ['Iran', 1, 34]],
# [['Serbia', 0, 38], ['Nigeria', 3, 41], ['Australia', 1, 43], ['Japan', 1, 44], ['Morocco', 3, 48], ['Panama', 4, 49], ['South Korea', 1, 62], ['Saudi Arabia', 1, 63]]]

pot = [[['Russia',0,65],['Germany', 0, 1], ['Brazil', 2, 2], ['Portugal', 0, 3], ['Argentina', 2, 4], ['Belgium', 0, 5], ['Poland', 0, 6], ['France',0,7]],
[['Spain', 0, 8],['Peru', 2, 10],['England', 0, 12], ['Colombia', 2, 13], ['Wales', 0, 14],['Italy', 0, 15],['Mexico', 4, 16], ['Uruguay', 2, 17]],
[['Netherlands',0,20],['Costa Rica', 4, 22],['Republic of Ireland',0,26],['USA', 4, 27],['Ukraine',0,30],['Senegal', 3, 32], ['Iran', 1, 34],['Congo DR',3,35]],
[['Nigeria', 3, 41],['Australia', 1, 43],['Japan', 1, 44],['Czech Republic',0,46],['Morocco', 3, 48],['South Korea', 1, 62], ['Algeria',3,67],['Honduras',4,69] ]]

beginner = [['乌咪',0],['孙小美',0],['糖糖',0]]
middle = [['阿土伯',1],['小丹尼',1],['沙隆巴斯',1],['宫本宝藏',1],['莎拉公主',1]]
upper = [['钱夫人',2],['忍太郎',2],['约翰乔',2],['金贝贝',2]]

# class_tier_1 = [['金贝贝',2],['莎拉公主',1],['阿土伯',1],['约翰乔',2]]
# class_tier_2 = [['宫本宝藏',1],['忍太郎',2],['沙隆巴斯',1],['钱夫人',2]]
# class_tier_3 = [['小丹尼',1],['孙小美',3],['糖糖',3],['乌咪',3]]




first = [['约翰乔','A'],['小丹尼','B'],['莎拉公主','C'],['忍太郎','A']]
runner_up = [['沙隆巴斯','B'],['孙小美','C'],['宫本宝藏','B'],['金贝贝','A']]
last = [['乌咪','C'],['钱夫人','A'],['阿土伯','B'],['糖糖','C']]

class_tier_1 = [['沙隆巴斯','B'],['小丹尼','B'],['莎拉公主','C'],['钱夫人','A']]
class_tier_2 = [['金贝贝','A'],['孙小美','C'],['乌咪','C'],['忍太郎','A']]
class_tier_3 = [['糖糖','C'],['阿土伯','B'],['宫本宝藏','B'],['约翰乔','A']]


# tier_1 = [['钱夫人','A'],['沙隆巴斯','B'],['金贝贝','A']]
# tier_2 = [['孙小美','C'],['小丹尼','B'],['忍太郎','A']]
# tier_3 = [['莎拉公主','C'],['阿土伯','B'],['约翰乔','A']]
# tier_4 = [['宫本宝藏','B'],['糖糖','C'],['乌咪','C']]

tier_1 = [['约翰乔','A',2],['宫本宝藏','B',1],['莎拉公主','C',0]]
tier_2 = [['金贝贝','A',3],['乌咪','C',1],['钱夫人','A',0]]
tier_3 = [['小丹尼','B',3],['沙隆巴斯','B',2],['孙小美','C',2]]
tier_4 = [['忍太郎','A',3],['糖糖','C',0],['阿土伯','B',1]]


# group_e = ["莎拉公主","金贝贝","宫本宝藏"]
# group_e = ["忍太郎","阿土伯","钱夫人"]
# group_f = ["约翰乔","沙隆巴斯",""]
# group_runner_ups = ["沙隆巴斯","金贝贝","阿土伯"] 

group_e = ["乌咪","沙隆巴斯",""]
group_f = ["金贝贝","孙小美","忍太郎"]
group_g = ["莎拉公主","小丹尼","钱夫人"]
group_runner_ups = ["沙隆巴斯","小丹尼","孙小美"] 

map = ["台湾","中国大陆","日本","美国"]

group_a = ["西班牙","塞尔维亚"]
group_b = ["美国","日本","法国"]
group_c = ["中国","比利时","澳大利亚"]

olympic_groups = [group_a,group_b,group_c]
best_runner_up = "比利时"


start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2014, 1, 1)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days



#  Select dfw teams
 
def dfw_team_select(result,pot,group_num,flag):
    back_up = copy.deepcopy(result)
    temp = copy.deepcopy(pot)
    random.shuffle(temp)
    for index in range(0,group_num):
        get_flag = False
        for key,nation in enumerate(temp):
            if (flag and result[index].valid_check_ver_2(nation) ) or ( not flag and result[index].valid_check(nation) ):
                result[index].member_update(nation,flag)
                result[index].nations.append(nation[0])
                temp.pop(key)
                get_flag = True
                break
        if not get_flag:
            result = copy.deepcopy(back_up)
            result = dfw_team_select(result,pot,group_num,flag)
            break
    for group in result:
        random.shuffle(group.nations)
    return result


def print_pots(pot,m):
        if m> len(pot):
            return 'Error!'
        cur_pot = pot[m]
        string = ""
        string += "第 "+str(m+1)+" 档 : "
        for i in cur_pot:
            string += i[0] + ","
        string = string[:-1]
        print(string)


def dfw_r2_draw():
    #dfw_pot = [first,runner_up,last]
    dfw_pot = [tier_1,tier_2,tier_3,tier_4]
    for i in range(4):
        print_pots(dfw_pot,i)
    result = []
    for i in range(0,3):
        result.append(dfw_group(i))
    
    for item in dfw_pot:
        result = dfw_team_select(result,item,3,True)

    for item in result:
        print (str(item.id) + " : " + str(item.nations))

def dfw_classification_draw():
    dfw_pot = [class_tier_1.copy(),class_tier_2.copy(),class_tier_3.copy()]
    for i in range(3):
        print_pots(dfw_pot,i)
    result = []
    for i in range(0,4):
        result.append(dfw_group(i))
    for item in dfw_pot:
        result = dfw_team_select(result,item,4,False)


    for item in result:
        string = ""
        for nation in (item.nations):
            string += nation + ","
        string = string[:-1]
        print (str(item.id) + "组 : " + string)
    # for i in range(4):
    #     print(chr(65+i),"组赛程：")
    #     schedule_helper(6)

def dfw_classification_schedule():
    schedule_helper(4,False)
    first = random.randrange(2) + 1
    first_rem = 3- first
    second = random.randrange(2) + 3
    second_rem = 7-second
    print("先手轮: ",first,second)
    print("后手轮: ",first_rem,second_rem)

def dfw_classification_tiebreaker_schedule():
    schedule_helper(1,False)
    
# def dfw_group_stage_schedule():
#     for i in ['E','F','G']:
#         print(i,"组赛程:")
#         schedule_helper(6,False)



# def dfw_group_stage_schedule():
    
#     random_number_of_days = random.randrange(days_between_dates)

#     random_number_of_days_two = random.randrange(days_between_dates)

#     random_date = start_date + datetime.timedelta(days=random_number_of_days)

#     random_date_two = start_date + datetime.timedelta(days=random_number_of_days_two)



#     map2 = map.copy()

#     random.shuffle(map2)

#     order = "先手" if random.randint(0,1) == 0 else "后手"

#     print("小组赛开始日期：1.",random_date," 2.",random_date_two)
#     print("选择地图: 1.",map2[0]," 2.",map2[1])
#     print("先后顺序: ",order)

def dfw_group_stage():
    t1 = ["小丹尼","约翰乔"]
    t2=["钱夫人","忍太郎"]
    t3=["阿土伯","莎拉公主"]
    t4= ["孙小美","乌咪","宫本宝藏","糖糖"]

    group_e = []
    group_f = []

    r1 = random.randrange(2)
    r2 = random.randrange(2)
    r3 = random.randrange(2)
    r4 = random.sample(t4,k=2)

    group_e.append(t1[r1])
    group_f.append(t1[1-r1])
    group_e.append(t2[r2])
    group_f.append(t2[1-r2])
    group_e.append(t3[r3])
    group_f.append(t3[1-r3])
    for ele in r4:
        group_e.append(ele)
    for ele in [x for x in t4 if x not in r4]:
        group_f.append(ele)
    random.shuffle(group_e)
    random.shuffle(group_f)

    
    string = ","
    string = string.join(group_e)
    print ("E组 : " + string)

    string = ","
    string = string.join(group_f)
    print ("F组 : " + string)

def dfw_group_stage_schedule():
    schedule_helper(2,False)
    first = random.randrange(2) + 1
    first_rem = 3- first
    print("先手轮: ",first)
    print("后手轮: ",first_rem)
    

def dfw_knockout_draw():


    r = random.randrange(6)
    if r ==0:
        pivot = group_e
        pivot_next = group_f
        pivot_prev = group_g
    elif r==1:
        pivot = group_f
        pivot_next = group_g
        pivot_prev = group_e
    elif r==2:
        pivot = group_g
        pivot_next = group_e
        pivot_prev = group_f
    elif r==3:
        pivot = group_e
        pivot_next = group_g
        pivot_prev = group_f
    elif r==4:
        pivot = group_g
        pivot_next = group_f
        pivot_prev = group_e
    else:
        pivot = group_f
        pivot_next = group_e
        pivot_prev = group_g
    

    possible_rivalry_dict={pivot[0]:[pivot_next[2],pivot_prev[2]], pivot_next[0]:pivot_prev[1],pivot_prev[0]:[pivot[2],pivot_next[2]]}
    
    if group_runner_ups.index(pivot[1]) < group_runner_ups.index(pivot_next[1]):
        possible_rivalry_dict[pivot[1]] = pivot_next[1]
    else:
        possible_rivalry_dict[pivot_next[1]] = pivot[1]
    
    

    only_choice = ""
    
    for k in possible_rivalry_dict.keys():
        if isinstance(possible_rivalry_dict[k],list) and "" in possible_rivalry_dict[k]:

            possible_rivalry_dict[k].remove("")
            only_choice = ''.join(possible_rivalry_dict[k])
            possible_rivalry_dict[k] = only_choice
    
    for k in possible_rivalry_dict.keys():
        if isinstance(possible_rivalry_dict[k],list) and only_choice in possible_rivalry_dict[k]:
            possible_rivalry_dict[k].remove(only_choice)
            the_other_only_choice = ''.join(possible_rivalry_dict[k])
            possible_rivalry_dict[k] = the_other_only_choice

    knockout_list = []
    for key,value in possible_rivalry_dict.items():
        knockout_list.append([key,value])
    
    random.shuffle(knockout_list)
    print("抽签顺序: ",str(r+1))
    print("对阵情况如下：")
    for i in range(len(knockout_list)):
        print("第",str(i+1),"场对决: ",knockout_list[i][0]," VS ",knockout_list[i][1])
       


def schedule_helper(round,extra_round_flag = True):
    round += 1 if extra_round_flag else 0
    random_days_list = [""] * round
    random_number_list = [""] * round
    for i in range(round):
        random_number_list[i] = random.randrange(days_between_dates)
        random_days_list[i] = (start_date+ datetime.timedelta(days=random_number_list[i]))
        y,m,d = str(random_days_list[i].year),str(random_days_list[i].month),str(random_days_list[i].day)
        random_days_list[i] = y + "/" + m + "/" + d

    map_copy = map.copy()
    random.shuffle(map_copy)
    for i in range(int(round/4)) :
        map_copy2 = map.copy()
        random.shuffle(map_copy2)
        map_copy += map_copy2
    for i in range(round):
        print("第",str(i+1),"轮: 地图: ",map_copy[i]," 开始时间: ",random_days_list[i])
    if extra_round_flag:
        print("附加轮 地图: ",map_copy[round]," 开始时间: ",random_days_list[round])  





def dfw_BO5():
    schedule_helper(5,False)


def dfw_BO3():
    schedule_helper(3,False)


# def dfw_classification_final_round_schedule():
#     group_winners = ["A1","B1","C1","D1"]
#     random.shuffle(group_winners)
#     print("排位赛决赛轮开始顺序： ")
#     for i in group_winners:
#         print(i)
#     schedule_helper(4)

def olympic_knockout_stage_draw():
    upper_half = [i[0] for i in olympic_groups]
    remaining_runner_ups = [i[1] for i in olympic_groups if i[1] != best_runner_up]
    lower_half = remaining_runner_ups+ [i[2] for i in olympic_groups if len(i)==3]
    upper_half.append(best_runner_up)
    random.shuffle(upper_half)
    random.shuffle(lower_half)

    best_runner_up_opponent = remaining_runner_ups[random.randint(0,1)]
    vs_table = [[best_runner_up,best_runner_up_opponent]]
    vs_table_temp=[]
    upper_half.remove(best_runner_up)
    lower_half.remove(best_runner_up_opponent)
    lower_half_copy = lower_half.copy()

    backtracking(vs_table_temp,upper_half,lower_half,lower_half_copy,0,0)
    for i in vs_table_temp:
        vs_table.append([upper_half[i[0]],lower_half[i[1]]])
    random.shuffle(vs_table)
    print(vs_table)


    # return

def check_availibility(list,a,b):
    if b not in list:
        return False
    for i in olympic_groups:
        if a in i and b in i:
            return False
    return True


def backtracking(table,list_a,list_b,list_b_copy,index_a,index_b):
    if index_a >= len(list_a):
        return

    if index_b >= len(list_b):
        last = table[-1]
        table.remove(last)
        list_b_copy.append(list_b[last[1]])
        backtracking(table,list_a,list_b,list_b_copy,last[0],last[1]+1)
        return
        

    if not check_availibility(list_b_copy,list_a[index_a],list_b[index_b]):
        backtracking(table,list_a,list_b,list_b_copy,index_a,index_b+1)
        return
    
    table.append([index_a,index_b])
    list_b_copy.remove(list_b[index_b])
    backtracking(table,list_a,list_b,list_b_copy,index_a+1,0)
    
    return



# def testing():
#     A=["中国","西班牙","美国"]
#     B=["塞尔维亚","澳大利亚","法国"]
#     B_copy= B.copy()
#     table=[]
#     backtracking(table,A,B,B_copy,0,0)

#     print("Final table :",table)




if __name__ == "__main__":
    while(1):
        try:
            input_val = input("请选择你想要的功能: 1. 大富翁排位赛分组 2.大富翁排位赛赛程 3.大富翁排位赛附加赛赛程 4.大富翁小组赛分组 5.大富翁小组赛赛程 6.大富翁淘汰赛抽签 7. BO5赛程 8.BO3赛程 0.退出\n")
            if input_val=="1":
                dfw_classification_draw()
            elif input_val=="2":
                dfw_classification_schedule()
            elif input_val=="3":
                dfw_classification_tiebreaker_schedule()
            elif input_val=="4":
                dfw_group_stage()
            elif input_val =="5":
                dfw_group_stage_schedule()
            elif input_val =="6":
                dfw_knockout_draw()
            elif input_val =="7":
                dfw_BO5()
            elif input_val =="8":
                dfw_BO3()
            elif input_val =="0":
                exit()
            elif input_val =="10":
                olympic_knockout_stage_draw()
            else:
                print("请重新输入!")
        except Exception:
            print("")