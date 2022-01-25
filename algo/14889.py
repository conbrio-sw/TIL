# https://www.acmicpc.net/problem/14889

def func(N, S):
    pass
    arr = [num for num in range(N)]
    a = list(johap(arr, len(arr)/2))
    #print(a, len(a))
    start_team = []
    link_team = []
    rst = -1
    for i in a:
        if i == a[len(a)//2]:
            break
        start_team = i
        for j in range(N):
            if j not in i:
                link_team.append(j)
        #print(start_team, link_team)
        start_team_score = 0
        for ii in start_team:
            for jj in start_team:
                start_team_score += S[ii][jj]
        link_team_score = 0
        for ii in link_team:
            for jj in link_team:
                link_team_score += S[ii][jj]
        if rst == -1:
            rst = abs(start_team_score-link_team_score)
        else:
            if abs(start_team_score-link_team_score) < rst:
                rst = abs(start_team_score-link_team_score)
        start_team = []
        link_team = []
    return rst
def johap(arr, end):
    for i in range(len(arr)):
        if end == 1:
            yield [arr[i]]
        else:
            for next in johap(arr[i+1:], end-1):
                yield [arr[i]] + next
     




arr = [num for num in range(10)]
a = johap(arr, len(arr)/2)
# s = 0
# for i in a:
#     print(i)
#     s+=1
# print(s)
s = [[0, 1, 2, 3], [4, 0, 5, 6], [7, 1, 0, 2], [3, 4, 5, 0]]
print(func(4, s))
ss = [
    [0,1,2,3,4,5],
    [1,0,2,3,4,5],
    [1,2,0,3,4,5],
    [1,2,3,0,4,5],
    [1,2,3,4,0,5],
    [1,2,3,4,5,0]
]
print(func(6,ss))

# N = int(input())
# arr = []
# for i in range(N):
#     ar = list(map(int, input().split()))
#     arr.append(ar)
# print(func(N, arr))