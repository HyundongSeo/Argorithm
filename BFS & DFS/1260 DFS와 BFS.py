N, M, V = map(int, input().split()) # 입력변수 받기

matrix=[[0] * (N + 1) for i in range(N + 1)] # 영행렬 생성

visited = [0] * (N + 1) # 방문한 곳 체크를 위한 배열

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1 # 입력 받는 두 값에 대해 영행렬에 1 넣기

def dfs(V):
    visited[V] = 1 # 방문한 곳은 1 넣기
    print(V, end=' ')
    # 재귀함수 선언=v와 인접한 곳을 찾고 방문 안했으면 함수 실행
    for i in range(1,N+1):
        if(visited[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue = [V] # 방문해야 할 곳 큐 생성
    visited[V] = 0 # dfs를 완료한뒤 visited 배열 1->0으로 방문 체크
    # 큐 안에 데이터가 없을 때까지
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visited[i] == 1 and matrix[V][i]==1):
                queue.append(i)
                visited[i] = 0

dfs(V)
print()
bfs(V)