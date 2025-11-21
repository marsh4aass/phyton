# ============================================
#        APLIKASI KASIR MINIMARKET
#        Dengan Error Handling
# ============================================

print("=== APLIKASI KASIR MINIMARKET ===")

daftar_barang = []


# --------------------------------------------
#            INPUT DATA BARANG
# --------------------------------------------
while True:
    print("\nMasukkan data barang:")
    nama = input("Nama barang (ketik 'stop' untuk selesai): ").strip()

    if nama == "":
        print("❌ Nama barang tidak boleh kosong!")
        continue

    if nama.lower() == "stop":
        break

    # Input harga dengan error handling
    while True:
        harga_input = input("Harga barang: ")
        try:
            harga = int(harga_input)
            if harga <= 0:
                print("❌ Harga harus lebih dari 0!")
                continue
            break
        except:
            print("❌ Input harga tidak valid! Masukkan angka yang benar.")

    # Input jumlah barang dengan error handling
    while True:
        jumlah_input = input("Jumlah barang: ")
        try:
            jumlah = int(jumlah_input)
            if jumlah <= 0:
                print("❌ Jumlah harus lebih dari 0!")
                continue
            break
        except:
            print("❌ Input jumlah tidak valid! Masukkan angka yang benar.")

    subtotal = harga * jumlah

    daftar_barang.append([nama, harga, jumlah, subtotal])


# --------------------------------------------
#          VALIDASI BARANG KOSONG
# --------------------------------------------
if len(daftar_barang) == 0:
    print("\n❌ Tidak ada barang yang dimasukkan. Program dihentikan.")
    exit()


# --------------------------------------------
#                CETAK STRUK
# --------------------------------------------
print("\n===================================")
print("              STRUK BELANJA        ")
print("===================================\n")

total = 0

for barang in daftar_barang:
    nama, harga, jumlah, subtotal = barang
    print(f"{nama:<15} {harga} x {jumlah} = {subtotal}")
    total += subtotal

print("\n-----------------------------------")
print(f"Total Belanja : {total}")
print("-----------------------------------")


# --------------------------------------------
#   INPUT PEMBAYARAN + ERROR HANDLING
# --------------------------------------------
while True:
    bayar_input = input("Uang yang dibayarkan: ")
    try:
        bayar = int(bayar_input)
        if bayar < total:
            print(f"❌ Uang tidak cukup! Total belanja {total}")
            continue
        break
    except:
        print("❌ Input tidak valid! Masukkan angka.")


kembalian = bayar - total
print(f"Kembalian      : {kembalian}")

print("\n=== Terima kasih telah berbelanja! ===")
