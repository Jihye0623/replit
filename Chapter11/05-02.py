n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
  array[x] += 1

result = 0

for i in range(1, m+1):
  # 무게 i인 볼링공의 개수 제외 (A가 선택할 수 있는 개수)
  n -= array[i]
  # B가 선택하는 경우의 수와 곱기기
  result += array[i] * n


print(result)