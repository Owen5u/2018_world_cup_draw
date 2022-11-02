from itertools import permutations
from copy import deepcopy
import random

n = 5
result=[]
players= list(range(n))
rounds = n-1 if n%2==0 else n
match_matrix= [[-1 for i in range(n)] for i in range(2*rounds)] 
visited_matrix= [[False for i in range(n)] for i in range(n)]   # visited_matrix[a][b] returns true if player a and b have met before
# match_matrix[a][b] = c means in round a, player b plays home against player c.

def duplicate():
    global match_matrix,rounds,n
    for i in range(rounds):
        for j in range(n):
            if match_matrix[i][j] != -1:
                opponent = match_matrix[i][j]
                match_matrix[i+rounds][opponent] = j

empty = []


def isValid(level):
    global match_matrix
    consecutive = [0 for i in range(n)]
    for i in range(level):
        for j in range(len(match_matrix[0])):
            if match_matrix[i][j] != -1:
                opponent = match_matrix[i][j]
                consecutive[j] = consecutive[j] + 1 if consecutive[j] >=0 else 1
                consecutive[opponent] = consecutive[opponent] - 1 if consecutive[opponent] <=0 else -1
                if consecutive[j] >=3 or consecutive[opponent] <= -3:
                    return False
        
    
    return True


def backtracking(level):
    global match_matrix,rounds,result,n
    if level == rounds:
        result = deepcopy(match_matrix[:rounds])
        return
    
    for i in range(n):
        if i in empty:
            continue
        
        if n%2==1:
            players.remove(i)
        perm = list(permutations(players))
        random.shuffle(perm)
        for permutation in perm:
            isValidFlag = True
            for ele in range(int(len(permutation)/2)):
                first, second = permutation[2*ele], permutation[2*ele+1]
                if visited_matrix[first][second]:
                    isValidFlag = False
                    break
            if not isValidFlag:
                continue
            for ele in range(int(len(permutation)/2)):
                first, second = permutation[2*ele], permutation[2*ele+1]
                match_matrix[level][first] = second
                visited_matrix[first][second] = True
                visited_matrix[second][first] = True
            if isValid(level+1) and level < rounds-1 :
                if n%2==1:
                    empty.append(i)
                    players.append(i)
                backtracking(level+1)
                if n%2==1:
                    players.pop()
                    empty.pop()
            elif level ==rounds-1:
                duplicate()
                if isValid(2 * rounds):
                    if n%2==1:
                        empty.append(i)
                        players.append(i)
                    backtracking(level+1)
                    if n%2==1:
                        players.pop()
                        empty.pop()   
            for ele in range(int(len(permutation)/2)):
                first, second = permutation[2*ele], permutation[2*ele+1]
                match_matrix[level][first] = -1
                visited_matrix[first][second] = False
                visited_matrix[second][first] = False
        if len(result) != 0:
            return
        if n%2==1:
            players.append(i)


backtracking(0)
for i in range(rounds):
    cur = result[i]
    result.append([-1] * n)
    for j in range(n):
        if result[i][j] != -1:
            opponent = result[i][j]
            result[i+rounds][opponent] = j

print(match_matrix)

for i in range(len(result)):
    print("第",(i+1),"轮赛程 : ",end=" ")
    string = ""
    for j in range(n):
        if result[i][j] != -1:
            string += str(j+1)+" VS "+str(result[i][j]+1)+"  "
    print(string)
    


    
       




