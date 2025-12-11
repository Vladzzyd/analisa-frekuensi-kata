import textwrap

# WARNA
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

daftar_fungsi = ("input","tampilkan","analisa","quit")
daftar_kalimat = {}

def judul(judul):
    print(MAGENTA+"="*50+RESET)
    print(MAGENTA+judul.center(50)+RESET)
    print(MAGENTA+"="*50+RESET)

def input_kalimat():
    judul("INPUT KALIMAT")
    
    while True:
        judul_kalimat = input(CYAN+"\nmasukkan judul kalimat: "+RESET).lower().strip()
        if not judul_kalimat or len(judul_kalimat) > 18:
            print(RED+"ERROR: judul kalimat tidak boleh kosong dan lebih dari 18 karakter!!"+RESET)

        elif judul_kalimat in daftar_kalimat:
            print(RED+"ERROR: judul kalimat ini sudah dipakai!"+RESET)

        else:
            print(GREEN+f"judul kalimat {judul_kalimat}..\n"+RESET)
            break

    while True:
        kalimat = input(CYAN+"masukkan kalimat: "+RESET).lower()
        if not kalimat:
            print(RED+"ERROR: kalimat tidak boleh kosong!!\n"+RESET)

        else:  
            daftar_kalimat[judul_kalimat] = kalimat
            print(GREEN+"berhasil memasukkan kalimat..\n"+RESET)
            break

def tampilkan():
    judul("DAFTAR KALIMAT TERSIMPAN")

    if not daftar_kalimat:
        print(YELLOW+"\ndaftar kalimat tersimpan masih kosong"+RESET)
        print(GREEN+"kembali ke menu utama..\n"+RESET)
        return

    print(GREEN+"\nmencari daftar kalimat.."+RESET)
    print(GREEN+"menampilkan daftar kalimat tersimpan..\n"+RESET)

    print(GREEN+"-"*19+"+"+"-"*30+RESET)
    print(GREEN+f"{'judul'.center(19)}|{'kalimat'.center(30)}"+RESET)
    print(GREEN+"-"*19+"+"+"-"*30+RESET)

    for key, item in daftar_kalimat.items():
        wrapped = textwrap.wrap(item, width=30)
        print(GREEN + f"{key.center(19)}| {wrapped[0].ljust(29)}" + RESET)
        for line in wrapped[1:]:
            print(GREEN + f"{' '.center(19)}| {line.ljust(29)}" + RESET)
        print(GREEN+"-"*19+"+"+"-"*30+RESET)
    print(GREEN+"kembali ke menu utama..\n"+RESET)

def frekuensi_kata():
    judul("ANALISA FREKUENSI")

    while True:
        judul_kalimat = input(CYAN+"\nmasukkan judul kalimat yang mau dianalisa: "+RESET).lower().strip()
        if not judul_kalimat:
            print(RED+"ERROR: judul kalimat tidak boleh kosong!!"+RESET)

        elif judul_kalimat not in daftar_kalimat:
            print(RED+"ERROR: judul kalimat tidak ditemukan"+RESET)

        else:
            print(GREEN+f"menganalisa kalimat dengan judul {judul_kalimat}..\n"+RESET)
            break

    kalimat_digunakan = daftar_kalimat[judul_kalimat]

    tanda_penting = (",",".","!","?",";",":","'",'"')
    for t in tanda_penting:
        kalimat_digunakan = kalimat_digunakan.replace(t,"")

    list_kata = kalimat_digunakan.split()
    frekuensi = {}

    for kata in list_kata:
        if kata in frekuensi:
            frekuensi[kata] += 1
        else:
            frekuensi[kata] = 1

    print(GREEN+"\nFrekuensi Kata:"+RESET)
    print(GREEN+"-"*30+RESET)
    for kata, jumlah in frekuensi.items():
        print(f"{GREEN}{kata.ljust(20)}{RESET}:{YELLOW}{str(jumlah).center(10)}{RESET}")
    print(GREEN+"-"*30+RESET)
    print(GREEN+f"Total kata unik: {len(frekuensi)}\n"+RESET)

while True:
    judul("PROGRAM ANALISA FREKUENSI KATA")

    for i, item in enumerate(daftar_fungsi, start=1):
        print(f"{MAGENTA}[{i}]{RESET} {item}")
    
    while True:
        fungsi = input(CYAN+"\nmasukkan pilihan fungsi: "+RESET).lower().strip()
        if not fungsi:
            print(RED+"ERROR: fungsi tidak boleh kosong"+RESET)

        elif fungsi not in daftar_fungsi:
            print(RED+"ERROR: fungsi tidak valid"+RESET)

        else:
            break

    if fungsi == "input":
        print(GREEN+"memasuki mennu input..\n"+RESET)
        input_kalimat()

    elif fungsi == "tampilkan":
        print(GREEN+"memasuki menu tampilkan daftar..\n"+RESET)
        tampilkan()

    elif fungsi == "analisa":
        print(GREEN+"memasuki menu analisa..\n"+RESET)
        frekuensi_kata()

    elif fungsi == "quit":
        print(RED+"mematikan program.."+RESET)
        break