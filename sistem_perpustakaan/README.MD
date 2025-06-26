# Sistem Perpustakaan Mini

Aplikasi katalog buku berbasis terminal yang dapat:
- Menampilkan daftar buku
- Mencari buku berdasarkan kata kunci
- Mencatat peminjaman dan pengembalian
- Menampilkan grafik genre dan status buku

## Cara Menjalankan
```bash
untuk menjalankan program sistem_perpustakaan, run main.py

1. jika ingin menampilkan semua buku dalam katalog ketik 1

2. jika ingin mencari buku secara filter ketik 2, lalu masukan keyword seperti Judul, Genre, atau Tahun (contoh : fiksi)

3. jika ingin meminjam buku ketik 3, lalu masukan keyword code buku yang ingin di pinjam (contoh : B001)

4. jika ingin mengembalikan buku yang sudah di pinjam ketik 4, lalu masukan keyword code buku yang sedang di pinjam yang ingin dikembalikan (contoh : B001)

5. jika ingin menampilkan grafik statistik buku yang ada seperti Genre, Tahun, dan Status Peminjaman ketik 5

6. jika ingin keluar dari program ketik 0

## Struktur Folder
```
sistem_perpustakaan/
├── main.py
├── katalog.py
├── pinjam.py
├── data_loader.py
├── visual.py
├── README.md
├── data/
│   └── daftar_buku.csv
└── img/
    ├── genre_bar.png
    └── status_pie.png
```

## Grafik
- `img/genre_bar.png`: Grafik jumlah buku per genre
- `img/status_pie.png`: Diagram lingkaran status buku
