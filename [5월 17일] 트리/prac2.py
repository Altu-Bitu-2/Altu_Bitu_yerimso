# 필수과제 2: 1713 후보 추천하기

import sys                       # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
input = sys.stdin.readline       # input 함수에 문자열을 입력받음

SIZE = 100                       # 학생 번호

"""
 [후보 추천하기]
 1. 비어있는 사진틀이 없는 경우, 가장 추천수가 작은 학생 중 게시 시간이 오래된 학생을 삭제
 2. 후보 학생을 바로 찾기 위해 본 풀이는 딕셔너리 컨테이너를 사용해 구현
 !주의! 게시 시간 정보 저장 시, 후보로 올라간 가장 첫 시간을 저장. 이미 후보에 있는데 게시 시간이 갱신되지 않도록 주의.
"""

n = int(input())                             # 사진틀의 개수 입력받기
k = int(input())                             # 전체 학생의 총 추천 횟수 입력받기
arr = list(map(int, input().split()))        # 추천받은 학생을 나타내는 번호 입력받기

number = [0]*(SIZE + 1)                      # 학생 리스트 생성
candidate = dict()                           # 후보자를 딕셔너리 자료형으로 저장
for idx, student in enumerate(arr):          # 인덱스와 원소를 동시접근하면서 루프를 돌림
    if student in candidate:                 # 이미 사진이 올라와 있는 경우
        candidate[student][0] += 1           # 추천 횟수 + 1
    else:                                    # 이미 사진이 올라와 있는 경우가 아니면
        if len(candidate) == n:              # 비어있는 사진 틀이 없을 때
            # 추천 횟수가 가장 적은 학생 찾기
            students = sorted(candidate.keys(), key=lambda x:candidate[x])
                                             # 추천 횟수 순서대로 정렬
            candidate.pop(students[0])       # 추천 횟수가 가장 적은 학생 탈락
        candidate[student] = [1, idx]        # 후보자에 추천받은 학생 올리기

print(*sorted(candidate.keys()))             # 최종 후보를 정렬 후 순서대로 출력