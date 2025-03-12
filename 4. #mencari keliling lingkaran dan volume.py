import math

def keliling_lingkaran(radius):
    return 2 * math.pi * radius

def volume_kubus(sisi):
    return sisi ** 3

# Menu untuk memilih perhitungan
print("Pilih perhitungan:")
print("1. Keliling Lingkaran")
print("2. Volume Kubus")

pilihan = input("Masukkan pilihan (1/2): ")

if pilihan == "1":
    r = float(input("Masukkan jari-jari lingkaran: "))
    hasil = keliling_lingkaran(r)
    print(f"Keliling lingkaran dengan jari-jari {r} adalah {hasil:.2f}")
elif pilihan == "2":
    s = float(input("Masukkan panjang sisi kubus: "))
    hasil = volume_kubus(s)
    print(f"Volume kubus dengan sisi {s} adalah {hasil:.2f}")
else:
    print("Pilihan tidak valid!")
