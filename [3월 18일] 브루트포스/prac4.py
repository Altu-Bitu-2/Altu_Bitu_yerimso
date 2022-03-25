#선택과제 2: 1759 암호 만들기
import sys                             # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from itertools import combinations     # itertools 모듈의 combinations 함수 제공
input = sys.stdin.readline             # input 함수에 문자열 입력받기

"""
[암호 만들기]
알파벳은 최대 15개 -> 브루트포스 가능
가능한 모든 조합 만들어서, 검사 통과하면 출력
"""
vowels = ['a', 'e', 'i', 'o', 'u']     # 모음 저장

def is_valid(cypher):                  # combinations으로 만들어진 암호가 유효한 암호인지 판별하는 함수
    count = 0                          # 모음 수
    for i in cypher:                   # cypher의 문자 개수만큼 반복
        if i in vowels:                # 만약 문자 i가 모음이라면
            count += 1                 # count + 1


    return count >= 1 and len(cypher) - count >= 2    # 모음 한개 이상, 자음 2개 이상

# 입력
n, m = map(int, input().split())       # 두 정수 L, C 입력받기(공백으로 분리)
alphabets = list(input().split())      # 소문자 알파벳들을 입력받아 alphabets 리스트에 저장

alphabets.sort()                       # 오름차순 암호를 만들기 위해 정렬

# 반복문을 돌리기 위해서 굳이 list로 감싸지 않아도 됨, iterator형은 반복문을 바로 돌릴 수 있음
for cypher in combinations(alphabets, n):
    if is_valid(cypher):               # 유효한 암호일 경우
        print(''.join(cypher))         # '구분자'.join(리스트), 공백이 구분자인 digits 리스트를 문자열로 합쳐서 반환함