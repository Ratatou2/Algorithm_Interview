# 인터넷에서 구한 조합 코드 살짝 바꾼 원문
# (동일한 코드가 워낙 많아서 정확한 출처 기억 안남)
# 이걸로 공부할거임

''' <전반적인 코드>
- 일단 이 코드는 굉장히 섹시했다
- 내가 아직 뉴비이기도 하지만, 생각의 구조가 굉장히 신박했음
- 일단 이 코드는 재귀를 함으로써 for문을 한개만 써도 충분하도록 해놨다
- 따라서 이해하는데 상당한 시간을 소요했으며, 그래도 이해했다는게 뿌듯하여 주석과 수정한 부분 모두 그대로 달아둘 생각
'''

def combination(arr, Num_Of_Dig):
    # 일단 들어온 함수를 오름차순으로 배열해준다, 조합은 한번 쓴건 못쓰기 떄문에.
    arr = sorted(arr)
    print("<combination start>")

    # 재귀를 반복할 함수
    # 이 함수 덕분에 for문을 한번만 쓰면서도, 조건에 맞는 조합은 출력까지 가능하다
    def recursive(list_to_add):
        # 아래 print들은 내가 구분하기 위한 print
        # 아래의 if문은 list_to_add의 길이와 Num_of_digit이 같을 경우에 해당 조합을 출력한다
        # 한마디로 내가 설정한 자릿수(ex. 3자리)를 만족하는 조합이 있으면 참(True)으로 받아들이고 출력한다.
        # 미리 설정해둔 조합 조건에 맞지 않으면, 따로 else가 없기 떄문에 바로 아래 코드로 넘어감
        print("<recursive start>")
        print("현재 list_to_add len(길이) -> ", len(list_to_add), "list_to_add : ", list_to_add, end = " / ")
        print("현재 num_of_digit(자릿수) -> ", Num_Of_Dig)
        if len(list_to_add) == Num_Of_Dig:
            print(list_to_add)
            print("<recursive end>")
            return # 바로 종료, 이게 필요한 이유는 밑에 for문에서 이 함수르 다시 호출(재귀)할 것이기 때문이다.

        # start는 순서 상관 없이 원소가 같은 배열이 나올 수 없도록 시작 지점 설정하는 역할
        # index(pick[-1])이란 것은 pick[-1]가 리스트 내에서 몇번째인가? 하는 것임(코드 맨 밑에 예시(1))
        # start 해석 : list_to_add가 정상이라면(= 무언가 값이 있다면) start를 실행하는데 그게 아니면 0
        # -> 맨처음에 이 코드가 돌떈, list_to_add에 아무 값도 없으니 이 if문은 당연히 성립이 안되고 그럼 자동으로 0이 들어감(else문)
        # 한마디로 list_to_add가 아무것도 없는 None상태면 당연히 이 if문은 거짓이 됨
        # 그 말인 즉슨 아무것도 없는 상태니 else문 실행 -> start = 0 이 된다.
        start = arr.index(list_to_add[-1]) + 1 if list_to_add else 0

        print("<for start>", start)
        # 따라서 start는 시작지점을 찝어주는 것이고 이는 N~9까지 차례로 증가할 것이다.

        # for문이 시작되면 일단 i를 list_to_add에 추가한다
        # 그러고나서 recursive(list_to_add)를 함, 이는 현재 list_to_add가 위의 if문 조건을 만족하는지 확인하기 위함이다
        # 만족을 하면 print()를 진행하고 그대로 return 후 for문의 list_to_add에 들어있는 끝의 요소를 끄집어낸다
        # 만족 못할 경우(= 자릿수가 충족이 안될 경우) 그대로 내려와서 start를 진행하고는 for문 다시 진행
        # 자릿수가 여러개라면 해당 자릿수가 다 채워질때까지 반복하게 된다
        # 이런식의 운용 덕분에 for문 한개로도 자릿수 여러개를 충분히 충족할 수 있다
        for i in range(start, len(arr)): # start ~ arr길이만큼 반복 / 반복 될 수록 start가 증가하기에 반복회수는 적어짐
            list_to_add.append(arr[i])
            print("for문 도입하고 나서 list_to_add", list_to_add)
            recursive(list_to_add) # 내가 제일 헷갈렸던 부분인데, 여기서 recursive를 실행하고 끝나게 되면 밑의 pop을 실행하는 것이다.
            print("list_to_add before pop", list_to_add)
            list_to_add.pop() # for문의 중첩이 겹치면 pop이 여러번 일어날수가 있음, recursive가 끝나면 pop이 이뤄지니까
            print("list_to_add after pop", list_to_add)
        print("<for end>\n")

    recursive([]) # 현재 recursive는 (list_to_add)의 len(길이)로 움직이니까 리스트로 돌려줘야함
    print("<combination end>")


# 아래는 간단한 반복문 -> 자릿수를 몇개(r)로 할 것인지 지정해준다.
r = 4
#r = int(input())
for i in range(1, r+1):
    combination([1, 2, 3, 4, 5, 6, 7, 8, 9], i)

''' <예시 1>
한마디로
pick = [1,2,3,4,5,6,7,8,9] 가 있는데
print(pick.index(5)) 를 하면
5라는 요소가 몇번째 요소(= index가 몇이냐)라는 의미
-> 당연히 해답은 4번째(리스트는 0번부터 세니까)        
'''