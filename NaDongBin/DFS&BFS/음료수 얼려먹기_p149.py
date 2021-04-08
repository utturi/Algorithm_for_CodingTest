import sys

N, M = map(int, sys.stdin.readline().split()) # N, M : 1~1,000
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)] # 2차원 리스트로 받기(문자열로 받아서 int형으로 저장)

def dfs(row, col, visited):
    # 범위가 벗어나면 dfs 종료
    if row < 0 or row >= N or col < 0 or col >= M: 
        return False

    if arr[row][col] == 0 and visited[row][col] == False:
        visited[row][col] = True # 방문한 노드 처리
        # 상하좌우 탐색
        dfs(row-1, col, visited)
        dfs(row+1, col, visited)
        dfs(row, col-1, visited)
        dfs(row, col+1, visited)
        return True
    
    return False

visited = [[False]*M for _ in range(N)] # 방문처리 리스트(N x M)
result = 0 # 얼릴 수 있는 구역 개수
for x in range(N):
    for y in range(M):
        if arr[x][y] == 0 and not visited[x][y]:
            if dfs(x, y, visited) == True:
                result += 1

print(result)