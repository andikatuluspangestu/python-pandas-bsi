# Praktikum 7

# Import Module Library
import pandas as pd

# Deklarasi Variable
list_nim    = []
list_nama   = []
list_uts    = []
list_uas    = []
list_total  = []

ulang = 3
for i in range(ulang):
    print("Data ke - ", i + 1)
    list_nim.append(input(" NIM         : "))
    list_nama.append(input(" Nama        : "))
    list_uts.append(int(input(" Nilai UTS   : ")))
    list_uas.append(int(input(" Nilai UAS   : ")))

# Proses
for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)

tamu = {
    "NIM"          : list_nim,
    "Nama Lengkap" : list_nama,
    "Nilai UTS"    : list_uts,
    "Nilai UAS"    : list_uas,
    "Rata-rata"    : list_total
}

data_tamu = pd.DataFrame(tamu)

print("=" * 60)
print(data_tamu)
print("=" * 60)




