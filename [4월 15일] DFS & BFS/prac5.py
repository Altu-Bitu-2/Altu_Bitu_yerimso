# 선택과제 3: 2667 단지번호붙이기

import sys                         # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import deque      # collections 모듈의 deque 클래스 사용
input = sys.stdin.readline         # input변수에 문자열을 입력받음

"""
[단지 번호 붙이기] - bfs
- 단순 탐색
- (주의) 단지 내 집의 수를 "오름차순"으로 출력
- 이 풀이에서는 방문체크 배열을 따로 사용하지 않고, 처음 지도에 표기를 1 -> 0으로 바꾸어 중복으로 탐색하지 않도록 함
"""

def bfs(i, j, n, matrix):    # bfs 탐색
    dr = [-1, 1, 0, 0]       # 현재 구역에 인접한 구역의 상대적인 행 좌표
    dc = [0, 0, -1, 1]       # 현재 구역에 인접한 구역의 상대적인 열 좌표

    que = deque()            # 빈 큐 만들기
    que.append((i, j))       # 현재 구역의 좌표 큐에 넣기
    count = 1                # count 1로 초기화

    while que:                       # que가 비어있지 않을 동안 반복
        r, c = que.popleft()         # que의 가장 앞에 저장되어 있는 구역 pop
        for x in range(4):           # 현재 나라의 위, 아래, 왼쪽, 오른쪽 모두 확인
            new_r = r + dr[x]        # 인접한 나라의 row 좌표
            new_c = c + dc[x]        # 인접한 나라의 column 좌표
            # 새 좌표가 범위에 맞지 않거나, matrix에 0으로 표기되어 있으면 건너 뜀
            if not (0 <= new_r < n and 0 <= new_c < n) or not matrix[new_r][new_c]:
                continue             # 건너뛰기
            matrix[new_r][new_c] = 0        # 새 좌표 0으로 바꾸기
            que.append((new_r, new_c))      # 새 좌표 que에 추가하기
            count += 1                      # 단지수 + 1

    return count                            # count 리턴하기

# 입력
n = int(input())                                               # 지도의 크기 입력받기
matrix = [list(map(int, input().rstrip())) for _ in range(n)]  # N*N개의 자료 입력받기

apartment = []                                                 # 단지 수 저장할 리스트

for i in range(n):                                             # 모든 행 반복
    for j in range(n):                                         # 모든 열 반복
        if not matrix[i][j]:                                   # matrix[i][j]가 0이면
            continue                                           # 건너뛰기
        matrix[i][j] = 0                                       # matrix[i][j] 0으로 초기화
        apartment.append(bfs(i, j, n, matrix))                 # bfs 탐색

apartment.sort()                # 정렬

# 출력
print(len(apartment))           # 총 단지수 출력
print(*apartment, sep='\n')     # 각 단지내 집의 수 출력