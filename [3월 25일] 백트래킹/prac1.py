# 필수과제 1: 20055 컨베이어 벨트 위의 로봇

import sys                       # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import deque    # collections 모듈의 deque 클래스 사용: double-ended queue

input = sys.stdin.readline       # input 함수에 문자열 입력받기

"""
 [컨베이어 벨트 위의 로봇 문제]
 1. 벨트가 각 칸 위의 로봇과 함께 한 칸 회전
 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트 회전 방향으로 한 칸 이동할 수 있다면 이동 (이동가능: 이동하려는 칸에 로봇이 없고, 그 칸의 내구도가 1 이상이어야 함)
 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇 올림
 4. 내구도가 0인 칸의 개수가 k개 이상이라면 과정 종료. 그렇지 않다면 1로 돌아감
 [문제 풀이]
 벨트의 회전을 구현하기 위해서 deque 사용
 1번: 벨트를 오른쪽으로 한칸 회전
 2번: 가장 먼저 올라간 로봇부터 고려해야 하므로 (내리는 위치 - 1)부터 (올리는 위치)까지 검사 -> 로봇 옮기는 거 가능하면 존재여부 체크하고 내구도 감소
 3번: 올리는 위치 칸 내구도 0이 아니라면 해당 칸 로봇 존재 여부 체크 + 내구도 감소
"""


def simulation(n, k, belt):          # 컨베이어벨트 회전이 종료되었을 때 몇번째 단계가 진행중이었는지 구하는 함수
    size = 2 * n                     # 벨트의 사이즈 = 컨베이어벨트의 사이즈 * 2
    robots = deque([False] * size)   # 로봇의 존재 여부를 저장

    up_idx = 0                       # 로봇을 올리는 위치
    down_idx = n - 1                 # 로봇을 내리는 위치

    step = 0                         # 단계 0으로 초기화
    count = 0                        # 내구도가 0인 칸의 수

    while True:                      # True인 동안 반복
        step += 1                    # 단계 + 1

        # 1. 회전
        robots.rotate(1)             # 로봇 1칸 회전
        belt.rotate(1)               # 컨베이어 벨트 1칸 회전

        robots[down_idx] = False     # 로봇 내리기

        # 2. 로봇 이동
        for idx in range(down_idx - 1, up_idx - 1, -1):  # 내리는 쪽에서 가까운 로봇부터 이동할 수 있는 만큼 이동
            if robots[idx] and not robots[idx + 1] and belt[idx + 1] > 0:  # 만약 로봇이 있는 칸의 오른쪽 칸의 로봇이 없고 그 칸의 내구도가 0 이상이라면
                robots[idx] = False      # 원래 로봇이 있던 칸에서 로봇 제거
                robots[idx + 1] = True   # 1칸 오른쪽으로 이동
                belt[idx + 1] -= 1       # 이동한 칸의 내구도 - 1
                if belt[idx + 1] == 0:   # 만약 이동한 칸의 내구도가 0이 되었다면
                    count += 1           # 내구도가 0인 칸의 수 + 1

        robots[down_idx] = False         # 내리는 위치에 로봇이 옮겨졌다면 바로 내리기

        # 3. 로봇 올리기
        if belt[up_idx] > 0:             # 올리는 칸의 내구도가 0 이상이면
            robots[up_idx] = True        # 로봇 올리기
            belt[up_idx] -= 1            # 올린 칸의 내구도 - 1
            if belt[up_idx] == 0:        # 올린 칸의 내구도가 0이 되었다면
                count += 1               # 내구도가 0인 칸의 수 + 1

        if count >= k:                   # 만약 내구도가 0인 칸의 수가 k개 이상이 되었다면
            break                        # while 빠져나오기

    return step                          # 진행된 단계 리턴하기


# 입력
n, k = map(int, input().split())         # N과 K를 입력받음
belt = deque(map(int, input().split()))  # 벨트의 내구도를 저장

# 연산 + 출력
print(simulation(n, k, belt))            # 몇번째 단계가 진행줄일때 종료되었는지 출력