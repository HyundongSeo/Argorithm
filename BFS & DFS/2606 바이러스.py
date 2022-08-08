n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)] # 경로를 저장하기 위한 2차원 리스트
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0 # 다녀간 점을 확인하기 위한 변수

visited = [0]*(n+1)

def dfs(V):
    global count
    visited[V] = 1
    for i in graph[V]:
        if visited[i]==0: # 들리지 않은 곳이면 dfs함수 반복
            dfs(i)
            count += 1

dfs(1)
print(count)