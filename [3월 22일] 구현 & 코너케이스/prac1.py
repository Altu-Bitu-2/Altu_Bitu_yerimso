# 선택과제 1: 1316 그룹단어체커
import sys                     # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline     # input 함수에 문자열 입력받기

"""
[그룹 단어 체커] - 단순 구현 문제
- 이미 등장한 알파벳 저장할 set() 선언 (탐색 O(1))
- 처음 등장하는 알파벳은 set에 추가하고, 무리에서 떨어졌는데 이미 등장한 알파벳이면 그룹 단어가 아니다.
"""


def is_group_word(word):       # 입력받은 단어가 그룹단어인지 판별하는 함수
    checked = set()            # 이미 등장한 알파벳을 저장하는 set 선언
    prev = None                # 직전에 등장한 알파벳을 기억해둠

    for c in word:             # 단어에 있는 문자 개수만큼 반복
        if c == prev:          # 만약 현재 알파벳이 직전에 등장한 알파벳과 같다면
            continue           # for문으로 돌아감

        if c in checked:       # 현재 알파벳과 직전의 알파벳과 다르면서 현재 알파벳이 checked set에 있을 때
            return False       # False를 리턴함

        checked.add(c)         # 현재 알파벳과 직전의 알파벳이 다르면서 이전에 등장한 적 없는 알파벳일 때, checked set에 추가함
        prev = c               # 현재의 알파벳은 직전의 알파벳으로 저장됨

    return True                # 입력받은 word가 그룹 단어이면 True를 리턴함


# 입력
n = int(input())               # 첫째 줄에 단어의 개수 N을 입력받음

# 입력 + 연산
count = 0                      # 그룹 단어의 개수 0으로 초기화

for _ in range(n):             # 단어의 개수만큼 반복문 시행
    word = input().rstrip()    # 단어를 입력받고 오른쪽 공백을 제거함
    if is_group_word(word):    # 만약 is_group_word()함수의 결과값이 True이면
        count += 1             # 그룹 단어의 개수 + 1

# 출력
print(count)                   # 그룹 단어의 총 개수 출력