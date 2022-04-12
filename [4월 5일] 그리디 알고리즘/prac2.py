# 선택과제 2: 1080 행렬

import sys                     # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
input = sys.stdin.readline     # input 함수에 문자열 입력받기

"""
[행렬]
- (0, 0) 인덱스부터 부분행렬을 만들 수 있는 마지막 인덱스까지 검사하며 그리디하게 푸는 문제
- A, B 행렬의 현재 인덱스 값이 서로 다르다면 A 행렬에서 현재 인덱스로 '시작'하는 3x3 크기만큼의 부분 행렬 원소 뒤집기
- 검사가 모두 끝난 후, A와 B가 서로 다르다면 바꿀 수 없는 경우임
 !주의! string은 immutable하므로, 입력을 받고 리스트 등으로 변환해 한 글자씩 나눠주어야 함.
"""


def flip_square(row, col, matrix):               # 부분행렬 뒤집는 함수
    for x in range(row, row+3):                  # 기준이 되는 행부터 아래 두번째 행까지 반복
        for y in range(col, col+3):              # 기준이 되는 열부터 오른쪽 두번째 열까지 반복
            matrix[x][y] = 1 - matrix[x][y]      # 각 위치의 값 0->1, 1->0으로 바꾸기
    return                                       # 함수 종료


def is_same(n, m, matrix_A, matrix_B):                 # 두 행렬이 같은지 확인하는 함수
    for i in range(n):                                 # 모든 행 반복
        for j in range(m):                             # 모든 열 반복
            if matrix_A[i][j] != matrix_B[i][j]:       # 만약 행렬 A의 어떤 위치의 값이 같은 위치의 행렬 B의 값과 다르면
                return False                           # False를 리턴
    return True                                        # 다른 값이 없으면 True로 종료

# 입력
n, m = map(int, input().split())                                         # 행렬의 크기 N, M 입력받기

matrix_A = [list(map(int, list(input().rstrip()))) for _ in range(n)]    # 행렬 A 입력받기
matrix_B = [list(map(int, list(input().rstrip()))) for _ in range(n)]    # 행렬 B 입력받기

count = 0   # 뒤집는 횟수

for i in range(n-2):                               # n-2번 반복 (3x3 크기의 행렬만 뒤집을 수 있으므로)
    for j in range(m-2):                           # m-2번 반복 (3x3 크기의 행렬만 뒤집을 수 있으므로)
        if matrix_A[i][j] != matrix_B[i][j]:       # 만약 행렬 A,B의 같은 위치의 값이 다를 때
            flip_square(i, j, matrix_A)            # 3X3 행렬 뒤집기
            count += 1                             # 연산 + 1

# 출력
if is_same(n, m, matrix_A, matrix_B):              # 모든 연산 끝에 행렬 A,B가 같아지면
    print(count)                                   # 연산 횟수를 출력
else:                                              # 모든 연산 후에도 행렬 A,B가 다를 때
    print(-1)                                      # -1 출력