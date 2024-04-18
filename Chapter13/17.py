from collections import deque

n, k = map(int, input().split())
graph = []  # 전체 보드 정보 담는 리스트
data = []  # 바이러스에 대한 정보 담는 리스트

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      # 바이러스 종류, 시간, 위치x, 위치y)
      data.append((graph[i][j], 0, i, j))

# 정렬 후 큐로 옮기기 - 낮은 번호의 바이러스가 먼저 증식하므
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
  virus, s, x, y = q.popleft()
  if s == target_s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = x + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])