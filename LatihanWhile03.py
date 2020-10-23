#Program untuk menampilkan bilangan bulat 0 - 100 yang ganjil

i = 1
jml = 0
sum = 0

while(i <= 100) :
    print(str(i) + '\n')
    i = i + 2
    jml = jml + 1
    sum = sum + i

print('Banyaknya Bilangan Ganjil : ' + str(jml))
print('Hasil Penjumlahannya adalah : ' + str(sum))
