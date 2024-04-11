n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
for i in range(0, len(data)):
  for j in range(i+1, len(data)):
    if data[i]!=data[j]:
      count+=1

print(count)