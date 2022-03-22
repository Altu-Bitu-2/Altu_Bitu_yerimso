#선택과제 3: 2436 공약수
import sys                #파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline      #input 함수에 문자열 입력받기

"""
[공약수]
최대공약수: gcd, 최소공배수: lcm
gcd * lcm = A * B이고,
A = gcd * a, B = gcd * b로 나타낼 수 있다. (이때, a와 b는 서로소)
따라서 gcd * lcm = A * B = gcd * gcd * a * b,
lcm / gcd = a * b
A+B의 최소 -> a+b의 최소 -> a, b의 차가 최소가 되도록
"""


def calc_gcd(a, b):                         # a > b일 때, a와 b의 최대공약수를 리턴
    if b == 0:                              #만약 b가 0이면
        return a                            #a를 리턴한다
    return calc_gcd(b, a % b)               #유클리드 호제법: b와 a를 b로 나눈 나머지의 최대공약수를 구함


gcd, lcm = map(int, input().split())        #두 수를 입력받아 공백으로 구분하고 앞의 수는 최대공약수에 뒤의 수는 최소공배수로 저장한다

ab = lcm // gcd                             #서로소인 a와 b의 곱은 최소공배수를 최대공약수로 나눈 몫
root_ab = ab ** (1 / 2)                     #ab의 제곱근을 계산

# root(ab)부터 1까지
for i in range(int(root_ab), 0, -1):        #ab의 제곱근에서 0까지 -1의 간격으로 반복문을 실행
    if ab % i > 0:                          #만약 ab를 i로 나눈 나머지가 0보다 크면
        continue                            #for문으로 돌아감

    a = i                                   #a에 i를 저장
    b = ab // i                             #b에 ab를 i로 나눈 몫을 저장

    # a와 b가 서로소인지 확인 - a는 항상 b보다 작다
    if calc_gcd(b, a) == 1:                 #만약 a와 b가 서로소이면
        break                               #for문을 탈출함

print(a * gcd, b * gcd)                     #a에 최대공약수를 구한 값과 b에 최대공약수를 구한 값을 출력: A,B
