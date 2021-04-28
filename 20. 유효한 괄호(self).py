

check = input()


open = ['(', '{', '[']
close = [')', '}', ']']

count = 0
for i in check:
    print(i)
    if i in open:
        count += 1
    elif i in close:
        count -= 1

print(count)