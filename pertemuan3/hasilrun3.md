koordinat titik

<img width="612" height="501" alt="image" src="https://github.com/user-attachments/assets/9ff8d1e2-5142-4ecd-9155-62102b79b36f" />


    for y in range(0,5):
    for x in range (0, 10):
        print(".", end="")
    print()

sistem koordinat

<img width="1450" height="668" alt="image" src="https://github.com/user-attachments/assets/6f24b9b3-7506-449a-9331-e3b235aeb0e7" />

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


soal no1

<img width="835" height="477" alt="image" src="https://github.com/user-attachments/assets/0933fe7d-5bbd-4eb3-a68d-2cbeba243cf6" />

     tinggi = 10
    lebar = 10
    grid = [['.' for _ in range(lebar)] for _ in range(tinggi)]

    # Menempatkan X di posisi (4,6)
    # Catatan: koordinat (x,y) dimana x=kolom, y=baris
     x_pos = 4
    y_pos = 6

    # Validasi posisi
    if 0 <= x_pos < lebar and 0 <= y_pos < tinggi:
    grid[y_pos][x_pos] = 'X'
    print(f"\nPiksel 'X' ditempatkan pada posisi ({x_pos}, {y_pos})\n")
    else:
    print(f"\nPosisi ({x_pos}, {y_pos}) di luar batas grid!\n")

    # Tampilkan grid dengan nomor koordinat
    print("  ", end="")
    for i in range(lebar):
    print(i, end=" ")
    print()

      for idx, baris in enumerate(grid):
    print(f"{idx} ", end="")
    print(' '.join(baris))


soal no2

<img width="847" height="360" alt="image" src="https://github.com/user-attachments/assets/5ab909f9-5a97-489a-a9a0-cf830aee8661" />


    # Titik awal dan akhir
    x0, y0 = 0, 0
    x1, y1 = 5, 3

    # Hitung perubahan
    dx = x1 - x0
    dy = y1 - y0
  
    # Tentukan jumlah langkah
    steps = max(abs(dx), abs(dy))

    # Hitung increment vektor tiap langkah
    x_inc = dx / steps
    y_inc = dy / steps

    # List untuk menyimpan titik hasil
    points = []

    x = x0
    y = y0
    for _ in range(steps + 1):
    points.append((round(x), round(y)))
    x += x_inc
    y += y_inc

    print("Titik-titik koordinat garis:")
    for p in points:
    print(p)




