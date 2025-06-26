import matplotlib.pyplot as plt
import seaborn as sns
import os

def grafik_genre(buku_list):
    genre_count = {}
    for buku in buku_list:
        genre = buku['genre']
        genre_count[genre] = genre_count.get(genre, 0) + 1

    plt.figure(figsize=(8,5))
    sns.barplot(x=list(genre_count.keys()), y=list(genre_count.values()))
    plt.title('Jumlah Buku per Genre')
    plt.ylabel('Jumlah')
    plt.xlabel('Genre')
    os.makedirs('img', exist_ok=True)
    plt.savefig('img/genre_bar.png')
    plt.show()   
    plt.close()
    

def grafik_status(buku_list):
    status_count = {'Tersedia': 0, 'Dipinjam': 0}
    for buku in buku_list:
        status_count[buku['status']] += 1

    plt.figure(figsize=(5,5))
    plt.pie(status_count.values(), labels=status_count.keys(), autopct='%1.1f%%')
    plt.title('Status Buku')
    os.makedirs('img', exist_ok=True)
    plt.savefig('img/status_pie.png')
    plt.show()
    plt.close()
