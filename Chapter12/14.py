# https://school.programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려 원형을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)

    answer = len(dist) + 1
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            # 시작점부터 모든 취약 지점 확인
            for index in range(start, start+length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer