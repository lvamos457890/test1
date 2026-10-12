def check_guess():
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt <5:
        guess = input("Guess: ")
        if guess.lower() == answer.lower():
            print("Correct answer!")
            score += 1
            still_guessing = False

        else:
            if attempt < 3:
                print("Wrong answer")
            attempt += 1

score = 0
print("Guess the Country")

print("1+1 = ")
answer = "3"
check_guess()


 
        
