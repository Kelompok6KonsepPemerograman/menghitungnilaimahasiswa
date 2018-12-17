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
def option():
	print("lanjutkan untuk meyimpan data")
	print("1. menyimpan data")
	print("2. tampilkan data mahasiswa")
	print("3. keluar program penghitungan nilai mahasiswa")
	pilihan = int(input("masukkan pilihan anda : "))
	return pilihan
pilihan	=	true
while (pilihan<3):
	pilihan = option()
	if(pilihan==1):
		nama_Mahasiswa = str(input("masukkan nama_Mahasiswa : "))
		nim_mahasiswa = str(input("masukkan nim_mahasiswa : "))
		nilai_keaktifan= str(input("masukkan nilai_keaktifan : "))
		nilai_tugas= str(input("masukkan nilai_tugas: "))
		nilai_uts= str(input("masukkan nilai_uts : "))
		nilai_uas= str(input("masukkan nilai_uas : "))
		nilai_rata_rata= str(input("masukkn nilai_rata_rata : "))
		jumlah_nilai_keseluruhan= str(input("jumlah_nilai_keseluruhan : "))
		nilai_huruf= str(input("masukkan nilai_huruf : "))
		keterangan= str(input("masukkan keterangan : "))
		meyimpan_biodata(nama_Mahasiswa,nim_mahasiswa,nilai_keaktifan,nilai_tugas,nilai_uts,nilai_uas,nilai_rata_rata,jumlah_nilai_keseluruhan,nilai_huruf,keterangan)
	elif(pilihan==2):
		tampilkan_semua_biodata()