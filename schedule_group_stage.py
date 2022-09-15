import random
import copy
import sys
import datetime
from group_config import *


group = ['D','E']
map = ["台湾","中国大陆","日本","美国"]
start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2014, 1, 1)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

def schedule_helper_group_stage():
    random_days_list = [[""] * 2 for i in range(10)]
    random_number_list = [[""] * 2 for i in range(10)]
    random_map_list = [[""] * 2 for i in range(10)]
    
    for i in range(2):


        for j in range(5):

            game_list = [j,j+5]
            index = [i,1-i]
            game_maps = random.sample(map,2)

            for r,k in enumerate(game_list):
                cur = index[r]
                random_number_list[k][cur] = random.randrange(days_between_dates)
                temp_day = (start_date+ datetime.timedelta(days=random_number_list[k][cur]))
                y,m,d = str(temp_day.year),str(temp_day.month),str(temp_day.day)
                random_days_list[k][cur] = y + "/" + m + "/" + d
                random_map_list[k][cur] = game_maps[r]               
            
    for i in range(10):
        string = ""
        for j in range(2):
            string += "第"+str(i+1)+"轮第"+str(j+1)+"场: 地图: "+str(random_map_list[i][j])+" 开始时间: "+str(random_days_list[i][j])+" "
        print(string)




     

schedule_helper_group_stage()  