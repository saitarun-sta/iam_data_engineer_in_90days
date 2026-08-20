guess = 6

guessed_number = int(input("Enter Number: "))

while guess:
    if guessed_number > guess:
        print("you entered high guess, try low")
    elif guessed_number < guess:
        print("you entered low guess, try high")
    else:
        print("Yay ! you got it")
        break

