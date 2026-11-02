import random

score = 0
life = 2

while life > 0:
    pertanyaan = int(input("Tebak Angka 1-3:"))
    
    randomnumber = random.randint(1,3)

    print("life =",life)
    
    if randomnumber == pertanyaan:
        score += 1

    
    else:
        life -= 1
    
    print("score =",score)
    

    print(randomnumber)
    print("")

    


print(life)
print("Final Score =",score)

