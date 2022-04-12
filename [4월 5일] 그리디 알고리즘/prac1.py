# 선택과제 1: 11000 강의실 배정

import sys                     # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
import heapq as hq             # heapq 모듈을 hq 이름으로 import

input = sys.stdin.readline     # input 함수에 문자열 입력받기

"""
[강의실 배정]
- 강의실 수를 최소로 하기 위해서, 현재 사용하는 강의실 중 가장 빨리 끝나는 강의실에 가장 먼저 시작하는 강의실을 배치해야 한다.
- 이 문제는 모든 강의를 다 진행해야 하므로, 회의실 배정 문제와는 다르다! 먼저 시작하는 순으로 정렬할 것.
- 현재 가장 빨리 끝나는 시간을 구하기 위해 최소 힙(우선순위 큐) 사용
"""



def get_min_classroom(lectures):                                    # 필요한 강의실 수를 구하는 함수
    lectures.sort()                                                 # 강의 진행 순서대로 나열하기
    pq = [-1]                                                       # 처음 인덱스 에러를 피하기 위해 음수 값 삽입. (첫번째 강의 때 갱신될 값)

    for start, end in lectures:                                     # 강의 개수만큼 반복
        if pq[0] <= start:                                          # 가장 빨리 끝나는 강의실을 사용할 수 있는 경우 (이전 강의가 끝나는 시간보다 현재 강의가 시작하는 시간이 클 경우)
            hq.heappop(pq)                                          # heap에서 pq를 꺼냄 (강의실에서 마지막으로 끝나는 강의 시간을 초기화)
        hq.heappush(pq, end)                                        # 끝나는 시간 삽입 (강의실에서 마지막으로 끝나는 강의 업데이트)

    return len(pq)                                                  # pq의 길이가 사용 중인 강의실의 수가 된다.


n = int(input())                                                    # 수업 개수 입력받기
lectures = [tuple(map(int, input().split())) for _ in range(n)]     # 수업 개수만큼 시작시간, 종료시간을 받아서 튜플로 저장하기

print(get_min_classroom(lectures))                                  # 연산 + 출력