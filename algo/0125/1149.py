import sys

# 동적프로그래밍용 리스트
# RGB_arr[i][0,1,2] 형식이다.
# 이때 0,1,2 는 각각 마지막이 red, green, blue 임을 의미한다.
RGB_arr = []

def RGB(arr):
    temp = []
    for i in arr[0]:
        temp.append(i)
    # RGB_arr[0] 값 넣어주기
    RGB_arr.append(temp)
    # 남은 거리 실행
    for i in range(1, len(arr)):
        # 새로운 리스트 미리 추가
        RGB_arr.append([0,0,0])
        # 순서대로 RGB 값 할당
        red = arr[i][0]
        green = arr[i][1]
        blue = arr[i][2]
        # 빨간색 칠하기
        # 이전항의 초록, 블루 값을 비교해서 낮은 값을 할당
        # 이후 그린, 블루도 마찬가지로 진행
        if RGB_arr[i-1][1] < RGB_arr[i-1][2]:
            RGB_arr[i][0] = RGB_arr[i-1][1] + red
        else:
            RGB_arr[i][0] = RGB_arr[i-1][2] + red

        if RGB_arr[i-1][0] < RGB_arr[i-1][2]:
            RGB_arr[i][1] = RGB_arr[i-1][0] + green
        else:
            RGB_arr[i][1] = RGB_arr[i-1][2] + green

        if RGB_arr[i-1][0] < RGB_arr[i-1][1]:
            RGB_arr[i][2] = RGB_arr[i-1][0] + blue
        else:
            RGB_arr[i][2] = RGB_arr[i-1][1] + blue

arr = []
# arr.append([26, 40, 83])
# arr.append([49, 60, 57])
# RGB(arr)
# print(RGB_arr)

N = int(sys.stdin.readline())
for i in range(N):
    arr_temp = list(map(int, sys.stdin.readline().split()))
    arr.append(arr_temp)
RGB(arr)
# print(RGB_arr)
print(min(RGB_arr[N-1]))
