# 선택과제 3: 14235 크리스마스 선물

import sys                     # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
import heapq as hq             # heapq 모듈을 hq 이름으로 import
input = sys.stdin.readline     # input 함수에 문자열 입력받기

"""
[크리스마스 선물] - 단순 구현 문제
- 0이 나올 때마다, 가지고 있는 선물 중 가장 가치가 큰 것을 삭제 & 출력
- 최대 힙의 연산을 하기 위해, 힙에 넣을 때는 -1을 곱해서 삽입하고, 출력할 때 다시 -1을 곱해서 출력
"""

n = int(input())                                # 아이들과 거점지를 방문한 횟수 n 입력
present = []                                    # 선물 list 생성

for _ in range(n):                              # 아이들과 거점지를 방문한 횟수만큼 반복
    nums = list(map(int, input().split()))      # 충전한 선물의 개수와 그 선물들의 가치 입력


    if len(nums) == 1:                          # 아이를 만난 경우
        if len(present) == 0:                   # 선물이 없는 경우
           print(-1)                            # -1 출력
        else:                                   # 선물이 있는 경우
            print(-hq.heappop(present))         # 선물의 가치가 가장 큰 선물 pop (최대 힙 연산을 위해 -1 출력)

    else:                                       # 선물을 충전하는 경우
        for value in nums[1:]:                  # nums list의 2번째 요소부터 끝까지 반복
            hq.heappush(present, -value)        # 최대 힙의 연산을 하기 위해 value에 -1을 곱해서 heap에 push함