def tampilkan_menu():
    print("\n---- MENU PILIHAN ----\n1. Tambah Item\n2. Hapus Item\n3. Hitung Total\n4. Keluar")

def tambah(barang):
    nama = input("Masukkan Nama Barang: ")
    harga = int(input("Masukkan Harga Barang: "))
    jumlah = int(input("Masukkan Jumlah Barang: "))
    barang.append({'Nama': nama, 'Harga': harga, 'Jumlah': jumlah})
    print(f"{nama} Berhasil ditambahkan!")

def hapus(daftar_barang):
    if not daftar_barang:
        print("Tidak ada barang yang dapat dihapus!")
        return
    print("Daftar barang yang tersedia:")
    for index, barang in enumerate(daftar_barang):
        print(f"{index + 1}. {barang['Nama']} (Harga: {barang['Harga']}, Jumlah: {barang['Jumlah']})")
    try:
        pilihan = int(input("Pilih barang yang ingin dihapus (nomor): ")) - 1
        if 0 <= pilihan < len(daftar_barang):
            barang_hapus = daftar_barang.pop(pilihan)
            print(f"{barang_hapus['Nama']} Berhasil dihapus!")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Masukkan nomor yang valid.")

def hitung_total(barang):
    if not barang:
        print("Tidak ada barang yang ditotal, Tambahkan Barang!")
        return
    total = 0
    for barang in barang:
        total += barang['Harga'] * barang['Jumlah']
    
    print(f"Total harga sebelum diskon: {total}")
    
    if total >= 100000:
        diskon = total * 0.1
        total_akhir = total - diskon
        print(f"Diskon 10%: {diskon}")
        print(f"Total setelah diskon: {total_akhir}")

def main():
    barang = []
    while True:
        tampilkan_menu()
        pilihan = input("1/2/3/4 = ")
        if pilihan.isdigit():
            pilihan = int(pilihan)
            if pilihan == 1:
                tambah(barang)
            elif pilihan == 2:
                if barang:
                    hapus(barang)
                else:
                    print("Masukkan pilihan yang valid")
            elif pilihan == 3:
                hitung_total(barang)
            elif pilihan == 4:
                print("Terima kasih !!")
                break
            else:
                print("Pilih antara 1-4")
        else:
            print("Masukkan pilihan yang valid")


main()

# perbaikan
# huruf kecil ==> kapital in hapus
# barang ==> daftar_barang
# line 54 ==> tambahi if & elif