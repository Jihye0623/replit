import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적 있다면 무시
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
  if d != INF:
    count += 1
    max_distance = max(max_distance, d)

# 시작 노드는 제외해야 해서 count-1
print(count-1, max_distance)