inp = input('Masukkan suatu input: ')
if len(inp) != 3:
 print('Panjang string ', len(inp),'tidak sama dengan 3')
else:
 print('Panjang input sesuai yang diinginkan')

nilai = int(input('Masukkan nilai: '))
if nilai >= 90:
 print('Nilai huruf: A')
elif nilai > 75:
 print('Nilai huruf: B')
elif nilai > 55:
 print('Nilai huruf: C')
else:
 print('Nilai huruf: D')