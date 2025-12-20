/*
Menggabungkan kolom tr_penjualan dan ms_produk menggunakan UNION

Dari tabel ms_produk_1 dan ms_produk_2
1. no_urut
2. kode_produk
3. nama_produk
4. harga 

TUGAS:
- Tampilkan hanya data produk dengan harga di bawah 100K untuk kode produk prod-1 sampai prod-5;
dan dibawah 50K untuk kode produk prod-6 sampai prod-10, tanpa mencantumkan kolom no_urut.
*/
SELECT kode_produk, nama_produk, harga 
FROM ms_produk_1
WHERE harga < 100000
UNION
SELECT kode_produk, nama_produk, harga 
FROM ms_produk_2
WHERE harga < 50000;
