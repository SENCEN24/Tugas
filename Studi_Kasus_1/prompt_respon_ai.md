1. promt untuk membagus kan outputnya

        from Address import Address
        from Student import Student
        from Professor import Professor


        def pesanint(pesan):
            while True:
                try:
                    return int(input(pesan))
                except ValueError:
                    print("masukan angka tampa huruf ")


        def main():

            # Membuat objek Address
            print("\n========== ALAMAT ==========")
            alamat = Address("Jln. Subita", "Denpasar Selatan", "Bali", 67811, "Indonesia")
            # alamat = Address(
            #     street=str(input("masukan Street      : ")),
            #     city=str(input("masukan City        : ")),
            #     state=str(input("masukan State       : ")),
            #     postalCode=pesanint("masukan Postal Code : "),
            #     country=str(input("masukan Country     : ")),
            # )
            print("======================================")

            # Membuat mahasiswa
            print("\n========== MAHASISWA ==========")
            mhs = Student("Astawa", "08123", "astawa@gmail.com", 101, 80, alamat)
            # mhs = Student(
            #     name=str(input("Masukan Nama Kamu       : ")),
            #     phoneNumber=str(input("Masukan Nomer Tlpn Kamu : ")),
            #     emailAddress=str(input("Masukan Email Kamu      : ")),
            #     studentNumber=pesanint("Masukan NIM Kamu        : "),
            #     averageMark=pesanint("Masukan Nilai Kamu      : "),
            #     address=alamat,
            # )
            print("======================================")

            print("\n========== MATAKULIAH ==========")

            # if mhs.averageMark < 50:
            #     print(f"{mhs.name} TIDAK boleh mengambil mata kuliah")
            # else:
            #     mk = input("Silahkan Mengambil Matakuliah : ")
            #     print("Eligible daftar matkul :", mhs.isEligibleToEnroll(mk))
            print("======================================")

            print("\n========== DOSEN/PROFESSOR ==========")

            # Membuat dosen
            dosen = Professor(
                "PUTU", "08222", "putu@kampus.ac.id", 10000000, 2002, 5, 2, alamat
            )

            # dosen = Professor(
            #     name=str(input("Masukan Nama Dosen          : ")),
            #     phoneNumber=str(input("Masukan Nomer Tlpn Dosen    : ")),
            #     emailAddress=str(input("Masukan Email Dosen         : ")),
            #     salary=pesanint("Masukan Gaji Dosen          : "),
            #     staffNumber=pesanint("Masukan NIP Dosen           : "),
            #     yearsOfService=pesanint("Masukan Lama Berkerja Dosen : "),
            #     numberOfClasses=pesanint("Masukan Nomer Kelas Dosen   : "),
            # )
            print("======================================")

            print("\n========== SEMINAR ==========")
            # seminar = input("Apakah Kamu Ikut Seminya [ya/tidak] : ").lower()
            print("======================================")

            # Output sederhana

            print("\n========== OUTPUT ==========")
            print(f"Data Mahasiswa : Nama : {mhs.name}, NIM : {mhs.studentNumber}, Alamat : {mhs.address.outputAsLabel()}")
            # print(mhs.getSeminarsTaken(seminar))
            print(mhs.getSeminarsTaken("ya"))
            print("Nama Mahasiswa :", mhs.name)
            print("Eligible daftar matkul :", mhs.isEligibleToEnroll("OOP"))
            print("Alamat :", mhs.address.outputAsLabel())
            print(f"Pak {dosen.purchaseParkingPass()}")
            

            print(alamat.postalCode)
            print("======================================")


        if __name__ == "__main__":
            main()

        BUAT OUTPUTNYA AGAR BAGUS

2. menanyakan kenapa Error
            from Person import Person


            class Student(Person):
                def __init__(
                    self, name, phoneNumber, emailAddress, studentNumber, averageMark, address=None
                ):
                    Person.__init__(self, name, phoneNumber, emailAddress, address)
                    self.studentNumber = studentNumber
                    self.averageMark = averageMark

                def isEligibleToEnroll(self, matakuliah):
                    """
                    FUNGSI INI DI GUNAKAN UNTUK MENGECEK MAHASISWA MEMENUHI SYARAT ATAU TIDAK
                    averageMark
                    """
                    if self.averageMark >= 50:
                        return f"{self.name} boleh mengambil mata kuliah {matakuliah}"

                    # return self.averageMark >= 50

                def getSeminarsTaken(self, seminar):
                    if seminar == "ya":
                        return f"{self.name} Mengikuti Seminar"
                    else:
                        return f"{self.name} Tidak Mengikuti Seminar"


            mhs = Student("Budi", "08123", "budi@gmail.com", 101, 45)
            seminar = (input("Apakah Kamu Ikut Seminya [ya/tidak] : ").lower(),)

            # Output sederhana
            print(mhs.getSeminarsTaken(seminar))

            PS D:\TUGAS\Studi_Kasus_1> & C:\Users\NGURAH\AppData\Local\Programs\Python\Python314\python.exe d:/TUGAS/Studi_Kasus_1/Student.py
            Apakah Kamu Ikut Seminya [ya/tidak] : ya
            Budi Tidak Mengikuti Seminar
            PS D:\TUGAS\Studi_Kasus_1>  

            Kenapa Eror seperti itu dan bagaimana cara mengatasinya

3.  from Address import Address
    from Student import Student
    from Professor import Professor


    def postalCode(pesan):
        while True:
            try:
                return int(input(pesan))
            except ValueError:
                print("masukan postalCode tampa huruf ")


    def main():

        # Membuat objek Address
        print("\n========== ALAMAT ==========")
        alamat = Address(
            street=str(input("masukan Street      : ")),
            city=str(input("masukan City        : ")),
            state=str(input("masukan State       : ")),
            postalCode=postalCode("masukan Postal Code : "),
            country=str(input("masukan Country     : ")),
        )
        print("======================================")

        # Membuat mahasiswa
        # mhs = Student("Budi", "08123", "budi@gmail.com", 101, 45, alamat)
        print("\n========== MAHASISWA ==========")
        mhs = Student(
            name=str(input("Masukan Nama Kamu       : ")),
            phoneNumber=str(input("Masukan Nomer Tlpn Kamu : ")),
            emailAddress=str(input("Masukan Email Kamu      : ")),
            studentNumber=int(input("Masukan NIM Kamu        : ")),
            averageMark=int(input("Masukan Nilai Kamu      : ")),
            alamat=alamat,
        )
        print("======================================")

        # Membuat dosen
        dosen = Professor(
            "Pak Andi", "08222", "andi@kampus.ac.id", 10000000, 2002, 5, 2, alamat
        )

        if mhs.averageMark < 50:
            print(f"{mhs.name} TIDAK boleh mengambil mata kuliah")
        else:
            mk = input("Silahkan Mengambil Matakuliah : ")
            print("Eligible daftar matkul :", mhs.isEligibleToEnroll(mk))

        # Output sederhana
        print("Nama Mahasiswa :", mhs.name)
        # print("Eligible daftar matkul :", mhs.isEligibleToEnroll("OOP"))
        print("Alamat :", mhs.address.outputAsLabel())
        print(dosen.purchaseParkingPass())
        print(
            f"Data Mahasiswa : {mhs.name},{mhs.studentNumber}, {mhs.address.outputAsLabel()}"
        )

        print(alamat.postalCode)


    if __name__ == "__main__":
        main()

    PS D:\TUGAS\Studi_Kasus_1> & C:\Users\NGURAH\AppData\Local\Programs\Python\Python314\python.exe d:/TUGAS/Studi_Kasus_1/main.py

    ========== ALAMAT ==========
    masukan Street      : W
    masukan City        : W
    masukan State       : W
    masukan Postal Code : 2
    masukan Country     : W
    ======================================

    ========== MAHASISWA ==========
    Masukan Nama Kamu       : W
    Masukan Nomer Tlpn Kamu : W
    Masukan Email Kamu      : W
    Masukan NIM Kamu       : 09
    Masukan Nilai Kamu      : 45
    Traceback (most recent call last):
    File "d:\TUGAS\Studi_Kasus_1\main.py", line 64, in <module>
        main()
        ~~~~^^
    File "d:\TUGAS\Studi_Kasus_1\main.py", line 30, in main
        mhs = Student(
            name=str(input("Masukan Nama Kamu       : ")),
        ...<4 lines>...
            alamat=alamat,
        )
    TypeError: Student.__init__() got an unexpected keyword argument 'alamat'
    PS D:\TUGAS\Studi_Kasus_1> 

    JELASKAN ERRORNYA DAN BAGAIMANA CARA SAYA MENGATASINYA