# Mengambil input dari pengguna
n = int(input("Masukkan nilai n: "))

print("Bilangan ganjil hingga", n, "adalah:")

# Loop untuk mencetak bilangan ganjil hingga n
for i in range(1, n+1):
    if i % 2 != 0:  # Jika i bukan kelipatan 2, maka i adalah bilangan ganjil
        print(i, end=' ')  # Cetak bilangan ganjil tanpa pindah baris

print()  # Pindah ke baris baru setelah selesai mencetak
