# zero, one 함수는
# 각각 해당인덱스번째 피보나치 함수에 0이, 1이 몇번 들어갔는지를 의미한다.
zero = [1, 0, 1]
one = [0, 1, 1]

def fibo_num(n):
    # 만약 인식해둔 zero, one의 인덱스가 넘어가면
    # 새로운 인덱스를 집어 넣어줘야한다.
    length = len(zero)
    if n >= length:
        # fibo[n] = fibo[n-1] + fibo[n-2] 을 생각해보자
        # zero, one 역시 똑같이 위와 더해지는 것을 알 수 있다.
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])


T = int(input())
rst = [0, 0]
for i in range(T):
    n = int(input())
    fibo_num(n)