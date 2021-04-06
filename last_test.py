def solution(arr):
    n = len(arr)
    picked = []
    start = 0
    def recur(start, n):
        if len(picked) == 2:
            print(picked)
            return

        for i in range(start, n):
            picked.append(i)
            #picked에서 마지막 부터 가져오는 이유는 그전 것들은 이미 썼던 요소들이라서 맨 끝값부터 가져오는 거임
            start = picked[-1] + 1
            recur(start, n)
            picked.pop()
    recur(start, n)

solution([1,2,3,4,5,6,7,8,9])
