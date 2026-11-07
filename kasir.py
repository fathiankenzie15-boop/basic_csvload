daftar_harga = {
    "kopi": 15000,
    "teh": 10000,
    "roti": 12000
}

def proses_transaksi(pesanan):
    total = 0
    for item, jumlah in pesanan.items():
        if item in daftar_harga:
            subtotal = daftar_harga[item] * jumlah
            total += subtotal
            print(f"{item} x{jumlah} = Rp{subtotal}")
    return total

pesanan_pelanggan = {
    "kopi": 2,
    "roti": 1,
    "teh": 1
}

total_bayar = proses_transaksi(pesanan_pelanggan)
print(f"Total belanja: Rp{total_bayar}")