class databuku(object):    
    judul = ""
    ISBN = ""
    tahunterbit = 0 
    penulis = ""
    jumlahhalaman = 0

    def __init__ (self, judul, ISBN, tahunterbit, penulis, jumlahhalaman):
        self.judul = judul
        self.ISBN = ISBN
        self.tahunterbit = tahunterbit
        self.penulis = penulis
        self.jumlahhalaman = jumlahhalaman
        pass

    def databuku(self):
        print("Judul Buku = " + self.judul)
        print("No. ISBN = " + self.ISBN)
        print("Tahun Penerbitan = " + self.tahunterbit)
        print("Penulis = " + self.penulis)
        print("Jumlah Halaman = " + self.jumlahhalaman)