import os
os.system('clear')


nim = ['2','3','1','0','3','1','0','2','8']
#nim2 = '231031028'
print (nim[1:3])
#print (nim2[1:3])

print('===============Latihan item===============\n')
#Akses item
print(f'item indeks 0: {nim[0]}')
print(f'item indeks 4:{nim[4]}')
print(f'item indeks terakhir:{nim[len(nim)-1]}')

print('===============Latihan Negatif===============\n')
#Akses indeks negatif
print(f'item indeks terakhir:{nim[-1]}')
print(f'item indeks pertama:{nim[len(nim)-1]}')
print(f'item indeks 6 [-3]:{nim[-3]}')
print(f'item indeks 4 [-5]:{nim[-5]}')
print(f'item indeks 7 [-2]:{nim[-2]}')

print('===============Latihan Batas===============\n')
#Akses indeks batas 
print(f'item indeks 1,2....: \n {nim[1:]}')
print(f'item indeks 3,4....: \n {nim[3:]}')
print(f'item indeks 0,1,2....: \n {nim[3:]}')
print(f'item indeks 0,1,2,3....: \n {nim[4:]}')
print(f'item indeks semua : \n {nim[:]}')
print(f'item indeks [:8]  :\n {nim[4:]}')
print(f'item indeks[:6]  \n : {nim[4:]}')

print('===============Latihan Pengirisan===============\n')
#Pengirisan
print(f'item indeks 1,2: \n {nim[3:]}')
print(f'item indeks 2,3,4: \n {nim[2:5]}')
print(f'item indeks kosong \n {nim[3:3]}')
print(f'item indeks [8:8] kosong \n {nim[-1:1]}')
print(f'item indeks [1:8] kosong \n {nim[1:-1]}')
print(f'item indeks [2:7] kosong \n {nim[2:-2]}')

print('===============Latihan List===============\n')
#Latihan List 
print('\n latihan list ','=*20)')
data = ['Saylandra Aulia Ramadhani',2023,'Aktif']
nilai =[90,89,93,97]

print ('Nama : '+ data [0])
print ('Angkatan: ',data [1])
print ('Status  :  '+ data [2])

print(f'{data[0]} status kuliah: {data [2]}')
print(f'Data terbesar nilai adalah : {max(nilai)}')
print(f'Data terkecil nilai adalah : {min(nilai)}')
x_bar = sum (nilai)/len(nilai)
print(f'Rata-rata nilai adalah : {x_bar}') 

print('===============Latihan TUPLE===============\n')
# Latihan Tuple
data = ('Saylandra Aulia Ramadhani',2023,'Aktif')
nilai= (98,89,93,97)

print(f'Jumlah nilai mahasiswa adalah {len(nilai)}\n')
print(f'Data terbesar nilai adalah :{max(nilai)}\n')
print(f'Data terkecil nilai adalah: {min(nilai)}\n')
print(f'Rata-rata nilai nilai adalah: {sum(nilai)/len(nilai)}')

print('===============Latihan NESTED LIST===============\n')
# Latihan nested list
print ('latihan nested list','='*20)
data = [['Saylandra',2023,'aktif'],
        [98,93,97],
        [20,22],
        ['S1-Reguler','Ganjil']]

print (f'Angkatan \nprogram pendidikan {data[0][0]}: {data [3][0]}\n')
print (f'Angkatan {data[0][1]}: {data [3][1]}\n')
print (f'Jumlah Nilai {data[0][0]} adalah :{len(data[1])}\n')
print (f'Data terbesar {data[0][0]} adalah :{max (data[1])}\n')
print (f'Data terkecil {data[0][0]} adalah :{min (data[1])}\n')
print (f'Data Rata-rata nilai adalah : {sum(data[1])/len(data[1])}\n')

#======================== Tugas 4 ========================
print ('========================Tugas Praktikum 4========================\n')

data = [['Saylandra Aulia Ramadhani',2023,'Aktif'],
[97,95,96,97],
[20,22],
['S1-Reguler','Ganjil']]

matkul = ['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan Cinta IPTEK dan IMTAQ']
sks    = [2,2,2,2]
# Menambahkan matkul dan sks ke dalam data (di akhir)
data.append(matkul)
data.append(sks)

# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'{data[4][0]} dengan jumlah {data[-1][0]} sks\n')
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f'{data[4][1]} dengan jumlah {data[-1][1]} sks\n')
# Mata kuliah 3: Matkul3 dengan jumlah 3 sks
print(f'{data[4][2]} dengan jumlah {data[-1][2]} sks\n')
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f'{data[4][3]} dengan jumlah {data[-1][3]} sks\n')
data[4].append('Pengantar Pemrograman')
data[5].append(3)
# print(data)
# Tambahkan 3 matkul dengan sks nya
data[4].append('Pengantar Teknologi Informasi')
data[5].append(3)
data[4].append('Kalkulus Dasar 1')
data[5].append(3)
data[4].append('Sains Terpadu')
data[5].append(3)
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'{data[4][4]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'{data[4][5]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'{data[4][6]} dengan jumlah {data[-1][6]} sks\n')

# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'{data[4][0]} dengan jumlah {data[-1][0]} sks\n')
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f'{data[4][1]} dengan jumlah {data[-1][1]} sks\n')
# Mata kuliah 3: Matkul3 dengan jumlah 3 sks
print(f'{data[4][2]} dengan jumlah {data[-1][2]} sks\n')
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f'{data[4][3]} dengan jumlah {data[-1][3]} sks\n')
data[4].append('Pengantar Pemrograman')
data[5].append(3)
# print(data)
# Tambahkan 3 matkul dengan sks nya
data[4].append('Pengantar Teknologi Informasi')
data[5].append(3)
data[4].append('Kalkulus Dasar 1')
data[5].append(3)
data[4].append('Sains Terpadu')
data[5].append(3)
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'{data[4][4]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'{data[4][5]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'{data[4][6]} dengan jumlah {data[-1][6]} sks\n')

print('======================== Tugas Selesai ========================')
