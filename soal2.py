# Mengambil input dari pengguna
angka1 = input ("Masukkan angka pertama: ")
# Mengambil input dari pengguna
angka2 = input ("Masukkan angka kedua: ")
# Mengambil input dari pengguna
angka3 = input ("Masukkan angka ketiga: ")

# Memeriksa apakah angka pertama lebih besar atau sama dengan angka kedua dan ketiga
if angka1 >= angka2 and angka1 >= angka3:
    angkaBesar = angka1  # Jika benar, angka pertama adalah yang terbesar
# Memeriksa apakah angka kedua lebih besar atau sama dengan angka pertama dan ketiga
elif angka2 >= angka1 and angka2 >= angka3:
    angkaBesar = angka2  # Jika benar, angka kedua adalah yang terbesar
# Jika kedua kondisi di atas salah, berarti angka ketiga adalah yang terbesar
else:
    angkaBesar = angka3  # Angka ketiga adalah yang terbesar

# Mencetak angka terbesar
print("Angka terbesar adalah: ", angkaBesar)