import pprint
import this
print('A1', 'b2')

print('A1', 'B1', sep=', ')

print('me', end='')
print('&')
print('you')

a = ['a', 'b', 'c']

print(a)
print(' '.join(a))

print('❤'.join(a))

idx = 1
fruit = 'apple'

print(f'{idx + 1} : {fruit}')


a = { 'result': True, 'records': [ { 'id': 1, 'value': 'First Value' }, { 'id': 2, 'value': 'Second Value' } ], 'count': 2 }
print(a)
pprint.pprint(a)

print('input timing')

n = int(input())
multi = 1
R = 0
for _ in range(1, n+1):
    cal = n*(n-1)
    multi = cal * multi
    cal = 0
    n = n - 2
    if n <= 1:
        print(multi)
        print('break')
        break


if __name__ == 'main':
    n = int(sys.stdin.readline())
    result:int = 1
    for i in range(1, n+1):
        result *= i
    print(result)




