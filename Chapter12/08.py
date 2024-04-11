data = input()
n = []
value = 0

for i in data:
  if i.isalpha():
    n.append(i)
  else:
    value += int(i)

n.sort()

for i in n:
  print(i, end='')

print(value)
