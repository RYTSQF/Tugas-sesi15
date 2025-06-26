from data_loader import load_data, save_data
from katalog import tampilkan_semua_buku, cari_buku
from pinjam import pinjam_buku, kembalikan_buku
from visual import grafik_genre, grafik_status

data_file = 'data/daftar_buku.csv'
buku_list = load_data(data_file)

while True:
    print("\n===== SISTEM PERPUSTAKAAN MINI =====")
    print("1. Tampilkan semua buku")
    print("2. Cari buku")
    print("3. Pinjam buku")
    print("4. Kembalikan buku")
    print("5. Tampilkan grafik")
    print("0. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tampilkan_semua_buku(buku_list)
    elif pilihan == '2':
        keyword = input("Masukkan judul/genre/tahun: ")
        hasil = cari_buku(buku_list, keyword)
        tampilkan_semua_buku(hasil)
    elif pilihan == '3':
        kode = input("Masukkan kode buku: ")
        pinjam_buku(buku_list, kode)
    elif pilihan == '4':
        kode = input("Masukkan kode buku: ")
        kembalikan_buku(buku_list, kode)
    elif pilihan == '5':
        grafik_genre(buku_list)
        grafik_status(buku_list)
        print("Grafik disimpan dalam folder 'img'.")
    elif pilihan == '0':
        save_data(data_file, buku_list)
        break
    else:
        print("Menu tidak valid. Coba lagi.")