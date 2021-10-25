# Matriks Perkalian

bil_satu = [
    [8, 0],
    [4, 6],
]

bil_dua = [
    [4, 2],
    [4, 2],
]

bil_tiga = []

for x in range(0, len(bil_satu)):
    row = []
    for y in range(0, len(bil_satu[0])):
        total = 0
        for z in range(0, len(bil_satu)):
            total = total + (bil_satu[x][z] * bil_dua[z][y])
        row.append(total)
    bil_tiga.append(row)


print("-" * 17)
print("Matriks Perkalian")
print("-" * 17)
for x in range(0, len(bil_tiga)):
    for y in range(0, len(bil_tiga[0])):
        print (bil_tiga[x][y], end=' ')
    print ()
print("-" * 17)



# Matriks Penjumlahan

def cetak_matriks(matriks):
 for row in matriks:
  print (row)

def panjang_matriks(matriks):
 return len(matriks[0])

def lebar_matriks(matriks):
 return len(matriks)

def hitung_matriks(mat_a, mat_b):
 temp_row = []
 temp_mat = []

 for i in range(0, lebar_matriks(mat_a)):
  for j in range(0, panjang_matriks(mat_a)):
   temp_row.append(mat_a[i][j] + mat_b[i][j])
  temp_mat.append(temp_row)
  temp_row = []
 return temp_mat

matriks_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriks_b = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
jumlah = hitung_matriks(matriks_a, matriks_b)

print("-" * 21)
print("Penjumlahan Matriks")
print("-" * 21)

for a in range(0, len(jumlah)):
    for b in range(0, len(jumlah[0])):
        print (jumlah[a][b], end=' ')
    print ()

