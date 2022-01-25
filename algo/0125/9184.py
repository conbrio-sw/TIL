W = []
for i in range(51):
    W.append([])
    for j in range(51):
        W[i].append([])
        for k in range(51):
            W[i][j].append(1)




def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
def ww(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return ww(20, 20, 20)
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                if i < j < k:
                    W[i][j][k] = W[i][j][k-1] + W[i][j][k-1] - W[i][j-1][k]
                else:
                    W[i][j][k] = W[i-1][j][k] + W[i-1][j-1][k] + W[i-1][j][k-1] - W[i-1][j-1][k-1]
    return W[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(ww(a,b,c))


