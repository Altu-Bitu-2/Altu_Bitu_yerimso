#필수과제 1: 1213 팰린드롬 만들기
import sys  #파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import Counter  #collections 모듈의 counter 클래스 사용: 단어에 포함된 각 알파벳의 글자 수를 셀 수 있음

input = sys.stdin.readline   #input변수에 문자열을 받음

"""
 [팰린드롬 만들기] - 단순 구현 문제
 팰린드롬 문자열은 part1(part3의 대칭) + part2(최대 1글자) + part3(part1의 대칭)으로 이루어진다.
 1. 팰린드롬 문자열을 만들기 위해, 각 알파벳이 몇 개씩 존재하는지 리스트에 저장한다.
 2. 사전순으로 앞선 팰린드롬 수를 만들어야 하므로, 'A'부터 시작해서 part1을 문자의 개수에 맞춰 더해나간다.
 3. 만약 알파벳의 개수가 홀수인 경우, part2에 할당하고, 이미 part2에 문자가 있는 경우엔 팰린드롬을 만들 수 없다.
"""


def make_palindrome(text):
    # 각 알파벳의 수를 가지고 팰린드롬 문자열을 리턴하는 함수
    # 만들 수 없으면 "I'm Sorry Hansoo" 리턴
    part1 = ""  #짝수개인 알파벳들의 문자열
    part2 = ""  #홀수개인 알파벳의 문자열

    # Counter(text): 각 문자가 몇개씩 들어있는지 dictionary 형태로 돌려줌
    # .items() : key와 value를 짝 지어서 돌려줌
    # sorted - 사전적으로 가장 앞서는 문자열을 만들기 위해 정렬
    alphabets = sorted(Counter(text).items())
    #입력받은 문자열에서 각 문자가 몇개씩 들어있는지 파악하고 알파벳을 key값으로 알파벳의 개수를 value로 짝지어 받은 후 알파벳 순으로 정렬한다.

    for key, value in alphabets: #모든 알파벳을 홀수인지 짝수인지 확인하고 팰린드롬 형태로 바꿀수 있는지 판단
        if value % 2 == 1:  #만약 알파벳이 홀수개인지 확인한다.
            # 만약 가운데 글자가 있다면 더 이상 불가능
            if (len(part2) == 1):  #이미 홀수개인 알파벳이 있는지 확인한다.
                # 주의! 문자열에 '가 들어있기 때문에, ""로 감싸주어야 합니다.
                return "I'm Sorry Hansoo"  #이미 홀수개인 알파벳이 있다면 I'm Sorry Hansoo를 리턴한다.
            # 비어있다면, 할당
            part2 = key  #이전에 홀수개인 알파벳이 없었을 경우 part2에 홀수개인 알파벳을 저장한다.

        part1 += key * (value // 2)
        #짝수개인 알파벳이라면 절반만 part1에 추가로 저장한다.
        #홀수개인 알파벳이라면 (key-1)/2개만 part1에 추가로 저장한다.

    return part1 + part2 + part1[::-1]
    #정렬되어 있는 part1 다음 유일한 홀수개 알파벳 part2가 오고 part1의 역순인 문자열이 뒤에 온다.


# 입력
text = input().rstrip()  #문자열을 입력받고 오른쪽의 공백을 제거한다.

# 연산 + 출력
print(make_palindrome(text))  #팰린드롬 문자열이나 I'm Sorry Hansoo를 출력한다.