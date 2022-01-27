n = int(input())    
edge = input()      
edgelist = edge.split(",")  
adjlist = {}    
for edgei in edgelist:
    l = edgei.split("-")    
    x = int(l[0][1])
    y = int(l[1][1]) 
    if x in adjlist:
        adjlist[x].append(y) 
    else:
        adjlist[x] = [y]    
    if y in adjlist:    
        adjlist[y].append(x)    
    else:
        adjlist[y] = [x]


def bfs(adjlist,n,src): 
    from collections import deque
    q = deque()     
    visited = [False]*(n+1)     
    q.append(src)       
    while q:
        top = q.pop()      
        visited[top] = True     
        for v in adjlist[top]:
            if visited[v] == False:
                q.append(v)             
    
    if visited.count(True) == n:    
        return True     
    else:
        return False    
        
if bfs(adjlist,n,1) == True:    
    print("Connected")
else:
    print("Not Connected")
