arr = [1, 1]

def number_2jinsu(N, arr):
    number_0 = 0
    number_1 = 0
    rst = 0
    c = fact(N, arr)
    for i in range(0, N+1):
        if i * 2 > N:
            break
        number_0 = i
        number_1 = N - i*2
        d = arr[number_1+number_0]
        a = arr[number_0]
        b = arr[number_1]
        rst += int(d/a/b)
    return rst%15746

def fact(N, arr):
    if N == 1:
        return arr[1]
    for i in range(2, N+1):
        arr.append(arr[i-1]*i)
    return arr[N]

N = int(input())
print(number_2jinsu(N, arr))

import sys 
input = sys.stdin.readline 
n = int(input()) 
dp = [0] * 1000001 
dp[1] = 1 
dp[2] = 2 
for k in range(3,n+1): 
    dp[k] = (dp[k-1]+ dp[k-2])%15746 
print(dp[n])
