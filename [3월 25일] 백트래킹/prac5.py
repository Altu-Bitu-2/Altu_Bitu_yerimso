# 선택과제 3: 14888 연산자 끼워넣기

import sys                    # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
sys.stdin.readline            # 문자열 입력받기

"""
[연산자 끼워넣기]
연산자를 모두 돌려보면서 배치한 후, 각 연산자에 따른 값 계산
"""

MAX = 10**9  # Max는 10억

add = lambda x, y: x + y     # add는 x+y로 처리
sub = lambda x, y: x - y     # sub는 x-y로 처리
multiply = lambda x, y: x * y   # multiply는 x*y로 처리

# C++14 방식에 맞추어 나누기 함수 작성
def division(x, y):            # 나누기 함수 정의
    if x < 0:                  # 만약 x가 음수라면
        return - (-x // y)     # -x를 y로 나눈 몫을 음수로 바꾼것으로 정의
    return x // y              # x가 양수면 x를 y로 나눈 몫으로 정의

# 인덱스에 맞는 연산을 하기 위해 함수를 리스트에 저장
functions = [add, sub, multiply, division]

# cnt: 수 인덱스, value: 현재까지 연산 결과
def backtracking(cnt, value):     # 만들 수 있는 식의 최댓값, 최솟값을 찾는 함수
    global max_value, min_value   # max_value, min_value 변수를 전역 변수로 설정
    if cnt == n:    # 연산이 모두 완료 되었다면
        max_value = max(max_value, value)   # 지금 값과 max_value를 비교하여 최댓값 설정
        min_value = min(min_value, value)   # 지금 값과 min_value를 비교하여 최솟값 설정
        return    # 함수 종료

    for i in range(4):       # 연산자의 개수만큼 반복
        if operator[i] > 0:  # 만약 연산자의 개수가 0보다 크면
            operator[i] -= 1   # 연산자의 개수 - 1
            backtracking(cnt + 1, functions[i](value, numbers[cnt]))    # i번째 함수에 value와 numbers[cnt]를 인자로 넘겨주어 계산함
            operator[i] += 1   # 연산자의 개수 + 1
    return  # 함수 종료

# 입력
n = int(input())   # 수의 개수 입력받기
numbers = list(map(int, input().split()))   # n개의 수 입력받기
operator = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈의 개수 입력받기

max_value = -MAX   # 현재까지 최대값 기록
min_value = MAX    # 현재까지 최솟값 기록

# 연산
backtracking(1, numbers[0])
# 출력
print(max_value, min_value, sep='\n')