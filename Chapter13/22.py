# https://school.programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 반환 결과 ( 이동 가능한 위치들)
    pos = list(pos)  # 현재 위치 정보를 리스트로 변환 (집합 -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1],pos[1][0],pos[1][1]
    ## 상 하 좌 우 이동하는 경우 처리
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        pos1_nx, pos1_ny,pos2_nx,pos2_ny = pos1_x+dx[i], pos1_y+dy[i], pos2_x+dx[i], pos2_y+dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면, 
        if board[pos1_nx][pos1_ny] == 0 and board[pos2_nx][pos2_ny] == 0:
            next_pos.append({(pos1_nx, pos1_ny), (pos2_nx, pos2_ny)})

    ## 회전해서 이동하는 경우 처리         
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1,1]: # -1이면 아래칸 두칸이 빈 경우, +1이면 위칸 두칸이 빈 경우 
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # 비었으면
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})

    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1,1]: # -1이면 왼쪽 두칸이 빈 경우, +1이면 오른쪽 두칸이 빈 경우 
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i]==0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환 
    return next_pos 

def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]  # 테두리, 가로에 두칸이 늘고, 세로에 두칸이 늘어난다.
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]  # 두칸이 크니까 왼쪽에서 한칸만 떨어진곳에서 시작, 오른쪽에서 한칸 떨어진곳에서 끝난다.

    # BFS 수행
    q = deque()
    visited= []
    pos = {(1,1), (1,2)} # 시작 위치
    q.append((pos,0))  # 큐에 삽입한 후 
    visited.append(pos)  # 방문 처리 
    # 큐가 빌 때까지 반복
    while q :
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환 
        if (n,n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)                
    return 0      