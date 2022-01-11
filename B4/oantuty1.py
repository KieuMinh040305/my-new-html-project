from random import randint
player = input()
computer = randint(0,2)

if computer == 0:
    computer = "Đấm"
if computer == 1:
    computer = "Lá"
if computer == 2:
    computer = "Kéo"
print(computer)

print("---------")
print("Người :" + player)
print("Máy :" + computer)
print("---------")

if player == "Kéo":
    if computer == "Đấm":
        print("Thua")
    if computer == "Lá":
        print("Thắng")
    if computer == "Kéo":
        print("Hòa")

if player == "Đấm":
    if computer == "Đấm":
        print("Hòa")
    if computer == "Lá":
        print("Thua")
    if computer == "Kéo":
        print("Thắng")

if player == "Lá":
    if computer == "Đấm":
        print("Thắng")
    if computer == "Lá":
        print("Hòa")
    if computer == "Kéo":
        print("Thua")