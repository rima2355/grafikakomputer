aritmatika
<img width="845" height="498" alt="image" src="https://github.com/user-attachments/assets/145ce1cb-eb88-4578-bfa7-9e3793acf2e1" />
   
    x1, y1 = 20,30
    x2, y2 = 30,50
    dx = x2 - x1
    dy = y2 - y1

    print ("seisih koordinat:",dx,dy)

fungsi
<img width="1107" height="520" alt="image" src="https://github.com/user-attachments/assets/f6d57b0d-18f7-4436-bab0-0798a634ca22" />

    def name (nama):
    print("hai,", nama, "selamat bergabung di ilkom!")
    
    name("cece")
    name("budi")

intput output

<img width="943" height="477" alt="image" src="https://github.com/user-attachments/assets/cf78cd53-1eae-4d3f-8393-da1f352fcfe3" />

    sisi= int(input("masukkan panjang sisi: "))
    warna = input ("masukkan warna:" )

    print(f"persegi dengan sisi {sisi} berwarna {warna}")


 kondisi
  <img width="878" height="450" alt="image" src="https://github.com/user-attachments/assets/26f95ea6-b8ab-4b26-9f5a-80c5381996ca" />

        x= 50
        if x > 0:
        print("titik berada di sisi kanan sumbu Y")
    else:
    print("titik berada di sisi kiri sumbu Y")


 perulangan
 
 <img width="712" height="680" alt="image" src="https://github.com/user-attachments/assets/0d2ee910-a95d-4979-87a9-61511400c9c6" />


    for i in range(10):
    print("titik ke-", i)

 soal no 1
 
 <img width="985" height="447" alt="image" src="https://github.com/user-attachments/assets/c6eda38d-1a54-4e42-accb-0a31cd662794" />

     x=50
    y=100
    warna="merah"
    print(f"koordinat titik ({x},{y})dengan warna {warna}.")

  soal no 2
  <img width="962" height="526" alt="image" src="https://github.com/user-attachments/assets/7746cc86-4664-4e0f-b756-c2445692d3f4" />

    x=int(input("masukkan nilai x: "))
    y=int(input("masukkan nilai y: "))
    warna = input("masukkan warna titik: ")

    print(f"titik berada di ({x},{y}) dan berwarna {warna}.")


    soal no 3
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

   soal no 4
  <img width="937" height="538" alt="image" src="https://github.com/user-attachments/assets/2fd886a1-4001-4f40-94d3-3979fe872393" />

    import math

    def hitung_jarak (x1, y1, x2, y2):
      jarak = math.sqrt((x2-x1)**2+ (y2-y1)**2)
      return jarak

    hasil = hitung_jarak(0,0,3,4)
    print(f"jarak antara dua titik: {hasil}")


soal no5

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



    





    




