# 선택과제 1: 2075 N번쨰 큰 수

import sys                   # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
import heapq as hq           # heapq 모듈을 hq 이름으로 import
input = sys.stdin.readline   # input 함수에 문자열 입력받기

"""
[N번째 큰 수]
메모리 제한이 있으므로, 입력값을 모두 저장하면 안된다.
상위 n개만 저장하는 "최소" 힙을 만들어서 heap[0]을 현재까지의 N번째 큰수로 유지하는 풀이
"""

n = int(input())                                       # n 입력받기

# 첫 줄은 n이니까 그대로 받아서 min heap으로 만들기
min_heap = list(map(int, input().split()))             # n개의 숫자를 입력받아 min_heap list에 저장
hq.heapify(min_heap)                                   # min_heap list를 min heap로 변환

# 이후 n-1 줄에 대해 들어오는 수들을 검사
for _ in range(n-1):                                   # 나머지 n-1줄 반복
    line = map(int, input().split())                   # n개의 수 입력받기
    for x in line:                                     # line의 수 만큼 반복
        # 상위 n개 중 가장 작은 수보다 커야 상위 n개 힙에 삽입할 수 있음
        if x > min_heap[0]:                            # 만약 line에 있는 수가 min_heap의 가장 작은 수보다 크면
            # x를 push하고, pop한다
            # 순서 중요! pop부터 해야 되는 상황에는 쓰지 않도록 주의한다.
            hq.heappushpop(min_heap, x)                # 표의 규칙을 잘 맞춰서 입력했다면 (n-1)*n개의 수가 pop해서 결국 n개의 수만 남음

print(min_heap[0])                                     # N번째 큰 수 출력