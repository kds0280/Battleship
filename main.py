import random
board = [["-" for i in range(10)]for i in range(10)]
ships = {1:[[],[],[],[]],
        2:[[],[],[]],
        3:[[],[],[]],
        4:[[],[]],
        5:[[],[]],
        6:[[],[]],
        7:[[]],
        8:[[]],
        9:[[]],
        10:[[]]}
chance = 15
correct_count = 0
correct_ships = []
wrong_ships = []
#4칸짜리 ship 1개 랜덤배치
ships[1][0].append(random.randrange(0,7))  #10칸을 넘어서는 안되므로 범위 7까지 지정
ships[1][0].append(random.randrange(0,10))
for location in range(3):
    ships[1][location+1].append(ships[1][location][0]+1)  #오른쪽으로 한칸씩 배치
    ships[1][location+1].append(ships[1][location][1])
#3칸짜리 ship 2개 랜덤배치
for num in range(2,4):
    overlap = "fail"
    while(overlap == "fail"):  #다른 배와 겹칠시에 범위 재지정
        ships[num][0].append(random.randrange(0,8))  #10칸을 넘어서는 안되므로 범위 8까지 지정
        ships[num][0].append(random.randrange(0,10))
        for location in range(2):
            ships[num][location+1].append(ships[num][location][0]+1)  #오른쪽으로 한칸씩 배치
            ships[num][location+1].append(ships[num][location][1])
        #overlap check
        for i in ships[num]:
            for j in range(1,num):
                if i not in ships[j]:
                    overlap = "pass"
#2칸짜리 ship 3개 랜덤배치
for num in range(4,7):
    overlap = "fail"
    while(overlap == "fail"):  #다른 배와 겹칠시에 범위 재지정
        ships[num][0].append(random.randrange(0,9))  #10칸을 넘어서는 안되므로 범위 9까지 지정
        ships[num][0].append(random.randrange(0,10))
        for location in range(1):
            ships[num][location+1].append(ships[num][location][0]+1)  #오른쪽으로 한칸씩 배치
            ships[num][location+1].append(ships[num][location][1])
        #overlap check
        for i in ships[num]:
            for j in range(1,num):
                if i not in ships[j]:
                    overlap = "pass"
#2칸짜리 ship 4개 랜덤배치
for num in range(7,11):
    overlap = "fail"
    while(overlap == "fail"):  #다른 배와 겹칠시에 범위 재지정
        for location in range(2):
            ships[num][0].append(random.randrange(0,10))
        #overlap check
        for j in range(1,num):
            if ships[num] not in ships[j]:
                overlap = "pass"
def show_board():
    for loca in correct_ships:
        board[loca[0]][loca[1]] = "X"
    for i in board:
        for j in i:
            print(j, end = "")
        print()
guess = []
guess.append(int(input("맞추고자 하는 x좌표를 적어주세요 : ")))
guess.append(int(input("맞추고자 하는 y좌표를 적어주세요 : ")))
while(chance>1 and correct_count<9):
    result = "wrong"
    for key, value in ships.items():
        if guess in value:
            result = "correct"
            number_of_correct_ship = key
    if result == "correct":
        print(result)
        correct_count = correct_count +1
        print("{}번 맞췄습니다.".format(correct_count))
        #맞은 배는 correct_ship에 저장
        for i in ships[number_of_correct_ship]:
            print(i)
            correct_ships.append(i)
        show_board()
    else:
            print(result)
            chance = chance -1
            print("남은 기회는{} 번 입니다.".format(chance))
            #틀린 배는 correct_ship에 저장
            wrong_ships.append(guess)
    guess = []
    guess.append(int(input("맞추고자 하는 x좌표를 적어주세요 : ")))
    guess.append(int(input("맞추고자 하는 y좌표를 적어주세요 : ")))
if(chance == 1):
    print("You Lose!!")
else:
    print("You Win!!")