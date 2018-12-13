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