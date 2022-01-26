# 45656처럼
# 모든 자리의 차이가 1이면
# 계단 수

# 초기 값 (1의 자리수)
dp = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def stair_num(N):
    
    for num in range(1, N):
        temp = [0] * 10
        dp.append(temp)

        # 다음 계단은
        # 이전 계단에 +1, -1 한 값을 붙이는 것과 같다
        # 이를 반대로 동적 프로그래밍해서 짠다.
        # 이떄 끝의 자리가 0, 9인 경우는 if문으로 다르게 처리해준다.
        for i in range(10):
            if i == 0:
                dp[-1][i] = dp[-2][i+1]
            elif i == 9:
                dp[-1][i] = dp[-2][i-1] 
            else:
                dp[-1][i] = dp[-2][i-1] + dp[-2][i+1]




    return sum(dp[N-1])

N = int(input())
print(stair_num(N)%1000000000)