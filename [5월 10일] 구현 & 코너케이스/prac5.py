# 선택과제 3: 2607 비슷한 단어

import sys                              # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import Counter         # collections 모듈의 Counter 클래스 사용

input = sys.stdin.readline              # input 함수에 문자열을 입력받음

SIZE = 26                               # 사이즈 26

"""
 [비슷한 단어]
 단어가 같은 구성일 조건
 1. 두 개의 단어가 같은 종류의 문자로 이루어짐
 2. 같은 문자는 같은 개수만큼 있음
 비슷한 단어의 조건
 1. 한 단어에서 한 문자를 더하거나, 빼면 같은 구성이 됨
    -> 두 단어에서 다른 문자의 개수가 총 1개
 2. 한 단어에서 한 문자를 바꾸면 같은 구성이 됨
    -> 두 단어에서 다른 문자의 개수가 총 2개
    -> !주의! 이때, 두 단어의 길이가 같아야 함 cf) doll | do
 <Counter>
 - iterable한 객체를 받아서 횟수를 기록하여 Counter 객체로 반환.
 - 이때 Counter 객체는 유사 dictionary라고 생각할 수 있다.
 - 주의할 점은, 일반 dictionary와는 다르게 default 값이 0으로 설정되어 있어, 삽입하지 않은 키 값에 대한 조회가 가능하다.
"""

# 입력
n = int(input())                                                # 단어의 개수 입력

source = input().rstrip()                                       # 첫번째 단어 입력받기
source_cnt = Counter(source)                                    # 첫번째 단어를 Counter 객체로 변환해서 source_ct에 저장
ans = 0                                                         # 비슷한 단어의 개수 0으로 초기화

alphabets = [chr(i + ord('A')) for i in range(SIZE)]            # 알파벳 리스트

for _ in range(n - 1):                                          # 나머지 단어 확인하기
    target = input().rstrip()                                   # 단어 입력
    diff = 0                                                    # 차이 0으로 초기화
    target_cnt = Counter(target)                                # Counter 객체로 변환

    for key in alphabets:                                       # 모든 알파벳 반복
        diff += abs(target_cnt[key] - source_cnt[key])          # Counter 객체이므로 키가 존재하는지 확인 불필요

    if diff <= 1 or (diff == 2 and len(target) == len(source)): # 알파벳 종류의 차이가 1 이하이거나 차이가 2이고 차이가 2이고 길이가 같으면
        ans += 1                                                # 비슷한 단어의 개수 + 1

print(ans)                                                      # 비슷한 단어의 개수 출력