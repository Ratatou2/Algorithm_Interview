def comb(arr, spot):
    arr = sorted(arr)
    ans = []
    def recur(llist):
        if len(llist) == spot:
            llist = map(str, llist)
            ans.append(''.join(llist))

            return

        start = arr.index(llist[-1]) + 1 if llist else 0

        for i in range(start, len(arr)):
            llist.append(arr[i])
            recur(llist)
            llist.pop()

    recur([])
    print(', '.join(ans), end=', ')

r = 3
for i in range(1, r+1):
    comb([0,1,2,3,4,5,6,7,8,9], i+1)



