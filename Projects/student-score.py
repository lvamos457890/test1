Totalmurid = int(input("total murid berapa"))
i =  1
TotalNilai = []
total = 0
while i <= int(Totalmurid):

   nilai = int(input("Nilainya berapa"))
   print(nilai)
   TotalNilai.append(nilai)
   print(TotalNilai)
   total = total + nilai
   print(total)
   i+= 1
   print(i)

rata_rata = total / Totalmurid

print(rata_rata)







