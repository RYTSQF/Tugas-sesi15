import csv

def load_data(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print("File data tidak ditemukan.")
        return []

def save_data(file_path, data):
    if not data:
        return
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


## File: katalog.py

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
