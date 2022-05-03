# 필수과제 2: 13422 도둑

import sys                                   # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline                   # input변수에 문자열을 입력받음

"""
 [도둑]
 1. 연속해서 훔쳐야 할 집이 m으로 고정됐기 때문에 슬라이딩 윈도우
 2. 직선이 아니라 원 형태의 배열! 모듈러 연산을 통해 윈도우의 양 끝 위치 조절하기
 !주의! 마을에 있는 집의 개수와 도둑이 훔칠 집의 개수가 같을 때(n==m) 도둑이 훔칠 수 있는 경우의 수 1개!
    => 예를 들어, n = m = 3, k = 4, house = [1, 1, 1] 일 때, 실제 방법의 수는 1번, 2번, 3번 집을 택하는 경우밖에 없지만
       예외 처리를 안해줄 경우, 원형으로 돌며 3을 출력하게 됨!
"""


def steal(n, m, k, house):                      # M개의 연속된 집을 고르는 방법의 수를 리턴하는 함수
    # 윈도우 초기화
    money = sum(house[:m])                      # 첫번째 집부터 M개의 집의 모든 돈의 합 구하기
    count = 0                                   # 경우의 수 0으로 초기화

    if money < k:                               # 만약 M개의 집의 모든 돈의 합이 K보다 작다면
        count += 1                              # 경우의 수 + 1

    if n == m:                                  # 집의 수 = 훔칠 수 있는 집의 수이면
        return count                            # count 리턴하기

    for i in range(m, n + m - 1):               # M개의 연속된 집을 고르는 나머지 방법들 반복
        money -= house[i - m]                   # 처음 집의 돈 빼기
        money += house[i % n]                   # 마지막 집의 다음 집의 돈 더하기

        if money < k:                           # 돈의 합이 K보다 작으면
            count += 1                          # 경우의 수 + 1

    return count                                # 방법의 수 리턴하기


# 입력
t = int(input())                                # 테스트 케이스의 개수 입력받기

for _ in range(t):                              # 테스트 케이스의 개수만큼 반복
    # 입력
    n, m, k = map(int, input().split())         # 마을에 있는 집의 개수, 도둑이 돈을 훔칠 연속된 집의 개수, 자동 방범 장치가 작동하는 최소 돈의 양 입력받기
    house = list(map(int, input().split()))     # N개의 집에서 각각 보관중인 돈의 양 입력받기

    print(steal(n, m, k, house))                # 연산 + 출력