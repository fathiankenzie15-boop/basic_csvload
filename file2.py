with open('catatan.txt','w') as berkas:
    berkas.write('ini ditulis menggunakan pernyataan with\n')
    # Berkas otomatis tertutup setelah blok with selesai 
    berkas.write('ini tulisan yang kedua')
    #berkas otomatis tertutup setelah blok with selesai