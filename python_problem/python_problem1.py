num = 0

while True:
    playNumA = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

    while True:
        try:
            playNumA = int(playNumA)
            if playNumA not in [1,2,3]:
                print("1,2,3 중 하나를 입력하세요.")
                playNumA = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")
            else:
                break
        except ValueError:
            print("정수를 입력하세요.")
            playNumA = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

    playNumA = int(playNumA)

    for i in range(playNumA):
        callNumA=num+1+i
        if callNumA!=32:
            print("playerA :",callNumA)
        else:
            print("playerB win!")
            break

    num = num+playNumA

    #playB
    playNumB = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

    while True:
        try:
            playNumB = int(playNumB)
            if playNumB not in [1,2,3]:
                print("1,2,3 중 하나를 입력하세요.")
                playNumB = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")
            else:
                break
        except ValueError:
            print("정수를 입력하세요.")
            playNumB = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

    playNumB = int(playNumB)

    for i in range(playNumB):
        callNumB=num+1+i
        if callNumB!=32:
            print("playerB :",callNumB)
        else:
            print("palyerA win!")
            break

    num = num+playNumB





    

