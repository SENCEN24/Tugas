1. Struktur File
   project-folder
      - main.py
      - Address.py
      - Person.py
      - Student.py
      - Professor.py
      - README.md
2. Struktur relasi
      - Person  class induk
         - memiliki atribut dasar : name, phoneNumber, emailAddress, dan address
      - Student(Person) class turunan
         - menambah atribut : studentNumber, averageMark
         - memiliki method : isEligibleToEnroll(), getSeminarsTaken()
      - Professor(Person) class turunan
         - menambah atribut: salary, staffNumber, yearsOfService, numberOfClasses
      - Address class sendiiri yang digunakan oleh Person untuk mengambil alamat professor dan juga student

Program menerima input dari user, memvalidasi data tertentu seperti nilai yang bertipe integer/int, dan menghasilkan output berupa informasi studen dan juga professor.

3. Alur Program 
      1. Program di Jalankan dengan main.py
      2. User mengisi alamat mahasiswa
      3. User megisi data mahasiswa
      4. Program mengecek apakah boleh ambil mata kuliah
      5. User memilih ikut seminar atau tidak
      6. User mengisi alamat dosen
      7. User mengisi data dosen
      8. Program menampilkan output lengkap:
         - data mahasiswa  
         - data dosen  
         - mata kuliah  
         - seminar    
         - status parkir  



3. Contoh Output Program
      =============== OUTPUT ===============
      ======================================
                  DATA MAHASISWA
      ======================================
      Nama Mahasiswa   : Astawa
      NIM              : 101
      Alamat           : Jln. Subita, Denpasar Timur, Bali, 67811, Indonesia
      Nilai Rata-rata  : 80
      Mata Kuliah      : OOP
      Status Matkul    : Astawa boleh mengambil mata kuliah OOP
      Seminar          : Astawa Mengikuti Seminar
      --------------------------------------
                     DATA DOSEN
      --------------------------------------
      Nama Dosen       : PUTU
      NIP              : 2002
      Alamat           : Jln. Pulau Kawe, Denpasar Selatan, Bali, 123456, Indonesia
      HP               : 08222
      Email            : putu@kampus.ac.id
      Gaji             : 10000000
      Lama Kerja       : 5
      Nomer Kelas      : 2
      --------------------------------------
      Status Parkir    : Astawa Membeli Tiket Parkir
      Status Parkir    : PUTU Membeli Tiket Parkir
      ======================================

4. prompt ai dan respon (untuk prom lengkapnya ada di file prompt_respon_ai.md )
   1. Baguskan outputnya
      respon :    print("\n========== OUTPUT ==========")
                  print("======================================")
                  print("             DATA MAHASISWA           ")
                  print("======================================")
                  print(f"Nama Mahasiswa   : {mhs.name}")
                  print(f"NIM              : {mhs.studentNumber}")
                  print(f"Alamat           : {mhs.address.outputAsLabel()}")
                  print(f"Nilai Rata-rata  : {mhs.averageMark}")

                  # Mata kuliah
                  mk = "OOP"
                  status_matkul = mhs.isEligibleToEnroll(mk)
                  print(f"Mata Kuliah      : {mk}")
                  print(f"Status Matkul    : {status_matkul}")

                  # Seminar
                  seminar_status = mhs.getSeminarsTaken("ya")
                  print(f"Seminar          : {seminar_status}")

                  print("--------------------------------------")
                  print("               DATA DOSEN             ")
                  print("--------------------------------------")
                  print(f"Nama Dosen       : {dosen.name}")
                  print(f"NIP              : {dosen.staffNumber}")
                  print(f"Gaji             : {dosen.salary}")

                  print("--------------------------------------")
                  print(f"Status Parkir    : {dosen.purchaseParkingPass()}")
                  print("======================================")
                  print(f"Kode Pos         : {alamat.postalCode}")
                  print("======================================")
   2. kenapa Error seperti ini
      respon : seminar = (input("Apakah Kamu Ikut Seminya [ya/tidak] : ").lower(),)
               Perhatikan:
               Kamu tidak menyimpan string "ya" atau "tidak", tapi kamu membuat TUPLE karena ada koma di belakang.
   3. JELASKAN ERRORNYA DAN BAGAIMANA CARA SAYA MENGATASINYA
      respon : 
               TypeError: Student.__init__() got an unexpected keyword argument 'alamat'
               Artinya: constructor ( init ) di class Student tidak memiliki parameter bernama alamat, tetapi Anda mengirimkan parameter itu di bagian:

               python
               Salin kode
               mhs = Student(
                  name=...,
                  phoneNumber=...,
                  emailAddress=...,
                  studentNumber=...,
                  averageMark=...,
                  alamat=alamat,   # ← ERROR di sini
               )
               Padahal definisi Student Anda adalah:

               python
               Salin kode
               class Student(Person):
                  def __init__(
                     self, name, phoneNumber, emailAddress, studentNumber, averageMark, address=None
                  ):
                     Person.__init__(self, name, phoneNumber, emailAddress, address)
                     self.studentNumber = studentNumber
                     self.averageMark = averageMark