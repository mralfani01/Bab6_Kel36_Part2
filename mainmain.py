from buku import buku

lanjut = True
bukuKe = []

prisoner = buku("21120116140068", "Perahu Kertas", 2009, ("Romance","Remaja"), "Dewi Lestari", 500)
bukuKe.append(prisoner) # ada di bab 5 :v

laskar = buku("21120116130086", "Laskar Pelangi", 2005, ("Adventure", "Study"), "Andrea Hirata", 700)
bukuKe.append(laskar)

while lanjut == True:
    print('\n--- Selamat Datang di Perpustakaan Kelompok 14 ---')
    print('1. Tambah Buku\n2. Cari Buku\n3. Baca Buku\n4. Cetak Buku\n5. Ganti Judul\n6. Keluar')
    pilih = int(input('Pilih operasi Anda : '))

    while(not(pilih >= 1 and pilih <= 6)): #jika inputnya bukan antara 1 dan 6
        print('Menu pilihan ', pilih, ' tidak ada dalam menu, silahkan pilih kembali')
        print('1. Tambah Buku\n2. Cari Buku\n3. Baca Buku\n4. Cetak Buku\n5. Ganti Judul\n6. Keluar')
        pilih = int(input('Pilih operasi Anda : '))

    if pilih == 1:
        print('\nIni adalah menu Tambah Buku')
        kodeBukuBaru = input('ISDN\t: ')
        judulBaru    = input('Judul\t: ')
        penulisBaru  = input('Penulis\t: ')
        tahunTerbit  = input('Tahun\t: ')
        cetakan      = input('Cetakan\t: ')
        genreBaru    = input('Genre\t: ')
        halaman      = input('Jumlah halaman\t: ')
        
        bukuBaru = buku(kodeBukuBaru, judulBaru, tahunTerbit, genreBaru, penulisBaru,halaman)
        bukuKe.append(bukuBaru)

    elif pilih == 2:
        print('\nIni adalah menu Cari Buku')
        noUrut = int(input('Pilih nomor buku : '))
        cariBuku = bukuKe[noUrut - 1]

        print('ISDN\t\t: ', cariBuku.ISDN)
        print('Judul\t\t: ', cariBuku.judul)
        print('Tahun terbit\t: ', cariBuku.tahunTerbit)
        print('Cetakan\t\t: ', cariBuku.cetakan)
        print('Genre\t\t: ', cariBuku.genre)
        print('Penulis\t\t: ', cariBuku.penulis)
        print('Jumlah halaman\t: ', cariBuku.jumlahHalaman)
        print('Jumlah peredaran: ', cariBuku.cekPeredaran())

    elif pilih == 3:
        print('\nIni adalah menu Baca Buku')
        noUrut = int(input('Pilih nomor buku : '))
        bacaBuku = bukuKe[noUrut - 1]
        bacaBuku.baca()

    elif pilih == 4:
        print('\nIni adalah menu Cetak Buku')
        noUrut = int(input('Pilih nomor buku\t: '))
        cetakan= int(input('Jumlah cetakan\t: '))
        cetakBuku = bukuKe[noUrut - 1]
        cetakBuku.cetak(cetakan)

    elif pilih == 5:
        print('\nIni adalah menu Ganti Judul')
        noUrut   = int(input('Pilih nomor buku\t: '))
        bukuJudulBaru = bukuKe[noUrut - 1]
        
        judulBaru = input('Judul baru : ')
        bukuJudulBaru.gantiJudul(judulBaru)

    elif pilih == 6:
        lanjut = False

    pilihLanjut = input('\nIngin lagi? y/n : ')

    if pilihLanjut == 'y':
        lanjut = True
    else :
        lanjut = False
