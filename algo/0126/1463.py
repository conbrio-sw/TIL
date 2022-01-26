# X가 3으로 나누어 떨어지면 3으로 나눈다
# X가 2로 나누어 떨어지면 2로 나눈다
# 1을 뺀다.


arr = [-1]

def Xop(n):

    for number in  range(1, n+1):
        # 초기값 설정해주는 친구들
        if number == 1:
            arr.append(0)
        elif number == 2:
            arr.append(1)
        elif number == 3:
            arr.append(1)
        
        else:
            # number가 2, 3 모두 나누어 떨어지면 /2, /3, -1 인 케이스를 비교해서 최소값에 + 1을 더해준다
            if number % 6 == 0:
                minvalue = min([arr[number-1], arr[number//2], arr[number//3]])
            # /3, -1인 케이스 비교
            elif number % 3 == 0:
                minvalue = min([arr[number-1], arr[number//3]])
            # /2, -1인 케이스 비교
            elif number % 2 == 0:
                minvalue = min([arr[number-1], arr[number//2]])
            # /2, /3으로 나누어 떨어지는 게 없으면 number-1의 연산에 +1해준다.
            else:
                minvalue = arr[number-1]
            arr.append(minvalue + 1)
    return arr[n]

N = int(input())
print(Xop(N))