print('praktikum-a2\n')

print('NAMA    : SAYLANDRA AULIA RAMADHANI')
print('NIM     : 231031028')
print('Prodi   : Sistem Informasi A\n')

# INI OPERATOR ASSIGNMENT
a=19
print('Nilai a adalah',a)
a+=3
print('Nilai a a+=3 adalah',a)

a=19
print('Nilai a adalah',a)
a-=3
print('Nilai a a-=3 adalah',a)

a=19
print('Nilai a adalah',a)
a*=2
print('Nilai a a*=2 adalah',a)

a=19
print('Nilai a adalah',a)
a/=2
print('Nilai a a/=2 adalah',a)

a=3
print('Nilai a adalah',a)
a**=2
print('Nilai a a**=2 adalah',a)

a=19
print('Nilai a adalah',a)
a%=4
print('Nilai a a%=4 adalah',a)

a=35
print('Nilai a adalah',a)
a%=32
print('Nilai a a%=32 adalah',a)

a=35
print('Nilai a adalah',a)
a//=32
print('Nilai a a//=32 adalah',a)


# Tugas melanjutkan untuk operator selanjutnya line 25-line 59
#OR
b=True
print('\n--------Nilai b =',b)
b|=False
print('Nilai b|=False akan menjadi',b)
b=False
print('Nilai b=',b)
b|=False
print('Nilai b|=False akan menjadi',b)

#AND
b=True
print('\n--------Nilai b=',b)
b&=False
print('Nilai b&=False akan menjadi',b)
b=False
print('Nilai b=',b)
b&=False
print('Nilai b&=False akan menjadi',b)

#XOR
b=True
print('\n--------Nilai b=',b)
b^=False
print('Nilai b^=False akan menjadi',b)
b=False
print('Nilai b=',b)
b^=False
print('Nilai b^=False akan menjadi',b)

#Shifting
c=0b0100
print('\n--------Nilai c=',format(c, '04b'))
c>>=1
print('Nilai c>>=1 akan menjadi',format(c, '04b'))
c=0b0100
c<<=1
print('Nilai c<<=1 akan menjadi',format(c, '04b'))



# OPERATOR PERBANDINGAN
a=9
b=13
print('\n--------- Besar dari 28')
hasil= a>28
print(a,'> 13 adalah',hasil)
hasil= b>28
print(b,'> 13 adalah',hasil)

print('\n--------- Kecil dari 28')
hasil= a<28
print(a,'< 13 adalah',hasil)
hasil= b<28
print(b,'< 13 adalah',hasil)

print('\n--------- Besar atau sama dari 28')
hasil= a>=28
print(a,'>= 28 adalah',hasil)
hasil= b>=28
print(b,'>= 28 adalah',hasil)

print('\n--------- Kecil atau sama dari 28')
hasil= a<=28
print(a,'<= 28 adalah',hasil)
hasil= b<=28
print(b,'<= 28 adalah',hasil)

print('\n--------- Sama dari 28')
hasil= a==28
print(a,'== 28 adalah',hasil)
hasil= b==28
print(b,'== 28 adalah',hasil)

print('\n--------- Tidak sama dari 28')
hasil= a!=28
print(a,'!= 28 adalah',hasil)
hasil= b!=28
print(b,'!= 28 adalah',hasil)


# OPERATOR LOGIKA
a=True
b=False
print('\n==========AND==========')

hasil = a and a
print(a,'and',a,'hasilnya=',hasil)

hasil = a and b
print(a,'and',b,'hasilnya=',hasil)

hasil = b and a
print(b,'and',a,'hasilnya=',hasil)

hasil = b and b
print(b,'and',b,'hasilnya=',hasil)

# Tugas Melanjutkan (==========OR==========)
print('\n==========OR==========')
hasil = a or a
print(a,'or',a,'hasilnya=',hasil)

hasil = a or b
print(a,'or',b,'hasilnya=',hasil)

hasil = b or a
print(b,'or',a,'hasilnya=',hasil)

hasil = b or b
print(b,'or',b,'hasilnya=',hasil)

print('\n==========XOR==========')

hasil = a ^ a
print(a,'xor',a,'hasilnya=',hasil)

hasil = a ^ b
print(a,'xor',b,'hasilnya=',hasil)

hasil = b ^ a
print(b,'xor',a,'hasilnya=',hasil)

hasil = b ^ b
print(b,'xor',b,'hasilnya=',hasil)

# Tugas melanjutkan operasi(==========NOT==========)
print('\n==========NOT==========')

hasil = not a
print('not',a,'hasilnya=',hasil)

hasil = not b
print('not',b,'hasilnya=',hasil)



# OPERATOR MEMBERSHIP
print('\n===============IN')
nama= 'Saylandra Aulia Ramadhani'

test= 'ay'
cek= test in nama
print(test,'terdapat di',nama,'adalah',cek)

test= 'ya'
cek= test in nama
print(test,'terdapat di',nama,'adalah',cek)
print()
test1='a'
test2='i'
test3='u'
test4='e'
test5='o'

cek= test1 in nama
print(test1,'terdapat di',nama,'adalah',cek)
cek= test2 in nama
print(test2,'terdapat di',nama,'adalah',cek)
cek= test3 in nama
print(test3,'terdapat di',nama,'adalah',cek)
cek= test4 in nama
print(test4,'terdapat di',nama,'adalah',cek)
cek= test5 in nama
print(test5,'terdapat di',nama,'adalah',cek)


# Tugas lanjutan untuk NOT IN dengan cara yang sama
print('\n=============== NOT IN')
nama= 'Saylandra Aulia Ramadhani'

test= 'ay'
cek= test not in nama
print(test,'tidak terdapat di',nama,'adalah',cek)

test= 'ya'
cek= test not in nama
print(test,'tidak terdapat di',nama,'adalah',cek)
print()
test1='a'
test2='i'
test3='u'
test4='e'
test5='o'

cek= test1 not in nama
print(test1,'tidak terdapat di',nama,'adalah',cek)
cek= test2 not in nama
print(test2,'tidak terdapat di',nama,'adalah',cek)
cek= test3 not in nama
print(test3,'tidak terdapat di',nama,'adalah',cek)
cek= test4 not in nama
print(test4,'tidak terdapat di',nama,'adalah',cek)
cek= test5 not in nama
print(test5,'tidak terdapat di',nama,'adalah',cek)

