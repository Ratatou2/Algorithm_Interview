'''
해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
문자열 배열을 받아 애너그램 단위로 그룹핑하라

[ex]
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

<내 생각에는>
풀이법은 일단 입력 받는 것들을 쪼개서 정렬을 시킨 다음 같은 것들만 묶어야 할 듯 싶다
- 정렬하여 딕셔너리에 추가
- 정렬하면 애너그램끼린 서로 같은 값을 같게됨
- sorted()는 문자열도 잘 정렬하면서 결과를 리스트 형태로 리턴
- 사용할땐 join()으로 합쳐서 이 값을 키로 하는 딕셔너리를 구성
- 그러면 이제 애너그램끼리 같은 키를 갖게 되고 따라서 여기에 append하는 형태가 됨
'''
import collections
#데이터 처리를 위한 collectinos 모듈
#우리는 deafultdict를 쓰기 위해 선언하였다

def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)
    ''' <anagrams = collections.defaultdict(list)에 대한 이해>
    - 일단 collections.defulatdict라고 쓰는 것은 내가 import collections만 해줬기 떄문이다.
    - 간결하게 싶으면 위의 import 문을 from collections import defaultdict라고 적어주면 된다
    - 그러면 단순하게 아래와 같이 적을 수 있다.
        - anagrams = defaultdict(list)
    - 또한 defualitdict(list)라는 것은 인자로 주어진 list라는 객체의 기본값을 딕셔너리의 초깃값으로 지정한다는 것이다.
    - 한마디로 defaultdict는 anagrams라는 딕셔너리의 초기값을 list로 지정한다는 것이다.
        
    defaultdict()는 딕셔너리를 만드는 dict클래스의 서브 클래스이다.
    +a 원래 딕셔너리는 존재하지 않는 키를 삽입하려하면 에러가 난다
    그런데 defaultdict()를 해주면 항상 디폴트를 생성해주기 때문에, 매번 키 존재 여부를 체크하지 않고 비교 구문을 생략해 간결하게 구성할 수 있다.
    '''
    print("anagram's type? : ", type(anagrams))
    print('anagram : ', anagrams)
    print('전체 strs : ', strs)

    for word in strs:
        print('해당 차례의 word : ', word)
        print('정렬된 상태의 word : ', sorted(word))
        anagrams[''.join(sorted(word))].append(word)
        print(anagrams)

    ''' <for문에 대한 이해>
    - 위의 for문은 strs 안에 있는 것들을 하나씩 word에 넣어서 반복하는 for문이다
    - 그렇게 나온 word를 anagrams 리스트에 하나씩 추가하는 것임
        - 그 word들은 sorted()에 의해 철자 하나 하나 분해되어 리스트로 정렬되어있음
        - 근데 그런 식이면 현재 sorted(word)는 ['a', 'e', 't'] 이런 값을 가져야한다.
        - 그렇게 나오지 않게 하기 위해 join을 사용한 것이다
            - join 사용법
                - join의 기본 구조는 다음과 같다
                - '구분자'.join(리스트)
                - 이러한 구조에 의하여 위의 코드를 보면 일단, 문자끼리 구분해줄 구분자는 ''으로 말그대로 공백, 아무것도 없다
                - 그러고 나서 .join을 하였으니 ['a', 'e', 't']가 aet로 출력되는 것이다
                - 정리하면
                    - sorted(word) => ['a', 'e', 't']
                    - ''.join(sorted(word)) => aet
        - 그다음에 anagrma에 append함
        - 근데 저렇게 그룹핑할 수 있는 이유는 anagrams을 생성할때 리스트를 초기값으로 받는 딕셔너리로 생성했기 때문이다..
        - 그렇기 때문에 정렬한 aet라는 단어를 키로 잡고, 정렬되기 전의 단어를 값으로 잡는 것이다.
        - 그렇게하면 같은 키(ex. aet)를 가지는 애들은 한군데에 모여 값이 될 것이고, 우리는 나중에 같은 키에의해 모인 값들만 추출하면 된다 
    
    +a sorted()라는 함수 외에도 리스트 자료형에 sort() 메소드를 따로 제공한다.
    둘의 가장 큰 차이점은 sort()는 리스트 자체를 제자리 정렬하며 None을 리턴한다는 것,
    sorted()는 정렬 결과를 별도로 리턴한다는 것이 다르다.
    
    +a sorted()는 key=옵션을 지정해 정렬을 위한 키 또는 함수를 별도 지정 가능
    ex.
        str_list = ['ccc', 'aaaa', 'd', 'bb']
        sorted(str_list, key=len) #키의 길이순으로 정렬하라는 뜻
        >>>['d', 'bb', 'ccc', 'aaaa'] 
    '''
    return anagrams.values()
    #그리고 같은 키에 모인 값들만 출력하기 위해서 위 함수의 결과를 anagrams의 values(값)로 return 하는 것이다.


strs_list = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs_list))