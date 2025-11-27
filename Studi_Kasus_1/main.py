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

    print("\n========== ALAMAT ==========")
    alamatMhs = Address(
        street=str(input("masukan Street      : ")),
        city=str(input("masukan City        : ")),
        state=str(input("masukan State       : ")),
        postalCode=pesanint("masukan Postal Code : "),
        country=str(input("masukan Country     : ")),
    )
    print("======================================")

    print("\n========== MAHASISWA ==========")
    mhs = Student(
        name=str(input("Masukan Nama Kamu       : ")),
        phoneNumber=str(input("Masukan Nomer Tlpn Kamu : ")),
        emailAddress=str(input("Masukan Email Kamu      : ")),
        studentNumber=pesanint("Masukan NIM Kamu        : "),
        averageMark=pesanint("Masukan Nilai Kamu      : "),
        address=alamatMhs,
    )
    print("======================================")

    print("\n========== MATAKULIAH ==========")
    if mhs.averageMark < 50:
        print(f"{mhs.name} TIDAK boleh mengambil mata kuliah")
    else:
        mk = input("Silahkan Mengambil Matakuliah : ")
        print("Eligible daftar matkul :", mhs.isEligibleToEnroll(mk))
    print("======================================")

    print("\n========== SEMINAR ==========")
    seminar = input("Apakah Kamu Ikut Seminya [ya/tidak] : ").lower()
    print("======================================")

    print("\n========== ALAMAT DOSEN ==========")
    alamatDs = Address(
        street=str(input("masukan Street      : ")),
        city=str(input("masukan City        : ")),
        state=str(input("masukan State       : ")),
        postalCode=pesanint("masukan Postal Code : "),
        country=str(input("masukan Country     : ")),
    )
    print("======================================")

    print("\n========== DOSEN/PROFESSOR ==========")
    dosen = Professor(
        name=str(input("Masukan Nama Dosen          : ")),
        phoneNumber=str(input("Masukan Nomer Tlpn Dosen    : ")),
        emailAddress=str(input("Masukan Email Dosen         : ")),
        salary=pesanint("Masukan Gaji Dosen          : "),
        staffNumber=pesanint("Masukan NIP Dosen           : "),
        yearsOfService=pesanint("Masukan Lama Berkerja Dosen : "),
        numberOfClasses=pesanint("Masukan Nomer Kelas Dosen   : "),
        address=alamatDs,
    )
    print("======================================")

    # alamatMhs = Address("Jln. Subita", "Denpasar Timur", "Bali", 67811, "Indonesia")
    # mhs = Student("Astawa", "08123", "astawa@gmail.com", 101, 80, alamatMhs)
    # mk = "OOP"
    # seminar = "ya"
    # alamatDs = Address(
    #     "Jln. Pulau Kawe", "Denpasar Selatan", "Bali", 123456, "Indonesia"
    # )
    # dosen = Professor(
    #     "PUTU", "08222", "putu@kampus.ac.id", 10000000, 2002, 5, 2, alamatDs
    # )

    # Output sederhana
    print("\n=============== OUTPUT ===============")

    print("======================================")
    print("             DATA MAHASISWA           ")
    print("======================================")
    print(f"Nama Mahasiswa   : {mhs.name}")
    print(f"NIM              : {mhs.studentNumber}")
    print(f"Alamat           : {mhs.address.outputAsLabel()}")
    print(f"Nilai Rata-rata  : {mhs.averageMark}")
    # Mata kuliah
    print(f"Mata Kuliah      : {mk}")
    print(f"Status Matkul    : {mhs.isEligibleToEnroll(mk)}")
    # Seminar
    print(f"Seminar          : {mhs.getSeminarsTaken(seminar)}")

    print("--------------------------------------")
    print("               DATA DOSEN             ")
    print("--------------------------------------")
    print(f"Nama Dosen       : {dosen.name}")
    print(f"NIP              : {dosen.staffNumber}")
    print(f"Alamat           : {dosen.address.outputAsLabel()}")
    print(f"HP               : {dosen.phoneNumber}")
    print(f"Email            : {dosen.emailAddress}")
    print(f"Gaji             : {dosen.salary}")
    print(f"Lama Kerja       : {dosen.yearsOfService}")
    print(f"Nomer Kelas      : {dosen.numberOfClasses}")
    print("--------------------------------------")
    print(f"Status Parkir    : {mhs.purchaseParkingPass()}")
    print(f"Status Parkir    : {dosen.purchaseParkingPass()}")
    print("======================================")


if __name__ == "__main__":
    main()
