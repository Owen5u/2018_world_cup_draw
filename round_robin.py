from itertools import permutations
from copy import deepcopy
import random

n = 5
result=[]
players= list(range(n))
match_matrix= [[-1 for i in range(n)] for i in range(2*n)] if n % 2 == 1 else [[-1 for i in range(n)] for i in range(2*(n-1))]     #奇数是2n偶数是2(n-1)
visited_matrix= [[False for i in range(n)] for i in range(n)] 
# match_matrix[0][0] = 3
# match_matrix[0][1] = 4
# match_matrix[1][3] = 2
# match_matrix[1][1] = 0
# match_matrix[2][0] = 2
# match_matrix[2][4] = 3
# match_matrix[3][2] = 4
# match_matrix[3][3] = 1
# match_matrix[4][0] = 4
# match_matrix[4][1] = 2 

def duplicate():
    global match_matrix,n
    for i in range(n):
        for j in range(n):
            if match_matrix[i][j] != -1:
                opponent = match_matrix[i][j]
                match_matrix[i+5][opponent] = j

empty = []

def isValid(level):
    global match_matrix
    consecutive = [0,0,0,0,0]
    for i in range(level):
        for j in range(len(match_matrix[0])):
            if match_matrix[i][j] != -1:
                opponent = match_matrix[i][j]
                consecutive[j] = consecutive[j] + 1 if consecutive[j] >=0 else 1
                consecutive[opponent] = consecutive[opponent] - 1 if consecutive[opponent] <=0 else -1
                if consecutive[j] >=3 or consecutive[opponent] <= -3:
                    return False
        
    
    return True


# match_matrix = [[0,3,1,4,2],
#                 [3,2,1,0,4],
#                 [0,2,4,3,1],
#                 [2,4,3,1,0],
#                 [0,4,1,2,3],
#                 [4,1,3,0,2],
#                 [0,1,2,3,4],
#                 [3,4,2,0,1],
#                 [1,3,4,2,0],
#                 [2,1,4,0,3]
#                 ]




def backtracking(level):
    global match_matrix,n,result
    if level == n:
        result = deepcopy(match_matrix[:n])
        return
    
    for i in range(n):
        if i in empty:
            continue
        
        players.remove(i)
        perm = list(permutations(players))
        random.shuffle(perm)
        for m1,m2,m3,m4 in perm:
            if visited_matrix[m1][m2] or visited_matrix[m3][m4]:
                continue
            match_matrix[level][m1] = m2
            match_matrix[level][m3] = m4
            visited_matrix[m1][m2] = True
            visited_matrix[m2][m1] = True
            visited_matrix[m3][m4] = True
            visited_matrix[m4][m3] = True
            if isValid(level+1) and level < n-1 :
                empty.append(i)
                players.append(i)
                backtracking(level+1)
                players.remove(i)
                empty.pop()
            elif level ==n-1:
                duplicate()
                if isValid(2 * n):
                    empty.append(i)
                    players.append(i)
                    backtracking(level+1)
                    players.remove(i)
                    empty.pop()   
            match_matrix[level][m1] = -1
            match_matrix[level][m3] = -1
            visited_matrix[m1][m2] = False
            visited_matrix[m2][m1] = False
            visited_matrix[m3][m4] = False
            visited_matrix[m4][m3] = False
            if len(result) != 0:
                return
        players.append(i)


backtracking(0)
for i in range(n):
    cur = result[i]
    result.append([-1] * n)
    for j in range(n):
        if result[i][j] != -1:
            opponent = result[i][j]
            result[i+n][opponent] = j

for i in range(len(result)):
    print("第",(i+1),"轮赛程 : ",end=" ")
    string = ""
    for j in range(n):
        if result[i][j] != -1:
            string += str(j+1)+" VS "+str(result[i][j]+1)+"  "
    print(string)
    


    
       




