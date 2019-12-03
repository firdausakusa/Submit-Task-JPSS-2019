'''
TUGAS 3

1. Class rekening
    *Constructor
    *Method setor
    *Method ambil_uang
    *Transfer (plus, minus)
    *Cek saldo
    *Informasi
2. Class Nasabah
    *Constructor
    *log in 
    *transaksi
- Pada sebuah bank, nasabah yang membuka rekening harus menyetor minimal 100000 terlebih dahulu. 
- Buatlah program sederhana untuk mesin ATM dengan kelas 
Nasabah dan Rekening. 
- Fungsi/method yang harus ada adalah fungsi 
ambil uang, setor, dan transfer. 
- Kemudian buatlah nasabah bernama Aldo dan Aldi. 
Simulasikan kejadian Aldo melakukan pengambilan uang 
sebanyak 150000. Aldi mentransfer uang sejumlah 50000 ke 
rekening Aldo. 
- Lalu cetak data kedua nasabah! (catatan: ketika terjadi suatu kegiatan 
di ATM (setor, tarik, transfer) 
akan ada output berupa keterangan kejadian. 
Contoh “Transfer sebesar xxxxx ke rekening xxxxx”. 
Format keterangan yang dicetak bebas).
'''

data = {"name":"Aldo",
       "pin":"1510828",
       "Norek":"001002003",
        'Saldo':100000}
data1 = {"name":"Aldi",
         "pin":"180888",
         "Norek":"001002004",
         "Saldo":100000}

user = input("Username : ")
psw = input("Password : ")

class nasabah():
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
    def login(self,name = user, pin = psw):
        self.name = user
        self.pin = psw

class rekening(nasabah):
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
    def tarik(self):
        nominal = int(input("Jumlah Tarik Tunai : "))
        saldo = data["Saldo"]-nominal
        saldo1 = data1["Saldo"]-nominal
        if saldo < 50000 and saldo1 < 50000:
            print("Transaksi Gagal")
        else:
            print("\n=====Sukses=====\n")
            print("Username : ",self.name)
            print("Anda Melakukan Tarik Tunai Senilai : ",nominal)
        return nominal
    def setor(self):
        nominal = int(input("Jumlah Setor Tunai : "))
        saldo = data1["Saldo"]
        saldo1 = data["Saldo"]
        print("\n=====Sukses=====\n")
        print("Username : ",self.name)
        print("Anda Melakukan Setor Tunai Senilai : ", nominal)
        return nominal
    def transfer(self):
        rek = input("No. Rekening Tujuan : ")
        if rek == data['Norek'] or rek == data1['Norek']:
            nominal = int(input("Jumlah Transfer : "))
            if data["Saldo"] - nominal < 50000 and data1["Saldo"] - nominal < 50000:
                print("Saldo Anda Tidak Mencukupi")
            else:
                print("\n=====Sukses=====\n")
                print("Username : ", self.name)
                print("No. Rekening Tujuan : ",rek)
                print("Jumlah Transfer : ",nominal)
                return nominal, rek
            return rek
        else:
            print("Data Tidak Ditemukan")
            return rek
    def menu(self):
        print("""\n=====Menu=====
        1. Tarik Tunai
        2. Setor Tunai
        3. Transfer""")
        menu = int(input("Masukan Pilihan : "))
        return menu
nes = rekening(user,psw)
nes.login()
if user == data['name'] and psw == data['pin']:
    men = nes.menu()
    if men == 1:
        nom = nes.tarik()
        if data["Saldo"]-nom < 50000 and data1["Saldo"]-nom < 50000:
            print("Saldo Anda Tidak Mencukupi")
        else:
            total = data['Saldo'] - nom
            print("Saldo Anda : ",total)
            print("No. Rekening : ",data['Norek'])
    elif men == 2:
        nom = nes.setor()
        total = data["Saldo"] + nom
        print("Saldo Anda : ", total)
        print("No. Rekening : ", data['Norek'])
    elif men == 3:
        trans = nes.transfer()
        if trans[1] == data['Norek'] or trans[1] == data1['Norek'] :
            if data['Saldo'] - trans[0] < 50000 and data1['Saldo'] - trans[0] < 50000:
                print()
            else:
                print("Sisa Saldo : ",data['Saldo']-trans[0])
        else:
            print()

elif user == data1['name'] and psw == data1['pin']:
    men = nes.menu()
    if men == 1:
        nom = nes.tarik()
        if data['Saldo'] - nom < 50000 and data1['Saldo'] - nom < 50000:
            print("Saldo Anda Tidak Mencukupi")
        else:
            total = data1['Saldo'] - nom
            print("Saldo Anda : ", total)
            print("No. Rekening : ", data1['Norek'])
    elif men == 2:
        nom = nes.setor()
        total = data1['Saldo'] + nom
        print("Saldo Anda : ", total)
        print("No. Rekening : ", data1['Norek'])
    elif men == 3:
        trans = nes.transfer()
        if trans[1] == data['Norek'] or trans[1] == data1['Norek'] :
            if data['Saldo'] - trans[0] < 50000 and data1['Saldo'] - trans[0] < 50000:
                print()
            else:
                print("Sisa Saldo : ",data1['Saldo']-trans[0])
        else:
            print()
else:
    print("Error")