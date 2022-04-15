# 선택과제 3: 1477 휴게소 세우기

import sys                    # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline    # input 함수에 문자열 입력받기

"""
 [휴게소 세우기]
 M개의 휴게소를 짓고 난 후에 휴게소가 없는 구간의 최댓값의 최솟값은?
 -> 휴게소가 없는 구간의 최댓값이 k(임의의 수)일 때, M개의 휴게소를 지을 수 있는가?
 left: 휴게소가 없는 구간의 최솟값 -> 1
 right: 휴게소가 없는 구간의 최댓값 -> l - 1
 휴게소 구간의 최댓값이 주어졌을 때, 몇 개의 휴게소 짓는지 구하는 방법
 -> 처음 존재하는 휴게소 구간을 최대값으로 나누면 그 몫이 최대 구간이 최대값이 되도록 현재 구간 안에 설치해야 하는 휴게소 개수!
"""


def calc_rest(dist, n, location):              # m개의 휴게소를 추가해서 휴게소 없는 구간이 dist 이하로 만들 수 있는지 확인하는 함수
    count = 0                                  # 휴게소의 개수
    for i in range(n - 1):                     # 도로의 모든 휴게소 사이의 구간 구하기
        if location[i + 1] - location[i] > dist:                      # 두 휴게소 사이의 거리가 dist 보다 크면
            count += (location[i + 1] - location[i] - 1) // dist      # count + 구간을 dist로 나눈 몫

    return count                               # 휴게소의 개수 리턴하기



def binary_search(n, m, l, location):          # 가능한 최댓값을 구하는 형식
    left = 1                                   # left의 초기값 1로 설정
    right = l - 1                              # right의 초기값 고속도로의 길이 - 1 (고속도로의 끝에 휴게소 X)
    while left <= right:                       # right의 길이가 left의 길이보다 크거나 같을 때까지 반복
        mid = (left + right) // 2              # 중간값 구하기
        if calc_rest(mid, n, location) <= m:   # 휴게소 간의 거리가 mid일 때 만들어지는 휴게소의 개수가 m보다 작거나 같으면
            right = mid - 1                    # right를 중간값 - 1로 바꾸기
        else:                                  # 휴게소 간의 거리가 mid일 때 만들어지는 휴게소의 개수가 m보다 크면
            left = mid + 1                     # left를 중간값 + 1로 바꾸기
    return right + 1                           # right + 1 리턴하기


# 입력
n, m, l = map(int, input().split())            # 현재 휴게소의 개수 N, 더 지으려고 하는 휴게소의 개수 M, 고속도로의 길이 L 입력받기
location = list(map(int, input().split()))     # 현재 휴게소의 위치 입력받기
# 도로의 시작과 끝을 추가하여, 도로 시작 ~ 첫 휴게소, 마지막 휴게소 ~ 도로 끝 구간도 체크할 수 있도록 한다.
location.append(0)                             # 도로의 시작 추가
location.append(l)                             # 도로의 끝 추가
location.sort()                                # 인접한 휴게소의 거리를 계산해야 하므로 정렬

print(binary_search(n + 2, m, l, location))    # 양 끝값을 추가했으므로 n+2 대입