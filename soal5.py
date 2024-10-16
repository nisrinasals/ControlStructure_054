# Mengambil input dari pengguna
n = int(input("Masukkan nilai n: "))

# Loop untuk mencetak pola
for i in range(1, n+1):  # Mulai loop dari 1 hingga n (termasuk n)
    print((str(i) + ' ') * i)  # Mencetak angka i sebanyak i kali dalam satu baris
#str(i) mengonversi angka i menjadi string, sehingga hasilnya berupa "1", "2", "3", dan seterusnya