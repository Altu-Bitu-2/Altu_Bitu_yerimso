# 필수과제 2: 5397 키로거

import sys                      # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import deque   # collections 모듈의 deque 클래스 사용: double-ended queue

input = sys.stdin.readline      # input 함수에 문자열 입력받기

"""
 [키로거]
 해당 풀이는, 글자 삽입 삭제 시 이동시키는 과정에서 생기는 코너케이스를 해결하기 위해 커서를 기준으로 왼쪽, 오른쪽으로 나눠서 값을 저장함
 1. 커서 앞의 글자를 지울 때, 글자가 없는 경우 주의
 2. 커서를 왼쪽으로 이동할 때, 이미 가장 왼쪽에 커서가 있는 경우 주의
 3. 커서를 오른쪽으로 이동할 때, 이미 가장 오른쪽에 커서가 있는 경우 주의
"""

t = int(input())                                  # 테스트 케이스 입력받기

for _ in range(t):                                # 테스트 케이스만큼 반복
    front = deque()                               # 커서 이전 내용을 저장
    back = deque()                                # 커서 이후 내용을 저장

    log = input().rstrip()                        # 강산이가 입력한 문자열 입력받기

    for c in log:                                 # 문자열 log에 있는 문자 개수만큼 반복
        # 현재 커서 앞에 있는 글자를 지운다.
        if c == '-':                              # 문자 c가 -이면
            if front:                             # 커서 이전 내용이 있다면
                front.pop()                       # 커서 이전 문자 삭제
        # 커서를 왼쪽으로 이동 -> front의 마지막 원소를 back 앞에 삽입
        elif c == '<':                            # 문자 c가 <이면
            if front:                             # 커서 이전 내용이 있다면
                back.appendleft(front.pop())
        # 커서를 오른쪽으로 이동 -> back의 처음 원소를 front 뒤에 삽입
        elif c == '>':                            # 문자 c가 >이면
            if back:                              # 커서 이후 내용이 있다면
                front.append(back.popleft())      # back의 첫번째 원소를 front 뒤에 삽입
        # 문자인 경우, 입력을 하면 커서보다 왼쪽에 위치하므로 front에 삽입
        else:                                     # 문자 c가 -, <, >가 아니면
            front.append(c)                       # 문자 c를 front 뒤에 삽입

    print(''.join(front) + ''.join(back))         # front que와 back que에 있는 문자열 합치기