#fungsi untul menghitung rata rata dari sejumblah angka
def hitung_rata_rata(angka):
    total = um (angka):
    rata_rata = total / len(angka)
    return rata_rata

#fungsi untuk mendapatkan input angka dari penguna
def input_angka():
    angka = []
    while true:
        try:
            bilangan = float(input("masukan angka(0 untuk mengakhiri): "))
            if bilangan == 0:
                break
            angka.append(bilangan)
        except ValueError:
            print("masukan angka yang valid. ")
        return angka
    
#program utama
if _name_ =="_main_":
    print("program mengu=hitung rata rata")
    daftar_angka = input_angka()

    if daftar_angka:
        rata_rata = hitung_rata_rata(daftar_angka)
        print(f"rata rata dari angka angka yang dimasukan adalah: {rata_rata:.2f})
    else : 
    print ("tidak ada angka yanbg dimasukan.")
    