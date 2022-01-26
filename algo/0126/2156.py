# 포도주 시식
# 포도주 잔을 선택하면 그 포도주 다 마시고, 원래 위치로 다시
# 연속으로 놓여있는 3잔을 모두 마실 수는 없다
# 많은 포도주를 마셔야한다.

wines = []

def wine_amount(arr):
    # 초기값 넣어주기
    wines.append(arr[0])

    # for i in range(1, len(arr)):
    #     temp = [0, 0]
    #     if i == 1:
    #         temp[0] = arr[0] + arr[1]
    #         temp[1] = arr[1]

    #     else:
    #         temp[0] = wines[i-1][1] + arr[i]
    #         temp[1] = wines[i-2][0] + arr[i]
    #     wines.append(temp)
    # if len(arr) == 1:
    #     return arr[0]
    # max1 = max(wines[-1])
    # max2 = max(wines[-2])
    # if max1 > max2:
    #     return max1
    # return max2
    for i in range(1, len(arr)):
        # 두번째 항일때는 무조건 1항 2항 더한게 가장 크다
        if i == 1:
            wines.append(arr[0]+arr[1])
        # 3번째 항일때는 이전항, 1+3, 2+3 항 중에 가장 큰 값
        elif i == 2:
            wines.append(max(arr[0] + arr[2], arr[1] + arr[2], wines[i-1]))
        # 나머진 이전항, i-2항에 arr[i] 더한 값, i-3항에 arr[i-1] + arr[i] 를 더한 값 중 가장 큰값
        else:
            wines.append(max(wines[i-3] + arr[i-1] + arr[i], wines[i-2] + arr[i], wines[i-1]))
    return wines[-1]

# arr = [6, 10, 13, 9, 8, 1]
# print(wine_amount(arr))
# # print(wines)

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

print(wine_amount(arr))
# print(wines)