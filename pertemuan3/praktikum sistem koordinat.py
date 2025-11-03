import math
# Input titik
x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))
x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

# Hitung jarak antar titik
jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Tentukan kuadran titik pertama
if x1 > 0 and y1 > 0:
    kuadran = "Kuadran I"
elif x1 < 0 and y1 > 0:
    kuadran = "Kuadran II"
elif x1 < 0 and y1 < 0:
    kuadran = "Kuadran III"
elif x1 > 0 and y1 < 0:
    kuadran = "Kuadran IV"
else:
    kuadran = "Berada di sumbu"

# Tampilkan hasil sesuai contoh
print("\n=== HASIL ===")
print(f"Titik pertama : ({x1}, {y1})")
print(f"Titik kedua   : ({x2}, {y2})")
print(f"Jarak antar titik: {jarak:.2f}")
print(f"Titik pertama berada di: {kuadran}")

# === SOAL 2 ===
print("\nSoal 2:")
print("Simulasikan sistem koordinat layar 10x5 piksel dan tampilkan titik (x=3, y=2) dengan simbol 'X'.\n")

# Ukuran layar
lebar = 10
tinggi = 5

# Titik yang akan ditampilkan
x = 3
y = 2

# Cetak koordinat
for baris in range(tinggi):
    for kolom in range(lebar):
        if kolom == x and baris == y:
            print("X", end=" ")
        else:
            print(".", end=" ")
    print()
