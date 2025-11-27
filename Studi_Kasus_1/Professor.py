from Person import Person


class Professor(Person):
    def __init__(
        self,
        name,
        phoneNumber,
        emailAddress,
        salary,
        staffNumber,
        yearsOfService,
        numberOfClasses,
        address=None,
    ):
        Person.__init__(self, name, phoneNumber, emailAddress, address)
        self.salary = salary
        self.staffNumber = staffNumber
        self.yearsOfService = yearsOfService
        self.numberOfClasses = numberOfClasses

        """
         MENDESKRIPSIKAN OBJEK DAN PARAMETER YANG DIGUNAKA DALAM FUNGSI DI CLASS PERSON
         __init__           = FUNGSINYA UNTUK LANGSUNG MENJALANKAN DEF TAMPA DI DEKLASI LAGI
         self               = OBJEK
         name               = PARAMETER BERTIPE STR
         phoneNumber        = PARAMETER BERTIPE STR
         emailAddress       = PARAMETER BERTIPE STR
         salary             = PARAMETER BERTIPE INT
         staffNumber        = PARAMETER BERTIPE INT
         yearsOfService     = PARAMETER BERTIPE INT
         numberOfClasses    = PARAMETER BERTIPE INT
         address            = PARAMETER BERTIPE YANG DIMANA DI GUNAKAN UNTUK MENGAMBIL NILAI ADDRESS PADA CLASS ADRRESNYA NILAI AWALNYA NONE ATAU NULL
         ------------------------------------------------------------------------------------------------------------------------------------
         Person.__init__(self, name, phoneNumber, emailAddress, address)
         MEMANGGIL CONSTRUCTOR MILIK CLASS PERSON
         
         self.salary            = salary
         self.staffNumber       = staffNumber
         self.yearsOfService    = yearsOfService
         self.numberOfClasses   = numberOfClasses
        
         MENYIPAN NILAI PARAMETER PADA OBJEKNYA MASING MASING
        """
