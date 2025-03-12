# Definisi angka awal
harga_barang1 = 5000   # Harga barang pertama
harga_barang2 = 2000   # Harga barang kedua
potongan_diskon = 200  # Diskon atau pengurangan harga

# Menambahkan bonus atau kenaikan harga sebesar 500 pada barang pertama dan kedua
harga_barang1 += 500   # Harga barang pertama naik 500
harga_barang2 += 500   # Harga barang kedua naik 500

# Menghitung total setelah penyesuaian harga
total_harga = (harga_barang1 + harga_barang2) - potongan_diskon

# Menampilkan hasil perhitungan dengan format yang rapi
print(f"Harga barang pertama setelah kenaikan : {harga_barang1}")
print(f"Harga barang kedua setelah kenaikan  : {harga_barang2}")
print(f"Potongan diskon                      : {potongan_diskon}")
print(f"Total harga akhir                    : ({harga_barang1} + {harga_barang2}) - {potongan_diskon} = {total_harga}")
