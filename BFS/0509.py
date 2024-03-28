from collections import deque

def bfs(graph, start, visited):
  #큐 구현
  queue = deque([start])
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
    

graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# index가 1부터 시작하여서 9개 (0은 무시)
visited = [False] * 9
bfs(graph, 1, visited)