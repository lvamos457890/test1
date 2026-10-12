# i = 0

# Point = 0

soalsoal = {
    "Apa nama makanan dari Papua": "Papeda",
    "Apa nama makanan dari DKI Jakarta": "Kerak Telor",
    "Apa nama makanan dari Makassar": "Coto Makassar",
    "Apa nama makanan dari Pontianak": "Bubur Pedas",
    "Apa nama makanan dari Medan": "Bika Ambon"
}

    
# Papua = input("Papua:")
# DKIJakarta = input("DKI Jakarta:")
# Makassar = input("Makassar:")
# Pontianak = input("Pontianak:")
# Medan = input("Medan:")

def check_guess():
    global score
    still_guessing = True
    attempt = 3
    for soal, answer in soalsoal.items():
        if attempt == 0:
            break

        print(soal)

        while still_guessing and attempt >=1:
            print("life =",attempt)
            guess = input("Guess: ")
            if guess.lower() == answer.lower():
                print("Correct answer!")
                score += 1
                still_guessing = False
            
            else:
                print("Wrong answer")
                attempt -= 1

        still_guessing = True


score = 0

print("Tebak makanannya!")
check_guess()
print("Score mu adalah" , (score))
# while i == 0:        
    
#     Papua = input("Papua:")
#     DKIJakarta = input("DKI Jakarta:")
#     Makassar = input("Makassar:")
#     Pontianak = input("Pontianak:")
#     Medan = input("Medan:")

#     daerah = [Papua, DKIJakarta, Makassar, Pontianak, Medan]

#     print(".......")
#     print("   ")

#     if daerah[0] == "Papeda": 
#         Point += 1
    
    
#     if daerah[1] == "Kerak Telor":
#         Point += 1

#     if daerah[2] == "Coto Makassar":
#         Point += 1


#     if daerah[3] == "Bubur Pedas":
#         Point += 1

#     if daerah[4] == "Bika Ambon":
#         Point += 1

# print("Point:",Point)

    



    
    




    
