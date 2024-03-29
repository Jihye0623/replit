array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array)+1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')

# 시간 복잡도 O(N+K)
# 데이터의 크기 범위가 제한되어 있는 정수 형태로 표현할 수 있을 때만 사용 가능