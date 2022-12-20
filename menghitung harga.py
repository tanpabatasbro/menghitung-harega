print('''menghitung harga diskon suatu produk
''')

while True:
    nama = input("Masukkan Nama Produk : ")
    harga = int(input("Masukkan Harga Produk : "))
    diskon = int(input("Masukkan Diskon (tanpa%): "))

    total = (diskon /100 * harga)

    print(f"nama produk : {nama}\nharga produk : {total}")
