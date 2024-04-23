import itertools

n, m = map(int, input().split())
data = list(map(int, input().split()))

com = itertools.combinations(data, 2)

result = 0

for x, y in com:
  if x != y:
    result += 1

print(result)