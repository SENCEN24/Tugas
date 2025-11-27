# FILE PERSON


class Person:  # MEBUAT FUNGSI YANG BERNAMA PERSON
    def __init__(self, name, phoneNumber, emailAddress, address=None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.address = address
        """
         MENDESKRIPSIKAN OBJEK DAN PARAMETER YANG DIGUNAKA DALAM FUNGSI DI CLASS PERSON
         __init__ = FUNGSINYA UNTUK LANGSUNG MENJALANKAN DEF TAMPA DI DEKLASI LAGI
         self = OBJEK
         name = PARAMETER BERTIPE STR
         phoneNumber = PARAMETER BERTIPE STR
         emailAddress = PARAMETER BERTIPE STR
         address = PARAMETER BERTIPE YANG DIMANA DI GUNAKAN UNTUK MENGAMBIL NILAI ADDRESS PADA CLASS ADRRESNYA NILAI AWALNYA NONE ATAU NULL
         ------------------------------------------------------------------------------------------------------------------------------------
         self.name = name
         self.phoneNumber = phoneNumber
         self.emailAddress = emailAddress
         self.address = address
        
         MENYIPAN NILAI PARAMETER PADA OBJEKNYA MASING MASING
        """

    def purchaseParkingPass(self):  # MEMBUAT FUNGSI YANG BERNAMA purchaseParkingPass
        return f"{self.name} Membeli Tiket Parkir"
        """
        MEMBUAT SUATU FUNGSI YANG MEMBERITAU BAHWA SESEORANG MEMBELI TIKET PARKIR
        MENGAMBIL NILAI NAME YANG PADA FUNGSI YANG DI ATAS UNTUK KEMBALIKAN LAGI DENGAN MENGGUNAKAN RETURN
        """
