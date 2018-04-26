import module1
import module6
import module4
objekmenu = module1
objek4b = module4
objek8a = module6
class menu4a:
    def menu4ac():
        print("\nApa yang ingin anda lakukan selanjutnya?")
        print("1. Lihat Daftar Buku")
        print("2. Keluar")
        menu4ac = input("Masukkan pilihan yang anda inginkan : ")

        if menu4ac == "1":
            objekmenu.menu1a.menu5aa()
        elif menu4ac == "2":
            exit()
        else:
            print ("Pilihan yang anda masukkan salah")
            objek4b.menu4a.menu4ac()

    def menu4aa():
        print ("\nApa yang ingin anda lakukan selanjutnya?")
        print("1. Lihat buku lainnya")
        print("2. Pembayaran")
        print("3. Keluar")
        menu4aa = input("Masukkan pilihan yang anda inginkan : ")

        if menu4aa == "1":
            objekmenu.menu1a.menu5aa()
        elif menu4aa == "2":
            objek4b.menu4a.for8aa()
        elif menu4aa == "3":
            exit()
        else:
            print ("Pilihan yang anda masukkan salah")
            objek4b.menu4a.menu4aa()

    def for8aa():
        buku = [" ", "Assalamu'alaikum Beijing" , "WHY? The Universe - Alam Semesta"]
        for i in range (1,3):
            print (" ")
            kode = int(input("Masukkan kode buku (jika tidak ada isikan 0) : "))
            print(buku[kode])

        objek8a.tanggal6aa.tanggal6aa()