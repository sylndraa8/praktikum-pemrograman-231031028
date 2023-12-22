kesempatan = 3
pw_1 = 000
pw_2 = 111
pw_3 = 222

while True:
    if kesempatan != 0:
        inp = int(input('Masukkan password : '))
        if inp == pw_1:
            print('Berhasil')
            inp = int(input('Masukkan password kedua: '))
            if inp == pw_2:
                print('Berhasil')
                inp = int(input('Masukkan password ketiga: '))
                if inp == pw_3:
                    print('Anda berhasil login')
                    break
                elif inp != pw_3:
                    kesempatan -= 1
                    print('Password salah.')
                    print(f'Kesempatan anda tersisa {kesempatan} kali')
                    continue
                else:
                    print('Anda terblokir. Silahkan coba lain kali')
                    break
            elif inp != pw_2:
                kesempatan -= 1
                print('Password salah.')
                print(f'Kesempatan anda tersisa {kesempatan} kali')
                continue
            else:
                print('Anda terblokir. Silahkan coba lain kali')
                break
        elif inp != pw_1:
            kesempatan -= 1
            print('Password salah.')
            print(f'Kesempatan anda tersisa {kesempatan} kali')
            continue
        else:
            print('Anda terblokir. Silahkan coba lain kali')
            break
    else:
        print('\nAnda terblokir. Kesempatan anda telah habis')
        break