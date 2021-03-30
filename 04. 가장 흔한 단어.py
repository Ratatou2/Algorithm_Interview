'''
해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다

#04. 가장 흔한 단어
#금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
#대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다

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

remove_count1 = list_ca.count(banned[0])
for i in range(remove_count1):
    if list_ca.count(banned[0]) > 0:
        list_ca.remove(banned[0]) #금지한 단어를 리스트에서 삭제시키고,
print(list_ca)

#리스트안에 카운트 하는 코드를 짜줄 차례
#리스트 두개를 운용해서 키와 값을 따로 모아주는 식으로 쓸 예정
word_list = []
count_list = []
for i in range(len(list_ca)):
    count_word = list_ca[0]

    #딕셔너리에 추가
    word_list.append(count_word)
    count_list.append(list_ca.count(count_word))

    print(count_word, end=' : ')
    print(list_ca.count(count_word))

    remove_count2 =list_ca.count(count_word)
    for i in range(remove_count2):
        if list_ca.count(count_word) > 0:
            list_ca.remove(count_word)
            print(list_ca)
        else:
            print(list_ca)

    if len(list_ca) == 0: #더 이상 체크할게 남아있지 않다면 그냥 끝내기
        break

print(word_list)
print(count_list)
which = max(count_list)

#카운트 리스트에서 가장 큰 인덱스 찾기
max_index = count_list.index(which)
print(word_list[max_index])

'''
<해설>
1. 일단 딕셔너리를 사용해서 키와 값으로 분리하여 젤 높은 키값(카운트 젤 높은거)을 호출하려고 했는데 잘 안됐음
2. 그래서 그냥 배열을 두개 준다음 하나는 키, 하나는 값만 모아둔 배열로 사용하기로 했음
3. 다만 순서는 보장 되어야하므로 둘의 순서는 바뀌면 안됨, 그래서 sorted를 써줄 수 없었음
4. 그래서 일단 카운트 횟수가 제일 높은 값을 count_list에서 찾은 다음
5. 해당 값의 인덱스를 추출, 추출된 인덱스로 word_list에서 검색해서 카운트가 제일 높은 문자열을 찾아냈음
6. 짜고 보니 나 왜 이렇게 복잡하게 짰니... ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
7. 그래도 완성해서 뿌듯하긴하다...에휴... 
'''