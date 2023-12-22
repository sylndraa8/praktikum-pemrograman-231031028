print('Tugas Praktikum 3'.center(40))
nama = 'Saylandra Aulia Ramadhani'
nim  = '231031028'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')

print()

'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''


str1 = 'duFort Frankel Von Neumann'
a = str1.upper()
b = a.strip('NEUMANN')
c = ('NEUMANN ')
d = c+b
print(d)
#output: NEUMANN DUFORT FRANKEL VON

print()

str2 = 'duFort Frankel Von Neumann'
a = str2.upper()
print(a[0:1]+a[2:3]+a[15:16],a[19:])
#output: DFV NEUMANN

print()

str3 = 'duFort Frankel Von Neumann'
a = str3.upper()
print(b[0:7],b[2:3]+b[15:16]+b[10:11])
#output: DUFORT FVN

print()

str4 = 'duFort Frankel Von Neumann'
a = str4.lower()
b = a.replace('f','F',1)
print(b[19:20].upper(),b[0:6],b[7:8].upper()+b[15:16].upper())
#output: N duFort FV

print()

str5 = 'duFort Frankel Von Neumann'
a = str5.upper()
b = a.strip('NEUMANN')
c = ('NEUMANN ')
d = b.lower()
print(c+ d[0:1],d[2:3],d[15:16])
#output: NEUMANN d f v

print()

str6 = 'duFort Frankel Von Neumann'
a = str6.upper()
b = a.strip('NEUMANN')
c = ('NEUMANN ')
print(c+b[0:1]+b[2:3]+b[15:16])
#output: NEUMANN DFV

print()

str7 = '@duFort Frankel Von Neumann$'
a=str7.strip('@,$')
b = a.replace('Neumann','NEUMANN')
print(b)
#output: duFort Frankel Von NEUMANN

print()

str8 = '#duFort4Frankel4Von4Neumann$'
a = str8.strip('#,$')
b = a.replace('4',' ')
print(b)
#output: duFort Frankel Von Neumann

print()

str9 = '@duFort@-^Frankel*-(Von(-(Neumann$'
a = str9.replace('@-^',' ').replace('*-(', ' ').replace('(-(',' ').strip('@,$')
print(a)
#output: duFort Frankel Von Neumann

print()

str10 = '@DUFort@1^FraNkel*1(VoN(1(NeuMann^'
a = str10.replace('@1^', ' ').replace('*1(', ' ').replace('(1(', ' ').strip('@,^')
b = a.lower()
c = b.title()
d = c.replace('D','d').replace('f','F')
print(d)
#output: duFort Frankel Von Neumann
