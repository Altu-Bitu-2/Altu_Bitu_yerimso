# 선택과제 1: 10026: 적록색약

import sys                         # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import deque      # collections 모듈의 deque 클래스 사용

input = sys.stdin.readline         # input변수에 문자열을 입력받음

"""
[적록색약]
그림의 색을 기준으로 구역을 나누는 문제
1. 적록색약이 아닌 사람 기준으로 구역을 나눈다.
2. 그림의 초록을 모두 빨강으로 바꾼 후, 적록색약인 사람 기준으로 구역을 나눈다.
"""


def bfs(i, j, picture, visited):                  # bfs 탐색
    dr = [-1, 1, 0, 0]                            # 현재 구역에 인접한 구역의 상대적인 행 좌표
    dc = [0, 0, -1, 1]                            # 현재 구역에 인접한 구역의 상대적인 열 좌표

    que = deque()                                 # 빈 큐 만들기
    que.append((i, j))                            # 현재 구역의 좌표 큐에 넣기
    visited[i][j] = True                          # 현재 구역 방문함으로 표시

    while que:                                    # que가 비어있지 않을 동안 반복
        r, c = que.popleft()                      # que의 가장 앞에 저장되어 있는 구역 pop
        for x in range(4):                        # 현재 나라의 위, 아래, 왼쪽, 오른쪽 모두 확인
            new_r = r + dr[x]                     # 인접한 나라의 row 좌표
            new_c = c + dc[x]                     # 인접한 나라의 column 좌표
            # 새 좌표가 범위에 맞지 않거나, 이미 방문했으면 건너 뜀
            if not (0 <= new_r < n and 0 <= new_c < n) or visited[new_r][new_c]:
                continue                          # 다음 구역
            # 새 좌표의 구역과 기존 좌표의 구역의 색이 다르면
            if picture[new_r][new_c] != picture[r][c]:
                continue                          # 다음 구역
            visited[new_r][new_c] = True          # 새 좌표의 구역과 기존 좌표의 구역의 색이 같으면 true로 표시
            que.append((new_r, new_c))            # que에 인접한 구역의 좌표 넣기

    return                                        # 함수 리턴


def count_area(n, picture):                             # 구역의 개수를 구하는 함수
    visited = [[False] * n for _ in range(n)]           # 방문한 구역 리스트
    area = 0                                            # 구역의 개수 0으로 초기화

    for i in range(n):                                  # 모든 행 반복
        for j in range(n):                              # 모든 열 반복
            if visited[i][j]:                           # 만약 방문한 구역이라면
                continue                                # 다음 구역

            area += 1                                   # 구역의 개수 + 1
            bfs(i, j, picture, visited)                 # bfs 탐색

    return area                                         # 구역의 수 출력하기


def green_to_red(n, picture):                           # 그림의 초록을 모두 빨강으로 바꾸는 함수
    for i in range(n):                                  # 모든 행 반복
        for j in range(n):                              # 모든 열 반복
            if picture[i][j] == 'G':                    # 만약 구역이 초록이라면
                picture[i][j] = 'R'                     # 빨강으로 바꾸기

    return picture                                      # 바뀐 그림 리턴하기


# 입력
n = int(input())                                        # N 입력받기
picture = [list(input().rstrip()) for _ in range(n)]    # 그림 입력받기
ans = []                                                # 빈 list 생성

ans.append(count_area(n, picture))                      # 적록색약이 아닌 사람이 봤을 때 구역의 개수 출력
picture = green_to_red(n, picture)                      # 적록색약인 사람이 본 그림으로 바꾸기
ans.append(count_area(n, picture))                      # 적록색약인 사람이 봤을 때 구역의 개수 출력

print(*ans)                                             # 구역의 수 출력