# Q. 극장의 좌석은 한 줄로 되어 있으며 왼쪽부터 차례대로 1번부터 N 번까지 번호가 매겨져 있다.
# 공연을 보러 온 사람들은 자기의 입장권에 표시되어 있는 좌석에 앉아야 한다.
#
# 예를 들어서, 입장권에 5번이 쓰여 있으면 5번 좌석에 앉아야 한다.
# 단, 자기의 바로 왼쪽 좌석 또는 바로 오른쪽 좌석으로는 자리를 옮길 수 있다.
#
# 예를 들어서, 7번 입장권을 가진 사람은 7번 좌석은 물론이고,
# 6번 좌석이나 8번 좌석에도 앉을 수 있다.
# 그러나 5번 좌석이나 9번 좌석에는 앉을 수 없다.
#
# 그런데 이 극장에는 “VIP 회원”들이 있다.
# 이 사람들은 반드시 자기 좌석에만 앉아야 하며 옆 좌석으로 자리를 옮길 수 없다.
#
# 예를 들어서,
# 그림과 같이 좌석이 9개이고,
# 4번 좌석과 7번 좌석이 VIP 석인 경우에 <123456789>는 물론 가능한 배치이다.
# 또한 <213465789> 와 <132465798> 도 가능한 배치이다.
# 그러나 <312456789> 와 <123546789> 는 허용되지 않는 배치 방법이다.
#
# 오늘 공연은 입장권이 매진되어 1번 좌석부터 N번 좌석까지 모든 좌석이 다 팔렸다.
# 총 좌석의 개수와 VIP 회원들의 좌석 번호들이 주어졌을 때,
# 사람들이 좌석에 앉는 서로 다른 방법의 가짓수를 반환하시오.
# 예전에 만들었던 fibonacci_dynamic_programming 에서 가져오면 됩니다!
def DP_fibonacci(n, fibonacci_memo):
    if n in fibonacci_memo:
        return fibonacci_memo[n]

    nth_fibonacci = DP_fibonacci(n - 1, fibonacci_memo) + DP_fibonacci(n - 2, fibonacci_memo)
    fibonacci_memo[n] = nth_fibonacci
    return nth_fibonacci


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = DP_fibonacci(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = DP_fibonacci(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways


memo = {1: 1, 2: 2, 3: 3, 4: 5, 5: 8}  # .....fibonacci...
print("정답 = 12 / 현재 풀이 값 =", get_all_ways_of_theater_seat(9, [4, 7]))
print("정답 = 4 / 현재 풀이 값 =", get_all_ways_of_theater_seat(9, [2, 4, 7]))
print("정답 = 26 / 현재 풀이 값 =", get_all_ways_of_theater_seat(11, [2, 5]))
print("정답 = 6 / 현재 풀이 값 =", get_all_ways_of_theater_seat(10, [2, 6, 9]))
