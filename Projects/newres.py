Makanan = ["nasi goreng", "mie ayam ", "soto "]
print(Makanan)
Harga = [1000, 2000 ,3000]
print(Harga)
pesananmakanan = []

Total = 0

i = 0


while True:
    pesanan = int(input("mau pesan apa"))



    if pesanan == 1:

        print(Harga[0])
        print(Makanan[0])
        pesananmakanan.append(Makanan[0])
        Total = Total + Harga[0]

    if pesanan == 2:

        print(Harga[1])    
        print(Makanan[1])
        pesananmakanan.append(Makanan[1])
        Total = Total + Harga[1]
            
    if pesanan == 3:
    
        print(Harga[2])
        print(Makanan[2])
        pesananmakanan.append(Makanan[2])
        Total = Total + Harga[2]
        


    stop = input("apakah ingin memesan lagi? Y/N").lower()
    if stop == "n":
          break
print(pesananmakanan)
print(Total)

          
    

    