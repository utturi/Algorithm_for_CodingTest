import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split()) # N, M : 4~200
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)] # 미로의 정보(정수로 리스트에 저장)

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 미로 찾기 공간에 있는 경우 진행
            if new_x >= 0 and new_x < N and new_y >= 0 and new_y < M:
                # 괴물이 없고 처음 방문하는 곳이면 진행
                if arr[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                    visited[new_x][new_y] = visited[x][y] + 1 # depth를 구하는 식
                    queue.append((new_x, new_y))

    print(visited[N-1][M-1])

visited = [[0]*M for _ in range(N)] # 방문처리 2차원 리스트(각 노드의 depth를 저장)
bfs(0, 0, visited)