# a. Buat list berisi tiga pasangan titik dan tampilkan dengan for
titik_list = [(0, 0), (50, 50), (100, 0)]

print("Daftar titik:")
for titik in titik_list:
    print(titik)
    
# b. Simpan satu titik dalam tuple bernama pusat dan tampilkan
pusat = (0, 0)

print("\nTitik pusat:")
print(pusat)

# c. Buat dictionary dan tampilkan dengan format teks
objek = {"x": 10, "y": 20, "warna": "biru"}

# Menggunakan f-string (f"...") untuk memformat teks
print("\nInfo Objek:")
print(f"Titik ({objek['x']},{objek['y']}) berwarna {objek['warna']}.")