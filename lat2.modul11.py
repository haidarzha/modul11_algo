class DataObjek:
    def __init__(self):
        self.__nama = None
        self.__nilai = None

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_nilai(self):
        return self.__nilai

    def set_nilai(self, nilai):
        self.__nilai = nilai

def main():
    objek = DataObjek()

    while True:
        print("\n===== Program OOP =====")
        print("1. Mendeklarasikan Objek")
        print("2. Menampilkan Objek")
        print("3. Merubah Nilai Objek")
        print("4. Menghapus Objek")
        print("5. Keluar Dari Program")

        pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4/5): ")

        if pilihan == "1":
            nama = input("Masukkan Namamu: ")
            nilai = input("Masukkan Nilaimu: ")
            objek.set_nama(nama)
            objek.set_nilai(nilai)
            print("Data Berhasil Ditambahkan")

        elif pilihan == "2":
            nama = objek.get_nama()
            nilai = objek.get_nilai()
            if nama and nilai:
                print(f"Nama: {nama}")
                print(f"Nilai: {nilai}")
            else:
                print("Belum ada data yang ditambahkan.")

        elif pilihan == "3":
            print("Pilih data yang ingin diubah:")
            print("1. Ubah Nama")
            print("2. Ubah Nilai")
            sub_pilihan = input("Masukkan Pilihan (1/2): ")

            if sub_pilihan == "1":
                nama = input("Masukkan Nama Baru: ")
                objek.set_nama(nama)
                print("Nama Berhasil Diubah")

            elif sub_pilihan == "2":
                nilai = input("Masukkan Nilai Baru: ")
                objek.set_nilai(nilai)
                print("Nilai Berhasil Diubah")

            else:
                print("Pilihan tidak valid, silakan coba lagi.")

        elif pilihan == "4":
            konfirmasi = input("Yakin ingin menghapus data? (y/n): ")
            if konfirmasi.lower() == "y":
                objek.set_nama(None)
                objek.set_nilai(None)
                print("Data Berhasil Dihapus")
            else:
                print("Data Tidak Dihapus")

        elif pilihan == "5":
            print("Keluar dari program. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
