#선택과제 2: 14490 백대열
import sys                              #파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
input = sys.stdin.readline              #input 함수에 문자열 입력받기

"""
[백대열]
- n과 m의 최대공약수를 찾아서 나눠준다.
"""

def calc_gcd(a, b):                     # a > b일 때, a와 b의 최대공약수를 리턴
    if b == 0:                          #만약 b가 0이면
        return a                        #a를 리턴하기
    return calc_gcd(b, a % b)           #유클리드 호제법: b와 a를 b로 나눈 나머지의 최대공약수를 구함

# 입력
n, m = map(int, input().split(':'))     # ':' 기준으로 나누기, n과 m 입력받기

# 연산 + 출력
gcd = calc_gcd(max(n, m), min(n, m))    #a>b일 때 calc_gcd 함수를 실행하기 위해 max, min 이용
# / 로 계산하면 1.0 과 같이 소수점이 표기되므로 주의
print(n // gcd, ':', m // gcd, sep='')  #'n을 최대공약수로 나눈 값 : m을 최대공약수로 나눈 값' 을 출력, 공백을 없앰
