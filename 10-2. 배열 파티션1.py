# 해당 코드는 박상길 저자의 '파이썬 알고리즘 인터뷰'를 공부하며 적은 내용입니다
# 근데 이렇게 풀다보니 사실 리스트의 짝수번째에 있는 놈들만 더해도 될 것 같다(0부터 시작이니까)
# 왜냐면 정렬된 상태에선 항상 짝수번째에 작은 값이 위치하기 때문

def arrayPartition(target_list:list):
    sum = 0
    target_list.sort()
    for i in range(0, len(target_list)):
        if i % 2 == 0:
            sum += target_list[i]

    return sum

t_list = [1,4,3,2]

print(arrayPartition(t_list))

'''
- 위 코드가 내가 짠 코드인데 수정해줄 곳이 몇군데 있다
- 일단 내가 준 배열은 정렬되어 있지만, 랜덤 인풋을 받을 경우 정렬되어있지 않을 확률이 더 높기에 sort가 필요하다는 점
- 둘째로 enumerate를 써도 된다는 점

    <enumerate>
    - 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가짐
    - enumerate : 열거하다
    - 보통 for문과 자주 씀
    - 다음 코드를 테스트해보면 얼추 어떤 기능인지 알수 있음
    
    nums = [1,2,3,4,5,6,7]
    
    for i, n in enumerate(nums):
        print(i)
        print(n)
        
    - n을 따로 주지 않으면, i하나에 인덱스와 값 모두가 들어간다
'''