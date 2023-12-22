nama = input('Masukkan Nama Karyawan:')
pendapatan = int(input('Masukkan pendapatan Karyawan:'))
print('Nama Karyawan:', nama)
print('Pendapatan:',pendapatan)
if pendapatan > 1000:
     print('Status: Berhak')
else:
     print('Status: Tidak Berhak')