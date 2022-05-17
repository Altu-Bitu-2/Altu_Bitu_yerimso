# 선택과제 2: 3613 Java vs C++

import sys                    # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline    # input 함수에 문자열을 입력받음

"""
 [Java vs C++]
 1. 입력으로 주어진 변수가 C++ 형식에도 맞고, JAVA 형식에도 맞을 수 있음 (ex. name)
 2. "Error!"인 경우 
    2-1. (공통) 알파벳 소문자로 시작하지 않는 변수
    2-2. (Java)
        - 언더바('_')가 등장하는 변수
    2-3. (C++)
        - 언더바('_')가 연속해서 등장하는 변수
        - 대문자가 등장하는 변수
(주의) python에서 string은 immutable한 객체이다 -> 변경이 불가능
ex) 아래 코드를 실행해보세요
    a = "hello"
    a[0] = "H" 
"""


def to_cpp(word):                                           # cpp 형식으로 바꾸는 함수
    result = ""                                             # result null로 초기화

    for c in word:                                          # word의 모든 문자 반복
        if c == c.upper():                                  # 만약 현재 문자가 대문자면
            result += '_'                                   # 언더바 추가
        result += c.lower()                                 # 현재 문자를 소문자로 바꿔서 출력

    return result                                           # result 반환


def to_java_if_possible(word_list):                         # 가능하면 java형식으로 바꾸는 함수
    result = []                                             # result 리스트 만들기
    for word in word_list:                                  # word_list에 있는 모든 단어
        if len(word) == 0 or word != word.lower():          # 만약 단어의 개수가 0이거나 전부 소문자가 아니면
            return "Error!"                                 # Error! 출력
        result.append(word.capitalize())                    # result에 단어의 첫 글자를 대문자로 변경해서 추가

    result[0] = result[0].lower()                           # 첫 단어는 capitalize하면 안됨
    return ''.join(result)                                  # result의 단어 모두 붙여서 반환


# 입력
word = input().rstrip()                                     # 변수명 입력받기

if (not word[0].isalpha()) or word[0] == word[0].upper():   # 공통 예외에 포함되는 경우
    print("Error!")                                         # Error! 출력
elif word.isalpha():                                        # Java식 변수인 경우
    print(to_cpp(word))                                     # C++식 변수로 출력
else:                                                       # 나머지 경우 (error || cpp식 변수)
    word_list = word.split('_')                             # _로 분리하기
    print(to_java_if_possible(word_list))                   # 가능하면 java식 변수로 바꿔서 출력