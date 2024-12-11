class Mahasiswa:
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"Nim: {self.nim}")
        print(f"Angkatan: {self.angkatan}")

if __name__ == "__main__":
    print("Masukkan Namamu:")
    nama = input()
    print("Masukkan NIM kamu:")
    nim = input()
    print("Masukkan Tahun Angkatan:")
    angkatan = input()

    mahasiswa = Mahasiswa(nama, nim, angkatan)

    print("\nBiodata Mahasiswa")
    mahasiswa.tampilkan_biodata()

    print("\nTotal Mahasiswa 1")
