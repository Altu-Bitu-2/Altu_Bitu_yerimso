# 필수과제 1: 2840 행운의 바퀴

import sys                     # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline     # input 함수에 문자열 입력받기

"""
[행운의 바퀴]
- 바퀴가 돌아갈 필요 X
- 화살표가 가르키는 인덱스를 회전 정보에 따라 바꿔줌
1. 화살표가 가르키는 칸이 결정되지 않았으면 알파벳을 바퀴에 적는다.
2. 이미 알파벳이 써 있는 경우, 같은 알파벳이 아닌 경우 조건에 해당하는 바퀴 만들 수 없다.
3. 바퀴에 쓰여있는 알파벳은 중복되지 않으므로 동일한 알파벳이 여러 자리에 있을 수 없다.
"""


def make_wheel(n, record):              # 행운의 바퀴가 있는지 판단하는 함수
    wheel = ['?'] * n                   # 바퀴의 상태
    is_available = dict()               # 해당 알파벳을 새로 쓸 수 있는지 확인하는 딕셔너리

    # 모든 알파벳에 대해 우선 True로 저장
    # ord(문자) = 아스키코드
    # chr(아스키코드) = 문자
    ord_a = ord('A')                    # ord_a에 A의 아스키코드를 저장함
    for i in range(26):                 # 알파벳 개수만큼 반복
        is_available[chr(i + ord_a)] = True        # A부터 Z까지 해당 알파벳을 새로 쓸 수 있는지 확인

    idx = 0                             # 화살표가 가르키는 인덱스

    for rot, alpha in record:           # record의 S와 문자쌍 전부 반복
        idx = (idx - int(rot)) % n      # 바퀴를 회전시켰을 때 현재 화살표가 가리키는 인덱스에서 얼마나 떨어졌는지 확인


        if wheel[idx] == alpha:         # 바퀴를 회전시킨 후 같은 알파벳이 바퀴에 써있는 경우
            continue                    # 다음 record로

        if wheel[idx] != '?' or not is_available[alpha]:   # 다른 알파벳이 써 있거나, 이미 알파벳을 다른 자리에 사용한 경우
            return '!'                  # ! 출력
        wheel[idx] = alpha              # 바퀴를 회전한 위치에 alpha 문자 저장하기
        is_available[alpha] = False     # alpha 문자를 앞으로 새로 쓸 수 없음

    return ''.join(wheel[idx:] + wheel[:idx])   # wheel 바퀴의 마지막 회전에서 화살표가 가리키는 문자부터 시계방향으로 출력


# 입력
n, k = map(int, input().split())                # 바퀴의 칸의 수 N, 바퀴를 돌리는 횟수 K 입력받기
record = [input().split() for _ in range(k)]    # 바퀴를 회전시켰을 때 화살표가 가리키는 글자가 몇번 바뀌었는지를 나타내는 S와 회전을 멈추었을 때 가리키던 글자

print(make_wheel(n, record))                    # 연산 + 출력