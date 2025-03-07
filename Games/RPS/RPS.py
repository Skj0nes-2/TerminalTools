
from random import randint

print(f"1. Rock\n2. Paper\n3. Scissors\n")
hand = int(input("Choose: "))
botHand = randint(1, 3)
filePath = "RPS.log"

if hand == 1:
    handType = "Rock"
elif hand == 2:
    handType = "Paper"
else:
    handType = "Scissors"

if botHand == 1:
    botHandType = "Rock"
elif botHand == 2:
    botHandType = "Paper"
else:
    botHandType = "Scissors"


if hand == 1 and botHand != 2:
    win = True

elif hand == 2 and botHand != 3:
    win = True

elif hand == 3 and botHand != 1:
    win = True

else:
    win = False

if win:
    print(f"\nYou won!")
    winType = "Win"
else:
    print(f"\nYou Lost...")
    winType = "Lost"
with open(filePath, 'a') as file:
    file.write(f"\nResult: {winType}\nHand: {handType}\nBot Hand: {botHandType}\n")
    print(f"Game Logged in '{filePath}'")