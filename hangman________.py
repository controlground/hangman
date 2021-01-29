import random

file = open("wordd.txt","r")
pyth = file.read()
pyth = pyth.split()
creat = random.choice(pyth)
lengh = len(creat)
current_state = ['_'] * lengh
answer = 12
while True:
    print(" ".join(current_state))
    if answer == 0:
        print("아쉽지만 기회가 끝났습니다.")
        break
    else:
        print("기회가 " + str(answer) + "번 남았습니다.")
    correct = input()
    i = 0
    while i < len(creat):
        if correct == creat[i]:
            current_state[i] = correct
        i += 1
    answer -= 1
    if '_' not in current_state:
        print("정답을 맞히셨습니다!!!")
        break
print(creat)