num = 0

def brgame(a):
    while True:
        try:
            a = int(a)
            if a not in [1,2,3]:
                print("1,2,3 중 하나를 입력하세요.")
                a = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")
            else:
                return a
        except ValueError:
            print("정수를 입력하세요.")
            a = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

while True:
    #playerA
    playerNumA = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

    playerNumA=brgame(playerNumA) #함수 안에서 제대로 다시 받은 값을 playerNum으로 가지도록

    playerNumA=int(playerNumA)

    for i in range(playerNumA):
        callPlayerNumA=num+1+i
        if callPlayerNumA<31:
            print("playerA",callPlayerNumA)
        elif callPlayerNumA ==31:
            print("playerA 31")
            print("playerB win!")
            break
        else:
            print("playerB win!")
            break
    
    num = num+playerNumA

    if callPlayerNumA == 31:
        break

    #playerB
    playerNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

    playerNum=brgame(playerNum) #함수 안에서 제대로 다시 받은 값을 playerNum으로 가지도록

    playerNum=int(playerNum)

    for i in range(playerNum):
        callPlayerNum=num+1+i
        if callPlayerNum<31:
            print("playerB",callPlayerNum)
        elif callPlayerNum ==31:
            print("playerB 31")
            print("playerA win!")
            break
        else:
            print("playerA win!")
            break
    
    num = num+playerNum

    if callPlayerNum == 31:
        break
