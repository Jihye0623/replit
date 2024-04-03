import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호 
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))


# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n+1):
    if distance[i]<min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  # 시작 노드를 제외한 n-1개에 대해 반복
  for i in range(n-1):
    now = get_smallest_node()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])