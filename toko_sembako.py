import csv

# Node Linked List
class ProductNode:
    def __init__(self, product):
        self.product = product
        self.next = None

# Struktur Data & Fitur Utama
class SimpleStore:
    def __init__(self):
        self.products = {}
        self.head = None

    def tambah_produk(self, id, nama, harga, jumlah):
        if id in self.products:
            print("ID produk sudah ada.")
            return
        product = {"id": id, "nama": nama, "harga": harga, "jumlah": jumlah}
        self.products[id] = product
        node = ProductNode(product)

        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        print("Produk berhasil ditambahkan.")
        self.simpan_csv()

    def ubah_produk(self, id):
        if id not in self.products:
            print("Produk tidak ditemukan.")
            return
        print("Masukkan data baru (kosongkan jika tidak ingin diubah):")
        nama_baru = input("Nama baru: ")
        harga_baru = input("Harga baru: ")
        jumlah_baru = input("Jumlah baru: ")

        if nama_baru:
            self.products[id]["nama"] = nama_baru
        if harga_baru:
            self.products[id]["harga"] = int(harga_baru)
        if jumlah_baru:
            self.products[id]["jumlah"] = int(jumlah_baru)
        print("Produk berhasil diubah.")
        self.simpan_csv()

    def hapus_produk(self, id):
        if id not in self.products:
            print("Produk tidak ditemukan.")
            return
        del self.products[id]
        curr = self.head
        prev = None
        while curr:
            if curr.product["id"] == id:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                break
            prev = curr
            curr = curr.next
        print("Produk berhasil dihapus.")
        self.simpan_csv()

    def lihat_produk(self):
        if not self.products:
            print("Belum ada produk.")
            return
        print("\nDaftar Produk:")
        print("{:<10} {:<20} {:<10} {:<10}".format("ID", "Nama", "Harga", "Jumlah"))
        print("-" * 55)
        curr = self.head
        while curr:
            p = curr.product
            print("{:<10} {:<20} {:<10} {:<10}".format(p["id"], p["nama"], p["harga"], p["jumlah"]))
            curr = curr.next

    def simpan_csv(self, nama_file="toko_sembako.csv"):
        with open(nama_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama", "Harga", "Jumlah"])
            for p in self.products.values():
                writer.writerow([p["id"], p["nama"], p["harga"], p["jumlah"]])

    def impor_csv(self, nama_file="toko_sembako.csv"):
        try:
            with open(nama_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tambah_produk(
                        row["ID"],
                        row["Nama"],
                        int(row["Harga"]),
                        int(row["Jumlah"])
                    )
        except FileNotFoundError:
            pass  # File belum ada, tidak masalah

# Program Utama
def main():
    toko = SimpleStore()
    toko.impor_csv()

    while True:
        print("\n=== Menu Toko Sembako ===")
        print("1. Tambah Barang")
        print("2. Ubah Barang")
        print("3. Hapus Barang")
        print("4. Lihat Semua Barang")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            id = input("Masukkan ID Barang: ")
            nama = input("Masukkan Nama Barang: ")
            harga = int(input("Masukkan Harga Barang: "))
            jumlah = int(input("Masukkan Jumlah Barang: "))
            toko.tambah_produk(id, nama, harga, jumlah)

        elif pilihan == "2":
            id = input("Masukkan ID Barang yang Ingin Diubah: ")
            toko.ubah_produk(id)

        elif pilihan == "3":
            id = input("Masukkan ID Barang yang Ingin Dihapus: ")
            toko.hapus_produk(id)

        elif pilihan == "4":
            toko.lihat_produk()

        elif pilihan == "5":
            print("Terima kasih, program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
