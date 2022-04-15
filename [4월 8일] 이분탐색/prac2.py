# 필수과제 2: 17281 야구

import sys                           # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from itertools import permutations   # itertools 모듈의 permutations 함수 제공
input = sys.stdin.readline           # input 함수에 문자열 입력받기

"""
[야구]
1. 가능한 모든 배치를 구한다.
    - 이때, 4번 타자는 항상 1번 선수(0번 인덱스)여야 함을 주의
2. 구한 배치에 대해 점수를 계산
    - out이 3번을 기록하여 이닝이 바뀔 때, 이전에 베이스에 있던 선수들을 비워주어야 함
    - 선수 인덱스를 갱신하는 과정에서 인덱스 에러가 나지 않도록 모듈러 연산 해주기
"""


def calc_score(order, result):                     # 구한 순서에 대해 점수를 계산
    player = 0                                     # 1번 타자부터 시작
    score = 0                                      # 스코어 0으로 초기화

    for inning in result:                          # result의 한 행이 inning이 되고,
        out = 0                                    # 현재 이닝에서 out 개수
        base1 = base2 = base3 = 0                  # 현재 베이스 초기화
        while out < 3:                             # out이 3개보다 적은 동안만 반복
            p = inning[order[player]]              # 이번 타자의 포인트
            if p == 0:                             # p가 out이면
                out += 1                           # out 개수 + 1
            elif p == 1:                           # p가 안타이면
                score += base3                     # base3에 선수가 있으면 + 1
                base3 = base2                      # base2 선수 base3로 이동
                base2 = base1                      # base1 선수 base2로 이동
                base1 = 1                          # 타석 선수 base1로 이동
            elif p == 2:                           # p가 2루타이면
                score += base3 + base2             # score + 2루타, 3루타에 있는 선수의 수
                base3 = base1                      # base1 선수 base3로 이동
                base2 = 1                          # 타석 선수 base2로 이동
                base1 = 0                          # base1 비우기
            elif p == 3:                           # p가 3루타이면
                score += base3 + base2 + base1     # score + 1루타, 2루타, 3루타에 있는 선수의 수
                base3 = 1                          # 타석 선수 base3로 이동
                base2 = base1 = 0                  # base1, base2 비우기
            else:                                  # p가 홈런이면
                score += base3 + base2 + base1 + 1 # score + 타석, 1루타, 2루타, 3루타에 있는 선수의 수
                base3 = base2 = base1 = 0          # base1, base2, base3 비우기

            player = (player + 1) % 9              # 다음 타자로 바꿔 줌

    return score                                   # 모든 이닝 끝난 후 score 리턴하기


# 입력
n = int(input())                                                # 이닝 수 입력
result = [list(map(int, input().split())) for _ in range(n)]    # 각 이닝별 득점결과
answer = 0                                                      # 점수 0으로 초기화


# 가능한 모든 배치를 구하되, 1번타자(0번 인덱스)는 고정되어 있음을 주의
for order in permutations(range(1, 9), 8):                      # 8명의 선수 중 가능한 배치 모두 반복
    order = list(order)                                         # 현재 배치 list에 저장하기
    order.insert(3, 0)                                          # 4번 위치에 1번 타자 위치시키기

    answer = max(answer, calc_score(order, result))             # 최댓값 갱신

print(answer)                                                   # 아인타 팀이 얻을 수 있는 최대 점수 출력