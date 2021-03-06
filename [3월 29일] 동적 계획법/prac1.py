# 선택과제 1: 11727 2xn 타일링 2

import sys                         # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
input = sys.stdin.readline         # input 함수에 문자열 입력받기

"""
 너비를 인덱스로 써서 n까지의 너비를 채우는 방법의 수를 저장하자!
 우선, 너비 1은 2(높이)x1(너비) 타일로 채우는 경우밖에 없음
 너비 2는 1x2 2개와 2x2 1개 총 2 경우 + 너비 1에 2x1 타일을 더한 1 경우 -> 3 경우
 그 후, 너비 3부터는 각각 너비 1, 2만큼을 뺀 타일에서 1, 2 너비 타일을 각각 더하는 경우를 생각해주자
 이때, 중복 경우의 수가 생기지 않도록 너비 2의 경우에서 1에서 더한 경우는 빼줌
 -> dp[n] = (너비 1인 타일 채우는 경우의 수 = 1) * dp[n - 1]
          + (너비 2인 타일 채우는 경우의 수 = 2) * dp[n - 2]
 -> dp[n] = 1 * dp[n - 1] + 2 * dp[n - 2] (n >= 3)
 !주의! 모듈러 연산 해야함
"""

MOD = 10007                                 # 10007로 나눈 나머지를 출력하기 위해 변수로 저장

def fill_tile(n):                           # 2xn 크기의 직사각형을 채우는 방법의 수를 구하고 100007로 나눈 나머지를 구하기 위한 함수
    if n == 1:                              # 1일 때는 바로 값 리턴 (인덱스 에러 방지)
        return 1                            # 1 리턴

    dp = [0] * (n + 1)                      # n까지 포함하는 배열 만들기

    dp[1] = 1                               # 1까지의 너비를 채우는 방법: 1
    dp[2] = 3                               # 2까지의 너비를 채우는 방법: 3

    for i in range(3, n + 1):               # 3부터 n까지 반복
        dp[i] = dp[i-2] * 2 + dp[i-1]       # dp[n] = (너비 1인 타일 채우는 경우의 수 = 1) * dp[n - 1] + (너비 2인 타일 채우는 경우의 수 = 2) * dp[n - 2]
        dp[i] %= MOD                        # 중간 과정에서 MOD연산을 통해 숫자를 줄임

    return dp[n]                            # dp[n] 리턴

n = int(input())                            # n을 입력받음

print(fill_tile(n))                         # 연산 + 출력