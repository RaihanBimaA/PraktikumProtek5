scoresalah = 0

print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')

tebakan = int(input('Tebakan Anda : '))

while True :
    if(tebakan < 10) :
        print('Hehehe… Bilangan tebakan anda terlalu kecil')
        scoresalah += 2
        tebakan = int(input('Tebakan Anda : '))
        
    elif(tebakan > 10):
        print('Hehehe… Bilangan tebakan anda terlalu besar')
        scoresalah += 2
        tebakan = int(input('Tebakan Anda : '))

    elif(tebakan == 10):
        scoreAkhir = 100 - scoresalah
        print('Yeeee… Bilangan tebakan anda BENAR :-)')
        print('Score Anda : ' + str(scoreAkhir))
        break
