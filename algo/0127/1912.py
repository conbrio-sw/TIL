# 연속합


import sys

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))


dp = [0] * N
dp[0] = M[0]
max_value = M[0]
max_value_present = M[0]
for i in range(1, N):
    # M[i]가 양수면 이전 dp에 그 값을 더해준다
    if M[i] >= 0:
        # 근데 이전 dp가 음수면 그냥 M[i]를 할당한다
        if dp[i-1] < 0:
            dp[i] = M[i]
        else:
            dp[i] = dp[i-1] + M[i]
    # 음수 일때 그냥 더해준다.
    else:
        dp[i] = dp[i-1] + M[i]
        if M[i] > dp[i]:
            dp[i] = M[i]

print(max(dp))