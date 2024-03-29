array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start>=end:  # 원소가 1개인 경우 종료
    return
  pivot = start
  left = start+1
  right = end
  while left<=right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left<=end and array[left]<=array[pivot]:
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while right>start and array[right]>=array[pivot]:
      right-=1
    if left>right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[right], array[left] = array[left], array[right]
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# 평균적인 시간복잡도 O(NlogN)
# 최악의 경우는 O(N^2) : 이미 데이터가 정렬되어 있는 경우