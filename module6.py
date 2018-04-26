import module6
objek6 = module6
class tanggal6aa(object):
    def tanggal6aa():
        print (" ")
        jml = int(input("Masukkan jumlah buku : "))
        print (" ")
        print ("Masukkan tanggal peminjaman : ")

        bulan = {1:'Januari' , 2:'Februari' , 3:'Maret' , 4:'April' , 5:'Mei' , 6:'Juni' , 7:'Juli' , 8:'Agustus' , 9:'September' , 10:'Oktober' , 11:'November' , 12:'Desember'}
    
        TP = int(input('Tanggal : '))
        BP = int(input('Bulan   : '))
        THP = int(input('Tahun  : '))
        
        print (" ")
        print ("Paket peminjaman")
        print ("1. 1 minggu")
        print ("2. 1 bulan")
        
        paket = input("Masukkan pilihan yang anda inginkan : ")

        if paket == "1" :
            biaya = jml*7*2000
            LP = "1 minggu"
            if TP < 24 :
                TK = TP + 7
                BK = BP
                THK = THP
            elif TP >= 24 :
                TK = TP + 7 - 30
                if BP < 12 :
                    BK = BP + 1
                    THK = THP
                elif BP == 12 :
                    BK = BP + 1 - 12
                    THK = THP + 1
                else :
                    print ("Data yang anda masukkan salah")
                    objek6.tanggal6aa.tanggal6aa()
            else :
                print ("Data yang anda masukkan salah")
                objek6.tanggal6aa.tanggal6aa()
        
        elif paket == "2" :
            biaya = jml*30*2000
            LP = "1 bulan"
            TK = TP
            if BP < 12 :
                BK = BP + 1
                THK = THP
            elif BP == 12 :
                BK = BP + 1 - 12
                THK = THP
            else :
                print ("Data yang anda masukkan salah")
                objek6.tanggal6aa.tanggal6aa()
        else :
            print ("Data yang anda masukkan salah")
            objek6.tanggal6aa.tanggal6aa()


                    
        print ('')
        print ('Anda melakukan peminjaman ' , jml , " buku dengan paket peminjaman " , LP , ' dan total biaya Rp ', biaya ,', kembali pada tanggal ', TK ,', bulan ' , bulan[BK], ', tahun ', THK , ".")
        print (" ")
        