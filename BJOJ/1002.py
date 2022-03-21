# 조규현과 백승환은 터렛에 근무하는 직원이다.
# 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다.
# 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다.
# 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
# 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고,
# 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
# 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 다음과 같이 이루어져 있다.
# 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다.
# x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.

# 출력
# 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다.
# 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

"""
두 사람의 좌표 사이의 직선 거리 위에 류재명이 위치할 경우 1 그렇지 않은 경우 2개의 점이 만남.
무한대의 좌표가 존재할 경우 -1 (두 원이 일치해 무한한 점에서 만남)
두 거리를 합한 것보다 두 점 사이 거리가 더 큰 경우 혹은 두 거리 사이의 차이가 두 점 사이의 거리보다 큰 경우 만나지 않음
"""
from math import sqrt, pow

count = int(input())
for _ in range(count):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 사람의 좌표를 통과하는 직선
    line = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    r1, r2 = min(r1, r2), max(r1, r2)
    if line == 0 and r1 == r2:
        print(-1)
    elif line > r1 + r2 or line < r2 - r1:
        print(0)
    elif line == r1 + r2 or line == r2 - r1:
        print(1)
    elif r2 - r1 < line < r1 + r2:
        print(2)

