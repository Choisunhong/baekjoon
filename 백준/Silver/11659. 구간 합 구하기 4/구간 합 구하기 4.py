import sys
input = sys.stdin.readline
N, M = map(int, input().split()) 
arr = list(map(int, input().split()))

res = [0]*(N+1)
for i in range(1, N + 1):
    res[i] = res[i - 1] + arr[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    result = res[j] - res[i - 1]
    print(result)