num = 0

def brgame(a):
    while True:
        try:
            a = int(playNumA)
            if a not in [1,2,3]:
                print("1,2,3 중 하나를 입력하세요.")
                a = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")
            else:
                break
        except ValueError:
            print("정수를 입력하세요.")
            a = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

while True:
    #playerA
    playNumA = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

    brgame(playNumA)

    playNumA=int(playNumA)
    
    for i in range(playNumA):
        callNumA=num+1+i
        if callNumA!=32:
            print("playerA :",callNumA)
        else:
            print("playerB win!")
            break

    num = num+playNumA

    #playerB
    playNumB = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

    brgame(playNumB)

    playNumB=int(playNumB)

    for i in range(playNumB):
        callNumB=num+1+i
        if callNumB!=32:
            print("playerB :",callNumB)
        else:
            print("palyerA win!")
            break

    num = num+playNumB





    

