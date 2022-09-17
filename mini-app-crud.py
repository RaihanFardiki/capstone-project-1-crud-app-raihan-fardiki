'''
TUGAS CAPSTONE PROJECT
NAMA : AKHMAD RAIHAN FARDIKI 

'''


isiYP = {
    14041 : {"nama"     : "sasuke uchiha",
             "alamat"   : "jl.dahlia no.17",
             "pekerjaan": "mahasiswa",
             "nomor"    : "088913412312"
},
    14042 : {"nama"     : "naruto uzumaki",
             "alamat"   : "jl.anggrek no. 14",
             "pekerjaan": "mahasiswa",
             "nomor"    : "088913718393"
},
    14043 : {"nama"     : "monkey D luffy",
             "alamat"   : "jl.seroja 4 no.55",
             "pekerjaan": "mahasiswa",
             "nomor"    : "088222178750"
},
    14044 : {"nama"     : "levi ackerman",
             "alamat"   : "jl.bougenvile 99",
             "pekerjaan": "mahasiswa",
             "nomor"    : "088222178750"
},
    14045 : {"nama"     : "gojo satoru",
             "alamat"   : "jl. kaktus raya 77",
             "pekerjaan": "mahasiswa",
             "nomor"    : "088222178750"
}}

def tabel():
    if len(isiYP) == 0:
        print("    Tidak ada data")
    else:
        print('''KODE\t|NAMA\t\t\t|ALAMAT\t\t\t|PEKERJAAN\t|NOMOR''')
        for i in isiYP:
            print(f"{i}\t|{isiYP[i]['nama']}\t\t|{isiYP[i]['alamat']}\t|{isiYP[i]['pekerjaan']}\t|{isiYP[i]['nomor']}")

def fungsi1(): #fungsi menu menampilkan
    print('''       
    Anda Berada Di Menu Tampilkan Data
        1. Tampilkan Semua Data
        2. Tampilkan Data Tertentu
        3. Back
    ''')
    input_user1= input("    Masukkan Nomor Yang Ingin Dijalankan: ")
    if input_user1 == "1":
        tabel()
        fungsi1()
    elif input_user1 == "2":
        input_user1 = input("    Masukkan Nomor Kunci Anda: ")
        if input_user1.isdigit():
            if int(input_user1) in list(isiYP.keys()):
                print("KODE\t|NAMA\t\t\t|ALAMAT\t\t\t|PEKERJAAN\t|NOMOR")
                print(f"{int(input_user1)}\t|{isiYP[int(input_user1)]['nama']}\t\t|{isiYP[int(input_user1)]['alamat']}\t|{isiYP[int(input_user1)]['pekerjaan']}\t|{isiYP[int(input_user1)]['nomor']}")
                fungsi1()
            else:
                print("    Data Tidak Ditemukan")
                fungsi1()
        else:
            print("    MASUKKAN NOMOR DENGAN BENAR!")
            fungsi1()
    elif input_user1 == "3":
        print('''    Yakin Keluar Dari Menu Lihat Data?
        1.YA
        2.TIDAK''')
        input_user1 = input("    Masukkan Nomor Yang Ingin Dijalankan: ")
        if input_user1 == "1":
            start()
        elif input_user1 == "2":
            fungsi1()
        else:
            print("    MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
            fungsi1()
    else:
        print("    MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
        fungsi1()

def fungsi2(): #fungsi menambahkan data
    print('''
    Anda Berada Dalam Menu Tambahkan Data
        1. Masukkan Data Baru Dalam Yellow Pages
        2. Back
    ''')
    input_user1 = input("    Masukkan Nomor Yang Ingin Dijalankan: ")
    if input_user1 == "1":
        input_kode = input("    Masukkan Kode Nomor Yang Ingin Dibuat: ")
        if input_kode.isdigit():
            if int(input_kode) in list(isiYP.keys()):
                print("    KODE NOMOR SUDAH DIGUNAKAN")
                fungsi2()
            elif int(input_kode) not in list(isiYP.keys()) and len(input_kode) == 5:
                input_nama = input("    Masukkan Nama: ")
                input_alamat = input("    Masukkan Alamat: ")
                input_pekerjaan = input("    Masukkan Pekerjaan: ")
                input_nomor = input("    Masukkan Nomor Yang Bisa Dihubungi: ")
                print("KODE\t|NAMA\t\t\t|ALAMAT\t\t\t|PEKERJAAN\t|NOMOR")
                print(f"{int(input_kode)}\t|{input_nama}\t\t|{input_alamat}\t|{input_pekerjaan}\t|{input_nomor}")
                print('''    
        Apakah Anda Ingin Menyimpan Data Ini Dalam Yellow Pages?
        1. YA
        2. TIDAK
                ''')
                input_user1 = input("   Masukkan Nomor Yang Ingin Dijalankan: ")
                if input_user1 == "1":
                    isiYP[int(input_kode)] = {"nama" : input_nama, "alamat" : input_alamat, "pekerjaan" : input_pekerjaan, "nomor" : input_nomor}
                    print("   Data Berhasil Disimpan")
                    fungsi2()
                elif input_user1 == "2":
                    print("    Data Tidak Disimpan")
                    fungsi2()
                else:
                    print("   MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
                    fungsi2()
            else:
                print("    Panjang Kode Harus Memiliki 5 Karakter")
                fungsi2()
        else: 
            print("    KODE NOMOR HARUS BERUPA ANGKA DAN MEMILIKI JUMLAH 5 KARAKTER!")
            fungsi2()
    elif input_user1 == "2":
        print('''
    Apakah Anda Ingin Ingin Meninggalkan Menu Tambahkan Data?
        1. YA
        2. TIDAK
                ''')
        input_user1 = input("    Masukkan Nomor Yang Ingin Dijalankan: ")
        if input_user1 == "1":
            start()
        elif input_user1 == "2":
            fungsi2()
        else:
            print("   MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
            fungsi2()
    else:
        print("    MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
        fungsi2()

def fungsi3(): #fungsi mengupdate data
    print('''
    Anda Berada Dalam Menu Update Data
        1. Update Data Pada Yellow Pages
        2. Back
    ''')
    input_user1 = input("    Masukkan Nomor Yang Ingin Dijalankan: ")
    if input_user1 == "1":
        input_kode = input("    Masukkan Kode Number Yang Ingin Diganti: ")
        if input_kode.isdigit():
            if int(input_kode) in list(isiYP.keys()):
                print("KODE\t|NAMA\t\t\t|ALAMAT\t\t\t|PEKERJAAN\t|NOMOR")
                print(f"{int(input_kode)}\t|{isiYP[int(input_kode)]['nama']}\t\t|{isiYP[int(input_kode)]['alamat']}\t|{isiYP[int(input_kode)]['pekerjaan']}\t|{isiYP[int(input_kode)]['nomor']}")
                print('''             
    Apakah Anda Ingin Mengupdate Data Ini?
        1. YA
        2. TIDAK
                ''')
                input_user1 = input("    Masukkan Nomor Yang Ingin Dijalankan: ")
                if input_user1 == "1":
                    print('''    
    Nama Kolom Yang Akan Diganti?
        1. Nama
        2. Alamat
        3. Pekerjaan
        4. Nomor
    ''')
                    input_user1 = input("    Masukkan Nomor Pada Nama Kolom Yang Akan Diganti? ")
                    if input_user1 == "1":
                        input_nama = input("    Masukkan Nama Yang Baru: ")
                    elif input_user1 == "2":
                        input_alamat = input("    Masukkan Alamat Yang Baru: ")
                    elif input_user1 == "3":
                        input_pekerjaan = input("    Masukkan Pekerjaan Baru: ")
                    elif input_user1 == "4":
                        input_nomor = input("    Masukkan Nomor Baru Yang Bisa Dihubungi: ")
                    else:
                        print("    MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
                        fungsi3()
                    print('''    
    Yakin Ingin Mengubah Data?
        1. YA 
        2. TIDAK''')
                    input_user2 = input("    Masukkan Nomor Yang Ingin Dijalankan? ")
                    if input_user1 == "1" and input_user2 == "1":
                        isiYP[int(input_kode)] = {"nama" : input_nama, "alamat" : isiYP[int(input_kode)]["alamat"], "pekerjaan" : isiYP[int(input_kode)]["pekerjaan"], "nomor" : isiYP[int(input_kode)]["nomor"]}
                        print("    Data Berhasil Diganti")
                        fungsi3()
                    elif input_user1 == "2" and input_user2 == "1":
                        isiYP[int(input_kode)] = {"nama" : isiYP[int(input_kode)]["nama"], "alamat" : input_alamat, "pekerjaan" : isiYP[int(input_kode)]["pekerjaan"], "nomor" : isiYP[int(input_kode)]["nomor"]}
                        print("    Data Berhasil Diganti")
                        fungsi3()
                    elif input_user1 == "3" and input_user2 == "1":
                        isiYP[int(input_kode)] = {"nama" : isiYP[int(input_kode)]["nama"], "alamat" : isiYP[int(input_kode)]["alamat"], "pekerjaan" : input_pekerjaan, "nomor" : isiYP[int(input_kode)]["nomor"]}
                        print("    Data Berhasil Diganti")
                        fungsi3()
                    elif input_user1 == "4" and input_user2 == "1":
                        isiYP[int(input_kode)] = {"nama" : isiYP[int(input_kode)]["nama"], "alamat" : isiYP[int(input_kode)]["alamat"], "pekerjaan" : isiYP[int(input_kode)]["pekerjaan"], "nomor" : input_nomor}
                        print("    Data Berhasil Diganti")
                        fungsi3()
                    elif input_user2 == "2":
                        print("    Data Tidak Diubah")
                        fungsi3()
                    else:
                        print("   Masukkan Sesuai Nomor Yang Disediakan")
                        fungsi3()
                elif input_user1 == "2":
                    fungsi3()
                else:
                    print("    MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
                    fungsi3()
            elif int(input_kode) not in list(isiYP.keys()):
                print("    Data Yang Anda Cari Tidak Ditemukan")
                fungsi3()
            else:
                print("    KODE NOMOR HARUS BERUPA ANGKA DAN MEMILIKI JUMLAH 5 KARAKTER!")
                fungsi3()
        else:
            print("    KODE NOMOR HARUS BERUPA ANGKA!")
            fungsi3()
    elif input_user1 == "2":
        print('''
    Apakah Anda Ingin Ingin Meninggalkan Menu Update Data?
        1. YA
        2. TIDAK
                ''')
        input_user1 = input("    Masukkan Nomor Yang Ingin Dijalankan: ")
        if input_user1 == "1":
            start()
        elif input_user1 == "2":
            fungsi3()
        else:
            print("   MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
            fungsi3()
    else:
        print("    MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
        fungsi3()

def fungsi4(): #fungsi menghapus data
    print('''
    Anda Berada Dalam Menu Hapus Data
        1. Hapus Data Dalam Yellow Pages
        2. Back
    ''')
    input_user1 = input("    Masukkan Nomor Yang Ingin Dijalankan: ")
    if input_user1 == "1":
        input_kode = input("    Masukkan Kode Number Yang Ingin Dihapus: ")
        if input_kode.isdigit():
            if int(input_kode) in list(isiYP.keys()):
                print("KODE\t|NAMA\t\t\t|ALAMAT\t\t\t|PEKERJAAN\t|NOMOR")
                print(f"{int(input_kode)}\t|{isiYP[int(input_kode)]['nama']}\t\t|{isiYP[int(input_kode)]['alamat']}\t|{isiYP[int(input_kode)]['pekerjaan']}\t|{isiYP[int(input_kode)]['nomor']}")
                print('''             
    Apakah Anda Ingin Menghapus Data Ini?
    1. YA
    2. TIDAK
                ''')
                input_user1 = input("    Masukkan Nomor Yang Ingin Dijalankan? ")
                if input_user1 == "1":
                    isiYP.pop(int(input_kode))
                    print("    Data Berhasil Dihapus")
                    fungsi4()
                elif input_user1 == "2":
                    print("    Data Tidak Dihapus")
                    fungsi4()
                else:
                    print("    MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
                    fungsi4()
            elif int(input_kode) not in list(isiYP.keys()):
                print("    Data Yang Anda Cari Tidak Ditemukan")
                fungsi4()
            else:
                print("    KODE NOMOR HARUS BERUPA ANGKA DAN MEMILIKI JUMLAH 5 KARAKTER!")
                fungsi4()
        else:
            print("    KODE NOMOR HARUS BERUPA ANGKA!")
            fungsi4()
    elif input_user1 == "2":
        print('''
    Apakah Anda Ingin Ingin Meninggalkan Menu Hapus Data?
        1. YA
        2. TIDAK
                ''')
        input_user1 = input("    Masukkan Nomor Yang Ingin Dijalankan: ")
        if input_user1 == "1":
            start()
        elif input_user1 == "2":
            fungsi4()
        else:
            print("   MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
            fungsi4()
    else:
        print("    MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
        fungsi4()



def start(): #fungsi menu awal
    print('''       
    WELCOME TO RAIHAN FARDIKI's CAPSTONE PROJECT

        1. Tampilkan Isi Yellow Page
        2. Tambahkan Isi Yelllow Page
        3. Ganti Isi Yellow Page
        4. Hapus Isi Dari Yellow Page
        5. Keluar Dari Yellow Page    
    ''')
    input_user = input("    Masukkan Nomor Yang Ingin Dijalankan: ")
    if input_user == "1":
        fungsi1()
    elif input_user == "2":
        fungsi2()
    elif input_user == "3":
        fungsi3()
    elif input_user == "4":
        fungsi4()
    elif input_user == "5":
        print('''    Yakin Keluar Dari Raihan Fardiki's Capstone Project?
        1.YA
        2.TIDAK''')
        input_user1 = input("    Masukkan Nomor Yang Ingin Dijalankan: ")
        if input_user1 == "1":
            print("    Terima Kasih Telah Menggunakan Raihan Fardiki's Capstone Project")
        elif input_user1 == "2":
            start()
        else:
            print("    MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
            start()
    else:
        print("    MASUKAN SESUAI DENGAN NOMOR YANG TERSEDIA!")
        start()
       
start()
