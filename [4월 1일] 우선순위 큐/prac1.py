# 필수과제 1: 7662 이중 우선순위 큐

import sys                   # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
import heapq as hq           # heapq 모듈을 hq 이름으로 import

input = sys.stdin.readline   # input 함수에 문자열 입력받기

"""
[이중 우선순위 큐]
최대 힙과 최소 힙 두가지로 나누어 저장
다른 힙에서 이미 제거된 값을 판단하기 위해, 큐에 값이 들어올 때마다 is_valid에 상태를 저장한다.
만약 최대 힙/최소 힙에서 값을 꺼냈을 때 해당 인덱스의 is_valid 원소가 False로 표기되어 있다면, 이미 다른 큐를 통해 제거된 값이므로 버리고 다시 꺼내야 한다.
"""

testcase = int(input())               # 테스트 케이스의 개수 입력받기


# 힙에서 유효하지 않은 값 삭제하는 함수
def remove_invalid_data(heap):
    # 힙에 데이터가 하나라도 있고, top이 invalid 하면 pop해줌
    while heap and not is_valid[heap[0][1]]:
        hq.heappop(heap)    # heap에서 가장 작은 항목을 제거
    return                  # 반환


for _ in range(testcase):             # 테스트 케이스 개수만큼 반복
    t = int(input())                  # Q에 적용할 연산의 개수 입력받기

    max_heap = list()                 # 최댓값을 저장하는 list
    min_heap = list()                 # 최솟값을 저장하는 list
    is_valid = list()                 # 값의 유효성을 저장하는 list
    idx = 0                           # 이번에 들어올 값의 인덱스
    # is_valid[idx]에 값의 유효성이 저장된다.

    for _ in range(t):                # 연산의 개수만큼 반복
        cmd, n = input().split()      # 연산의 종료와 정수를 차례로 입력
        if cmd == 'D':                # 연산의 종류가 D이고
            if int(n) == 1:           # n이 1이라면
                remove_invalid_data(max_heap)          # max_heap에서 최댓값 제거
                if max_heap:                           # max_heap list에 원소가 존재한다면
                    # 값을 제거한 후에 유효성을 갱신
                    is_valid[hq.heappop(max_heap)[1]] = False
            else:                     # n이 -1이라면
                remove_invalid_data(min_heap)          # min_heap에서 최솟값 제거
                if min_heap:                           # min_heap list에 원소가 존재한다면
                    # 값을 제거한 후에 유효성을 갱신
                    is_valid[hq.heappop(min_heap)[1]] = False
        else:                         # 연산의 종류가 I라면
            hq.heappush(max_heap, (-int(n), idx))      # max_heap에 -n을 추가, 오름차순으로 저장되므로
            hq.heappush(min_heap, (int(n), idx))       # min_heap에 n을 추가
            is_valid.append(True)                      # 우선 유효하다고 저장
            idx += 1                                   # 다음에 들어올 값의 인덱스

    # 최종 최솟값과 최댓값을 구하기 전, 유효하지 않은 값이 top에 있으면 제거한다.
    remove_invalid_data(max_heap)       # 최댓값이 유효한지 확인, 아니면 제거
    remove_invalid_data(min_heap)       # 최솟값이 유효한지 확인, 아니면 제거

    if max_heap:                        # 만약 max_heap에 원소가 존재한다면
        print(-max_heap[0][0], min_heap[0][0])      # 최댓값, 최솟값을 출력
    else:                               # max_heap에 원소가 없다면
        print("EMPTY")                  # EMPTY 출력