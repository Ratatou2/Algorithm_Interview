#04. 가장 흔한 단어
#금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
#대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다

'''
물이방법
1. 일단 각 입력값이 하나씩 따로 꺼낼 수 있는 코드를 짠다
2. 꺼낸 것들이 대소문자 구분없이, 구두점은 지우는 코드를 짠다.
3. 금지된 단어를 제외하고, 각 단어들이 몇번씩 쓰였는지 카운트한다
4. 제일 자주쓰인 단어를 출력한다.
'''

#파이썬에서 제공하는 re(Regular Expression)의 sub(Substitiution) 함수를 이용할거임
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

#특수 문자를 제거하는 것은 import re 해서 쓰면 됨 
#아래는 re.sub의 형식임
clean_a = re.sub(pattern = '[^\w\s]' , repl='', string=paragraph) #쓸모없는 특수문자들을 전부 제거
transform_a = clean_a.lower() #일괄적으로 소문자처리
list_ca = transform_a.split() #쓸데없는 것들 삭제한걸 리스트로 쪼갬

remove_count = list_ca.count(banned[0])
for i in range(remove_count):
    if list_ca.count(banned[0]) > 0:
        list_ca.remove(banned[0]) #금지한 단어를 리스트에서 삭제시키고,
print(list_ca)

#리스트안에 카운트 하는 코드를 짜줄 차례


for i in range(len(list_ca)):
    count_word = list_ca[0]
    print(count_word, end=' : ')
    print(list_ca.count(count_word))
    list_ca.remove(count_word)
    if list_ca.count(count_word) > 0:
        list_ca.remove(count_word)
        print(list_ca)
    else:
        print(list_ca)

    if len(list_ca) == 0:
        break