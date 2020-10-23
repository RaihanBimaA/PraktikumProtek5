#program menentukan kelulusan
indo=int(input('Masukan nilai Bhs Indonesia:'))
ipa=int(input('masukan nilai IPA:'))
mtk=int(input('masukan nilai mtk:'))
print('\n')

if(indo<=0 or indo>=100):
    print('Maaf input ada yang tidak valid')
elif(ipa<=0 or ipa>=100):
    print('Maaf input ada yang tidak valid')
elif(mtk<=0 or mtk>=100):
    print('Maaf input ada yang tidak valid')
elif(indo>=60 and ipa>=60 and mtk>70):
    print('LULUS')
else:
    print('TIDAK LULUS')
    print('Sebab : ')
     
    if(indo < 60) :
         print('- Nilai Bahasa Indonesia kurang dari 60')
    if(ipa < 60) :
         print('- Nilai IPA kurang dari 60')
    if(mtk <= 70) :
         print('- Nilai Matematika kurang dari 70')
        
