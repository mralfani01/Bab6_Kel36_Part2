from databuku import databuku
import module1
import module4
import module6
objek1 = module1
objek1a = module4
objek2 = module6

class menu1a:
    def menu5aa():
        koleksibuku = []
        
        novel1 = databuku("Assalamualaikum Beijing" , "978-602-9055-25-2" , 2014 , "Asma Nadia", 360)
        koleksibuku.append(novel1)

        astro1 = databuku("WHY? The Universe - Alam Semesta" , "978-979-27-4541-2" , 2009 , "Lee, Kwang Woong" , 160)
        koleksibuku.append(astro1)

        print("\n1. Assalamu'alaikum Beijing")
        print("2. WHY? The Universe - Alam Semesta")
            
        print("\nApa yang ingin anda lakukan selanjutnya?")
        print("1. Lihat Data Buku")
        print("2. Pembayaran")
        print("3. Keluar")
        menu1aaa = input("Masukkan pilihan anda : ")

        if menu1aaa == "1":
            indeksstr = input("\nMasukkan indeks buku : ")
            if indeksstr == "1" or indeksstr == "2" :
                indeksawal = int(indeksstr)
                if 1 <= indeksawal <= 2:
                    indeks = indeksawal - 1
                    lihatdata = koleksibuku[indeks]
                    print('Judul\t\t: ', lihatdata.judul)
                    print('ISBN\t\t: ',  lihatdata.ISBN)
                    print('Tahun terbit\t: ', lihatdata.tahunterbit)
                    print('Penulis\t\t: ', lihatdata.penulis)
                    print('Jumlah halaman\t: ', lihatdata.jumlahhalaman)
                    objek1a.menu4a.menu4aa()           
            else :
                print ("Indeks yang anda masukkan salah.") 
                objek1a.menu4a.menu4ac()
        elif menu1aaa == "2":
            objek2.tanggal6aa.tanggal6aa()
        elif menu1aaa == "3":
            exit()
        else:
            print ("Pilihan yang anda masukkan salah")
            objek1a.menu4a.menu4ac()
