## aritmatika
<img width="845" height="498" alt="image" src="https://github.com/user-attachments/assets/145ce1cb-eb88-4578-bfa7-9e3793acf2e1" />
   
    x1, y1 = 20,30
    x2, y2 = 30,50
    dx = x2 - x1
    dy = y2 - y1

    print ("seisih koordinat:",dx,dy)

       ##Program ini menghitung selisih (perbedaan) antara dua titik koordinat:

      Titik pertama: (20, 30)  
      Titik kedua: (30, 50)
      Selisihnya adalah:
      dx = 10 
      dy = 20
      Sehingga output menunjukkan perubahan posisi dari titik pertama ke titik kedua, yaitu bergeser 10 satuan ke kanan (sumbu X) dan 20 satuan ke atas (sumbu Y).

## fungsi
<img width="1107" height="520" alt="image" src="https://github.com/user-attachments/assets/f6d57b0d-18f7-4436-bab0-0798a634ca22" />

    def name (nama):
    print("hai,", nama, "selamat bergabung di ilkom!")
    
    name("cece")
    name("budi")

    ## penjelasan kode:
    def digunakan untuk membuat fungsi.

    Fungsi name() menerima satu parameter yaitu nama.
      Setiap kali fungsi dipanggil, ia menampilkan pesan sambutan dengan nama yang berbeda.
      Jadi, fungsi ini berguna untuk mengulang pesan sapaan dengan mudah tanpa menulis print berkali-kali.
   
    
## intput output

<img width="943" height="477" alt="image" src="https://github.com/user-attachments/assets/cf78cd53-1eae-4d3f-8393-da1f352fcfe3" />

    sisi= int(input("masukkan panjang sisi: "))
    warna = input ("masukkan warna:" )

    print(f"persegi dengan sisi {sisi} berwarna {warna}")

##penjelasan kode
Program ini:
Meminta pengguna memasukkan panjang sisi (angka),
Meminta warna persegi (teks),
Lalu menampilkan kalimat yang menjelaskan sisi dan warna persegi yang dimasukkan.
 
## kondisi
  <img width="878" height="450" alt="image" src="https://github.com/user-attachments/assets/26f95ea6-b8ab-4b26-9f5a-80c5381996ca" />

        x= 50
        if x > 0:
        print("titik berada di sisi kanan sumbu Y")
    else:
    print("titik berada di sisi kiri sumbu Y")

penjellsan kode:
   else:
   Artinya: jika kondisi sebelumnya (x > 0) salah (False), maka jalankan perintah di bagian ini.
   print("titik berada di sisi kiri sumbu Y")
   Perintah ini hanya akan dijalankan kalau x ≤ 0
   Kode ini digunakan untuk menentukan posisi titik terhadap sumbu Y:
Jika x > 0 → titik di kanan sumbu Y
Jika x ≤ 0 → titik di kiri sumbu Y
## perulangan
 
 <img width="712" height="680" alt="image" src="https://github.com/user-attachments/assets/0d2ee910-a95d-4979-87a9-61511400c9c6" />


    for i in range(10):
    print("titik ke-", i)

penjelasan program:
or i in range(10):
Ini adalah perulangan for.
Fungsi range(10) akan menghasilkan deretan angka mulai dari 0 sampai 9 (ingat: angka terakhir tidak ikut).
Jadi, nilai i akan berubah setiap kali perulangan berjalan:
Kode ini menampilkan tulisan "titik ke-" sebanyak 10 kali, dimulai dari 0 sampai 9.
Ini berguna kalau kamu ingin menampilkan urutan, misalnya nomor titik, daftar data, atau menghitung jumlah pengulangan.

## soal no 1
 
 <img width="985" height="447" alt="image" src="https://github.com/user-attachments/assets/c6eda38d-1a54-4e42-accb-0a31cd662794" />

     x=50
    y=100
    warna="merah"
    print(f"koordinat titik ({x},{y})dengan warna {warna}.")

penjelasan kode:
Kode ini menampilkan informasi tentang sebuah titik di bidang koordinat:
Titik berada di posisi (50, 100)
Warnanya merah
-Variabel (x, y, warna)
-Tipe data (angka dan string)

## soal no 2
  <img width="962" height="526" alt="image" src="https://github.com/user-attachments/assets/7746cc86-4664-4e0f-b756-c2445692d3f4" />

    x=int(input("masukkan nilai x: "))
    y=int(input("masukkan nilai y: "))
    warna = input("masukkan warna titik: ")

    print(f"titik berada di ({x},{y}) dan berwarna {warna}.")

penjelasan kode:
Kode tersebut meminta pengguna memasukkan nilai untuk variabel x dan y dalam bentuk angka, serta warna dalam bentuk teks, lalu menampilkan hasilnya dalam kalimat "Titik berada di (x,y) dan berwarna warna" menggunakan print() dan f-string.


## soal no 3
  <img width="722" height="682" alt="image" src="https://github.com/user-attachments/assets/10d84fa6-a36c-49d2-a511-53c24f0fbf17" />

    x = int(input("masukkan nilai x: "))

    if x > 0:
      print("titik di kanan layar.")
    elif x < 0:
      print("titik di kiri layar.")
    else:
      print("titik di tengah.")

    print("menampilkan 5 titik:")
    for i in range (1,6):
      print(f"titik ke-{i}")

 penjelasan kode:
 Kode tersebut meminta pengguna memasukkan nilai untuk variabel x, lalu memeriksa posisinya dengan if, elif, dan else. Jika x > 0, program menampilkan "Titik di Kanan layar"; jika x == 0, menampilkan "Titik di Tengah"; dan jika x < 0, menampilkan "Titik di Kiri Layar". Setelah itu, program menampilkan judul "Perulangan 1-5", lalu menggunakan perulangan for dengan range(1,6) untuk mencetak teks "Titik ke-1" hingga "Titik ke-5" secara berurutan. 
      

## soal no 4
  <img width="937" height="538" alt="image" src="https://github.com/user-attachments/assets/2fd886a1-4001-4f40-94d3-3979fe872393" />

    import math

    def hitung_jarak (x1, y1, x2, y2):
      jarak = math.sqrt((x2-x1)**2+ (y2-y1)**2)
      return jarak

    hasil = hitung_jarak(0,0,3,4)
    print(f"jarak antara dua titik: {hasil}")

penjelasan program:
Kode tersebut menggunakan modul math untuk menghitung jarak antara dua titik pada bidang koordinat. Fungsi hitung_jarak(x1, y1, x2, y2) menerima empat parameter, yaitu koordinat titik pertama (x1, y1) dan titik kedua (x2, y2). Di dalam fungsi, rumus **math.sqrt((x2 - x1)**2 + (y2 - y1)2) digunakan untuk menghitung jarak antara kedua titik menggunakan rumus jarak Euclidean. Nilai hasil perhitungan tersebut kemudian dikembalikan dengan return jarak. Selanjutnya, fungsi dipanggil dengan nilai (0, 0, 3, 4), dan hasilnya disimpan dalam variabel hasil. Program kemudian menampilkan output “Jarak antara dua titik : 5.0”, karena jarak antara titik (0,0) dan (3,4) adalah 5 satuan
## soal no5

<img width="614" height="326" alt="image" src="https://github.com/user-attachments/assets/3d83aba0-494b-463e-8c73-1296c1bdb857" />

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

penjelasan program:
 Kode tersebut menunjukkan tiga cara berbeda untuk menyimpan dan menampilkan data titik pada Python:
   
  List: Variabel titik_list berisi beberapa titik sebagai tuple, yaitu (0,0), (50,50), (100,0). Program kemudian menggunakan for loop untuk menampilkan tiap titik satu per satu.
   Tuple: Variabel pusat menyimpan satu titik (0,0). Program menampilkan titik pusat ini dengan menuliskannya langsung.
   Dictionary: Variabel objek menyimpan informasi titik dalam bentuk pasangan kunci-nilai (x, y, warna). Program menampilkan titik ini dengan f-string, menghasilkan teks “Titik (10,20) berwarna biru.”



    





    




