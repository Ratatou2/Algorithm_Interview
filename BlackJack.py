# 기본 룰 설명하는 타이밍이 있어야함
# 돈을 다 잃을 때까지 진행
# 딜러와 플레이어가 동시에 버스트가 되어도 플레이어 패배
# 딜러는 17미만일 경우 카드를 더 뽑아야함
# 스플릿 없음
# 컴퓨터의 랜덤 함수는 일반적으로 완벽하게 랜덤할 수가 없다고 생각함

import random

deck = ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4',
        '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8',
        '9', '9', '9', '9', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K',
        'A', 'A', 'A', 'A']

myMoney = 1000

def checkCard(define):
    if define == 'J':
        return 10
    elif define == 'Q':
        return 10
    elif define == 'K':
        return 10
    elif define == 'A':
        print("A를 1과 11 둘중 하나로 사용할 수 있습니다\n 어느쪽으로 사용하시겠습니까?")
        ans = int(input())
        if ans == 1:
            return 1
        else:
            return 11

    else: return int(define)


# 딜러와 플레이어는 서로 한장씩 카드를 번갈아 가며 뽑아야 공평하다
def playerAndDealer():
    #betMoney = input()

    count_card = 51 # 총 카드 갯수

    # 딜러의 첫 카드
    D_first_card = deck[random.randint(0, count_card)]
    deck.remove(D_first_card)
    count_card -= 1

    # 플레이어의 첫 카드
    P_first_Card = deck[random.randint(0, count_card)]
    deck.remove(P_first_Card)
    count_card -= 1
    print("첫번째 카드입니다 >>>", P_first_Card)

    # 딜러의 두번째 카드
    D_second_Card = deck[random.randint(0, count_card)]
    deck.remove(D_second_Card)
    count_card -= 1

    # 플레이어의 두번째 카드
    P_second_Card = deck[random.randint(0, count_card)]
    deck.remove(P_second_Card)
    count_card -= 1
    print("두번째 카드입니다 >>>", P_second_Card)

    # 딜러의 총합
    D_check_card1 = checkCard(D_first_card)
    D_check_card2 = checkCard(D_second_Card)
    D_total_Sum = D_check_card1 + D_check_card2


    # 플레이어의 총합
    P_check_card1 = checkCard(P_first_Card)
    P_check_card2 = checkCard(P_second_Card)
    P_total_Sum = P_check_card1 + P_check_card2

    print("현재 카드의 총합입니다 >>>", P_total_Sum, '\n')


    # 고칠점 아직 이후의 추가 카드를 딜러와 번갈아 가며 뽑는게 구현이 안됐음

    # 딜러 총합 while문
    while True:
        if D_total_Sum > 21:
            break

        else:
            plus = deck[random.randint(0, count_card)]
            deck.remove(plus)
            count_card -= 1

            check_plus = checkCard(plus)

            P_total_Sum += check_plus



    # 플레이어 총합 while문
    while True:
        if P_total_Sum > 21:
            print("버스트, 패배하셨습니다")
            break

        print("더 뽑으시겠습니까?\n 1.예 / 2.아니오")
        ans = int(input())

        if ans == 1:
            plus = deck[random.randint(0, count_card)]
            deck.remove(plus)
            count_card -= 1
            print("추가 카드입니다 >>>", plus)

            check_plus = checkCard(plus)

            P_total_Sum += check_plus
            print("현재 카드의 총합입니다 >>>", P_total_Sum)

        elif ans == 2: break



print("게임을 시작합니다")
playerAndDealer()

