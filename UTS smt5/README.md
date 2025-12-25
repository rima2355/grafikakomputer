# mini scane (perubahan siang dan malam)
 Inisialisasi Library dan Pygame

    Pada bagian awal program, saya mengimpor beberapa library,
    seperti pygame untuk grafika, math untuk perhitungan matematika,
    random untuk efek acak, dan sys untuk penanganan error.
    Setelah itu, dilakukan inisialisasi Pygame
    untuk memastikan sistem grafika dapat berjalan dengan baik.

  Pengaturan Layar dan Konstanta

    Selanjutnya saya mendefinisikan ukuran layar,
    yaitu 800 kali 600 piksel,
    serta FPS untuk mengatur kecepatan animasi.
    Selain itu, saya juga mendefinisikan berbagai warna
    yang akan digunakan dalam scene.

 # Implementasi Algoritma Garis – DDA

    Bagian ini merupakan implementasi Algoritma DDA,
    yang menjadi poin utama dari soal.
    Fungsi draw_line_dda digunakan untuk menggambar garis
    antara dua titik dengan menghitung perubahan nilai x dan y secara bertahap,
    lalu menampilkan piksel satu per satu.
    Digunakan untuk:
    Sinar matahari, Sayap burung,Garis jendela rumah, Outline objek.

  # Implementasi Algoritma Lingkaran – Midpoint Circle

    Selanjutnya adalah Algoritma Midpoint Circle,
    yang saya gunakan untuk menggambar lingkaran secara simetris.
    Algoritma ini bekerja dengan memanfaatkan titik tengah
    dan simetri delapan arah untuk efisiensi.
     Digunakan untuk: Matahari,Bulan,Bintang,Riak air
    Lingkaran dibuat dari perhitungan piksel, bukan fungsi instan.

  # Algoritma Poligon
    Algoritma poligon digunakan untuk membentuk objek kompleks
    dengan menghubungkan beberapa titik menggunakan garis DDA.
    Poligon digunakan untuk membuat objek seperti:
    gunung, rumah, pohon, atap, dan kincir angin.

  # Transformasi Geometris 2D

    Pada program ini, saya juga menerapkan transformasi geometris 2D, yaitu:
    Translasi untuk pergerakan objek
    Rotasi untuk animasi berputar
    Skala untuk perubahan ukuran objek”
     Contoh:
    Matahari & bulan → translasi melingkar
    Sayap burung → rotasi
    Riak air → skala membesar
    Transformasi ini membuat animasi lebih hidup dan dinamis.

# Sistem Siklus Siang dan Malam
    Saya membuat sebuah kelas DayNightCycle
    untuk mengatur perubahan waktu, warna langit,
    posisi matahari dan bulan, serta tingkat kecerahan scene.
    Nilai waktu terus diperbarui sehingga
    terbentuk siklus siang dan malam secara otomatis.

# Game Loop (Main Loop)

    Seluruh program dijalankan di dalam game loop,
    yang berfungsi untuk:
        Menerima input pengguna
        Memperbarui posisi objek
        Menggambar ulang tampilan setiap frame
    Loop ini berjalan terus sampai aplikasi ditutup.

## CONTOH MENJALANKAN PROGRAM
    - Sebelum menjalankan program, pastikan Python sudah terinstal
      dan library Pygame sudah tersedia di komputer(Library Pygame digunakan sebagai media untuk menampilkan grafika 2D.)
    Menjalankan Program di Thonny
    “Program dijalankan menggunakan aplikasi Thonny.”
    Langkah-langkah:
    Buka aplikasi Thonny
    Buka file program Python (uts2d.py)
    Klik tombol Run atau tekan F5
    Objek-objek pada scene bergerak, berputar, dan berubah ukuran
    sesuai dengan transformasi geometris 2D yang diterapkan.
    Program akan berhenti saat jendela ditutup dan Pygame ditutup secara aman

# hasil run nya
   <img width="995" height="729" alt="image" src="https://github.com/user-attachments/assets/7cfdf2aa-58e3-4429-8826-997a42f5cf35" />
   <img width="990" height="746" alt="image" src="https://github.com/user-attachments/assets/81f89e5f-5f57-473e-9472-8e323d54744c" />





