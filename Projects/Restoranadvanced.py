

a = ["Selamat Datang Di Restoran B", "=============================", "Berikut merupakan menu kami"]

for i in range(len(a)):
    print(a[i])


# print("Selamat Datang Di Restoran B")
# print("=============================")
# print("Berikut merupakan menu kami")

makanan = ["nasi goreng", "nasi goreng special", "mie ayam"]
for i in range(len(makanan)): 
    print(makanan[i])

# print("1. Nasi Goreng")
# print("2. Nasi Goreng Special")
# print("3. Mie Ayam")

b = [ "=============================", "Sebutkan jumlah setiap makanan yang ingin di pesan" , "masukan angka 0 jika tidak ingin membeli makanan TSB" ]
for i in range(len(b)):
    print(b[i])

# print("=============================")
# print("Sebutkan jumlah setiap makanan yang ingin di pesan")
# print("masukan angka 0 jika tidak ingin membeli makanan TSB")

#int() untuk mengubah data menjadi integer(angka) 
#input untuk menerima data/jawaban dari pengguna
JumlahNasiGoreng = int(input("Nasi Goreng = "))
JumlahNasiGorengSpecial = int(input("Nasi Goreng Special = "))
JumlahMieAyam = int(input("Mie Ayam = "))

# Untuk menetapkan harga
# [0] HargaNasiGoreng = 50000
# [1] HargaNasiGorengSpecial = 10000
# [2] HargaMieAyam = 15000
HargaMakanan = [5000, 10000, 15000]

# menghitung total harga dari jumlah makanan yang di pesan
TotalNasiGoreng = JumlahNasiGoreng * HargaMakanan[0]
TotalNasiGorengSpecial = JumlahNasiGorengSpecial * HargaMakanan[1]
TotalMieAyam = JumlahMieAyam * HargaMakanan[2]


print("Total Nasi Goreng:",TotalNasiGoreng)
print("Total NasiGoreng Special",TotalNasiGorengSpecial)
print("Total Mie Ayam",TotalMieAyam)

# untuk menghitung total harga dari seluruh pesanan
TotalHarga = TotalNasiGoreng + TotalNasiGorengSpecial + TotalMieAyam
print("Before Discount:", TotalHarga)

# menghitung dan menambahkan discount dari total seluruh pesanan 
# < adalah untuk membandingkan apakah benar lebih kecil atau tidak
# > adalah untuk membandingkan apakah benar lebih besar atau tidak
# 20 >= 20 -> True
# 20 > 20 -> False
if TotalHarga >= 500000:
    # 0.2 desimal dari 20%
    Discount = TotalHarga * 0.2    
    TotalHarga = TotalHarga - Discount

elif TotalHarga >= 200000:
    Discount = TotalHarga * 0.1
    TotalHarga = TotalHarga - Discount

print("After Discount:",TotalHarga)
    
      
# untuk menghitung total harga dari seluruh pesanan dan ditambah tax
Tax = TotalHarga * 0.1
AfterTax = TotalHarga + Tax
print("After Tax:", AfterTax)








