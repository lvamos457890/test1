import math

def calculate_square_area(side):
        area = side * side
        return area


def calculate_circle_area(radius):
        area = math.pi * radius**2
        return area


def calculate_triangle_area(alas,tinggi):
    area = 0.5 * alas * tinggi
    return area

def calculate_rectangle_area(panjang,lebar):
    area = panjang * lebar
    return area


def calculate_square_perimeter(side):
    area = 4 * side
    return area

def calculate_circle_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter


def calculate_triangle_perimeter(side1,side2,side3):
    perimeter = side1 + side2 + side3
    return perimeter


def calculate_rectangle_perimeter(panjang,lebar):
    perimeter = panjang + lebar
    return perimeter

square = 1
circle = 2
triangle = 3
rectangle = 4

print("Square(1)")
print("Circle(2)")
print("Triangle(3)")
print("Rectangle(4)")

print("")

tanya = int(input("Butuh yang mana?"))
if tanya == 1:
    bentuk = "square"
    tanya2 = input("Area(1) Atau Perimeter(2?").lower()
    angka1 = int(input("Masukkan Angkanya: "))
    if tanya2 == "area" or tanya2 == "1":
        hasil = calculate_square_area(angka1)      

    if tanya2 == "perimeter" or tanya2 == "2":
        hasil = calculate_square_perimeter(angka1)

    

if tanya == 2:
    bentuk = "circle"
    tanya2 = input("Area(1) Atau Perimeter(2?").lower()
    angka1 = int(input("Masukkan Angkanya: "))
    if tanya2 == "area" or tanya2 == "1":
        hasil = calculate_circle_area(angka1)
                    
    if tanya2 == "perimeter" or tanya2 == "2":
        hasil = calculate_circle_perimeter(angka1)


if tanya == 3:
    bentuk = "triangle"
    tanya2 = input("Area(1) Atau Perimeter(2?").lower()
    if tanya2 == "area" or tanya2 == "1":
        
        angka1 = int(input("Masukkan Alas: "))
        angka2 = int(input("Masukan Tinggi: "))
        hasil = calculate_triangle_area(angka1,angka2)
        

    if tanya2 == "perimeter" or tanya2 == "2":
        angka1 = int(input("Masukan Sisi 1 "))
        angka2 = int(input("Masukan Sisi 2 "))
        angka3 = int(input("Masukan Sisi 3 "))
        hasil = calculate_triangle_perimeter(angka1,angka2,angka3)      


if tanya == 4:
    bentuk = "rectangle"
    tanya2 = input("Area(1) Atau Perimeter(2?").lower() 
    if tanya2 == "area" or tanya2 == "1":
        angka1 = int(input("Masukkan Panjang: "))
        angka2 = int(input("Masukkan Lebar: "))
        hasil = calculate_rectangle_area(angka1,angka2)

    if tanya2 == "perimeter" or tanya2 == "2":
        angka1 = int(input("Masukkan Panjang: "))
        angka2 = int(input("Masukkan Lebar: "))
        hasil = calculate_rectangle_perimeter(angka1,angka2)
        
if tanya2 == "1":
    hitung = "area"
if tanya2 == "2":
    hitung = "perimeter"

print("hasil", hitung, "dari",bentuk, "=" , hasil)