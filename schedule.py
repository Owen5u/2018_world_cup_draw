import random
import copy
import sys
import datetime
from group_config import *

group = ['A','B','C']
map = ["台湾","中国大陆","日本","美国"]
start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2014, 1, 1)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

def schedule_helper_classification():
    random_days_list = [[""] * 2 for i in range(12)]
    random_number_list = [[""] * 2 for i in range(12)]
    random_map_list = [[""] * 2 for i in range(12)]
    
    for i in range(2):


        for j in range(3):

            game_list = [2*j,2*j+1,2*j+6,2*j+7]
            map_copy = map.copy()
            random.shuffle(map_copy)

            for r,k in enumerate(game_list):

                random_number_list[k][i] = random.randrange(days_between_dates)
                temp_day = (start_date+ datetime.timedelta(days=random_number_list[k][i]))
                y,m,d = str(temp_day.year),str(temp_day.month),str(temp_day.day)
                random_days_list[k][i] = y + "/" + m + "/" + d
                random_map_list[k][i] = map_copy[r]               
            
    for i in range(6):
        print("第",str((int)(i/2)+1),"轮第",(int)(i%2+1),"局:")
        string = ""
        for j in range(2):
            string += "第"+str(j+1)+"场: 地图: "+str(random_map_list[i][j])+" 开始时间: "+str(random_days_list[i][j])+" "
        print(string)

    for i in range(6):
        print("第",str((int)(i/2)+4),"轮第",(int)(i%2+1),"局:")
        string = ""
        for j in range(2):
            string += "第"+str(j+1)+"场: 地图: "+str(random_map_list[i+6][1-j])+" 开始时间: "+str(random_days_list[i+6][1-j])+" "
        print(string)
    
    # for i in range(6):
    #     for j in range(2):
    #         print("第",str(i+7),"轮第",str(j+1),"场: 地图: ",random_map_list[i+6][1-j]," 开始时间: ",random_days_list[i+6][1-j])  

schedule_helper_classification()  