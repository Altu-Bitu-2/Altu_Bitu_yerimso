# 선택과제 2: 1009 분산처리
import sys                                  # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline                  # input 함수에 문자열 입력받기

"""
[분산처리]
- a^b의 일의 자리를 구하는 문제
- 일의 자리는 0~9 중 하나 이므로, 어떤 수를 계속 곱해 나가면 일의 자리는 패턴을 가지게 되어 있음
    ex) 2 -> 4 -> 8 -> 6 -> 2 ... 
- 0~9까지 일의 자리 패턴을 미리 구한 후, (b % 패턴의 길이)번째 수를 출력하면 된다.
- 0이 나올 경우 10번 컴퓨터가 처리하므로, 0이 출력되지 않도록 예외처리
"""

last_digit = [[i] for i in range(10)]        # 0부터 9까지의 패턴
size = []                                    # 패턴의 길이

for i in range(10):                          # 0부터 9까지 반복
    temp = i                                 # temp에 i를 저장
    while i != (temp * i) % 10:              # i와 1의 자리 수가 같지 않을 때까지 반복
        temp *= i                            # temp에 다시 i를 곱함
        temp %= 10                           # temp의 일의 자리를 구함
        last_digit[i].append(temp)           # last_digit[i] list에 temp를 추가함
    size.append(len(last_digit[i]))          # size list에 last_digit list의 길이를 추가

# 입력
t = int(input())                             # 테스트케이스의 개수 T를 입력받음

# 입력 + 연산
for _ in range(t):                           # 테스트케이스의 개수만큼 반복
    a, b = map(int, input().split())         # 각 테스트케이스마다 정수 a, b를 입력받음
    a %= 10                                  # 정수 a의 일의 자리 수를 구함

    if a == 0:                               # 만약 일의자리 수가 0이면
        print(10)                            # 10을 출력
        continue                             # 다시 for문으로 돌아감

    print(last_digit[a][b % size[a] - 1])    # 마지막 데이터가 처리될 컴ㅍ터의 번호를 출력