import sys
stair_list = []

def stair(N, arr):
    stair_list.append([arr[0]])
    if N == 1:
        return
    stair_list.append([arr[0]+arr[1] ,arr[1]])
    if N == 2:
        return
    stair_list.append([arr[1]+arr[2], arr[0] + arr[2]])
    if N == 3:
        return
    for i in range(3, N):
        temp = []
        
        temp.append(stair_list[i-1][1] + arr[i])
        
        if stair_list[i-2][0] > stair_list[i-2][1]:
            temp.append(stair_list[i-2][0] + arr[i])
        else:
            temp.append(stair_list[i-2][1] + arr[i])
        stair_list.append(temp)


N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
stair(N, arr)
print(max(stair_list[N-1]))