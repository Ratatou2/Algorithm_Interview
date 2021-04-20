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
count_card= 51 # 총 카드 갯수

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
    global myMoney
    global count_card

    def dealerDraw():
        D_card = deck[random.randint(0, count_card)]
        deck.remove(D_card)
        return D_card

    def playerDraw():
        P_card = deck[random.randint(0, count_card)]
        deck.remove(P_card)
        return P_card

    # 딜러의 첫 카드
    D_first = dealerDraw()
    count_card -= 1

    # 플레이어의 첫 카드
    P_first = playerDraw()
    count_card -= 1
    print("첫번째 카드 >>>", P_first)

    # 딜러의 두번째 카드
    D_second = dealerDraw()
    count_card -= 1

    # 플레이어의 두번째 카드
    P_second = playerDraw()
    count_card -= 1
    print("두번째 카드 >>>", P_second)

    # 딜러의 총합
    D_check_card1 = checkCard(D_first)
    D_check_card2 = checkCard(D_second)
    D_total_Sum = D_check_card1 + D_check_card2

    # 딜러는 자신의  합을 미리 보고 더 뽑아도 됨
    # 딜러의 조건부 세번째 카드
    if D_total_Sum < 17:
        D_plus = dealerDraw()
        count_card -= 1
        D_check = checkCard(D_plus)
        D_total_Sum += D_check
    elif 17 < D_total_Sum < 21:
        pass

    # 플레이어의 총합
    P_check_card1 = checkCard(P_first)
    P_check_card2 = checkCard(P_second)
    P_total_Sum = P_check_card1 + P_check_card2

    print("현재 플레이어 카드의 총합 >>>", P_total_Sum, '\n')


    # 플레이어 총합 while문
    while True:
        if D_total_Sum < 17:
            D_plus2 = dealerDraw()
            count_card -= 1
            D_check2 = checkCard(D_plus2)
            D_total_Sum += D_check2
        elif 17 < D_total_Sum < 21:
            pass

        if P_total_Sum == 21:
            print("<System> 블랙잭입니다!")
            break
        elif P_total_Sum > 22:
            print("<System> 플레이어 버스트")
            break

        print("<System> 더 뽑으시겠습니까?\n (1) 예 / (2) 아니오")
        ans = int(input())

        if ans == 1:
            plus = deck[random.randint(0, count_card)]
            deck.remove(plus)
            count_card -= 1
            print("추가 카드 >>>", plus)

            check_plus = checkCard(plus)

            P_total_Sum += check_plus
            print("현재 카드의 총합 >>>", P_total_Sum)

        elif ans == 2: break

    print("딜러의 총합 >>>", D_total_Sum)
    print("플레이어의 총합 >>>", P_total_Sum)

    if D_total_Sum > 21:
        if P_total_Sum > 21:
            myMoney -= 100

        else:
            print("<System> 딜러 버스트, 플레이어의 승리")
            myMoney += 100
    elif D_total_Sum == P_total_Sum:
        print("<System> 무승부, 돈을 돌려받습니다")
    elif D_total_Sum > P_total_Sum:
        print("<System> 딜러의 승리")
        myMoney -= 100
    elif D_total_Sum < P_total_Sum:
        if P_total_Sum < 22:
            print("<System> 플레이어의 승리")
            myMoney += 100
        else:
            print("<System> 버스트, 패배하였습니다.")
            myMoney -= 100

    print("현재 나의 돈 >>>", myMoney, "\n")
    print("-------------------------------")




while True:
    print("엔터를 치면 새 게임을 시작합니다")
    input()
    playerAndDealer()

    if myMoney == 0:
        print('당신은 파산하였습니다')
        break
    else: pass
