''' < 오늘 배운 것 활용>
1. collections의 defaultdict()를 사용해서 my_list를 리스트를 갖는 딕셔너리로 만든다
2. 함수에 대한 이해를 높이기 위해 함수를 하나 만들고 실행시킨다
'''

import collections

my_list = collections.defaultdict(list)
word = 21

print(my_list['Main'].append(word))
my_list['test'].append("it's me!")
print(my_list)


def myStatus(status):
    if status == 'good':
        print("I hope you have a satisfying day tomorrow too")

    else:
        print("I hope you have a satisfying day tomorrow")

print('How are you today??')
myStatus(input())
