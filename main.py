DISKON_GOLD = 0.10
DISKON_SILVER = 0.05

def proses_transaksi(daftar_barang, tipe_member):
    subtotal = 0
    for barang in daftar_barang:
        subtotal += barang['harga'] * barang['jumlah']
    
    diskon = 0
    # Mengganti angka mentah dengan konstanta deskriptif
    if tipe_member == "GOLD":
        diskon = subtotal * DISKON_GOLD
    elif tipe_member == "SILVER":
        diskon = subtotal * DISKON_SILVER
    else:
        diskon = 0
        
    total_akhir = subtotal - diskon
    
    print("=== STRUK BELANJA ===")
    for barang in daftar_barang:
        print(f"{barang['nama']} x{barang['jumlah']}: {barang['harga'] * barang['jumlah']}")
    print(f"Subtotal: {subtotal}")
    print(f"Diskon: {diskon}")
    print(f"Total Akhir: {total_akhir}")
    print("=====================")
    return total_akhir

item_belanja = [{'nama': 'Laptop', 'harga': 10000000, 'jumlah': 1}, {'nama': 'Mouse', 'harga': 200000, 'jumlah': 2}]
proses_transaksi(item_belanja, "GOLD")