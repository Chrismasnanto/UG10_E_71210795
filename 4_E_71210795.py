print("Masukkan 3 bilangan yang ingin di masukkan")

x = int(input("Masukkan bilangan 1 : "))
y = int(input("Masukkan bilangan 2 : "))
z = int(input("Masukkan bilangan 3 : "))
print("Urutan bilangan dari yang terkecil adalah")
if x>y and x>z:
    if y>z:
        print(z, y, x)
    else:
        print(y, z, x)
elif y>x and y>z:
    if x>z:
        print(z, x, y)
    else:
        print(x, z, y)
else:
    if x>y:
        print(y, x, z)
    else:
        print(x, y, z)
 