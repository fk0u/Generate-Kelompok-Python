import random

def generate_kelompok_siswa(nama_siswa, jumlah_kelompok):
    if len(nama_siswa) != jumlah_kelompok * 6:
        print("Jumlah siswa harus 36 untuk membaginya menjadi 6 kelompok, dengan setiap kelompok berisi 6 siswa.")
        return

    # Mengacak urutan siswa
    random.shuffle(nama_siswa)

    kelompok_siswa = {}
    for i in range(jumlah_kelompok):
        kelompok_nama = f"Kelompok {i+1}"
        kelompok_siswa[kelompok_nama] = nama_siswa[i * 6: (i + 1) * 6]

    return kelompok_siswa

# Input nama siswa
nama_siswa = ["Adji Ramada Dharma", "Al-Ghani Desta Setyawan", "Andhika Galih Isya Putra", "Asnia Amelia", "Aurelyo Daffa Zaqwan", "Chalel Ferguson Lonnie Christa", "Diaz Daffa Aulia", "Diva Silvianna", "Ghatan Abie Rieko Kumoro", "Glenn Juan Aldaro", "Hilal Sulthanul Adzam", "Mohamad Baihaqi Ibrani", "Mozzel Boru Mangunsong", "Muhammad Abizar Reivanda", "Muhammad Aldiansyah", "Muhammad Farhan Maulana Hermansyah", "Muhammad Fauzan", "Muhammad Habibi Lhaksono", "Muhammad Ikhsan Putra Subandi", "Muhammad Luthfi Fabian", "Muhammad Navies Ramadhan", "Muhammad Rifqi Ramadhan", "Muhammad Zidan Pratama", "Muhammad Bregas Arifin Ilham", "Nabilah Cahya Soepardja", "Nayla Nashwa Ilfiana", "Nur Nizar Ahnaf", "Rafif Fathi Mohammad", "Rafik Anugrah Yana", "Reza Surya Hamdani", "Ridho Adi Azna", "Rifqi Ahmad Lawindra", "Tristan Richardo Pieterson Pondaag", "Wahyu Indra Al Hadi", "Weka Banodava", "Widhi Nur Maulida"]

# Jumlah kelompok
jumlah_kelompok = 6

# Membuat kelompok siswa
kelompok_siswa = generate_kelompok_siswa(nama_siswa, jumlah_kelompok)

if kelompok_siswa:
    # Menampilkan hasil
    print(f"Jumlah siswa: {len(nama_siswa)}")
    print(f"Jumlah kelompok: {jumlah_kelompok}")
    for kelompok, siswa in kelompok_siswa.items():
        print(f"{kelompok}: {', '.join(siswa)}")

# Tekan Enter untuk mengakhiri program
input("Tekan Enter untuk keluar...")