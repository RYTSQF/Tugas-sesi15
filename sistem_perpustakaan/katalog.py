def tampilkan_semua_buku(buku_list):
    for buku in buku_list:
        print(f"{buku['kode']} | {buku['judul']} - {buku['pengarang']} ({buku['tahun']}) | {buku['genre']} | Status: {buku['status']}")

def cari_buku(buku_list, keyword):
    hasil = []
    keyword = keyword.lower()
    for buku in buku_list:
        if (keyword in buku['judul'].lower() or
            keyword in buku['genre'].lower() or
            keyword in buku['tahun'].lower()):
            hasil.append(buku)
    return hasil
