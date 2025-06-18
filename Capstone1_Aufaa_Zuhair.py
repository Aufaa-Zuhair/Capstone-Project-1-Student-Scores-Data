# Data Nilai Mahasiswa 

#-----Input Mahasiswa Ke-1-----
#Nama: Abel
#Umur: 20
#NIP: 10006
#Asal: Manado
#Alamat: Jalan Sejahtera
#Nilai : (Matematika: 80, Fisika: 85, Kimia: 85, Biologi: 75)

#-----Input Mahasiswa Ke-2-----
#Nama: Sukma
#Umur: 21
#NIP: 10007
#Asal: Sukabumi
#Alamat: Jalan kumbangan 1
#Nilai : (Matematika: 85, Fisika: 85, Kimia: 80, Biologi: 80)

#-----Input Mahasiswa Ke-3-----
#Nama: Clara
#Umur: 21
#NIP: 10008
#Asal: Medan
#Alamat: Jalan Bangau
#Nilai : (Matematika: 90, Fisika: 80, Kimia: 95, Biologi: 70)

#-----Input Mahasiswa Ke-4-----
#Nama: Ken
#Umur: 20
#NIP: 10009
#Asal: Bandung
#Alamat: Jalan Menteng
#Nilai : (Matematika: 80, Fisika: 80, Kimia: 90, Biologi: 75)

#-----Input Mahasiswa Ke-5-----
#Nama: Rudy
#Umur: 21
#NIP: 10010
#Asal: Surabaya
#Alamat: Jalan Bungur
#Nilai : (Matematika: 75, Fisika: 75, Kimia: 85, Biologi: 95)

Data = {
'Nama' : ["Abel", "Sukma", "Clara", "Ken", "Rudy"],
'Gender' : ["Pria", "Pria", "Wanita", "Pria", "Pria"],
'Umur' : ['20', '21', '21', '20', '21'],
'NIP' : ['10006', '10007', '10008', '10009', '10010'],
'Asal' : ["Manado", "Sukabumi", "Medan", "Bandung", "Surabaya"],
'Nilai Matematika' : ['80', '85', '90', '80', '75'],
'Nilai Fisika' : ['85', '85', '80', '80', '75'],
'Nilai Kimia' : ['85', '80', '95', '90', '85'],
'Nilai Biologi' : ['75', '80', '70', '75', '95']
}

def menu_utama():
    print("====================Data Nilai Mahasiswa====================")
    print("1. Melihat Data Mahasiswa")
    print("2. Menambah Data Mahasiswa")
    print("3. Mengubah Data Mahasiswa")
    print("4. Menghapus Data Mahasiswa") 
    print("5. Exit")
   

    print("Silahkan Pilih Menu yang Ingin Dipilih (1-5)")

def menu_1():
    print("==========Melihat Data Mahasiswa==========")
    print("1. Report Seluruh Data") #1a
    print("2. Report Data Tertentu") #1b
    print("3. Lihat Rata=Rata NIlai Seluruh Mahasiswa")
    print("4. Lihat Rata-Rata Nilai Mahasiswa ")
    print("5. Menampilkan Data Mahasiswa Lulus")
    print("6. Kembali ke Menu Utama")

def menu_2():
    print("==========Melihat Data Mahasiswa==========")
    print("1. Menambah Data Mahasiswa") #2a
    print("2. kembali ke Menu Utama")

def menu_3():
    print("==========Melihat Data Mahasiswa==========")
    print("1. Ubah Data Mahasiswa") #3a
    print("2. kembali ke Menu Utama")

def menu_4():
    print("==========Melihat Data Mahasiswa==========")
    print("1. Hapus Data Mahasiswa") #4a
    print("2. kembali ke Menu Utama")

    

def input_menu():
    global menu_dipilih
    menu_dipilih = input("Masukan menu yang ingin dipilih : ")
    print(f"Menu yang dipilih : {menu_dipilih}")
   

def inputTidakValid():
    print('Input yang dimasukkan tidak sesuai')


def fitur1a():
    n = len(Data["Nama"])
    print(f"|{'No' :<3}|  {'Nama' :<20}|  {'Gender' :<12}|  {'Umur' :<8}|  {'NIP' :<10}|  {'Asal' :<20}|  {'Nilai Matematika' :<20}|  {'Nilai Fisika' :<15}|  {'Nilai Kimia' :<15}|  {'Nilai Biologi':<20}|")
    print('='*171)
    for i in range(n):
        print(f"|{i+1:<3}|  {Data["Nama"][i] :<20}|  {Data["Gender"][i] :<12}|  {Data["Umur"][i]:<8}|  {Data["NIP"][i] :<10}|  {Data["Asal"][i] :<20}|  {Data["Nilai Matematika"][i]:<20}|  {Data["Nilai Fisika"][i]:<15}|  {Data["Nilai Kimia"][i] :<15}|  {Data["Nilai Biologi"][i] :<20}")


def fitur1b():
    while True:
        cariSiswa = input("Masukkan NIP siswa yang ingin dicari: ")
        if cariSiswa not in Data['NIP']:
            inputTidakValid()
            continue
        else:
            break

    i = Data['NIP'].index(cariSiswa)
    
    print(f"|{'No' :<3}|  {'Nama' :<20}|  {'Gender' :<12}|  {'Umur' :<8}|  {'NIP' :<10}|  {'Asal' :<20}|  {'Nilai Matematika' :<20}|  {'Nilai Fisika' :<15}|  {'Nilai Kimia' :<15}|  {'Nilai Biologi':<20}|")
    print('='*171)
    print(f"|{i+1:<3}|  {Data["Nama"][i] :<20}|  {Data["Gender"][i] :<12}|  {Data["Umur"][i]:<8}|  {Data["NIP"][i] :<10}|  {Data["Asal"][i] :<20}|  {Data["Nilai Matematika"][i]:<20}|  {Data["Nilai Fisika"][i]:<15}|  {Data["Nilai Kimia"][i] :<15}|  {Data["Nilai Biologi"][i] :<20}")


def fitur1c():
    for i in range(len(Data["Nama"])):
        Nama =  Data["Nama"][i]
        nilaiMTKInt = int(Data['Nilai Matematika'][i])
        nilaiFISInt = int(Data['Nilai Fisika'][i])
        nilaiKIMInt = int(Data['Nilai Kimia'][i])
        nilaiBIOInt = int(Data['Nilai Biologi'][i])

        rata_rata = (nilaiMTKInt + nilaiFISInt + nilaiKIMInt + nilaiBIOInt) / 4
        print(f"Nama: {Nama}, Rata-Rata: {rata_rata:.2f}")



        
def fitur1d():
    while True:
        nama_dicari = input("Masukkan nama mahasiswa yang ingin dilihat rata-ratanya (atau ketik 'exit' untuk keluar): ")

        if nama_dicari.capitalize() == "Exit":
            print("Keluar dari fitur pencarian.")
            break  

        elif nama_dicari.capitalize() not in Data["Nama"]:
            print("Mahasiswa tidak ditemukan, Coba lagi")
            continue  

        else:
            

            index = Data["Nama"].index(nama_dicari.capitalize())

            nilaiMTK = int(Data['Nilai Matematika'][index])
            nilaiFIS = int(Data['Nilai Fisika'][index])
            nilaiKIM = int(Data['Nilai Kimia'][index])
            nilaiBIO = int(Data['Nilai Biologi'][index])

            rata_rata = (nilaiMTK + nilaiFIS + nilaiKIM + nilaiBIO) / 4

            print(f"\nNama: {nama_dicari}")
            print(f"Matematika: {nilaiMTK}")
            print(f"Fisika: {nilaiFIS}")
            print(f"Kimia: {nilaiKIM}")
            print(f"Biologi: {nilaiBIO}")
            print(f"Rata-rata: {rata_rata:.2f}\n")

def fitur1e():
    print("Daftar Mahasiswa yang Lulus:\n")

    for i in range(len(Data["Nama"])):
        nama = Data["Nama"][i]
        mtk = int(Data["Nilai Matematika"][i])
        fisika = int(Data["Nilai Fisika"][i])
        kimia = int(Data["Nilai Kimia"][i])
        biologi = int(Data["Nilai Biologi"][i])
        
        rata_rata = (mtk + fisika + kimia + biologi) / 4

        if rata_rata >= 75:
            print(f"{nama} (Rata-rata: {rata_rata:.2f}) - LULUS")


def fitur1():

    while True:
        menu_1()
        input_menu()
        if menu_dipilih == '1':
            fitur1a()
            continue

        elif menu_dipilih == '2':
            fitur1b()
            continue

        elif menu_dipilih == '3':
            fitur1c()
            continue

        elif menu_dipilih == '4':
            fitur1d()
            continue

        elif menu_dipilih == '5':
            fitur1e()
            continue

        elif menu_dipilih == '6':
            break

        else:
            inputTidakValid()

def fitur2a():
    while True:
        nambah_mahasiswa = input("Masukan Nama Mahasiswa")
        if nambah_mahasiswa.isalpha():
            break
        else:
            inputTidakValid()
            continue
    while True:   
        nambah_gender = input("Masukan Gender Mahasiswa [pria/wanita]")
        if nambah_gender.upper() == 'PRIA' or nambah_gender.upper() == 'WANITA':
            break
        else:
            inputTidakValid()
            continue

    while True:
        nambah_umur = input("Masukan Umur Mahasiswa")
        if nambah_umur.isdigit():
            break
        else:
            inputTidakValid()
            continue
    
    while True:
        nambah_NIP = input("Masukan NIP Mahasiswa")
        if nambah_NIP.isdigit():
            break
        else:
            inputTidakValid()
            continue
    
    while True:
        nambah_asal = input("Masukan Asal Mahasiswa")
        if nambah_asal.isalpha():
            break
        else:
            inputTidakValid()
            continue

    while True:
        nambah_nilai_matematika = input("Masukan Nilai Matematika Mahasiswa")
        if nambah_nilai_matematika.isdigit():
            break
        else:
            inputTidakValid()
            continue

    while True:
        nambah_nilai_fisika = input("Masukan Nilai Fisika Mahasiswa")
        if nambah_nilai_fisika.isdigit():
            break
        else:
            inputTidakValid()
            continue
    while True:
        nambah_nilai_kimia = input("Masukan Nilai Kimia Mahasiswa")
        if nambah_nilai_kimia.isdigit():
            break
        else:
            inputTidakValid()
            continue
    
    while True:
        nambah_nilai_biologi = input("Masukan Nilai Biologi Mahasiswa")
        if nambah_nilai_biologi.isdigit():
            break
        else:
            inputTidakValid()
            continue
    

    Data['Nama'].append(nambah_mahasiswa)
    Data["Gender"].append(nambah_gender.capitalize())
    Data["Umur"].append(nambah_umur)
    Data["NIP"].append(nambah_NIP)
    Data["Asal"].append(nambah_asal)
    Data["Nilai Matematika"].append(nambah_nilai_matematika)
    Data["Nilai Fisika"].append(nambah_nilai_fisika)
    Data["Nilai Kimia"].append(nambah_nilai_kimia)
    Data["Nilai Biologi"].append(nambah_nilai_biologi)
    fitur1a()


def fitur2():
    while True:
        menu_2()
        input_menu()
        if menu_dipilih == '1':
            fitur2a()
            continue
        elif menu_dipilih == '2':
            break
        else:
            inputTidakValid()

def fitur3a():
    while True:
        masukan_NIP = input("Masukan NIP Mahasiswa yang Ingin Diupdate")
        if masukan_NIP not in Data["NIP"]:
            print("Mahasiswa Tidak Ditemukan")
            continue
        else:
            break

    i = Data["NIP"].index(masukan_NIP)

    while True:
        validasi = input(f"Apakah anda ingin mengubah data {Data['Nama'][i]} [Y/N]")
        if validasi.upper() == 'N':
            break
        elif validasi.upper() == 'Y':
            while True:
                update_dipilih = input("Masukan Kolom yang Ingin di update")
                if update_dipilih.title() not in Data:
                    inputTidakValid()
                    continue
                elif update_dipilih.upper() == "NIP":
                    print("NIP Primary Key Tidak Boleh di Ganti")
                    continue
                else:
                    break

            if update_dipilih == "Nama":
                while True:
                    value_baru = input("Masukan Nama Mahasiswa")
                    if value_baru.isalpha():
                        break
                    else:
                        inputTidakValid()
                        continue

            elif update_dipilih == "Gender":
                while True:
                    value_baru = input("Masukan Gender Mahasiswa")
                    if value_baru.upper() == 'PRIA' or value_baru.upper() == 'WANITA':
                        break
                    else:
                        inputTidakValid()
                        continue

            elif update_dipilih == "Umur":
                while True:
                    value_baru = input("Masukan Umur Mahasiswa")
                    if value_baru.isdigit():
                        break
                    else:
                        inputTidakValid()
                        continue

            elif update_dipilih == "Asal":
                while True:
                    value_baru = input("Masukan Asal Mahasiswa")
                    if value_baru.isalpha():
                        break
                    else:
                        inputTidakValid()
                        continue

            elif update_dipilih.title() == "Nilai Matematika":
                while True:
                    value_baru = input("Masukan Nilai Matematika Mahasiswa") 
                    
                    if value_baru.isdigit():
                            if int(value_baru) <= 100:
                                break
                            else:
                                print("Nilai Tidak Boleh Lebih Dari 100")
                                continue
                    else:
                        inputTidakValid()
                        continue
            
            elif update_dipilih.title() == "Nilai Fisika":
                while True:
                    value_baru = input("Masukan Nilai Fisika Mahasiswa") 
                    
                    if value_baru.isdigit():
                            if int(value_baru) <= 100:
                                break
                            else:
                                print("Nilai Tidak Boleh Lebih Dari 100")
                                continue
                    else:
                        inputTidakValid()
                        continue
            
            elif update_dipilih.title() == "Nilai Kimia":
                while True:
                    value_baru = input("Masukan Nilai Kimia Mahasiswa") 
                    
                    if value_baru.isdigit():
                            if int(value_baru) <= 100:
                                break
                            else:
                                print("Nilai Tidak Boleh Lebih Dari 100")
                                continue
                    else:
                        inputTidakValid()
                        continue
            
            elif update_dipilih.title() == "Nilai Biologi":
                while True:
                    value_baru = input("Masukan Nilai Biologi Mahasiswa") 
                    
                    if value_baru.isdigit():
                            if int(value_baru) <= 100:
                                break
                            else:
                                print("Nilai Tidak Boleh Lebih Dari 100")
                                continue
                    else:
                        inputTidakValid()
                        continue

            while True:
                validasi2 = input("Apakah anda ingin mengupdatenya? [Y/N]")
                if validasi2.upper() == 'Y':       
                    Data[update_dipilih.title()][i] = value_baru
                    break
                elif validasi2.upper() == 'N':
                    print("Data tidak jadi diperbarui")
                    break
                else:
                    inputTidakValid()
                    continue
            break
        else:
            inputTidakValid()
            continue

def fitur3():
    while True:
        menu_3()
        input_menu()
        if menu_dipilih == '1':
            fitur3a()
            continue
        elif menu_dipilih == '2':
            break
        else:
            inputTidakValid()

def fitur4a():
    while True:
        input_NIP = input("Masukan NIP Mahasiswa yang ingin di Hapus")
        if input_NIP not in Data["NIP"]:
            inputTidakValid()
            continue
        else:
            break
    
    i = Data["NIP"].index(input_NIP)

    while True:
        yang_dihapus = input(f"Apakah Anda Ingin Menghapus Data {Data["Nama"][i]} tersebut? [YA/TIDAK]")
        if yang_dihapus.upper() == "YA":
            for j in Data:
                del Data[j][i]
            print("Data Tesebut Sudah di Hapus")
            break
        elif yang_dihapus.upper() == "TIDAK":
            print("Data Tersebut Tidak Terhapus")
            break


def fitur4():
    while True:
        menu_4()
        input_menu()
        if menu_dipilih == '1':
            fitur4a()
            continue
        elif menu_dipilih == '2':
            break
        else:
            inputTidakValid()

while True:
    menu_utama()
    input_menu()

    if menu_dipilih == '1':
        fitur1()
        continue

    elif menu_dipilih == '2':
        fitur2()
        continue

    elif menu_dipilih == '3':
        fitur3()
        continue

    elif menu_dipilih == '4':
        fitur4()
        continue


    elif menu_dipilih == '5':
        print("Terima Kasih, Sampai Jumpa")
        break

    else:
        inputTidakValid()
        continue
    