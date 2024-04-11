s = input()
result = 0

if int(s[0])!=0:
  result = int(s[0])
elif int(s[0])==1:
  result = 0
else:
  result = 1

for i in range(1, len(s)):
  num = int(s[i])
  if num!=0 or num!=1:
    result = result*num
  if num==1:
    result = result + 1
    
print(result)