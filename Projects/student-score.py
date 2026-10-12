Totalmurid = int(input("total murid berapa"))
i =  1
TotalNilai = []
total = 0


totallulus = 0
totaltidaklulus = 0

semuanama = []
namalulus = []
namatidaklulus = []

while i <= int(Totalmurid):
   nama = input("namanya siapa ")
   semuanama.append(nama)
   
   
   nilai = int(input("Nilainya berapa"))
   TotalNilai.append(nilai)
   total = total + nilai


   if nilai >= 70:
      totallulus = totallulus + 1
      namalulus.append(nama)
      
   else:
    
      totaltidaklulus = totaltidaklulus + 1
      namatidaklulus.append(nama)
      
   i+= 1
   

print("Yang Lulus",totallulus)
print("")

print("Yang Tidak Lulus",totaltidaklulus)
print("")

print("Nama yang Lulus",namalulus)
print("")

print("Nama yang Tidak Lulus",namatidaklulus)
print("")

rata_rata = total / Totalmurid

print("rata rata dari nilai seluruh murid =",rata_rata)

print("Nama: Nilai")

print(semuanama[0]," = ",(TotalNilai[0]))
print(semuanama[1]," = ",(TotalNilai[1]))
print(semuanama[2]," = ",(TotalNilai[2]))










