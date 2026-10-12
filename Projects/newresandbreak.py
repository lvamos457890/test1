Makanan = ["nasi goreng", "mie ayam ", "soto "]
print(Makanan)
Harga = [1000, 2000 ,3000]
print(Harga)
pesananmakanan = []

Total = []

i = 0

def restoran(a):
    print(Harga[a])
    pesananmakanan.append(Makanan[a])
    Total.append(Harga[a])
    

while True:
    pesanan = int(input("mau pesan apa"))
    print(pesanan)
    pesanan = pesanan - 1
    print(pesanan)
    if pesanan == 1:
        restoran(pesanan)

    if pesanan == 2:

        restoran(pesanan)
            
    if pesanan == 3:
    
        restoran(pesanan)

    stop = input("apakah ingin memesan lagi? Y/N").lower()
    if stop == "n":
        break


totalakhir = 0
while i < (len(Total)):
    totalakhir = totalakhir + Total[i]
    i += 1

    
print(pesananmakanan)
print(totalakhir)

          
    

    