#선택과제 2: 18115 카드 놓기
import sys    #파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
from collections import deque  #collections 모듈의 deque 클래스 사용: double-ended queue
input = sys.stdin.readline  #input변수에 문자열을 입력받음

"""
 결과값을 보고 처음 도출 -> 기술을 모두 반대로 쓰자!
 1. 제일 위의 카드 바닥에 내려놓기 ->
    바닥에 내려놓은 카드를 다시 위에 ->
    제일 위의 카드 앞에 넣기
 2. 위에서 두 번째 카드 바닥에 내려놓기 ->
    바닥에 내려놓은 카드 위에서 두 번째에 넣기 ->
    제일 위의 카드 앞에서 두번째에 넣기
 3. 제일 밑에 있는 카드 바닥에 내려놓기 ->
    바닥에 내려놓은 카드 밑에 넣기 ->
    제일 아래의 카드 뒤에 넣기
"""

# 입력
n = int(input())   #카드의 개수 입력받음
cmd = list(map(int, input().split()))  #사용한 기술들을 순서대로 입력받아 int로 형변환하고 map객체를 list로 형변환한다.

cards = deque()  #빈 deque를 만든다.

# 1번부터 n번 카드까지
for i in range(1, n+1):   #카드의 개수만큼 반복
    op = cmd[-i]    # 기술을 뒤에서부터 쓰기
    if op == 1:     # 사용한 기술이 1번 기술이면
        cards.appendleft(i)   # i번 카드를 deque에 왼쪽 끝에 삽입한다(제일 위의 카드 앞에 넣기)
    elif op == 2:  # 사용한 기술이 2번 기술이면
        # cards = [temp, ...]
        temp = cards.popleft()  #deque의 왼쪽 끝 element를 pop한다. (가장 위의 카드를 뺀다)
        cards.appendleft(i) # cards = [i, ...], i번 카드를 deque의 왼쪽 끝에 삽입한다.(제일 위의 카드 앞에 넣기)
        cards.appendleft(temp) # cards = [temp, i, ...], 다시 원래 가장 위에 있던 카드를 deque의 왼쪽 끝에 삽입한다. (제일 위의 카드 앞에 넣기)
    else:  # 사용한 기술이 3번 기술이면
        cards.append(i)   #i번 카드를 deque의 오른쪽 끝에 삽입한다. (제일 아래의 카드 뒤에 넣기)

# 출력
for i in cards:  #카드의 개수만큼 반복
    print(i, end=' ')  #원래 카드의 상태를 위에서부터 일렬로 출력한다.