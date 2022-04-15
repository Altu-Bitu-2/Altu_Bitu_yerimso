# 선택과제 3: 2812 크게 만들기

import sys                        # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline        # input 함수에 문자열 입력받기

"""
[크게 만들기]
- 어차피 남는 수는 n-k자리 수!
- 가능한 앞자리에 큰 수를 배치하는 것이 유리하다.
- 수의 앞자리부터 탐색하며, 스택에 차례대로 저장
- 직전 자리보다 큰 수가 나오면 스택의 top이 자신보다 크거나 같아질 때까지 pop한 뒤에 추가
 ex) 1924 에서 2개를 지워서 큰 수를 만들어야 한다면
    stack: []           이번 숫자 '1' -> stack: ['1']
    stack: ['1']        이번 숫자 '9' -> stack: ['9']
    stack: ['9']        이번 숫자 '2' -> stack: ['9', '2']
    stack: ['9', '2']   이번 숫자 '4' -> stack: ['9', '4']

    답: 94
- 정확히 k개의 수를 지워야 함을 유의
"""


def find_max_number(n, k, num):               # 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수 찾기
    stack = []                                # 스택 생성
    count = 0                                 # 지운 숫자의 개수 count변수에 저장

    for digit in num:                         # num
        while count < k and stack and digit > stack[-1]:    # 지운 숫자의 개수가 k보다 작고 stack에 요소가 있고, digit이 stack의 마지막 숫자보다 크다면
            stack.pop()                       # stack의 마지막 수를 pop하기
            count += 1                        # 지운 횟수 + 1

        stack.append(digit)                   # stack에 digit 추가하기
    return ''.join(stack[:n - k])             # stack에서 처음부터 n-k-1번째 숫자까지 리턴


# 입력
n, k = map(int, input().split())              # N과 K 입력
num = list(input().rstrip())                  # N자리 숫자 입력받기

# 연산 + 출력
print(find_max_number(n, k, num))             # 연산 + 출력