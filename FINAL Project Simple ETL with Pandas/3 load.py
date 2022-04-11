Pada bagian load ini, data yang sudah ditransformasi sedemikian rupa sehingga sesuai dengan kebutuhan tim analyst dimasukkan kembali ke database yaitu Data Warehouse (DWH). Biasanya, dilakukan pendefinisian skema database terlebih dahulu seperti:

Nama kolom
Tipe kolom
Apakah primary key, unique key, index atau bukan
Panjang kolomnya
Karena umumnya Data Warehouse merupakan database yang terstruktur sehingga mereka memerlukan skema sebelum datanya dimasukkan.

Pandas sudah menyediakan fungsi untuk memasukkan data ke database yaitu to_sql().

Detail dari fungsi tersebut bisa dilihat pada dokumentasi Pandas: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html

