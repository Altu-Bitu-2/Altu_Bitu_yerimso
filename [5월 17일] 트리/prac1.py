#필수과제 1: 2022 KAKAO BLIND RECRUITMENT 양궁대회

SIZE = 10                                             # 과녁판 사이즈 = 10

"""
 [양궁대회]
 1. 가능한 모든 경우를 백트래킹 탐색을 통해 검사
 -> 라이언이 점수를 얻어가려면 어피치보다 1개 더 쏘는 경우가 최적. 어피치보다 적게 화살 쏘는 건 점수 못 얻어가므로 어차피 의미가 없음.
 -> 따라서 라이언이 각 점수에 화살을 아래와 같이 쏘는 2가지 경우만 고려해서 만들어지는 모든 경우를 백트래킹으로 탐색
    - 어피치가 점수 획득을 하는 경우: 해당 점수에는 화살을 한 발도 쏘지 않는 것이 이득
    - 라이언이 점수 획득을 하는 경우: 필요한 최소 화살을 사용하는 것이 이득이므로 어피치보다 정확히 한 발 더 쏨
 !주의! 0번 인덱스가 10점 과녁임을 주의
"""

max_diff = 1                                          # 점수 차
answer = [-1]                                         # 라이언이 이길 수 있는 방법이 없을 떄 리턴


def backtracking(idx, left, diff, ryan, appeach):     # 라이언이 이길 수 있는 모든 경우를 백트래킹 탐색을 통해 검사
    global max_diff, answer                           # 전역변수 max_diff, answer
    if idx == SIZE:                                   # 기저조건 - 0점 과녁까지 모두 탐색한 경우
        ryan[idx] = left                              # 남은 화살은 과녁을 맞추지 못함

        if diff > max_diff:                           # 점수차가 1보다 클 경우
            max_diff = diff                           # max_diff에 점수차 저장
            answer = ryan[:]                          # answer에 ryan의 점수표 반환
        elif diff == max_diff:                        # 점수차가 1일때
            if ryan[::-1] > answer[::-1]:             # 역순으로 비교했을때 ryan이 쏜 화살 수가 더 많으면
                answer = ryan[:]                      # answer에 ryan의 점수표 반환
        return                                        # 함수 종료

    if left > appeach[idx]:                           # 남은 화살로 라이언이 점수를 얻을 수 있는 경우
        ryan[idx] = appeach[idx] + 1                  # 해당 점수에서 라이언의 화살의 개수는 어피치보다 1개 많음
        backtracking(idx + 1, left - ryan[idx], diff + SIZE - idx, ryan, appeach)
                                                      # 다음 점수에서 탐색
        ryan[idx] = 0                                 # 이번 점수에서 점수를 얻지 않았을 경우

    if appeach[idx]:                                  # 어피치가 점수를 얻을 수 있는 경우 점수 계산
        diff -= SIZE - idx                            # 점수 차에서 현재 과녁의 점수 빼기
    backtracking(idx + 1, left, diff, ryan, appeach)  # 다음 점수에서 탐색
    return                                            # 함수 종료


def solution(n, info):                                # 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법을 구하는 함수
    ryan = [0] * 11                                   # 라이언 과녁 정보
    backtracking(0, n, 0, ryan, info)                 # 백트래킹 탐색

    return answer                                     # 라이언이 가장 큰 점수 차로 우승할 방법 리턴


# 디버깅 위한 메인 코드 - 프로그래머스에는 제출 X
if __name__ == "__main__":                            # prac1.py 파일에서만 실행되도록 함
    n = 5                                             # 어피치가 쏜 화살의 수
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0]             # 어피치는 10점 2발, 9점 1발, 8점 1발, 7점 1발을 쏨

    print(*solution(n, info))                         # solution을 모두 출력