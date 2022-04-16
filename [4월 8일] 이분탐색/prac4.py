# 선택과제 2: 16401 과자 나눠주기

import sys                   # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
input = sys.stdin.readline   # input 함수에 문자열 입력받기

"""
 [과자 나눠주기]
 n개의 과자가 있을 때 m명의 조카에게 각각 같은 길이로 줄 수 있는 과자의 최대 길이를 구하는 문제
 -> 특정 과자 길이에 대하여 m명의 조카에게 나누어 줄 수 있는가?
 left: 과자 길이의 최솟값 -> 1
 right: 과자 길이의 최댓값
"""


def split_snack(length, snacks):                 # 내림차순 정렬된 snacks 리스트에서 length 길이의 과자를 몇개 만들 수 있는지 개수를 세어 리턴하는 함수
    count = 0                                    # 과자의 개수 0으로 초기화
    for l in snacks:                             # 모든 과자 반복
        if l < length:                           # 만약 과자의 길이가 length보다 작으면
            return count                         # 현재 과자의 개수 리턴하기
        count += l // length                     # count + 현재 막대과자에서 만들어질 수 있는 length 길이의 과자 수

    return count                                 # count 리턴하기

def binary_search(m, snacks):                    # 조카 1명에게 줄 수 있는 막대과자의 최대 길이를 출력하는 함수
    left = 1                                     # left 초기값 1로 설정
    right = snacks[0]                            # right 초기값 가장 긴 막대과자의 길이로 설정
    while left <= right:                         # right가 left보다 길거나 같을 때까지만 반복
        mid = (left + right) // 2                # 중간값 구하기
        if split_snack(mid, snacks) >= m:        # 만약 중간값으로 과자의 길이를 설정했을 때 만들 수 있는 과자의 개수가 조카의 수보다 많으면
            left = mid + 1                       # left 값을 중간값 + 1로 변경
        else:                                    # 만약 중간값으로 과자의 길이를 설정했을 때 만들 수 있는 과자의 개수가 조카의 수보다 적으면
            right = mid - 1                      # right 값을 중간값 - 1로 변경
    return left - 1                              # left - 1 값 리턴하기

m, n = map(int, input().split())                 # 조카의 수 M, 과자의 수 N 입력받기
snacks = list(map(int, input().split()))         # 과자 N개의 길이 입력받기
snacks.sort(reverse=True)                        # 내림차순 정렬

print(binary_search(m, snacks))                  # 연산 + 출력