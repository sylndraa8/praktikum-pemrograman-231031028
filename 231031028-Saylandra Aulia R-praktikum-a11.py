def faktorial(nilai):
    if nilai <= 1:
        return 1
    else :
        return nilai*faktorial(nilai-1)
    
for i in range(11):
    print('%2d ! = %d' % (i,faktorial(i)))

print()

hasil = int(input ('Masukkan nilai faktorial ='))
hasil_faktorial = faktorial(hasil)
print(f'Nilai Faktorial dari {hasil}! = {hasil_faktorial}')
