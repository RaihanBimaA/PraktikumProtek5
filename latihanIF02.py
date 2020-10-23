#program menentukan kelulusan
indo=int(input('Masukan nilai Bhs Indonesia:'))
ipa=int(input('masukan nilai IPA:'))
mtk=int(input('masukan nilai mtk:'))
print('\n')

if(indo<0 or indo>100):
    print('Maaf input ada yang tidak valid')
elif(ipa<0 or ipa>100):
    print('Maaf input ada yang tidak valid')
elif(mtk<0 or mtk>100):
    print('Maaf input ada yang tidak valid')
    print('\n')
elif(indo>=60 and ipa>=60 and mtk>70):
    print('Status Kelulusan: LULUS')
else:
    print('Status Kelulusan: TIDAK LULUS')
