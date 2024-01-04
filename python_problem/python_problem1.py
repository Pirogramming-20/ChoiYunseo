import random

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
    #computer
    comNum = random.randint(1,3)
    
    for i in range(comNum):
        callcomNum=num+1+i
        if callcomNum<31:
            print("computer",callcomNum)
        elif callcomNum == 31:
            print("computer 31")
            print("player win!")
            break
        else:
            print("player win!")
            break
        
    num = num+comNum

    if callcomNum == 31:
        break

    #player
    playerNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

    playerNum=brgame(playerNum) #함수 안에서 제대로 다시 받은 값을 playerNum으로 가지도록

    playerNum=int(playerNum)

    for i in range(playerNum):
        callPlayerNum=num+1+i
        if callPlayerNum<31:
            print("player",callPlayerNum)
        elif callPlayerNum ==31:
            print("player 31")
            print("computer win!")
            break
        else:
            print("computer win!")
            break
    
    num = num+playerNum

    if callPlayerNum == 31:
        break

    



    

