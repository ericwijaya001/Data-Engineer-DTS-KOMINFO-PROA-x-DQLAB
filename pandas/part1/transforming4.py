# Di sub bab sebelumnya sudah mengetahui bahwa map hanya dapat digunakan untuk pandas series. Pada sub bab ini akan menggunakan method .applymap pada dataframe.

 

# Untuk itu perhatikan contoh berikut:



# Cara 1 dengan tanpa define function awalnya, langsung pake fungsi anonymous lambda x



# Cara 2 dengan define function



 

# Setelah dijalankan dengan menekan tombol  maka diperoleh output berikut di console.



# Cara 1 dan cara 2 menunjukkan bahwa keduanya menghasilkan dataframe yang sama.

 

# Tugas Praktek:

# Dengan cara yang sama seperti diatas buatlah matriks random ukuran 3 x 4 dengan seed random-nya 1234. Kemudian gunakan kedua cara seperti di atas untuk merubah seluruh isi dengan fungsi kuadrat x**2 + 3*x + 2.

# Jika kode dengan benar ditulis dan kemudian dijalankan dengan menekan tombol  diperoleh output berikut:


import numpy as np
import pandas as pd
# number generator, set angka seed menjadi suatu angka, bisa semua angka, supaya hasil random nya selalu sama ketika kita run
np.random.seed(1234)
# create dataframe 3 baris dan 4 kolom dengan angka random
df_tr = pd.DataFrame(np.random.rand(3,4)) 
# Cetak dataframe
print("Dataframe:\n", df_tr)
# Cara 1 dengan tanpa define function awalnya, langsung pake fungsi anonymous lambda x
df_tr1 = df_tr.applymap(lambda x: x**2+3*x+2) 
print("\nDataframe - cara 1:\n", df_tr1)
# Cara 2 dengan define function 
def qudratic_fun(x):
	return x**2+3*x+2
df_tr2 = df_tr.applymap(qudratic_fun)
print("\nDataframe - cara 2:\n", df_tr2)