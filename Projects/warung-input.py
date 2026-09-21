Hari = int(input("Berapa hari: "))
listtotalomset = []
total = 0
i= 0
# x=0

while i < Hari:
    omset = int(input("Omsetnya berapa: "))
    listtotalomset.append(omset)
    total = total + listtotalomset[i]
    # x = x + 1
    i = i + 1

print("list omset:",listtotalomset ) 



print("total omset:", total)




pajak = total / 10

print("pajak:",pajak)


