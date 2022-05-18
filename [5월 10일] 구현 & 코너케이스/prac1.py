# 필수과제 1: 16236 아기상어

import sys                       # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import deque    # collections 모듈의 deque 클래스 사용

input = sys.stdin.readline       # input 함수에 문자열을 입력받음

INF = 401                        # 이동 불가능한 거리

"""
 [아기 상어]
 1. 상어로부터 가장 가까운 거리에 있는 모든 물고기 탐색 (BFS)
 2. 우선순위 조건에 맞추어 먹으러 갈 물고기 확정
    탐색하는 방향에 우선순위를 두는 걸로 해결되지 않음! (예제 입력 4) 정렬 필요
 3. 상어가 이동할 수 있는 곳이 없을 때까지 BFS 탐색 반복
 입력 범위가 작기 때문에 매번 BFS 탐색을 반복해도 시간 초과 X
 가능한 물고기의 최대 마리 수 : 399마리
 최대 BFS 탐색 횟수 : 399회, 1회 탐색마다 while 문은 최대 400회 미만으로 순회
 총 연산 횟수 약 160000번으로 충분히 가능
 해설 : https://myunji.tistory.com/378
 *글 자체는 별로 도움이 안되고...그냥 리팩토링하면 코드가 이렇게 되는구나 정도만 봐주세요
"""


def next_pos(n, shark_size, shark, board):        # bfs 실행
    dr = [-1, 1, 0, 0]                            # 상, 하, 좌, 우
    dc = [0, 0, -1, 1]                            # 상. 하, 좌, 우

    min_dist = INF                                # 최단 거리 = INF
    que = deque()                                 # 상어가 갈 수 있는 곳
    dist = [[0] * n for _ in range(n)]            # 상어로부터의 거리 - 초기값은 0으로
    pos_list = []                                 # 상어가 먹을 수 있는 물고기들의 위치

    dist[shark[0]][shark[1]] = 1                  # 현재 상어의 위치까지의 거리 1
    que.append(shark)                             # que에 현재 상어의 위치 추가

    while que:                                    # que안의 모든 요소 확인
        row, col = que.popleft()                  # que의 가장 앞 요소를 꺼냄

                                                  # 최단거리 이상은 탐색할 필요 없음
        if dist[row][col] >= min_dist:            # 만약에 (row, col)까지의 거리가 최단거리보다 크다면
            continue                              # 다음 지점

        for i in range(4):                        # 상하좌우 탐색
            nr = row + dr[i]                      # 다음 행
            nc = col + dc[i]                      # 다음 열
            if not (0 <= nr < n and 0 <= nc < n) or dist[nr][nc] or board[nr][nc] > shark_size:    # 범위 내에 있지 않으면
                continue                          # 다음 지점

            dist[nr][nc] = dist[row][col] + 1     # 거리 1 추가

                                                  # 먹을 수 있는 물고기 발견
            if board[nr][nc] and board[nr][nc] < shark_size:    # 만약 물고기가 존재하고 사이즈가 상어보다 작다면
                pos_list.append((nr, nc))         # 상어가 먹을 수 있는 물고기들의 위치 큐에 추가
                min_dist = dist[nr][nc]           # 최단거리를 먹을 수 있는 물고기까지의 거리로 변경
                continue                          # 다음 지점

            que.append((nr, nc))                  # 상어가 갈수 있는 곳 큐에 다음 지점 추가


    if not pos_list:                              # 상어가 먹을 수 있는 물고기가 없다면
        return min_dist, (-1, -1)                 # 최단거리와 (-1, -1) 반환

    pos_list.sort()                               # 물고기들의 위치 정렬하기

    return min_dist - 1, pos_list[0]              # 최단거리 - 1, 가장 위, 왼쪽에 있는 물고기의 위치 반환


def simulation(n, shark, board):                  # 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 함수
    ans = cnt = 0                                 # 물고기를 잡아먹을 수 있는 시간, 물고기를 잡아먹은 횟수 0으로 초기화
    size = 2                                      # 상어크기 = 2

    while True:                                   # 계속 반복
        dist, pos = next_pos(n, size, shark, board)    # 거리와 다음 좌표 구하기
                                                  # 더 이상 먹을 수 있는 물고기가 공간에 없음
        if dist == INF:                           # 이동거리가 INF와 같다면
            break                                 # 엄마 상어에게 도움 요청

        ans += dist                               # 물고기를 잡아먹을 수 있는 시간에 이번 이동거리 더하기
        cnt += 1                                  # 물고기를 잡아먹은 횟수 + 1

                                                  # 상어 크기 증가
        if cnt == size:                           # 물고기를 잡아먹은 횟수와 상어의 크기가 같다면
            cnt = 0                               # count는 0
            size += 1                             # 상어의 사이즈 추가

                                                  # 상어 이동
        board[shark[0]][shark[1]] = 0             # 상어가 있던 자리의 상태 0으로 바꾸기
        shark = pos                               # 상어의 위치는 새로운 좌표로 바꾸기

    return ans                                    # 물고기를 잡아먹은 시간 반환하기


# 입력
n = int(input())                                              # 공간 사이즈 입력받기
board = [list(map(int, input().split())) for _ in range(n)]   # 공간의 상태 입력

for i in range(n):                                            # i번째 행
    for j in range(n):                                        # j번째 열의
        if board[i][j] == 9:                                  # 상태가 만약 9이면
            shark_pos = (i, j)                                # 상어의 위치는 (i, j)
            break                                             # 반복문 빠져나오기

print(simulation(n, shark_pos, board))                        # 연산 + 출력