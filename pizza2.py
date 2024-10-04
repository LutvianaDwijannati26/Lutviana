import os
hasil = os.system("cls")

# HEADER (JUDUL PROGRAM)
print("\n PIZZA HUT \n")
SALAMPEMBUKA = "Selamat Datang di Pizza HUT"
print("\n", SALAMPEMBUKA)
print("_" *90,"\n")

# DAFTAR MENU & HARGA
# 1. TOPING
print("""DAFTAR TOPPING \n
    1. frankfuter \t : Rp 50.000
    2. meatmonsta \t : Rp 35.000
    3. cheeselovers \t : Rp 20.000
      """)

# 2. CRUZT
print("""DAFTAR CRUZT \n
    1. cheesybites \t : Rp 30.000
    2. sosis \t\t : Rp 25.000
    3. panpizza \t : Rp 20.000
      """)

# 3. SIZE
print("""DAFTAR SIZE\n
    1. large \t\t : Rp 50.000
    2. medium \t\t : Rp 45.000
    3. small \t\t : Rp 30.000
      """)

# INPUT TOPING
PilihToping = str(input("Masukkan Pilihan Toping\t: "))

# PERCABANGAN IF-ELSE UNTUK PILIHAN TOPING YANG DIPILIH USER MELALUI INPUT
if PilihToping == "frankfuter":
    print("50.000")
    HargaToping = (int(50000))
elif PilihToping == "meatmonsta":
    print("35.000")
    HargaToping = (int(35000))
elif PilihToping == "cheeselovers":
    print("20.000")
    HargaToping = (int(20000))
else:
    "Topping yang anda pilih tidak tersedia"
    HargaToping = 0

# INPUT CRUZT
PilihCruzt = str(input("Masukkan Pilihan Cruzt\t: "))

# PERCABANGAN IF-ELSE UNTUK PILIHAN CRUZT YANG DIPILIH USER MELALUI INPUT
if PilihCruzt == "cheesybites":
    print("30.000")
    HargaCruzt = (int(30000))
elif PilihCruzt == "sosis":
    print("25.000")
    HargaCruzt = (int(25000))
elif PilihCruzt == "panpizza":
    print("20.000")
    HargaCruzt = (int(20000))
else:
    "Cruzt yang anda pilih tidak tersedia"
    HargaCruzt = 0

# INPUT SIZE
PilihSize = str(input("Masukkan Pilihan Size\t: "))

# PERCABANGAN IF-ELSE UNTUK PILIHAN SIZE YANG DIPILIH USER MELALUI INPUT
if PilihSize == "large":
    print("50.000")
    HargaSize = (int(50000))
elif PilihSize == "medium":
    print("45.000")
    HargaSize = (int(45000))
elif PilihSize == "small":
    print("30.000")
    HargaSize = (int(30000))
else:
    "Size yang anda pilih tidak tersedia" 
    HargaSize = 0

# INPUT TAMBAHAN KEJU
TambahanKeju = str(input("mau pakai keju? (yes/no) "))

# PERCABANGAN IF-ELSE UNTUK PILIHAN TAMBAHAN KEJU ATAU TIDAK
if TambahanKeju == "yes":
    print("+Keju 13.000")
    HargaTambahan = (int(13000))
else:
    HargaTambahan = int(0)

# TOTAL HARGA
print("_" *90,"\n")
print ("Thank you for choosing Pizzaa Hut Deliveries!")
HargaTotalPesananAnda = int((HargaToping + HargaCruzt + HargaSize + HargaTambahan))
print("Your Final bill is: Rp."+ str(HargaTotalPesananAnda))



