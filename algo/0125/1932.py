import sys

# 동적프로그래밍 용 리스트
rst_arr = []

def max_triangle(N, arr):
    # rst_arr[0] 에 해당하는 리스트 넣어줘서 베이스 라인 잡아주기
    temp = []
    temp.append(arr[0][0])
    rst_arr.append(temp)
    print(rst_arr)
    print("=============================")
    # 남은 리스트 순회
    for i in range(1, N):
        temp = []
        for j in range(len(arr[i])):
            # 새로운 변의 제일 왼쪽 값은
            # 이전 변의 제일 왼쪽 값에만 더할 수 있다.
            if j == 0:
                temp.append(rst_arr[i-1][0] + arr[i][j])
            # 중간에 있는 값들은
            # 이전 변의 같은 인덱스 값 혹은 -1 작은 인덱스 값에 더할 수 있다.
            # 최대값을 찾는 문제이므로 두 인덱스에 접근해 큰 값에다가 새로운 값을 더해준다.
            elif j < len(arr[i]) - 1:
                if rst_arr[i-1][j-1] > rst_arr[i-1][j]:
                    temp.append(rst_arr[i-1][j-1] + arr[i][j])
                else:
                    temp.append(rst_arr[i-1][j] + arr[i][j])
            # 새로운 변의 제일 오른쪽 값은
            # 이전 변의 제일 오른쪽 값에만 더할 수 있다.
            else:
                temp.append(rst_arr[i-1][j-1] + arr[i][j])
        rst_arr.append(temp)

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr_temp = list(map(int, sys.stdin.readline().split()))
    arr.append(arr_temp)
print(arr)
print("=============================")
max_triangle(N, arr)
print(rst_arr)