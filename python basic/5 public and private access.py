# Pada contoh di atas, terlihat bahwa atribut nama pada setiap objek dapat diakses secara bebas di luar scope dari sebuah class. Agar suatu properti ataupun fungsi dari sebuah class tidak dapat diakses secara bebas di luar scope milik suatu class, aku dapat mendefinisikan access modifier (level akses) saat sebuah atribut/fungsi didefinisikan.

# Terdapat 2 macam access modifier dalam Python, yakni.

# Public access: dapat aku definisikan dengan secara langsung menuliskan nama dari atribut/ fungsi. Dalam sebuah objek, atribut/fungsi yang bersifat public access dapat diakses di luar scope sebuah class
# Private access: dapat aku definisikan dengan menambahkan double underscore (__) sebelum menuliskan nama dari atribut/fungsi. Dalam sebuah objek, atribut/fungsi yang bersifat private access hanya dapat diakses di dalam scope sebuah class.

# Definisikan class Karyawan
class Karyawan: 
    nama_perusahaan = 'ABC' 
    __insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.__nama = nama
        self.__usia = usia 
        self.__pendapatan = pendapatan 
        self.__pendapatan_tambahan = 0
    def lembur(self):
        self.__pendapatan_tambahan += self.__insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.__pendapatan_tambahan +=insentif_proyek 
    def total_pendapatan(self):
        return self.__pendapatan + self.__pendapatan_tambahan
# Buat objek karyawan bernama Aksara
aksara = Karyawan('Aksara', 25, 8500000)
# Akses ke attribute class Karyawan
print(aksara.__class__.__nama)
# Akan menimbulkan error ketika di run
print(aksara.__nama)

# MEMANG BAKAL ERROR
# Traceback (most recent call last):
#   File "c:/Users/Eric/Documents/ONLINE COURSE CODE/DQLAB DTS KOMINFO/5.py", line 26, in <module>
#     print(aksara.__class__.__nama)
# AttributeError: type object 'Karyawan' has no attribute '__nama'