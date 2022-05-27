# 선택과제 1: 5639 이진 검색 트리

import sys                        # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

sys.setrecursionlimit(10 ** 6)    # 최대 재귀 횟수를 10 ** 6으로 늘림

"""
 Ver1. 트리를 직접 작성하는 방식 - 백준에 제출 시에는 시간초과가 나는 소스코드입니다. 다만 트리를 직접 구현한 코드를 한번 참고하시면 좋을거 같아서 업로드 합니다.
 맵과 셋 PPT 중 BST 노드 삽입 과정 참고
 [이진 검색 트리]
 1. 포인터로 왼쪽, 오른쪽 서브트리를 가리키는 구조체 선언
 2. NULL 만날 때까지 조건에 따라 왼쪽 또는 오른쪽으로 이동
 3. 노드가 들어갈 위치를 찾으면 동적할당 후 노드 만들기
 4. 완성한 트리를 후위 순회
"""


class node_info:                                  # node_info 클래스 생성
    def __init__(self, data):                     # 생성자
        self.data = data                          # data 값 할당
        self.left = None                          # 왼쪽 노드 X
        self.right = None                         # 오른쪽 노드 X


def make_tree(node, data):                        # 이진 트리 생성 함수
    if node == None:                              # 이번 노드가 들어가게 될 위치
        node = node_info(data)                    # 새로운 노드 생성
    elif node.data > data:                        # 만약 data가 루트 노드의 data보다 작다면
        node.left = make_tree(node.left, data)    # 루트 노드의 왼쪽 노드가 됨
    elif node.data < data:                        # 만약 data가 루트 노드의 data보다 크다면
        node.right = make_tree(node.right, data)  # 루트 노드의 왼쪽 노드가 됨

    return node                                   # node 리턴하기


def postorder(node):                              # 후위 순회
    if node == None:                              # 만약 루트노드가 없으면
        return                                    # 함수 종료

    postorder(node.left)                          # 왼쪽 서브트리부터 방문
    postorder(node.right)                         # 오른쪽 서브트리 방문
    print(node.data)                              # 루트 노드 출력


root = None                                       # 이진 트리가 생성되기 전 루트 존재 X

# 입력 & 연산
for i in sys.stdin:                               # 이진 검색 트리 입력받기
    root = make_tree(root, int(i))                # 이진 트리 생성하기

postorder(root)                                   # 생성된 이진 트리를 후위 순회하기