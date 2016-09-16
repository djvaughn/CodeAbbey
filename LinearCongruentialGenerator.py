numOfValues = int(input())
answer = []
for i in range(numOfValues):
    A, C, M, X0, N = input().split()
    A = int(A)
    C = int(C)
    M = int(M)
    X0 = int(X0)
    N = int(N)
    Xcur = X0
    for i in range(N):
        Xnext = (A * Xcur + C) % M
        Xcur = Xnext

    answer.append(Xcur)

print(*answer)
