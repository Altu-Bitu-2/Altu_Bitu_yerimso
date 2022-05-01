# 필수과제 1: 16234 인구 이동

import sys                          # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import deque       # collections 모듈의 deque 클래스 사용

input = sys.stdin.readline          # input변수에 문자열을 입력받음

"""
[인구이동]
0. 인구이동이 일어날 수 있는 나라(처음에는 모든 나라)의 좌표를 좌표 큐에 저장
1. bfs 탐색을 통해 연합을 확인하고, 연합에 포함된 나라의 인구이동을 진행한다.
2. 인구 이동이 있었던 나라는 다음 날에도 인구이동이 시작될 수 있으므로 좌표 큐에 다시 넣어준다.
    -> 직전 이동이 있었던 나라에 대해서만 bfs 탐색 진행
    - 인구 이동이 일어나지 않은 두 나라 사이에서는 다음 날에도 인구이동이 일어날 수 없음
3. 인구이동이 전혀 일어나지 않을 때까지 반복
"""


def bfs(n, left, right, i, j, day):            # 연합을 할 수 있는지 확인하는 함수
    dr = [-1, 1, 0, 0]                         # 현재 나라에 인접한 나라의 상대적인 행 좌표
    dc = [0, 0, -1, 1]                         # 현재 나라에 인접한 나라의 상대적인 열 좌표

    que = deque()                              # 빈 큐 만들기
    que.append((i, j))                         # 현재 나라의 좌표 큐에 넣기
    total = 0                                  # 연합의 인구 수 합계
    count = 0                                  # 연합에 포함된 나라의 수
    cord = []                                  # 연합에 포함된 나라의 좌표

    while que:                                 # que가 비어있지 않을 동안 반복
        r, c = que.popleft()                   # que의 가장 앞에 저장되어 있는 나라 pop
        count += 1                             # 연합에 포함된 나라의 수 + 1
        total += board[r][c]                   # 연합의 인구 수 + (r, c) 나라의 인구 수
        cord.append((r, c))                    # 연합에 포함된 나라의 좌표 + (r, c)

        for x in range(4):                     # 현재 나라의 위, 아래, 왼쪽, 오른쪽 모두 확인
            new_r = r + dr[x]                  # 인접한 나라의 row 좌표
            new_c = c + dc[x]                  # 인접한 나라의 column 좌표
            if not (0 <= new_r < n and 0 <= new_c < n) or visited[new_r][new_c] == day:
                # 만약 인접한 나라의 row, column 좌표가 땅을 벗어나거나 이미 방문했던 나라라면
                continue                       # 다음 나라 검색

            # 이 때 여기서 visited에 표기를 하면 안됨
            # 현재는 조건에 맞지 않지만, 이후에 연합에 있는 다른 나라에 의해 연합에 들어올 수 있음

            if left <= abs(board[new_r][new_c] - board[r][c]) <= right:     # 두 나라의 인구차이가 L명 이상, R명 이하라면
                que.append((new_r, new_c))     # que에 인접한 나라의 좌표 넣기
                visited[new_r][new_c] = day    # 이미 방문함으로 표시

    # 적어도 나라 2개 이상이 모여야 연합을 이루었다고 볼 수 있음
    if count > 1:                              # 연합을 이루었다면
        avg = total // count                   # 연합을 이루고 있는 각 칸의 인구수 구하기
        # 인구 이동
        for r, c in cord:                      # 연합에 포함된 나라
            board[r][c] = avg                  # 연합에 포함된 나라에 각 칸의 인구수 수정하기
            # 인구의 이동이 있는 나라는 다음 이동이 시작될 가능성이 있음
            countries.append((r, c))           # 나라 배열에 다시 추가하기

    return count > 1                           # 연합 존재 여부 리턴하기


def simulation(n, left, right):                                  # 인구 이동 발생 일수를 출력하는 함수
    day = 0                                                      # 인구 이동 발생 일수 0으로 초기화
    while True:                                                  # 인구 이동이 일어나지 않을 때까지 반복
        size = len(countries)                                    # 이번에 탐색할 수 있는 나라의 수
        flag = False                                             # 연합을 이루지 않은 상태로 초기화
        day += 1                                                 # 인구 이동 발생 일수 + 1
        for _ in range(size):                                    # 탐색할 수 있는 나라의 수만큼 반복
            i, j = countries.popleft()                           # 나라 배열에서 한 나라 선택
            if visited[i][j] == day:                             # 방문한 나라이면
                continue                                         # 다음 나라로
            visited[i][j] = day                                  # 방문하지 않은 나라이면 일수로 표시
            if bfs(n, left, right, i, j, day):                   # bfs 결과 true면 연합을 이루었다는 의미이므로 flag 표시
                flag = True                                      # 연합을 이룬 상태로 표시

        if not flag:                                             # 이번에 연합을 이룬 나라가 없으면
            return day - 1                                       # 인구 이동 발생 일수 - 1


n, left, right = map(int, input().split())                       # N, L, R 입력받기
board = [list(map(int, input().split())) for _ in range(n)]      # 각 나라의 인구수 입력

visited = [[0] * n for _ in range(n)]                            # 방문배열

countries = deque([(i, j) for i in range(n) for j in range(n)])  # 나라


print(simulation(n, left, right))                                # 연산 + 출력