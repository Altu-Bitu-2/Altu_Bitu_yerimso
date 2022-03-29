#필수과제 2: 2503 숫자 야구
import sys                               # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from itertools import permutations       # itertools 모듈의 permutations 함수 제공

input = sys.stdin.readline               # input 함수에 문자열 입력받기

"""
 [숫자 야구]
 서로 다른 세 자리 수에서 위치 + 수 같으면 스트라이크, 위치는 다르고 수가 존재하면 볼
 n개의 질문으로 수와 스트라이크와 볼 개수가 주어질 때, 이를 모두 만족하는 서로 다른 세 자리 정답 수의 개수
 [풀이]
 서로 다른 세 자리수는 123 ~ 987이 가능하다. 이는 총 865가지
 질문 n의 범위는 최대 100
 따라서 123부터 하나씩 증가시키며 정답이 되는지 검사해도 865 * 100 * 3(자릿수)으로 접근 충분히 가능!
"""


def count_strike_ball(s1, s2):           # a가 답이라고 가정하고, b에 대한 스트라이크와 볼 수를 세서 리턴한다.
    strike = 0                           # 스트라이크를 0으로 초기화
    ball = 0                             # 볼을 0으로 초기화
    for i in range(3):                   # 자릿수만큼 반복
        if s2[i] == s1[i]:               # 위치와 숫자가 모두 맞으면
            strike += 1                  # 스트라이크의 개수 추가
        elif s2[i] in s1:                # 숫자는 있지만 위치가 다르면
            ball += 1                    # 볼의 개수 추가

    return (strike, ball)                # 스트라이크와 볼의 개수 리턴



def play_game(questions):                # 반복문으로 직접 경우의 수 구하는 함수
    answer = 0                           # 정답 후보의 개수를 0으로 초기화

    for i in range(123, 987 + 1):        # 123부터 987까지 반복
        s1 = str(i)                      # i를 string으로 형변환해서 s1에 저장함

        if '0' in s1:                    # 0은 포함되지 않음
            continue                     # 다시 for문의 처음으로 돌아감

        if s1[0] == s1[1] or s1[0] == s1[2] or s1[1] == s1[2]:      # 같은 수를 중복해서 사용할 수 없음
            continue                     # 다시 for문의 처음으로 돌아감

        answer += 1                      # 정답 후보 +1

        for s2, count in questions:      # 민혁이가 질문한 세자리 수와 영수가 답한 스트라이크, 볼 개수를 n번 반복
            if count_strike_ball(s1, s2) != count:                  # s1을 답이라고 가정하고, 민혁이가 질문한 세자리 수에 대한 스트라이크와 볼 수가 count와 일치하지 않으면
                answer -= 1              # 조건을 만족하지 않기 때문에, 후보에서 제외하고 break
                break                    # for문으로 돌아가서 민혁이가 질문한 다른 세자리 수를 확인한다

    return answer                        # 정답 후보의 개수를 리턴



def play_game_with_permutations(questions):        # permutation 이용해서 경우의 수 구하는 함수
    digits = [str(i) for i in range(1, 10)]        # 1부터 9까지 string으로 형변환 후 digits 리스트에 저장한다.

    answer = 0                                     # 정답 후보의 개수를 0으로 초기화

    for s1 in permutations(digits, 3):             # 123부터 987까지 서로 다른 세자리수를 반복
        answer += 1                                # 정답 후보의 개수 + 1
        for s2, count in questions:                # 민혁이가 질문한 세자리 수와 영수가 답한 스트라이크, 볼 개수를 n번 반복
            if count_strike_ball(s1, s2) != count: # s1을 답이라고 가정하고, 민혁이가 질문한 세자리 수에 대한 스트라이크와 볼 수가 count와 일치하지 않으면
                answer -= 1                        # 조건을 만족하지 않기 때문에, 후보에서 제외하고 break
                break                              # for문으로 돌아가서 민혁이가 질문한 다른 세자리 수를 확인한다

    return answer                                  # 정답 후보의 개수를 리턴


# 입력
n = int(input())            #몇번이나 질문했는지 입력받기

initialize_input = lambda x: (x[0], (int(x[1]), int(x[2])))         # 세자리 수는 string, 스트라이크와 볼 수는 int형으로 tuple로 묶어서 저장
questions = [initialize_input(input().split()) for _ in range(n)]   # initialize_input을 질문 개수만큼 리스트에 저장

print(play_game_with_permutations(questions))                       # 연산 + 출력