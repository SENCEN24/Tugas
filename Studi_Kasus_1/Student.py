"""
Class Student merupakan turunan dari Person.
"""

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
        DIMANA KONDISINYA JIKA averageMark KURANG DARI 50 DIA TIDAK BISA MEMILIH MATAKULIAH
        """
        if self.averageMark >= 50:
            return f"{self.name} boleh mengambil mata kuliah {matakuliah}"

        # return self.averageMark >= 50

    def getSeminarsTaken(self, seminar):
        """
        KODISI DIMANA STUDENT MEMILIH SEMINAR ATAU TIDAK
        """
        if seminar == "ya":
            return f"{self.name} Mengikuti Seminar"
        else:
            return f"{self.name} Tidak Mengikuti Seminar"


# mhs = Student("Budi", "08123", "budi@gmail.com", 101, 45)
# seminar = input("Apakah Kamu Ikut Seminya [ya/tidak] : ").lower()

# # Output sederhana
# print(mhs.getSeminarsTaken(seminar))
