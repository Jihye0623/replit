from itertools import combinations

n = int(input())
board = [] # 복도 정보
teachers = [] # 선생님 위치 정보
spaces = [] # 빈공간 정보

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    if board[i][j] == 'T':
      teachers.append((i,j))
    if board[i][j] == 'X':
      spaces.append((i,j))

def watch(x, y, direction):
  # 왼쪽 방향
  if direction == 0:
    while y>=0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      y -= 1
  # 오른쪽 방향
  if direction == 1:
    while y<n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      y += 1
  # 위쪽 방향
  if direction == 2:
    while x>=0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      x -= 1
  # 아래쪽 방향
  if direction == 3:
    while x<n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      x += 1
  return False

def process():
  for x, y in teachers:
    for i in range(4):
      if watch(x, y, i):
        return True
  return False

find = False
for data in combinations(spaces, 3):
  for x, y in data:
    board[x][y] = 'O'
  if not process():
    find = True
    break
  for x, y in data:
    board[x][y] = 'X'

if find:
  print('YES')
else:
  print('NO')