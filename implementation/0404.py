n, m = map(int, input().split())
d = [[0]*m for _ in range(n)]

# 방문 위치를 저장하기 위해 맵을 생성하여 0으로 초기화
x,y,direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보 입력 받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  # 회전한 칸이 가보지 않은 칸이면
  if(d[nx][ny] == 0 and array[nx][ny] == 0):
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue

  # 회전한 칸이 가보았거나, 바다인 경우
  else:
    turn_time +=1

  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = x - dy[direction]

    # 뒤로 갈 수 있다면
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0


print(count)