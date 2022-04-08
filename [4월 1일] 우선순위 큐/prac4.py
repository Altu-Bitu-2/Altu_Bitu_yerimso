# 선택과제 2: 13975 파일 합치기 3

import sys                     # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
import heapq                   # heapq 모듈 import

input = sys.stdin.readline     # input 함수에 문자열 입력받기

"""
[파일 합치기 3]
- 파일을 전부 합치기 위해서는 어차피 하나로 만들어야 한다!
- 이 때, 여러번 더해지는 값은 작을 수록 좋다
- 따라서, 현재 가장 작은 파일 2개를 합쳐야 비용을 최소화 할 수 있다.
-> 최소 힙으로 구현
"""


def get_cost(pq):                            # 모든 장을 합치는데 필요한 최소비용을 출력하는 함수
    heapq.heapify(pq)                        # pq list를 heap으로 변환

    cost = 0                                 # cost 0으로 초기화
    while len(pq) > 1:                       # 만약 2장 이상이면
        file1 = heapq.heappop(pq)            # file1은 크기가 가장 작은 file
        file2 = heapq.heappop(pq)            # file2는 크기가 두번째로 작은 file
        cost += file1 + file2                # 비용 + (file1의 비용 + file2의 비용)
        heapq.heappush(pq, file1 + file2)    # heap에 file1과 file2를 더한 임시파일을 추가

    return cost                              # 최종 비용을 리턴


t = int(input())                             # 테스트 데이터의 개수 입력

for _ in range(t):                           # 테스트 데이터의 개수만큼 반복
    n = int(input())                         # 소설을 구성하는 장의 수 입력
    files = list(map(int, input().split()))        # 1장부터 n장까지 수록한 파일의 크기를 나타내는 양의 정수 n개 입력
    print(get_cost(files))                   # 연산 + 출력