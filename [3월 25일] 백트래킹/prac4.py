# 선택과제 2: 15663 N과M

import sys                   # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline   # input 함수에 문자열 입력받기

"""
 1. 우선 수열을 사전 순으로 증가하는 순서로 출력해야 하므로 주어진 수열을 오름차순 정렬
 2. 이 상태에서 우선, 같은 위치의 수를 또 선택하지 않도록 중복제거 (check 배열 사용)를 해줌
 3. 그 후, 중복되는 "수열"을 거르는 방법은 이전에 선택한 값을 변수에 저장해서, 수열을 만들다 다시 루트 노드로 돌아왔을 때
    이전에 선택한 값과 같은 값이면 넘어가면 됨! -> 어차피 같은 수이므로 같은 과정 반복해서 똑같은 수열이 나올 것
"""


def backtracking(idx, m):     # 수열을 사전 순으로 출력하는 함수
    if idx == m:              # 만약 자리 수가 m과 같다면
        print(*answer)  # *list -> 리스트의 요소를 하나씩 풀어서 print()에 인자로 넣어줌
        # print(*[1, 2, 3]) == print(1, 2, 3)
        return

    prev = 0  # 이전에 선택한 값
    for i in range(n):  # n-1만큼 반복
        if not checked[i] and arr[i] != prev:   # checked[i]가 false이고 arr[i]가 이전의 선택한 값과 다르면
            checked[i] = True    # checked[i]는 True로 바뀌고
            prev = arr[i]        # 이전에 선택한 값은 arr[i]로 바뀜
            answer[idx] = arr[i]       # answer[idx]는 arr[i]가 됨
            backtracking(idx + 1, m)   # idx+1번 자리의 수를 정하기 위해 backtracking함수를 불러옴
            checked[i] = False         # checked[i]의 수는 false로 바뀜

    return  # 가능한 모든 수열 출력후 함수 종료


n, m = map(int, input().split())         # N과 M 입력받기
arr = list(map(int, input().split()))    # N개의 자연수 입력하기
arr.sort()                               # N개의 자연수 정렬하기
checked = [False] * n                    # N개의 빈 요소를 가진 리스트 만들기
answer = [0] * m                         # 요소가 m개인 리스트 만들기

backtracking(0, m)                       # 수열 사전 순으로 출력하기