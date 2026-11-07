try:
    with open('data_tidak_ada.txt', 'w') as berkas:
        print('berkas'.read())
except FileNotFoundError:
     print('Berkas tidak ditemukan, periksa kembali')