/*
Menggabungkan kolom tr_penjualan dan ms_produk menggunakan INNER JOIN

Dari tabel tr_penjualan:
1. kode_transaksi
2. kode_pelanggan
3. no_urut
4. kode_produk
5. nama_produk
6. qty
Dari tabel ms_produk
1. nama_produk
2. harga
Dari tabel ms_pelanggan:
1. no_urut
2. kode_pelanggan
3. nama_customer
4. alamat  

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


/*
TUGAS II:
- Tampilkan data-data pelanggan (kode_pelanggan, nama_customer, alamat) yang membeli produk Kotak Pensil DQLab, Flashdisk DQLab 32 GB, dan Sticky Notes DQLab 500 sheets
*/
SELECT DISTINCT ms_pelanggan.kode_pelanggan, ms_pelanggan.nama_customer, ms_pelanggan.alamat 
FROM ms_pelanggan
INNER JOIN tr_penjualan
ON ms_pelanggan.kode_pelanggan = tr_penjualan.kode_pelanggan
WHERE tr_penjualan.nama_produk = 'Kotak Pensil DQLab' 
  OR tr_penjualan.nama_produk = 'Flashdisk DQLab 32 GB' 
  OR tr_penjualan.nama_produk = 'Sticky Notes DQLab 500 sheets';
