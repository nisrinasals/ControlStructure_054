# Mengambil input dari pengguna
n = int(input("Masukkan bilangan: "))  # Ubah input menjadi tipe integer

# Inisialisasi dua angka pertama dalam deret
a, b = 0, 1

print("Deret Fibonacci hingga", n, "adalah:")

# Menghitung dan mencetak deret Fibonacci
while a <= n:  # Selama a kurang atau sama dengan n
    print(a, end=' ')  # Cetak nilai a tanpa pindah baris
    a, b = b, a + b  # Update a dan b untuk mendapatkan angka berikutnya

print()  # Pindah ke baris baru setelah selesai mencetak


