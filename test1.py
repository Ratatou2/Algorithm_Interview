logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

letters, digits = [], []

for log in logs: #logs에서 하나씩 log로 불러옴
    print('처리할 로그 : ' + log)
    print('식별자를 제외한 첫 문자열은 무엇인가? : ' + log.split()[1])
    print('식별자를 제외한 첫 문자열이 숫자인가? : ', end='')
    print(log.split()[1].isdigit())
    #1번, 그러니까 두번째 요소가 숫자인지 아닌지 체크하는 이유는, 로그의 가장 앞부분은 식별자로써, 순서에 영향을 끼치지 않기 떄문이다
    #그래서 1번만 체크하고 1번이 숫자면(if ~ isdigit()) digitis 리스트에 추가하는 것이다.

    if log.split()[1].isdigit():
        digits.append(log)
        print("숫자니까 digtis에 집어 넣는다")
        print(digits, '\n')
    else:
        letters.append(log)
        print('숫자가 아니니까 letters에 집어 넣는다')
        print(letters, '\n')


print('final_letters: ', letters)
print('final_digits : ', digits)


letters.sort(key=lambda  x:(x.split()[1:], x.split()[0]))
conclision = letters + digits