def comb(arr, spot):
    arr = sorted(arr)

    def recur(llist):

        if len(llist) == spot:
            print(llist)
            return

        start = llist[-1] + 1 if llist else 0

        for i in range(start, len(arr)):
            llist.append(arr[i])
            recur(llist)
            llist.pop()
    recur([])

r = 2
for i in range(r):
    comb([1,2,3,4,5,6,7,8,9], i+1)

