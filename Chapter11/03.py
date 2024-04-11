n = input()

count = [0, 0]


for i in range(len(n)):
  num = int(n[i])
  if i!=0 and num == int(n[i-1]):
    continue
  count[num] += 1
  
print(min(count[0], count[1]))