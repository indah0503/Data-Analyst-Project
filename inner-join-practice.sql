/*
Menggabungkan kolom tr_penjualan dan ms_produk menggunakan INNER JOIN

Dari tabel tr_penjualan:
1. kode_transaksi
2. kode_pelanggan
3. kode_produk
4. qty
Dari tabel ms_produk
1. nama_produk
2. harga.

TUGAS:
- Tampilkan tabel dengan urutan kolom adalah kode_transaksi, kode_pelanggan, kode_produk, nama_produk, harga, qty, dan total
*/

SELECT tr_penjualan.kode_transaksi, 
  tr_penjualan.kode_pelanggan, 
  tr_penjualan.kode_produk, 
  ms_produk.nama_produk, 
  ms_produk.harga, 
  tr_penjualan.qty, 
  (ms_produk.harga * tr_penjualan.qty) AS total
FROM tr_penjualan
INNER JOIN ms_produk
ON tr_penjualan.kode_produk = ms_produk.kode_produk;
