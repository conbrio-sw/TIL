# 평범한 배낭
# 배낭을 가치있게 싸려고 함
# N개 물건
# 각 물건은 무게 W 가치 V를 가지는데
# 배낭넣으면 V만큼 가치 얻음



import sys

N, K = map(int, sys.stdin.readline().split())


arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
print(arr)

dp = []
# 최대무게 x 최대갯수의 2차 행렬을 만들어준다
for i in range(N+1):
    temp = []
    for j in range(K+1):
        temp.append(0)
    dp.append(temp)


# 물건이 늘어날때 마다 루프를 돈다
for i in range(N):
    # 무게가 1kg 씩 늘어난다고 가정하자
    for j in range(K+1):
        # 만약 새로 추가된 물건이 현재 최대 무게보다 같거나 작다고 할때
        if arr[i][0] <= j:
            # 현재 최대 무게 상태에서 새로운 물건을 안넣었을 때 가치와
            # 새로운 물건을 넣고, 현재 최대 무게 상태-새로운 물건 무게의 무게 상태의 최대 가치를 더한 값을
            # 비교해서 큰값을 넣어준다.
            if (arr[i][1] + dp[i-1][j-arr[i][0]] > dp[i-1][j]):
                dp[i][j] = arr[i][1] + dp[i-1][j-arr[i][0]]
            else:
                dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] 

print(dp[N-1][K])
print(dp)
