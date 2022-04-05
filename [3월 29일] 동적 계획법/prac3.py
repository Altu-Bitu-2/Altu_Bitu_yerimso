# 선택과제 3: 9251 LCS

import sys                     # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline     # input 함수에 문자열 입력받기

"""
 LCS (해당 풀이는 "08. 동적계획법.pdf" 참고)
 해당 풀이는 인덱스를 편하게 관리하기 위해 dp와 path 배열을 (1, 1)부터 시작
"""


def get_lcs_size(text1, text2):                              # 두 문자열의 부분 중 가장 긴 것을 찾는 함수
    size1 = len(text1)                                       # 문자열1의 길이 재기
    size2 = len(text2)                                       # 문자열2의 길이 재기
    dp = [[0] * (size2 + 1) for _ in range(size1 + 1)]       # size1 + 1, size2 + 1 사이즈의 표 만들기

    for i in range(1, size1 + 1):                            # dp[] 전체 반복
        for j in range(1, size2 + 1):                        # dp[i][] 전체 반복
            if text1[i - 1] == text2[j - 1]:                 # 두 문자가 같으면
                dp[i][j] = dp[i - 1][j - 1] + 1              # 왼쪽 대각선 위의 숫자 + 1
            else:                                            # 두 문자가 다르면
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])   # 왼쪽, 위쪽 숫자 중 최댓값

    return dp[size1][size2]                                  # 최종 lcs 길이 리턴


# 입력
text1 = input().rstrip()                                     # 문자열1 입력받기
text2 = input().rstrip()                                     # 문자열2 입력받기

print(get_lcs_size(text1, text2))                            # 연산 + 출력