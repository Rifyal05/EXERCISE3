Nama_karyawan = ''
input_nama = input('Masukan nama karyawan : ')
Nama_karyawan = str(input_nama)
print('Nama Karyawan : ', Nama_karyawan)

Jam_kerja = ''
input_jam = input('Masukan total Jam Kerja dalam sehari : ')
Jam_kerja= int(input_jam)
print('Jam Kerja Dalam Sehari : ', Jam_kerja,'jam')

Tarif_perjam = 0
Input_tarif = input('Masukan Tarif Perjamnya : ')
Tarif_perjam = int(Input_tarif)
print('Tarif perjam adalah :', Tarif_perjam)

Hitung_gaji= Jam_kerja * 20
Gaji_perbulan = Hitung_gaji * Tarif_perjam
Gaji_perbulan = "{:,.2f}".format(Gaji_perbulan)
print('Total jam kerja dalam sebulan adalah : ', Hitung_gaji, 'Jam')
print('Gaji perbulan adalah (Per-20 hari kerja) : ', Gaji_perbulan)



while True:
    Informasi_lengkap = input('Apakah anda ingin melihat informasi lengkapnya? : (Ya/Tidak)')
    Informasi_lengkap = Informasi_lengkap.capitalize()
    if Informasi_lengkap == 'Ya':
            print('Berikut adalah informasi lengkapnya : ' )
            print('Nama karyawa : ', Nama_karyawan)
            print('Jam Kerja Dalam Sehari : ', Jam_kerja , 'jam')
            print('Tarif perjam adalah :', Tarif_perjam)
            print('Total jam kerja dalam sebulan adalah : ', Hitung_gaji,'jam')
            print('Gaji perbulan adalah (Per-20 hari kerja) : ', Gaji_perbulan)
            break
    elif Informasi_lengkap == 'Tidak':
            print('Baiklah...')
            break
    else:
         print()
         print('Harap masukan input yang valid (Ya/Tidak)')
         print('anda harus memberikan input yang valid sebelum memulai  ulang termial')
        
