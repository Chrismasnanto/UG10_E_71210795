print("Test case 1")

print("Menambahkan siswa baru")

daftar = input("Masukkan daftar siswa :").title().split(",")
print("Daftar siswa:",daftar)

tambah = input("Masukkan siswa yang igin ditambahkan : ").lower()
if tambah.title()in daftar:
    print("Siswa atas nama",tambah.upper(),"sudah berada dalam daftar siswa")
else:
    daftar.append(tambah.upper())
    print("Hasil penambahan pada daftar siswa :",daftar)

print("Test case 2")

print("Menambahkan siswa baru")

daftar = input("Masukkan daftar siswa :").title().split(",")
print("Daftar siswa:",daftar)

tambah = input("Masukkan siswa yang igin ditambahkan : ").lower()
if tambah.title()in daftar:
    print("Siswa atas nama",tambah.upper(),"sudah berada dalam daftar siswa")
else:
    daftar.append(tambah.upper())
    print("Hasil penambahan pada daftar siswa :",daftar)
