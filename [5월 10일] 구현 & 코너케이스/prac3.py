# 선택과제 1: 16235 나무 재테크

import sys                       # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import deque    # collections 모듈의 deque 클래스 사용

input = sys.stdin.readline       # input 함수에 문자열을 입력받음

"""
 [문제 설명] - 단순 구현 문제
 봄: 하나의 칸마다 나이가 어린 나무부터 자신의 나이만큼 양분을 먹고, 나이가 1 증가함
    각 칸에 양분이 부족해 자신의 나이만큼 양분을 못 먹는 나무는 즉시 죽음
 여름: 봄에 죽은 나무가 양분으로 변함. 죽은 나무마다 나이를 2로 나눈 값이 양분으로 추가 (소수점 버림)
 가을: 나이가 5의 배수인 나무가 번식. 인접한 8개 칸에 나이가 1인 나무가 생김
 겨울: 로봇(S2D2)이 땅을 돌아다니면서 A[r][c]만큼 각 칸에 양분 추가
 K년이 지난 후 상도의 땅에 살아있는 나무의 개수
 [문제 풀이]
 a: 로봇(S2D2)가 겨울에 주는 양분의 양
 land: 땅의 현재 양분 상태
 tree[i][j]: 해당 영역에 존재하는 나이와 개수를 튜플로 묶어서 덱에 저장
 - 새로운 나무가 번식하기 때문에, 나이에 대한 오름차순을 유지하기 위해서는 앞에서의 삽입이 필요
"""


# 봄을 거쳐 나이를 먹은 나무들에 의해 새롭게 태어나게 되는 나무의 수를 계산
def breeding(breeding_src):
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]                  # 주위 8개의 영역의 행
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]                  # 주위 8개의 영역의 열

    breeding_cnt = [[0] * n for _ in range(n)]        # 새롭게 태어나게 되는 나무들의 영역 표시

    for r in range(n):                                # 모든 행
        for c in range(n):                            # 모든 열
            if breeding_src[r][c] == 0:               # 새롭게 태어나게 되는 나무가 없으면
                continue                              # 다음 영역
            for i in range(8):                        # 주위 8개의 영역 탐색
                nr = r + dr[i]                        # 새로운 행
                nc = c + dc[i]                        # 새로운 열
                if 0 <= nr < n and 0 <= nc < n:       # 영역이 유효하면
                    breeding_cnt[nr][nc] += breeding_src[r][c]     # 새롭게 태어나는 나무의 개수 추가

    return breeding_cnt                               # breeding_cnt 리턴


# 봄과 여름을 묶어서 진행
def spring_summer():
    breeding_src = [[0] * n for _ in range(n)]        # 나이가 5의 배수가 되어 가을에 번식을 하는 나무의 수를 각 영역에 저장

    for i in range(n):                                # 모든 열
        for j in range(n):                            # 모든 행
            next_year = deque()                       # next_year deque 생성
            dead = 0                                  # 죽는 나무의 수 0으로 초기화

            while tree[i][j]:                         # 각 영역의 나무 que
                age, cnt = tree[i][j].popleft()       # 나무 que의 한 나무 pop

                if land[i][j] < age * cnt:            # 해당 나이의 모든 나무에게 양분을 줄 수 없는 경우
                    dead = cnt - land[i][j] // age    # 죽는 나무의 개수
                    cnt = land[i][j] // age           # 살 수 있는 최대 수

                if cnt > 0:                           # 나무가 존재한다면
                    land[i][j] -= age * cnt           # 땅의 양분에서 나무가 먹는 양분만큼 빼기
                    next_year.append((age + 1, cnt))  # next_year deque에 나무 추가

                    if (age + 1) % 5 == 0:            # 만약 나무의 나이가 5배수라면
                        breeding_src[i][j] += cnt     # 영역에 번식하는 나무의 수 저장


                if dead > 0:                          # 죽은 나무가 생기면 그 이후의 나무는 모두 죽게 된다.
                    land[i][j] += (age // 2) * dead   # 여름에 양분이 됨
                    break                             # 다음 구역

            # 여름 -> 죽은 나무들이 양분이 됨
            while tree[i][j]:                         # 나무가 존재하는 동안
                age, dead = tree[i][j].popleft()      # 나무의 나이, 죽는 나무의 개수
                land[i][j] += (age // 2) * dead       # 나무에 죽는 나무만큼 양분 추가

            tree[i][j] = next_year                    # tree[i][j] que를 next_year que로 대체

    return breeding_src                               # breeding_src 리턴


def autumn_winter(breeding_src):
    # 봄에 나이를 먹은 나무들의 번식 결과
    breeding_cnt = breeding(breeding_src)

    for i in range(n):                                # 모든 행
        for j in range(n):                            # 모든 열
            # 가을 - 번식
            if breeding_cnt[i][j]:                    # 만약 새롭게 태어나는 나무가 있으면
                tree[i][j].appendleft((1, breeding_cnt[i][j]))  # 트리 deque에 나이와 개수 추가

            land[i][j] += winter_list[i][j]           # 겨울 - 로봇에 의해 양분 추가
    return


# 입력
n, m, k = map(int, input().split())                                  # N, M, K 입력받기
winter_list = [list(map(int, input().split())) for _ in range(n)]    # 각 칸에 추가되는 양분의 양 입력받기

land = [[5] * n for _ in range(n)]                                   # 초기 땅의 양분 상태
tree = [[deque() for _ in range(n)] for _ in range(n)]               # -> 만약 여기서 [deque()] * n으로 하면 어떻게 될까요?

for _ in range(m):                                                   # 나무의 개수만큼
    x, y, z = map(int, input().split())                              # 나무의 위치, 나이 입력받기
    tree[x - 1][y - 1].append((z, 1))                                # 나무의 위치에 나이와 개수 튜플로 추가하기

for _ in range(k):                                                   # k년 동안 시뮬레이션
    breeding_src = spring_summer()                                   # 양분을 먹고 죽는 나무 계산
    autumn_winter(breeding_src)                                      # 새로운 번식 계산

ans = 0                                                              # 남아있는 나무의 수 0으로 초기화

for line in tree:                                                    # 남아있는 나무 수 카운트
    for area in line:                                                # 모든 행
        for _, cnt in area:                                          # 모든 열에서 각 영역에 존재하는 나무의 수
            ans += cnt                                               # 남아있는 나무의 수 + 현재 영역에 존재하는 나무의 수

print(ans)                                                           # 남아있는 나무의 수 출력