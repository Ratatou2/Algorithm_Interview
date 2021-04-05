#해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다

# 인자를 두개 받는다
def twoSum(nums, target):
    # for문을 두 번 돌리는데 일단 n은 target에서 해당 숫자를

    # enumerate하면 값이 2개가 나오는데 각각이 i와 n에 담김
    # i -> 인덱스 (0~3) / n -> 값(2, 7, 11, 15)
    # 그러니 먼젓번 for문에서 target에서 인덱스 순서에 해당하는 값을 뺸 값을 complete에 넣고
    # 그 값이 주어진 배열(=nums)에 있다면 해당 인덱스(i)와 값(n)을 분리함
    for i, n in enumerate(nums): # 맨 아래에 공부(*)
        complement = target - n # 그리고 target에서 값을 뺀 것이 리스트에 있는지 확인하기 위해 commplement를 만듦

        if complement in nums[i + 1:]: # 혅재 i번은 검사하는데 쓰였으니 I+1로 그 이후 것을 검사함
            '''이게 보면 다음과 같은 조건일 때
            nums = [1, 3, 6, 9, 13, 17]
            target = 15
            - i가 2일때 처음으로 if문을 통과할 수 있음
            - i가 2일때, n은 6이고 그것의 인덱스는 2임
            - 같은 이치로 i = 2니까, i + 1 = 3 / complement = 15-6 = 9인 상황
            - num[3:].index((9)는 nums = [9, 13, 17] 중에 9의 인덱스를 구하라는 것이니까 0의 인덱스는 0
            - 그렇기 때문에 i + 1 = 3 이 추가로 더해져야하는 것이다
            - 온전히 이해하는데는 조금 걸렸지만 순서대로 차근차근 생각해보면 충분히 이해할 수 있음
            '''
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)


nums = [1, 3, 6, 9, 13, 17]
target = 15

print(twoSum(nums, target))

''' (*) < Enumberate 공부 >
- enumerate는 '열거하다'라는 뜻이다
- 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 ㅍ함하는 enumerate객체를 돌려준다
- 보통 for 문과 자주 사용한다
- 예제

a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for i in enumerate(a):
    print(i)


>> D:\Github\Clone\venv\Scripts\python.exe D:/Github/Clone/test.py
(0, 'A')
(1, 'B')
(2, 'C')
(3, 'D')
(4, 'E')
(5, 'F')
(6, 'G')
(7, 'H')
(8, 'I')
(9, 'J')

-> 즉, i에는 a에서 enumerate된 값들(일종의 키와 값)이 담기게 되는 것이다. 
'''