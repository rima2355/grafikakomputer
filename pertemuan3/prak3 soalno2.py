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
