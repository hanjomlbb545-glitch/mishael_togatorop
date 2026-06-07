def proses_transaksi(DaftarBarang, tipe_member):
    t = 0
    for b in DaftarBarang:
        t += b['harga'] * b['jumlah']
    
    d = 0
    if tipe_member == "GOLD":
        d = t * 0.1
    elif tipe_member == "SILVER":
        d = t * 0.05
    else:
        d = 0
        
    TotalAkhir = t - d
    
    print("=== STRUK BELANJA ===")
    for b in DaftarBarang:
        print(f"{b['nama']} x{b['jumlah']}: {b['harga'] * b['jumlah']}")
    print(f"Subtotal: {t}")
    print(f"Diskon: {d}")
    print(f"Total Akhir: {TotalAkhir}")
    print("=====================")
    return TotalAkhir

item_belanja = [{'nama': 'Laptop', 'harga': 10000000, 'jumlah': 1}, {'nama': 'Mouse', 'harga': 200000, 'jumlah': 2}]
proses_transaksi(item_belanja, "GOLD")