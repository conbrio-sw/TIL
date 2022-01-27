# 전깃줄
# 전깃줄 교차안하게


import sys




N = int(sys.stdin.readline())
arr = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append(temp)

dp = [0] * N

# arr_sort = sorted(arr, key= lambda arr: arr[0])
# print(arr_sort)

arr.sort(key=lambda arr: arr[0])

for i in range(N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = dp[j]
    
    dp[i] += 1

print("없애야할 수: ", N - max(dp))
print(dp)