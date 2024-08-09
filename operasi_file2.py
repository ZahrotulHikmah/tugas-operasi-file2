class Catatan:
    def baca_file(self,nama_file):
        try:
            with open(nama_file,"r") as baca:
                content = baca.read()
                print(content)
        except FileNotFoundError:
            print(f"File {nama_file} tidak ditemukan")

    def tulis_file(self,nama_file):
            content = input("\n")
            with open(nama_file,"w") as tulis:
                tulis.write(content)
                print(f"Teks sudah ditambahkan di {nama_file}")
        