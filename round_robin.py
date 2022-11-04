from itertools import permutations
from copy import deepcopy
import random

n = 5  # number of players
result=[]   # list of valid schedules
players= list(range(n))
rounds = n-1 if n%2==0 else n
match_matrix= [[-1 for i in range(n)] for i in range(2*rounds)] 
visited_matrix= [[False for i in range(n)] for i in range(n)]   

# visited_matrix[a][b] returns true if player a and b have met before
# match_matrix[a][b] = c means in round a, player b plays home against player c.

# def fillLine():
#     global match_matrix,rounds
#     for i in range(n):
#             if match_matrix[0][i] != -1:
#                 opponent = match_matrix[0][i]
#                 match_matrix[rounds][opponent] = i
#     return


def duplicate():
    global match_matrix,rounds,n
    for i in range(rounds):
        for j in range(n):
            match_matrix[i+rounds][j] = -1
    for i in range(rounds):
        for j in range(n):
            if match_matrix[i][j] != -1:
                opponent = match_matrix[i][j]
                match_matrix[i+rounds][opponent] = j
 
bye = [] #轮空


def isValid(level):
    global match_matrix,n
    consecutive = [0 for i in range(n)]
    for i in range(level+1):
        for j in range(len(match_matrix[0])):
            if match_matrix[i][j] != -1:
                opponent = match_matrix[i][j]
                consecutive[j] = consecutive[j] + 1 if consecutive[j] >=0 else 1
                consecutive[opponent] = consecutive[opponent] - 1 if consecutive[opponent] <=0 else -1
                if consecutive[j] >=3 or consecutive[opponent] <= -3:
                    return False
        
    
    return True


def backtracking(level):
    global old_players,bye,match_matrix,rounds,result,n,players
    if level == rounds:
        result = deepcopy(match_matrix[:rounds])
        return
    
    for i in range(n):
        first_player = old_players[i]
        if first_player in bye:
            continue
        
        players.remove(first_player)
        perm = list(permutations(players))
        random.shuffle(perm)
        for permutation in perm:
            isValidFlag = True
            for ele in range(int(len(permutation)/2)):
                first, second = permutation[2*ele], permutation[2*ele+1]
                if visited_matrix[first][second]:
                    isValidFlag = False
                    break
            if n%2==0 and visited_matrix[first_player][permutation[-1]]:
                continue
            if not isValidFlag:
                continue
            for ele in range(int(len(permutation)/2)):
                first, second = permutation[2*ele], permutation[2*ele+1]
                match_matrix[level][first] = second
                visited_matrix[first][second] = True
                visited_matrix[second][first] = True
            if n%2==0:
                match_matrix[level][first_player] = permutation[-1]
                visited_matrix[first_player][permutation[-1]] = True
                visited_matrix[permutation[-1]][first_player] = True
            if level < rounds-1 and isValid(level) :
                if n%2==1:
                    bye.append(first_player)
                players.append(first_player)
                backtracking(level+1)
                players.remove(first_player)
                if n%2==1:
                    bye.pop()
            elif level ==rounds-1:
                duplicate()
                if isValid(2*rounds-1):
                    if n%2==1:
                        bye.append(first_player)
                    players.append(first_player)
                    backtracking(level+1)
                    players.remove(first_player)
                    if n%2==1:
                        bye.pop()   
            for ele in range(int(len(permutation)/2)):
                first, second = permutation[2*ele], permutation[2*ele+1]
                match_matrix[level][first] = -1
                visited_matrix[first][second] = False
                visited_matrix[second][first] = False
            if len(result) != 0:
                return
        players.append(first_player)

random.shuffle(players)
old_players = deepcopy(players)
backtracking(0)
for i in range(rounds):
    cur = result[i]
    result.append([-1] * n)
    for j in range(n):
        if result[i][j] != -1:
            opponent = result[i][j]
            result[i+rounds][opponent] = j



for i in range(len(result)):
    print("第",(i+1),"轮赛程 : ",end=" ")
    string = ""
    for j in range(n):
        if result[i][j] != -1:
            string += str(j+1)+" VS "+str(result[i][j]+1)+"  "
    print(string)
    


    
       




