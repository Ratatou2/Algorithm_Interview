
#K : 바이러스 개수 / P배씩 증가 / N초
# 2 3 2 -> 2*
K, P, N = map(int, input().split())

v = K*(P**N)

print(v%1000000007)