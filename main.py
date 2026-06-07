# TAHAP 4: EXTRACT METHOD (MODULAR & CLEAN CODE)
DISKON_GOLD = 0.10
DISKON_SILVER = 0.05

def hitung_subtotal(daftar_barang):
    """Menghitung total harga sebelum diskon."""
    subtotal = 0
    for barang in daftar_barang:
        subtotal += barang['harga'] * barang['jumlah']
    return subtotal

def hitung_diskon(subtotal, tipe_member):
    """Menghitung potongan harga berdasarkan tipe keanggotaan."""
    if tipe_member.upper() == "GOLD":
        return subtotal * DISKON_GOLD
    if tipe_member.upper() == "SILVER":
        return subtotal * DISKON_SILVER
    return 0.0

def cetak_struk(daftar_barang, subtotal, diskon, total_akhir):
    """Menampilkan struk belanja yang rapi ke konsol."""
    print("\n" + "="*21)
    print("    STRUK BELANJA    ")
    print("="*21)
    for barang in daftar_barang:
        total_item = barang['harga'] * barang['jumlah']
        print(f"{barang['nama']:<10} x{barang['jumlah']}: Rp{total_item:,}")
    print("-"*21)
    print(f"Subtotal   : Rp{subtotal:,}")
    print(f"Diskon     : Rp{diskon:,}")
    print(f"Total Akhir: Rp{total_akhir:,}")
    print("="*21)

def proses_transaksi(daftar_barang, tipe_member):
    """Fungsi utama untuk mengontrol alur eksekusi transaksi."""
    subtotal = hitung_subtotal(daftar_barang)
    diskon = hitung_diskon(subtotal, tipe_member)
    total_akhir = subtotal - diskon
    
    cetak_struk(daftar_barang, subtotal, diskon, total_akhir)
    return total_akhir

if __name__ == "__main__":
    item_belanja = [
        {'nama': 'Laptop', 'harga': 10000000, 'jumlah': 1},
        {'nama': 'Mouse', 'harga': 200000, 'jumlah': 2}
    ]
    proses_transaksi(item_belanja, "GOLD")