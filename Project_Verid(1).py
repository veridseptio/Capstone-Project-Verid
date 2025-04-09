# Data dummy: list of dicts (collection)
gudang = [
    {
        "kode_barang": "PRF001",  # kolom unik
        "nama_barang": "Parfum SYNX Alpha",
        "kategori": "Parfum",
        "stok": 100,
        "lokasi": "Rak A1"
    },
    {
        "kode_barang": "PRF002",
        "nama_barang": "Parfum SYNX Noir",
        "kategori": "Parfum",
        "stok": 80,
        "lokasi": "Rak A2"
    }
]

# Menampilkan seluruh data
def tampilkan_data():
    while True:
        print("\n=== Tampilkan Data Gudang ===")
        print("1. Tampilkan Data Lengkap")
        print("2. Tampilkan Data Spesifik")
        print("0. Menu Sebelumnya")
        pilihan = input("Pilih menu (0-2): ")

        if pilihan == "1":
            print("\n=== Data Gudang Lengkap ===")
            if not gudang:
                print("Data kosong.")
            else:
                for barang in gudang:
                    print(f"{barang['kode_barang']} | {barang['nama_barang']} | {barang['kategori']} | {barang['stok']} | {barang['lokasi']}")
        elif pilihan == "2":
            kode = input("Masukkan kode barang yang ingin ditampilkan: ")
            ditemukan = False
            for barang in gudang:
                if barang['kode_barang'] == kode:
                    print(f"\nData Barang Spesifik: {barang}")
                    ditemukan = True
                    break
            if not ditemukan:
                print("Kode barang tidak ditemukan.")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")

# Menambahkan data baru
def tambah_data():
    print("\n=== Tambah Data Barang ===")
    kode = input("Masukkan kode barang (unik): ")

    # Cek apakah kode_barang sudah ada
    if any(barang['kode_barang'] == kode for barang in gudang):
        print("Kode barang sudah ada!")
        return

    nama = input("Masukkan nama barang: ")
    kategori = input("Masukkan kategori: ")

    try:
        stok = int(input("Masukkan jumlah stok: "))
    except ValueError:
        print("Stok harus berupa angka.")
        return

    lokasi = input("Masukkan lokasi penyimpanan: ")

    # Tambah ke list gudang
    gudang.append({
        "kode_barang": kode,
        "nama_barang": nama,
        "kategori": kategori,
        "stok": stok,
        "lokasi": lokasi
    })

    print("Data berhasil ditambahkan.")
# Mengupdate data berdasarkan kode_barang
def update_data():
    kode = input("Masukkan kode barang yang akan diupdate: ")
    for barang in gudang:
        if barang['kode_barang'] == kode:
            print(f"Data saat ini: {barang}")
            barang['nama_barang'] = input("Nama barang baru: ")
            barang['kategori'] = input("Kategori baru: ")
            try:
                barang['stok'] = int(input("Stok baru: "))
            except ValueError:
                print("Stok harus berupa angka. Update dibatalkan.")
                return
            barang['lokasi'] = input("Lokasi baru: ")
            print("Data berhasil diupdate.")
            return
    print("Data tidak ditemukan.")

# Menghapus data
def hapus_data():
    kode = input("Masukkan kode barang yang akan dihapus: ")
    for barang in gudang:
        if barang['kode_barang'] == kode:
            gudang.remove(barang)
            print("Data berhasil dihapus.")
            return
    print("Data tidak ditemukan.")

# Menu utama
def menu():
    while True:
        print("=== Selamat datang di Menu Gudang ===")
        print("1. Tampilkan Data")
        print("2. Tambah Data")
        print("3. Update Data")
        print("4. Hapus Data")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            update_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan menu
menu()
