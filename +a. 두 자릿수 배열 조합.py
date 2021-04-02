from itertools import combinations

items = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

n = int(input())
for i in range(1, n+1):
    print(list(map(''.join, combinations(items, i))))


''' <combination 공부>
- 알고보니 조합을 일일이 짤필요없이 파이썬은 따로 라이브러리에 가지고 있었다...
- 속도도 월등히 빠름

- 위 코드 해석은 일단 조합(combination)을 불러온 다음
- list에 적어 넣는데, combination, 즉 조합할 것들이 적혀있는 (리스트, i)를 적어 넣으면 된다
- 위 코드에서 i는 자릿수를 결정해준다.
- n은 어디까지 반복할 것인지 input으로 받아 들이는 것
'''