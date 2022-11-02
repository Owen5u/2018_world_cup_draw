from itertools import permutations
from copy import deepcopy
import random

n = 6
result=[]
players= list(range(n))
match_matrix= [[-1 for i in range(n)] for i in range(2*n)] if n % 2 == 1 else [[-1 for i in range(n)] for i in range(2*(n-1))]     #奇数是2n偶数是2(n-1)
visited_matrix= [[False for i in range(n)] for i in range(n)]   # visited_matrix[a][b] returns true if player a and b have met before
# match_matrix[a][b] = c means in round a, player b plays home against player c.

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
    global match_matrix,n,result
    if level == n:
        result = deepcopy(match_matrix[:n]) if n%2 == 1 else deepcopy(match_matrix[:n-1])
        return
    
    for i in range(n):
        if i in empty:
            continue
        
        if n%2==1:
            players.remove(i)
        perm = list(permutations(players))
        random.shuffle(perm)
        for permutation in perm:
            # not finished yet!

            for ele in range(int(len(permutation)/2)):
                first, second = permutation[2*ele], permutation[2*ele+1]
                if visited_matrix[first][second]:
                    break
                match_matrix[level][first] = second
                visited_matrix[first][second] = True
                visited_matrix[second][first] = True
                if isValid(level+1) and level < n-1 :
                    empty.append(i)
                    if n%2==1:
                        players.append(i)
                    backtracking(level+1)
                    if n%2==1:
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
                match_matrix[level][first] = -1
                visited_matrix[first][second] = False
                visited_matrix[second][first] = False
            if len(result) != 0:
                return
        if n%2==1:
            players.append(i)


backtracking(0)
for i in range(n):
    cur = result[i]
    result.append([-1] * n)
    for j in range(n):
        if result[i][j] != -1:
            opponent = result[i][j]
            result[i+n][opponent] = j

print(match_matrix)

for i in range(len(result)):
    print("第",(i+1),"轮赛程 : ",end=" ")
    string = ""
    for j in range(n):
        if result[i][j] != -1:
            string += str(j+1)+" VS "+str(result[i][j]+1)+"  "
    print(string)
    


    
       




