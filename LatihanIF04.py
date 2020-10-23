#kode program Python untuk menentukan gaji pokok dan gaji bersih dari seorang karyawan berdasarkan golongannya

kodeKaryawan = input('Masukkan kode karyawan   : ')
namaKaryawan = input('Masukkan nama karyawan  : ')
golongan = input('Masukkan golongan            : ')
print('')
gajiPokok = 0
potongan = 0

print(' ================================= ' + '\n')
print('       STRUK RINCIAN GAJI KARYAWAN' + '\n')
print(' --------------------------------- ' + '\n')

print('Nama Karyawan     : '  + namaKaryawan + ' (Kode: '+ kodeKaryawan + ')')
print('Golongan               : ' + golongan + '\n')
print(' --------------------------------- ' + '\n')

if(golongan == 'A') :
    gajiPokok = 10000000
    potongan = 2.5
    jumlahPotongan = 10000000 * potongan / 100
    gajiSetelahDipotong = 10000000 - jumlahPotongan
    

elif(golongan == 'B') :
    gajiPokok = 8500000
    potongan = 2.0
    jumlahPotongan = 8500000 * potongan / 100
    gajiSetelahDipotong = 8500000 - jumlahPotongan


elif(golongan == 'C') :
    gajiPokok = 7000000
    potongan = 1.5
    jumlahPotongan = 7000000 * potongan / 100
    gajiSetelahDipotong = 7000000 - jumlahPotongan


elif(golongan == 'D') :
    gajiPokok = 5500000
    potongan = 1.0
    jumlahPotongan = 5500000 * potongan / 100
    gajiSetelahDipotong = 5500000 - jumlahPotongan


print('Gaji Pokok             : Rp ' + str(gajiPokok))
print('Potongan ( ' + str(potongan) +' % )  : Rp ' + str(jumlahPotongan) + '\n')
print('+ ------------------------------- - +' + '\n')
print('Gaji Bersih           : Rp ' + str(gajiSetelahDipotong))
    
