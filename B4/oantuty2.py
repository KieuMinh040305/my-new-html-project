from random import randint
print("Nhập vào: Đấm, Lá hoặc Kéo")
player = input()
computer = randint(0,2)

if computer == 0:
    computer = "Đấm"
if computer == 1:
    computer = "Lá"
if computer == 2:
    computer = "Kéo"
# print(computer)

print("---------")
print("BẠN CHỌN :" + player)
print("MÁY CHỌN :" + computer)
print("VÁN NÀY BẠN ĐÃ :", end=" ")

if player == computer:
    print("Hòa")
else:
    if player == "Kéo":
        if computer == "Đấm":
            print("Thua")
        else:
            print("Thắng")
    elif player == "Đấm":
        if computer == "Kéo":
            print("Thắng")
        else:
            print("Thua")
    elif player == "Lá":
        if computer == "Kéo":
            print("Thua")
        else:
            print("Thắng")
    else:
        print("Nhập sai!")