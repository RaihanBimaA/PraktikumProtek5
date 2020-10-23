#program menentukan kelulusan
indo=int(input('Masukan nilai Bhs Indonesia:'))
if(indo>=0 and indo<=100):
    ipa=int(input('masukan nilai IPA:'))
if(ipa>=0 and ipa<=100):
    mtk=int(input('masukan nilai mtk:'))
if(mtk>=0 and mtk<=100):
    print('\n')
if(indo>=60 and ipa>=60 and mtk>70):
    print('Status Kelulusan: LULUS')
else:
    print('Status Kelulusan: TIDAK LULUS')
