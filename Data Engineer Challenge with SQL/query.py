# Mengacu pada table ms_produk, tampilkan daftar produk yang memiliki harga antara 50.000 and 150.000.
# Nama kolom yang harus ditampilkan: no_urut, kode_produk, nama_produk, dan harga.
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.

select no_urut, kode_produk, nama_produk, harga from ms_produk where harga between 50000 and 150000





# Thumb drive di DQLab Mart
# Tampilkan semua produk yang mengandung kata Flashdisk.
# Nama kolom yang harus ditampilkan: no_urut, kode_produk, nama_produk, dan harga.
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.

select no_urut, kode_produk, nama_produk, harga from ms_produk where nama_produk like '%Flashdisk%'





# Pelanggan Bergelar
# Tampilkan hanya nama-nama pelanggan yang hanya memiliki gelar-gelar berikut: S.H, Ir. dan Drs.
# Nama kolom yang harus ditampilkan: no_urut, kode_pelanggan, nama_pelanggan, dan alamat.
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.

select no_urut, kode_pelanggan, nama_pelanggan, alamat from ms_pelanggan where 
nama_pelanggan like '%S.H%' or nama_pelanggan like '%Ir.%' or nama_pelanggan like '%Drs.%'






# Mengurutkan Nama Pelanggan
# Tampilkan nama-nama pelanggan dan urutkan hasilnya berdasarkan kolom nama_pelanggan dari yang terkecil ke yang terbesar (A ke Z).
# Nama kolom yang harus ditampilkan: nama_pelanggan.
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.

select nama_pelanggan from ms_pelanggan order by nama_pelanggan






# Mengurutkan Nama Pelanggan Tanpa Gelar
# Tampilkan nama-nama pelanggan dan urutkan hasilnya berdasarkan kolom nama_pelanggan dari yang terkecil ke yang terbesar (A ke Z), namun gelar tidak boleh menjadi bagian dari urutan. Contoh: Ir. Agus Nugraha harus berada di atas Heidi Goh.
# Nama kolom yang harus ditampilkan: nama_pelanggan.
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.
# https://www.geeksforgeeks.org/substring_index-function-in-mysql/

select nama_pelanggan from ms_pelanggan  order by substring_index(nama_pelanggan, '. ', -1)






# Nama Pelanggan yang Paling Panjang
# Tampilkan nama pelanggan yang memiliki nama paling panjang. Jika ada lebih dari 1 orang yang memiliki panjang nama yang sama, tampilkan semuanya.
# Nama kolom yang harus ditampilkan: nama_pelanggan.
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.

select nama_pelanggan from ms_pelanggan having length(nama_pelanggan) = (select max(length(nama_pelanggan)) from ms_pelanggan)





# Nama Pelanggan yang Paling Panjang dengan Gelar
# Tampilkan nama orang yang memiliki nama paling panjang (pada row atas), dan nama orang paling pendek (pada row setelahnya). Gelar menjadi bagian dari nama. Jika ada lebih dari satu nama yang paling panjang atau paling pendek, harus ditampilkan semuanya.
# Nama kolom yang harus ditampilkan: nama_pelanggan.
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.

select nama_pelanggan from ms_pelanggan where length(nama_pelanggan) = (select max(length(nama_pelanggan)) from ms_pelanggan) 
or length(nama_pelanggan) = (select min(length(nama_pelanggan)) from ms_pelanggan) order by length(nama_pelanggan) desc





# Kuantitas Produk yang Banyak Terjual
# Tampilkan produk yang paling banyak terjual dari segi kuantitas. Jika ada lebih dari 1 produk dengan nilai yang sama, tampilkan semua produk tersebut.
# Nama kolom yang harus ditampilkan: kode_produk, nama_produk,total_qty.
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.

select mp.kode_produk,mp.nama_produk, sum(tpd.qty) total_qty from ms_produk mp join tr_penjualan_detail tpd 
on mp.kode_produk=tpd.kode_produk group by kode_produk, nama_produk having total_qty=7
ATAU 
select mp.kode_produk,mp.nama_produk, sum(tpd.qty) total_qty from ms_produk mp join tr_penjualan_detail tpd 
on mp.kode_produk=tpd.kode_produk group by kode_produk, nama_produk having total_qty=(select sum(tpd.qty) total_qty from tr_penjualan_detail tpd join ms_produk mp on tpd.kode_produk=mp.kode_produk group by tpd.kode_produk, mp.nama_produk order by total_qty desc limit 1)





# Pelanggan Paling Tinggi Nilai Belanjanya
# Siapa saja pelanggan yang paling banyak menghabiskan uangnya untuk belanja? Jika ada lebih dari 1 pelanggan dengan nilai yang sama, tampilkan semua pelanggan tersebut.
# Nama kolom yang harus ditampilkan: kode_pelanggan, nama_pelanggan, total_harga.
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.

select mp.kode_pelanggan, mp.nama_pelanggan, sum(tpd.qty*tpd.harga_satuan) total_harga
from ms_pelanggan mp join tr_penjualan tp on mp.kode_pelanggan=tp.kode_pelanggan
join tr_penjualan_detail tpd on tp.kode_transaksi=tpd.kode_transaksi
group by kode_pelanggan, nama_pelanggan
order by total_harga desc limit 1






# Pelanggan yang Belum Pernah Berbelanja
# Tampilkan daftar pelanggan yang belum pernah melakukan transaksi.
# Nama kolom yang harus ditampilkan: kode_pelanggan, nama_pelanggan, alamat.
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.

select kode_pelanggan, nama_pelanggan, alamat from ms_pelanggan 
where kode_pelanggan not in (select kode_pelanggan from tr_penjualan)






# Transaksi Belanja dengan Daftar Belanja lebih dari 1
# Tampilkan transaksi-transaksi yang memiliki jumlah item produk lebih dari 1 jenis produk. Dengan lain kalimat, tampilkan transaksi-transaksi yang memiliki jumlah baris data pada table tr_penjualan_detail lebih dari satu.
# Nama kolom yang harus ditampilkan:  kode_transaksi, kode_pelanggan, nama_pelanggan, tanggal_transaksi, jumlah_detail
# Semua table di atas sudah tersedia, Anda tinggal menulis query Anda dalam Code Editor.

select tp.kode_transaksi, mp.kode_pelanggan, mp.nama_pelanggan, tp.tanggal_transaksi, count(tpd.qty) jumlah_detail
from ms_pelanggan mp join tr_penjualan tp on mp.kode_pelanggan=tp.kode_pelanggan
join tr_penjualan_detail tpd on tp.kode_transaksi=tpd.kode_transaksi
group by tpd.kode_transaksi, tp.kode_pelanggan,
mp.nama_pelanggan, tp.tanggal_transaksi
having jumlah_detail>1