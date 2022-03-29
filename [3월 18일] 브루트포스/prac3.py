#선택과제 1: 2798 블랙잭
import sys                             # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from itertools import combinations     # itertools 모듈의 combinations 함수 제공

input = sys.stdin.readline             # input 함수에 문자열 입력받기

"""
[ 블랙잭 ] - 단순 구현
카드가 최대 100장이므로,
C(100, 3) < 100*100*100 = 1,000,000 -> 브루트포스 충분히 가능
ver1. 3중 for문 이용해서 구현
+) 코드의 효율성을 높이기 위해, 카드를 사전에 정렬하여 M을 넘어가는 순간 반복 종료
ver2. itertools.combinations 이용하여 모든 조합을 구해서 구현
"""


def play_blackjack(n, m, cards):              # M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합 출력하는 함수
    cards.sort()                              # 오름차순 정렬
    answer = 0                                # answer 0으로 초기화

    for i in range(n):                        # 카드의 개수만큼 반복
        for j in range(i + 1, n):             # i 카드보다 큰 숫자를 가진 카드 개수만큼 반복
            for k in range(j + 1, n):         # j 카드보다 큰 숫자를 가진 카드 개수만큼 반복
                temp = cards[i] + cards[j] + cards[k]            # i, j, k 카드에 적힌 숫자들의 합 구하기
                # cards 리스트가 오름차순 정렬되어 있으므로 k를 키우는 건 의미 없음
                if (temp > m):                # 세 카드의 적힌 숫자들의 합이 M보다 크면
                    break                     # j의 크기 증가
                answer = max(answer, temp)    # 최댓값 갱신
    return answer                             # M보다 크지 않고 M에 최대한 가까운 카드 3장의 합 리턴


def play_blackjack_with_combinations(n, m, cards):       # M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합 출력하는 함수
    combi = combinations(cards, 3)            # cards에서 3개로 이루어진 모든 조합 구하기
    arr = list(map(lambda x: sum(x), combi))  # 모든 조합에 대해 합 구하기
    arr.sort()                                # 오름차순 정렬

    answer = 0                                # answer 0으로 초기화
    for total in arr:                         # arr 리스트에 있는 수만큼 반복
        # 합이 m을 넘어가면 바로 종료
        if total > m:                         # 세 카드의 합이 M보다 크면
            break                             # for문 종료
        answer = total                        # 최댓값 갱신

    return answer                             # M보다 크지 않고 M에 최대한 가까운 카드 3장의 합 리턴


# 입력
n, m = map(int, input().split())                # 카드의 개수와 M 입력받기
cards = list(map(int, input().split()))         # 카드에 쓰여있는 수 입력받아 cards 리스트에 저장

print(play_blackjack(n, m, cards))              # 연산 + 출력
# print(play_blackjack_with_combinations(n, m, cards))