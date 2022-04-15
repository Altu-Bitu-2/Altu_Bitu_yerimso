# 선택과제 1: 2805 나무 자르기

import sys                  # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline  # input 함수에 문자열 입력받기

"""
 [나무 자르기]
 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값은?
 -> 절단기의 높이가 k(임의의 값)일 때, M미터의 나무를 집에 가져갈 수 있는가?
 left: 절단기의 최소 높이 -> 0
 right: 절단기의 최대 높이 -> 주어진 나무 중 가장 높은 나무 높이
"""


def cut_tree(height, tree):                   # 내림차순으로 정렬된 리스트에서 height보다 값이 큰 요소들에 대해 각 길이와 height의 차를 모두 더해서 리턴
    total = 0                                 # total(절단한 나무의 길이 합) 값 0으로 초기화

    for h in tree:                            # 모든 나무 반복
        if h <= height:                       # 만약 나무가 절단기 높이보다 작다면
            return total                      # total 리턴하기
        total += h - height                   # total에 절단된 나무값 더하기

    return total                              # total 리턴하기


def binary_search(target, tree):              # 절단기의 적정 높이를 리턴하는 함수
    left = 1                                  # left의 초기값 1로 설정
    right = tree[0]                           # right의 초기값 가장 높은 나무의 높이로 설정

    while left <= right:                      # right의 높이가 left의 높이보다 크거나 같을 동안 반복
        mid = (left + right) // 2             # 중간값 구하기
        if cut_tree(mid, tree) >= target:     # 만약 절단한 나무의 길이 합이 target보다 크다면
            left = mid + 1                    # left를 중간값 + 1으로 바꾸기
        else:                                 # 만약 절단한 나무의 길이 합이 target보다 작으면
            right = mid - 1                   # right를 중간값 + 1로 바꾸기

    return left - 1                           # left - 1 값 리턴하기


# 입력
n, m = map(int, input().split())              # 나무의 수 N과 필요한 나무의 길이 M 입력받기
tree = list(map(int, input().split()))        # 나무의 높이 입력받기
tree.sort(reverse=True)                       # 내림차순 정렬
print(binary_search(m, tree))                 # 연산 + 출력