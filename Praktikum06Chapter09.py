nilai = [{'nim' : 'A01', 'nama' : 'Agusina', 'mid' :50, 'uas': 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' :40, 'uas' :90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas':50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' :20, 'uas':100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' :70, 'uas': 100}]
print('=================================================')
print('NIM'.ljust(10), 'NAMA'.ljust(11), 'N.MID'.ljust(9), 'N.UAS'.ljust(9), 'N.AKHIR'.ljust(11), 'STATUS')
print('-------------------------------------------------')
 
for data in nilai:
    mid = str(data['mid'])
    uas = str(data['uas'])
    x = int((data['mid'] +2* (data['uas']))/3)
    hasil = str(x)
    if (x >= 60):
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'
    print(data['nim'].ljust(11), end='')
    print((data['nama'].upper()), end='')
    print(mid.rjust(6), uas.rjust(9), hasil.rjust(11), status.rjust(10))
print('-------------------------------------------------')
