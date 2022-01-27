# 가장 긴 바이토닉 부분 수열
# 수열 S가 보유한 어떤 값 기준으로
# 왼쪽 오른쪽 모두 작으면
# 바이토닉 수열이라고 한다.
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0,0] for i in range(N)]


for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and dp[i][1] < dp[j][1]:
            dp[i][1] = dp[j][1]
    dp[i][1] += 1
for i in range(N):
    for j in range(i):
        if arr[-1-i] > arr[-1-j] and dp[-1-i][0] < dp[-1-j][0]:
            dp[-1-i][0] = dp[-1-j][0]
    dp[-1-i][0] += 1



rst = [0 for i in range(N)]
for i in range(N):
    rst[i] = dp[i][0] + dp[i][1] - 1

print('rst: ', rst)
print('dp: ', dp)

print(max(rst))