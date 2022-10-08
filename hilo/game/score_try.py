initial_score = 300
run = True

while run:
    addition = int(input("add??  "))
    next_score = initial_score + addition

    print(next_score)
    initial_score = next_score

    exit = input("you exit?")
    if exit == "y":
        run = False
    else:
        pass