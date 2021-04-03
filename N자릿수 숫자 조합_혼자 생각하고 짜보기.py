def comb(arr, spot):
    arr = sorted(arr)
    ans = []
    def recur(list_to_fill):
        if len(list_to_fill) == spot:
            print(list_to_fill)
            return


        start = list_to_fill[-1] + 1 if list_to_fill else 0
        # 이 코드가 작동을 안했던 이유는 len을 list_to_fill로 줘서... 당연히 채워진게 없으니 for문이 돌지 않는다
        for i in range(start, len(list_to_fill)):
            list_to_fill.append(arr[i])
            recur(list_to_fill)
            list_to_fill.pop()

    recur([])

r = 2
for i in range(r):
    comb([1,2,3,4,5,6,7,8,9], i+1)

