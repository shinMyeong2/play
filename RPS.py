import os
import random

os.system('cls')
point = 0

while(True):
    player = input("주먹, 가위, 보 중 입력해주세요\n")
    if(player == "종료" or player == "q" or player == "Q" or player == "ㅂ"):
        print("게임을 종료합니다.")
        break
    elif(player != "주먹" and player != "가위" and player != "보"):
        os.system('cls')
        print("입력이 잘못되었습니다. 다시 선택해주세요")
        continue

    choices = ["주먹", "가위", "보"]
    computer = random.choice(choices)

    os.system('cls')
    print("플레이어 : %s\n컴퓨터 : %s"%(player, computer))

    if(player == computer):
        print("비겼습니다.")
    elif(player == "주먹"):
        if(computer == "가위"):
            print("이겼습니다.")
            point += 1
        elif(computer == "보"):
            print("졌습니다.")
    elif(player == "가위"):
        if(computer == "주먹"):
            print("졌습니다.")
        elif(computer == "보"):
            print("이겼습니다.")
            point += 1
    else:
        if(computer == "주먹"):
            print("이겼습니다.")
            point += 1
        elif(computer == "가위"):
            print("졌습니다.")
    print("점수 :", point)