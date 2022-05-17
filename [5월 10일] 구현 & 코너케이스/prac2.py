# 필수과제 2: 2615 오목

import sys                  # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline  # input 함수에 문자열을 입력받음

SIZE = 19                   # 바둑판의 모서리 사이즈 19

"""
 [오목]
 1. 특정 좌표(r, c)를 가장 왼쪽으로 하는 가능한 모든 오목 배치에 대해 오목 여부 확인
    가능한 모든 배치 :  오른쪽, 아래, 우하향, 우상향
 2. (주의) 육목이상이 되는지 확인해야 함
"""


def promising(r, c, stone, board):                        # 왼쪽, 위, 좌상향, 좌하향에 있는 돌이 있는지 같은색인지 확인하는 함수
    return 0 <= r < SIZE and 0 <= c < SIZE and board[r][c] == stone     # 같은 색 돌이 있다면


def check_dir(r, c, d, board):                            # (r,c)를 가장 왼쪽으로 하는 이어지는 바둑알이 5개 존재하는지 확인
    stone = board[r][c]                                   # 현재 위치의 돌의 색 확인

                                                          # 가로, 세로, 우하향 대각선, 우상향 대각선
    dr = [0, 1, 1, -1]                                    # 가로, 세로, 우하향 대각선, 우상향 대각선의 행 좌표
    dc = [1, 0, 1, 1]                                     # 가로, 세로, 우하향 대각선, 우상향 대각선의 열 좌표

    if promising(r - dr[d], c - dc[d], stone, board):     # 만약 왼쪽, 위, 좌상향, 좌하향에 같은 색 돌이 있다면
        return False                                      # 현재 가장 왼쪽(위쪽) 돌이 될수 없음

    cnt = 0                                               # (r, c)를 가장 왼쪽으로 하는 이어지는 바둑알의 개수

    while cnt < 6 and promising(r, c, stone, board):      # count가 6보다 작고 육목이 아닐때
        cnt += 1                                          # count + 1
        r += dr[d]                                        # 같은 방향으로 행 진행
        c += dc[d]                                        # 같은 방향으로 열 진행

    return cnt == 5                                       # 만약 count가 5개면 True 리턴


def is_end(r, c, board):                                  # 승부가 결정됐는지 확인하는 함수

    for i in range(4):                                    # 가로, 세로, 우하향 대각선, 우상향 대각선 확인
        if check_dir(r, c, i, board):                     # 만약 연속된 돌이 5개 존재한다면
            return True                                   # True를 리턴
    return False                                          # 5개의 연속된 돌이 존재하지 않다면 False를 리턴


def simulation(board):                                    # 오목 결과 출력 함수
    for i in range(SIZE):                                 # i번째 행
        for j in range(SIZE):                             # j번째 행

            if not board[i][j]:                           # 만약 돌이 없으면
                continue                                  # 다음 지점

            if is_end(i, j, board):                       # 누군가 이겼으면
                return "{}\n{} {}".format(board[i][j], i + 1, j + 1)      # 승부 결과, 연속된 바둑알 중 가장 왼쪽(위쪽)에 있는 바둑알의 좌표 반환

    return 0                                              # 승부 미결정 시 0 출력



board = [list(map(int, input().split())) for _ in range(SIZE)]          # 입력

print(simulation(board))                                                # 연산 + 출력