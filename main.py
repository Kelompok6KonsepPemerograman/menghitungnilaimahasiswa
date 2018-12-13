print("Selamat Datang Di Aplikasi penghitungan Nilai Mahasiswa")
print("Kelompok 6 Konsep Pemograman")

nama_Mahasiswa = str(input("nama_Mahasiswa  : "))
nim_Mahasiswa = int(input("nim_Mahasiswa 	: "))
nilai_keaktifan = int(input("nilai_keaktifan	: "))
nilai_tugas = int(input("nilai_tugas 	: "))
nilai_uts = int(input("nilai_uts 	: "))
nilai_uas = int(input("nilai_uas	: "))


nilai = nilai_keaktifan + nilai_tugas + nilai_uts + nilai_uas
rata_rata = nilai/4
print(("rata_rata : "), rata_rata)
print("jumlah nilai keseluruhan : ",(nilai))
print("nilai huruf : ")

if rata_rata >= 80 :
	print ("A")
elif rata_rata >= 70 :
	print ("B")
elif rata_rata >= 55 :
	print ("C")
elif rata_rata >= 40 :
	print ("D")
elif rata_rata <= 39 :
	print ("E")
if rata_rata <= 50 :
	print ("keterangan : tidak lulus")
else :
	print ("keterangan : lulus")

def meyimpan_biodata(nama_Mahasiswa,nim_mahasiswa,nilai_keaktifan,nilai_tugas,nilai_uts,nilai_uas,nilai_rata_rata,jumlah_nilai_keseluruhan,nilai_huruf,keterangan):
	file = open("database.txt","a+")
	data = file.write("nama_Mahasiswa: %s \n"% (nama_Mahasiswa))
	data = file.write("nim_mahasiswa :%s \n"% (nim_mahasiswa))
	data = file.write("nilai_keaktifan: %s \n"% (nilai_keaktifan))
	data = file.write("nilai_tugas: %s \n"% (nilai_tugas))
	data = file.write("nilai_uts: %s \n"% (nilai_uts))
	data = file.write("nilai_uas: %s \n"% (nilai_uas))
	data = file.write("nilai_rata_rata: %s \n"% (nilai_rata_rata))
	data = file.write("jumlah_nilai_keseluruhan: %s \n"% (jumlah_nilai_keseluruhan))
	data = file.write("nilai_huruf: %s \n"% (nilai_huruf))
	data = file.write("keterangan: %s \n"% (keterangan))
def tampilkan_semua_biodata():
	file = open("database.txt","r")
	print(file.read())
