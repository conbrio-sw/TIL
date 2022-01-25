import sys
P = [-1, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def func(N, P):
    if N <= 10:
        return P[N]
    P = [-1, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    for i in range(11, N+1):
        print(P[i-2], P[i-3], "   ",i-2, i-3)
        num = P[i-2] + P[i-3]
        P.append(num)
        print(P)
    return P[N]







# T = int(sys.stdin.readline())
# for i in range(T):
#     N = int(sys.stdin.readline())
#     print(func(N, P))


wh = [0 for i in range(101)]
wh[1] = 1
wh[2] = 1
wh[3] = 1
for i in range(0, 98):
    wh[i + 3] = wh[i] + wh[i + 1]
t = int(input())
for i in range(t):
    n = int(input())
    print(wh[n], func(n,P))