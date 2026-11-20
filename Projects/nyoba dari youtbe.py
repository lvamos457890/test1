# # umur = 13
# # tinggi = 178
# # nama = "amos"
# # print("hallo nama saya " + str(nama) + " umur saya " +str(umur)+ " tinggi saya " + str(tinggi) + "cm")


# # ada_kayu = True
# # if (ada_kayu):
# #     print ("lompat")
# # else:
# #     print ("jalan terus")




# # Doni = 61

# # if Doni > 60:
# #     print("Doni harus olahraga")
# # elif Doni == 60:
# #     print("Doni sudah kenyang")
# # else:
# #     print("Doni butuh makan")

# # import time
# # Doni = 60

# # Doni = int(input("berapa berat badan doni?"))

# # print("Sedang menganalisis...")
# # time.sleep(3)

# # if Doni > 60:
# #     print("Doni butuh olahraga")




# # if Doni == 60:
# #     print("Berat Doni ideal")



# # if Doni < 60:
# #     print("Doni butuh makan")







# # i di dalam (for i in range) itu cuma nama bebas aja bebas pake apa aja biasanya tergantung apa yang di promt


# # import time

# # for i in range(3):
# #     time.sleep(1)
# #     Doni = int(input("Berapa berat badan Doni? "))

# #     print("Sedang menganalisis...")
# #     time.sleep(3)

# #     if Doni > 60:
# #         print("Doni butuh olahraga")

# #     elif Doni == 60:
# #         print("Berat Doni ideal")

# #     else:
# #         print("Doni butuh makan")

# # print("END")





# olahraga=["football", "basketball", "volleyball"]
# print(olahraga[1])  




# # murid="jono", "siti", "tono"
# # for i in murid:
# #     print(i + " hadir pak🗿")

# # hobi=["main bola", "main game", "olahraga"]
# # print(hobi[1])

# # murid="jono", "budi", "sinta"
# # for i in murid:
# #     print(i + " hadir pak!")


# kipas_tidak_nyala=False
# while(kipas_tidak_nyala):
#     print("perbaikilahh")


import random
import time
import os

# =========================
# CLEAR SCREEN
# =========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# =========================
# PLAYER
# =========================

player = {
    "name": "PLAYER",
    "level": 1,
    "hp": 100,
    "max_hp": 100,
    "mana": 50,
    "max_mana": 50,
    "attack": 20,
    "defense": 5,
    "xp": 0,
    "xp_needed": 100,
    "gold": 100,
    "potions": 3
}


# =========================
# ENEMIES
# =========================

enemies = [
    {
        "name": "Goblin",
        "hp": 60,
        "attack": 12,
        "defense": 2,
        "xp": 40,
        "gold": 25
    },
    {
        "name": "Skeleton",
        "hp": 80,
        "attack": 16,
        "defense": 4,
        "xp": 55,
        "gold": 35
    },
    {
        "name": "Orc",
        "hp": 120,
        "attack": 22,
        "defense": 7,
        "xp": 80,
        "gold": 50
    },
    {
        "name": "Dark Knight",
        "hp": 180,
        "attack": 28,
        "defense": 10,
        "xp": 120,
        "gold": 80
    }
]


# =========================
# BOSS
# =========================

boss = {
    "name": "DRAGON LORD",
    "hp": 500,
    "attack": 45,
    "defense": 15,
    "xp": 500,
    "gold": 500
}


# =========================
# LOADING
# =========================

def loading(text):
    print(text)

    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    print()
    time.sleep(0.5)


# =========================
# HEALTH BAR
# =========================

def health_bar(hp, max_hp, size=25):

    hp = max(0, hp)

    filled = int((hp / max_hp) * size)

    empty = size - filled

    return "[" + "#" * filled + "-" * empty + "]"


# =========================
# PLAYER STATUS
# =========================

def show_status():

    print("\n========== PLAYER ==========")

    print("Level :", player["level"])

    print(
        "HP    :",
        health_bar(player["hp"], player["max_hp"]),
        player["hp"],
        "/",
        player["max_hp"]
    )

    print(
        "Mana  :",
        health_bar(player["mana"], player["max_mana"]),
        player["mana"],
        "/",
        player["max_mana"]
    )

    print("Attack:", player["attack"])
    print("Defense:", player["defense"])

    print("XP:", player["xp"], "/", player["xp_needed"])
    print("Gold:", player["gold"])
    print("Potions:", player["potions"])

    print("============================")


# =========================
# LEVEL UP
# =========================

def level_up():

    while player["xp"] >= player["xp_needed"]:

        player["xp"] -= player["xp_needed"]

        player["level"] += 1

        player["xp_needed"] = int(
            player["xp_needed"] * 1.5
        )

        player["max_hp"] += 25
        player["max_mana"] += 10

        player["attack"] += 7
        player["defense"] += 3

        player["hp"] = player["max_hp"]
        player["mana"] = player["max_mana"]

        print("\n🔥 LEVEL UP!")

        print(
            "You are now level",
            player["level"]
        )

        print("+25 Max HP")
        print("+10 Max Mana")
        print("+7 Attack")
        print("+3 Defense")

        time.sleep(2)


# =========================
# DAMAGE
# =========================

def calculate_damage(attack, defense):

    damage = attack - defense

    if damage < 1:
        damage = 1

    # Critical hit
    critical = random.randint(1, 100)

    if critical <= 20:

        damage *= 2

        print("💥 CRITICAL HIT!")

    # Random damage
    damage += random.randint(-3, 5)

    return max(1, damage)


# =========================
# NORMAL ATTACK
# =========================

def normal_attack(enemy):

    damage = calculate_damage(
        player["attack"],
        enemy["defense"]
    )

    enemy["hp"] -= damage

    print(
        "\n⚔️ You attacked",
        enemy["name"]
    )

    print(
        "Damage:",
        damage
    )

    time.sleep(1)


# =========================
# FIREBALL
# =========================

def fireball(enemy):

    mana_cost = 15

    if player["mana"] < mana_cost:

        print("❌ Mana tidak cukup!")

        time.sleep(1)

        return

    player["mana"] -= mana_cost

    damage = player["attack"] * 2

    damage += random.randint(5, 15)

    enemy["hp"] -= damage

    print("\n🔥 FIREBALL!")

    print(
        "Damage:",
        damage
    )

    time.sleep(1)


# =========================
# HEAL
# =========================

def heal():

    mana_cost = 10

    if player["mana"] < mana_cost:

        print("❌ Mana tidak cukup!")

        time.sleep(1)

        return

    if player["hp"] == player["max_hp"]:

        print("HP kamu sudah penuh!")

        time.sleep(1)

        return

    player["mana"] -= mana_cost

    amount = 35 + player["level"] * 5

    player["hp"] += amount

    if player["hp"] > player["max_hp"]:
        player["hp"] = player["max_hp"]

    print("\n💚 Kamu memulihkan", amount, "HP!")

    time.sleep(1)


# =========================
# POTION
# =========================

def use_potion():

    if player["potions"] <= 0:

        print("❌ Potion habis!")

        time.sleep(1)

        return

    player["potions"] -= 1

    amount = 50

    player["hp"] += amount

    if player["hp"] > player["max_hp"]:
        player["hp"] = player["max_hp"]

    print("\n🧪 Potion digunakan!")

    print("+", amount, "HP")

    time.sleep(1)


# =========================
# ENEMY ATTACK
# =========================

def enemy_attack(enemy):

    damage = calculate_damage(
        enemy["attack"],
        player["defense"]
    )

    player["hp"] -= damage

    print(
        "\n👹",
        enemy["name"],
        "attacked you!"
    )

    print(
        "Damage:",
        damage
    )

    time.sleep(1)


# =========================
# BATTLE
# =========================

def battle(enemy):

    enemy = enemy.copy()

    clear()

    print("================================")
    print("          ⚔️ BATTLE ⚔️")
    print("================================")

    print(
        "\nYou encountered:",
        enemy["name"]
    )

    time.sleep(1)

    while player["hp"] > 0 and enemy["hp"] > 0:

        clear()

        print("================================")
        print("          ⚔️ BATTLE ⚔️")
        print("================================")

        print(
            "\nEnemy:",
            enemy["name"]
        )

        print(
            "HP:",
            health_bar(
                enemy["hp"],
                enemy.get("max_hp", enemy["hp"])
            ),
            enemy["hp"]
        )

        show_status()

        print("\n1. ⚔️ Attack")
        print("2. 🔥 Fireball")
        print("3. 💚 Heal")
        print("4. 🧪 Potion")
        print("5. 🏃 Run")

        choice = input("\nChoose: ")

        if choice == "1":

            normal_attack(enemy)

        elif choice == "2":

            fireball(enemy)

        elif choice == "3":

            heal()

        elif choice == "4":

            use_potion()

        elif choice == "5":

            chance = random.randint(1, 100)

            if chance <= 50:

                print("\n🏃 You escaped!")

                time.sleep(1)

                return False

            else:

                print("\n❌ You failed to escape!")

                time.sleep(1)

        else:

            print("Pilihan tidak valid!")

            time.sleep(1)

            continue

        # Enemy turn

        if enemy["hp"] > 0:

            enemy_attack(enemy)

    # =========================
    # WIN
    # =========================

    if player["hp"] > 0:

        print("\n================================")
        print("          🏆 VICTORY!")
        print("================================")

        print(
            "\nYou defeated",
            enemy["name"]
        )

        print(
            "+",
            enemy["xp"],
            "XP"
        )

        print(
            "+",
            enemy["gold"],
            "Gold"
        )

        player["xp"] += enemy["xp"]
        player["gold"] += enemy["gold"]

        level_up()

        time.sleep(2)

        return True

    return False


# =========================
# BOSS FIGHT
# =========================

def boss_fight():

    enemy = boss.copy()

    enemy["max_hp"] = enemy["hp"]

    clear()

    print("======================================")
    print("             ☠️ WARNING ☠️")
    print("======================================")

    print("\nTHE DRAGON LORD HAS AWAKENED!")

    time.sleep(2)

    while player["hp"] > 0 and enemy["hp"] > 0:

        clear()

        print("======================================")
        print("             👹 BOSS FIGHT")
        print("======================================")

        print(
            "\nBOSS:",
            enemy["name"]
        )

        print(
            health_bar(
                enemy["hp"],
                enemy["max_hp"],
                40
            ),
            enemy["hp"],
            "/",
            enemy["max_hp"]
        )

        show_status()

        print("\n1. ⚔️ Attack")
        print("2. 🔥 Fireball")
        print("3. 💚 Heal")
        print("4. 🧪 Potion")

        choice = input("\nChoose: ")

        if choice == "1":

            normal_attack(enemy)

        elif choice == "2":

            fireball(enemy)

        elif choice == "3":

            heal()

        elif choice == "4":

            use_potion()

        else:

            print("Pilihan tidak valid!")

            time.sleep(1)

            continue

        if enemy["hp"] > 0:

            enemy_attack(enemy)

    if player["hp"] > 0:

        clear()

        print("======================================")
        print("        🏆 YOU DEFEATED THE BOSS")
        print("======================================")

        print("\n🔥 DRAGON LORD HAS FALLEN!")

        print("+500 XP")
        print("+500 GOLD")

        player["xp"] += 500
        player["gold"] += 500

        level_up()

        time.sleep(3)

        return True

    return False


# =========================
# MAIN MENU
# =========================

def main_menu():

    while True:

        clear()

        print("====================================")
        print("       ⚔️ LEGENDS OF PYTHON ⚔️")
        print("====================================")

        print("\n1. Start Game")
        print("2. Player Status")
        print("3. Exit")

        choice = input("\nChoose: ")

        if choice == "1":

            game()

        elif choice == "2":

            clear()

            show_status()

            input("\nPress ENTER...")

        elif choice == "3":

            print("\nGoodbye!")

            break

        else:

            print("Invalid choice!")

            time.sleep(1)


# =========================
# GAME
# =========================

def game():

    fights = 0

    while player["hp"] > 0:

        clear()

        print("====================================")
        print("             WORLD MAP")
        print("====================================")

        print("\n1. 🌲 Explore Forest")
        print("2. 🏰 Enter Dungeon")
        print("3. 👹 Fight Boss")
        print("4. 📊 Status")
        print("5. 🚪 Leave Game")

        choice = input("\nChoose: ")

        if choice == "1":

            enemy = random.choice(
                enemies[:2]
            )

            battle(enemy)

            fights += 1

        elif choice == "2":

            enemy = random.choice(
                enemies
            )

            battle(enemy)

            fights += 1

        elif choice == "3":

            if fights < 5:

                print(
                    "\n❌ You need to win",
                    5 - fights,
                    "more battles!"
                )

                time.sleep(2)

            else:

                boss_fight()

                if player["hp"] <= 0:

                    break

        elif choice == "4":

            clear()

            show_status()

            input("\nPress ENTER...")

        elif choice == "5":

            break

        else:

            print("Invalid choice!")

            time.sleep(1)

    if player["hp"] <= 0:

        clear()

        print("================================")
        print("          💀 YOU DIED")
        print("================================")

        print("\nFinal Level:", player["level"])
        print("Final Gold:", player["gold"])

        input("\nPress ENTER...")


# =========================
# START
# =========================

main_menu()