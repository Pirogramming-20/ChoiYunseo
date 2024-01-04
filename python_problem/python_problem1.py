num = 0
playNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

while True:
    try:
        playNum = int(playNum)
        if playNum not in [1,2,3]:
            print("1,2,3 중 하나를 입력하세요.")
            playNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")
        else:
            break
    except ValueError:
        print("정수를 입력하세요.")
        playNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")

playNum = int(playNum)
