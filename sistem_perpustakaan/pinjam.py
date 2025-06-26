def pinjam_buku(buku_list, kode):
    for buku in buku_list:
        if buku['kode'] == kode:
            if buku['status'] == 'Tersedia':
                buku['status'] = 'Dipinjam'
                print(f"Buku '{buku['judul']}' berhasil dipinjam.")
            else:
                print("Buku sedang dipinjam.")
            return
    print("Kode buku tidak ditemukan.")

def kembalikan_buku(buku_list, kode):
    for buku in buku_list:
        if buku['kode'] == kode:
            if buku['status'] == 'Dipinjam':
                buku['status'] = 'Tersedia'
                print(f"Buku '{buku['judul']}' berhasil dikembalikan.")
            else:
                print("Buku tidak sedang dipinjam.")
            return
    print("Kode buku tidak ditemukan.")