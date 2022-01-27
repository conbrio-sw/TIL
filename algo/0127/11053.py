# 수열 A가 주어졌을 때
# 가장 긴 증가하는 부분 수열을 구하자
import sys

# rst = []

# def find_longest(arr):
#     # 가장 초기값
#     rst.append([1, arr[0]])
#     for i in range(1, len(arr)):
#         for j in range(len(rst)):
#             if arr[i] > rst[j][1]:
#                 rst[j][0] += 1
#                 rst[j][1] = arr[i]
#         if arr[i] < rst[-1][1]:
#             rst.append([1, arr[i]])
#     max_rst = 0
#     # print('rst: ', rst)
#     for i in range(len(rst)):
#         if rst[i][0] > max_rst:
#             max_rst = rst[i][0]
#             # print(max_rst, i, rst[i][0])
#     return max_rst
#     pass

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(N)]

# 이중 포문
for i in range(N):
    for j in range(i):
        # 만약 현재 값이 이전 값보다 크면 작은 이전 값 중에서 가지는 최대
        # 경우를 덮어 씌어준다
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    # 그리고 본인꺼를 더해야하니깐 1을 더해준다.
    dp[i] += 1
print(max(dp))




# find_longest(arr)

# print(find_longest(arr))
# print(rst)