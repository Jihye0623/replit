S = input()

data = [0,0]

for i in range(len(S)):
  if i!=0 and S[i-1] != S[i]:
    if S[i] == '0':
      data[0] += 1
    else:
      data[1] += 1

print(min(data[0], data[1]))