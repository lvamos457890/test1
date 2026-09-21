print("Amos Calculator")
print("===============================================")
print("List Operator")
print("1. pertambahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")
print("===============================================")
angka1 = int(input("Masukkan angka 1 = "))
operator = input("ketik angka operator yang ingin digunakan (1-4): ")
angka2 = int(input("Masukkan angka 2 = "))

print("===============================================")
print("Hasil:")
if operator == "1":
    print(angka1 + angka2)
    
elif operator == "2":
    print(angka1 - angka2)

elif operator == "3":
    print(angka1 * angka2)

elif operator == "4":
    print(angka1 / angka2)

else: 
    print("Terjadi Kesalahan, Silakan Masukan Input Angka 1-4")
print("===============================================")


