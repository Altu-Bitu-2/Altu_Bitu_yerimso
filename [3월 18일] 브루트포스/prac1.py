#필수과제 1: 10757 큰수 A+B
import sys                   # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
input = sys.stdin.readline   # input 함수에 문자열 입력받기


"""
[큰수 A+B]
 1. 한 자릿수씩 더해서 리스트에 저장
 2. 한 자릿수씩 더할 때, 값이 10을 넘어가는 경우 고려 -> 자릿수 올림
 3. A와 B의 길이가 같지만, 둘의 합의 길이는 다른 경우 고려 -> 마지막 자리에서 올림
 4. A와 B의 길이가 다른 경우 고려 -> 더 긴 길이 처리 주의
"""

def calcPlus(a, b):                             # 항상 a가 b보다 자리수가 크다고 가정
    if len(a) < len(b):                         # 만약 정수 b의 길이가 정수 a의 길이보다 길다면
        a, b = b, a                             # a와 b의 순서를 바꿈, 자릿수가 더 높은 수가 a가 되도록

    ans = [0] * (len(a) + 1)                    # 정답 저장할 배열


    for i in range(-1, -len(b)-1, -1):          # -1, -2 ... 일의 자리부터 뒤에서 더하기 위해
        ans[i] += int(a[i]) + int(b[i])         # carry(올림) + a + b
        ans[i-1] = ans[i] // 10                 # carry가 존재한다면 미리 표기
        ans[i] %= 10                            # 올림 후 나머지만 저장

    for i in range(-len(b)-1, -len(a)-1, -1):   # 정수 a의 남은 자리 부분도 더하기
        ans[i] += int(a[i])                     # carry + a
        ans[i-1] = ans[i] // 10                 # carry가 존재한다면 미리 표기
        ans[i] %= 10                            # 올림 후 나머지만 저장

    # 맨 앞자리 0이 출력되지 않도록 int() 적용
    return int(''.join(map(str, ans)))          # '구분자'.join(리스트), 공백이 구분자인 digits 리스트를 문자열로 합쳐서 반환함

# 입력
a, b = input().split()                          # 정수 A와 B를 입력받음, 공백으로 분리
# 연산 + 출력
print(calcPlus(a, b))                           # calcPlus 함수를 이용해서 덧셈 연산을 수행 + 결과 출력