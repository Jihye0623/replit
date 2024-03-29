array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 첫번째 데이터는 그 자체로 정렬되어 있다 판단하여 1부터 시작
for i in range(1, len(array)):
  for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
    if array[j]<array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break
    
print(array)

# 시간 복잡도 O(N^2) => 그러나 이미 정렬된 상태라면 매우 빠르게 동작