# LCS
# 최장 공통 부분 수열
# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제


M = input()
N = input()
n = len(M)
dp = []
for i in range(len(M)):
    temp = [0, -1]
    dp.append(temp)

#print(f'dp 처음 : {dp}')
for i in range(len(M)):
    temp = 0
    for j in range(i):
        if dp[i][0] < dp[j][0] and M[i] in N[dp[j][1]+1:]:
            dp[i][0] = dp[j][0]
            temp = j
    

    if M[i] in N[dp[temp][1]+1:]:
        dp[i][0] += 1
        dp[i][1] = N[dp[temp][1]+1:].index(M[i]) + dp[temp][1]+1
    #print(f'{i}번쨰 {dp}')

#print(dp)
a = list(map(lambda x :x[0], dp))
print(a)
print(max(a))