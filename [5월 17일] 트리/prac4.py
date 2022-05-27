# 선택과제 2: 1068 트리

import sys                       # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline       # input 함수에 문자열을 입력받음

"""
 [트리]
 기존 리프 노드 개수를 세는 dfs 탐색에서 지우는 정점을 만나면 더 이상 탐색하지 않고 0을 리턴
 !주의! 지우는 정점이 해당 부모 노드의 유일한 자식 노드였을 경우, 해당 정점을 지우면 부모 노드가 리프 노드가 돼서 개수가 1 증가함을 주의
 !주의! 루트 노드가 항상 0이 아님을 주의
"""



def erase_leaf_cnt(node, erase_node):         # 주어진 정점을 지웠을 때의 리프 노드의 수
    if node == erase_node:                    # 만약 지울 노드가 루트 노드이면
        return 0                              # 더 이상 탐색하지 않고 0을 리턴
    if not tree[node] or (len(tree[node]) == 1 and tree[node][0] == erase_node):
                                              # 만약 트리에 노드가 존재하지 않거나 지우는 노드가 해당 부모 노드의 유일한 자식 노드 였을 경우
        return 1                              # 1 리턴하기

    cnt = 0                                   # 리프 노드의 개수 0으로 초기화

    for i in range(len(tree[node])):          # 모든 노드 탐색
        cnt += erase_leaf_cnt(tree[node][i], erase_node)
                                              # dfs 탐색
    return cnt                                # 리프 노드의 개수 반환


# 입력
n = int(input())                              # 트리의 노드 개수 입력받기
tree = [list() for _ in range(n)]             # 리스트 n개를 원소로 가진 리스트 생성

for idx, x in enumerate(input().split()):     # 0번 노드부터 N-1 노드까지 각 노드의 부모 입력받기
    if x == "-1":                             # 만약 부모노드가 없으면
        root = idx                            # 루트노드
    else:                                     # 만약 부모노드가 있으면
        tree[int(x)].append(idx)              # 입력받은 값을 tree[int(x)] 리스트에 추가하기

erase_node = int(input())                     # 지울 노드의 번호 입력받기

print(erase_leaf_cnt(root, erase_node))       # 연산 & 출력