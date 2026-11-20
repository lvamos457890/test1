def greetings(nama, umur):
    hasil = "hello", nama, "saya tebak umur anda", umur
    return hasil

def sum():
    x = 100
    y = 50
    total = x+y  #local variable
    print(total)
    return total


a = greetings("sam", 12)

print(a)
 
total = 100  #global variable
print(total)
total = sum()# local dipindahkan menjadi global
print(total)

