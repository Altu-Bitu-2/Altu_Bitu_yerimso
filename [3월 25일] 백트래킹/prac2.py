# 필수과제 2: 1205 등수 구하기

import sys                       # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline       # input 함수에 문자열 입력받기

"""
[등수 구하기]
1. n = 0일 때, 고려
2. 등수는 p보다 작지만, 랭킹 리스트에 들어가지 못하는 경우 고려
.find(value): value가 있는 첫번째 인덱스를 리턴, 없으면 에러 발생
입력된 점수를 기존 리스트에 넣고 인덱스 구하기 -> 해당 점수의 첫번째 인덱스 리턴
.count(value): 리스트에서 value의 수를 세어 리턴, 없으면 에러 발생
전체 점수 중 동점자의 수 구하기 -> 첫번째 등수(인덱스 + 1) + 동점자 수 - 1 
                                = 첫번째 인덱스 + 동점자 수 
                                = 해당 점수의 마지막 등수
마지막 등수가 p를 넘지 않으면, 첫번째 인덱스로 구한 등수가 정답
"""

# 입력
n, new_score, p = map(int, input().split())   # 리스트에 있는 점수, 태수의 새로운 점수, 랭킹 리스트에 올라갈 수 있는 점수의 개수 입력

if n == 0:                                    # 만약 리스트에 있는 점수가 0개라면
    answer = 1                                # 태수는 랭킹 1위
else:                                         # 리스트에 있는 점수가 1개 이상이면
    # 입력
    scores = list(map(int, input().split()))  # 현재 랭킹 리스트에 있는 점수 비오름차순으로 입력

    # 해당 점수의 가장 상위 등수 구하기
    scores.append(new_score)                  # 태수의 점수를 score list에 추가하기
    scores.sort(reverse=True)                 # 랭킹 리스트를 비오름차순으로 정렬하기
    first_idx = scores.index(new_score)       # 태수의 점수 중 가장 작은 등수 구하기

    same_score = scores.count(new_score)      # 동점자가 몇 명 있는지 구하기

    if first_idx + same_score <= p:           # 만약 첫번째 등수(인덱스+1) + 동점자 수 - 1 = 해당 점수의 마지막 등수가 p보다 작다면
        answer = first_idx + 1                # 태수의 등수는 해당 점수의 첫번째 등수
    else:                                     # 이미 스코어 보드가 다 찬 경우
        answer = -1                           # -1 출력

print(answer)                                 # 태수의 등수나 -1 출력