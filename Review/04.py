n = int(input())
data = list(map(int, input().split()))
data.sort()

if data[0] != 1:
  print(1)
  exit()

result, j = 0, 0
for i in range(1, data[-1]):
  result += data[j]
  if i > result:
    break
  j=+1

print(result)