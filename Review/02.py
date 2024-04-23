s = input()

result = int(s[0])

if s[0] == '0':
  result = 1

for i in range(1,len(s)):
  data = int(s[i])
  if data == 1:
    result += data
  elif data != 0:
    result *= data

print(result)