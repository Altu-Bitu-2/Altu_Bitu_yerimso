# 선택과제 3: 19636 요요 시뮬레이션
import sys                    # 파이썬 인터프리트가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

input = sys.stdin.readline    # input 함수에 문자열 입력받기

"""
[요요 시뮬레이션] - 단순 구현 문제
체중(weight): 일일 에너지 섭취량(energy_in) - 일일 에너지 소비량(energy_out) (일일 기초 대사량(b) + 일일 활동 대사량(a))
if |일일 에너지 섭취량(energy_in) - 일일 에너지 소비량(energy_out)| > 기초 대사량 변화 역치(T)
-> 일일 기초 대사량(b) += [(일일 에너지 섭취량(energy_in) - 일일 에너지 소비량(energy_out)) / 2]
-> !주의! 이때 일일 기초 대사량에서 더해지는 값이 Floor 함수 적용이므로 음수일 때 값처리 주의해야 함
기초 대사량(b) 변화를 고려하지 않는 경우는, b == I0이므로 한번에 계산
"""


def diet_simulation(initial_weight, I0, T, period, energy_in, a):    # 기초대사량이 변화를 고려할 때 다이어트 후 체중, 일일 기초대사량을 연산하는 함수
    b = I0                                          # 초기 일일 기초대사량 저장
    weight = initial_weight                         # 초기 몸무게 저장
    for _ in range(period):                         # 다이어트 기간만큼 반복
        energy_out = a + b                          # 일일 에너지 소비량 연산 (일일 기초 대사량 + 일일 활동 대사량)
        weight += energy_in - energy_out            # 에너지 섭취량에서 에너지 소비량을 뺀만큼 체중이 증가

        if abs(energy_in - energy_out) > T:         # 만약 (일일 에너지 섭취량 - 일일 에너지 소비량)의 절댓값이 역치 T보다 크다면
            b += (energy_in - energy_out) // 2      # 기초대사량 += (일일 에너지 섭취량 - 일일 에너지 소비량)/2

    return weight, b                                # 다이어트 후 최종 몸무게와 기초대사량을 반환한다


# 입력
initial_weight, I0, T = map(int, input().split())     # 다이어트 전 체중, 다이어트 전 일일 에너지 섭취량 및 일일 기초대사량, 기초 대사량 변화 역치를 입력받음
period, energy_in, a = map(int, input().split())      # 다이어트 기간, 다이어트 기간 일일 에너지 섭취량, 다이어트 기간 일일 활동 대사량을 입력받음

# 연산 + 출력

# 기초 대사량 변화 고려하지 않는 경우
weight = initial_weight + (energy_in - (I0 + a)) * period   # 다이어트 후 체중 = 초기 체중 + (일일 에너지 섭취량 - 일일 에너지 소비량) * 다이어트 기간
if weight <= 0:             # 만약 다이어트 후 체중이 0보다 작은 경우
    print("Danger Diet")    # Danger Diet를 출력
else:                       # 만약 다이어트 후 체중이 0보다 큰 경우,
    print(weight, I0)       # 다이어트 후 체중과 일일 기초대사량을 출력

# 기초 대사량 변화 고려한 경우
weight, b = diet_simulation(initial_weight, I0, T, period, energy_in, a)        # diet_simulation 함수를 통해 다이어트 후 체중과 일일 기초대사량 연산

if weight <= 0 or b <= 0:    # 만약 몸무게나 일일 기초 기초대사량이 0 이하인 경우
    print("Danger Diet")     # Danger Diet를 출력
else:                        # 만약 다이어트 후 체중과 일일 기초 대사량이 0보다 큰 경우
    if b < I0:               # 만약 변화한 일일 기초대사량이 초기 일일 기초 대사량보다 작아진 경우
        answer = "YOYO"      # YOYO를 출력
    else:                    # 만약 변화한 일일 기초대사량이 초기 일일 기초 대사량보다 크거나 같은 경우
        answer = "NO"        # NO를 출력
    print(weight, b, answer)     # 다이어트 후 체중, 변화한 일일 기초대사량과 요요가 올지 여부를 출력