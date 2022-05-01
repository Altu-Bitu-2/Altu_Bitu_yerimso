# 선택과제 2: 1697 숨바꼭질

import sys                         # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import deque      # collections 모듈의 deque 클래스 사용

input = sys.stdin.readline         # input변수에 문자열을 입력받음

"""
[숨바꼭질]
 x좌표 위에서 x-1, x+1, 2*x의 위치로 계속 이동하며 탐색
 가장 빠른 시간을 찾아야 하므로 주변 노드부터 탐색하는 풀이로 풀어서 k에 도달하면 바로 탐색 종료 (bfs)
"""
SIZE = 10 ** 5                             # 수빈이와 동생이 있을 수 있는 구간의 범위


def bfs(n, k):                             # 수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구하는 함수
    time = [-1] * (SIZE + 1)               # 구간의 길이만큼 time list 생성
    que = deque()                          # 빈 que 생성
    que.append(n)                          # que에 수빈이의 위치 추가
    time[n] = 0                            # time list에서 수빈의 위치 -1 -> 0

    while que:                             # que가 비어있지 않을 동안 반복
        curr = que.popleft()               # que의 가장 앞에 저장되어 있는 구역 pop
        if curr == k:                      # 만약 curr이 K와 같으면
            return time[curr]              # time list의 curr번째 원소 출력

        for next in (curr * 2, curr + 1, curr - 1):           # 순간이동, 걸어서 이동할 수 있는 모든 구간 탐색
            if next < 0 or next > SIZE or time[next] > -1:    # 만약 이동한 구간이 범위를 벗어나거나 이동한 구간의 time이 -1보다 클 때
                continue                                      # 건너뛰기
            time[next] = time[curr] + 1                       # 이동한 구간의 값을 (현재 시간 + 1)로 바꾸기
            que.append(next)                                  # que에 next 위치 추가


# 입력
n, k = map(int, input().split())            # 수빈이가 있는 위치 N과 동생이 있는 위치 K 입력받기

print(bfs(n, k))                            # 연산 + 출력