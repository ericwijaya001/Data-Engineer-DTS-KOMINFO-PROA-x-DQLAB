# Dalam sub bab sebelumnya telah mempelajari bagaimana melakukan slicing/filtering dataset dengan menggunakan method .loc pada kolom dataset.

# Sekarang, menerapkan berdasarkan index. Tentu syaratnya adalah dataset sudah dilakukan indexing terlebih dahulu melalui penerapan method .set_index 

 

# Cara 1: Gunakan method .loc seperti yang dicontohkan berikut:



# Output cara 1:



 

# Cara 2: Gunakan pd.IndexSlice sebagai varaibel untuk melakukan slicing index



# Output cara 2:



 

# Tugas praktek:

# Pada code editor dapat terlihat kode-kode yang tidak lengkap. Tugas kamu adalah mengganti tanda _ _ _ di code editor dengan yang sesuai.  

# Baca kembali file TSV "sample_csv.csv" dan set terlebih dahulu indexnya yaitu order_date, order_id, dan product_id. Kemudian slice/filter-lah dataset jika order_date adalah 2019-01-01, order_id adalah 1612339 dan product_id-nya yaitu P2154 dan P2159. Gunakanlah cara pertama.

# Notes :

# Dataset :  https://storage.googleapis.com/dqlab-dataset/sample_csv.csv

# Jika berhasil dijalankan kodenya maka akan tampil hasil berikut:




import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Set index dari df sesuai instruksi
df = df.set_index(["order_date","order_id","product_id"])
# Slice sesuai intruksi
df_slice = df.loc[("2019-01-01",1612339,["P2154","P2159"]),:]
print("Slice df:\n", df_slice)