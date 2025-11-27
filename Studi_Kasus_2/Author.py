class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

        """
         MENDESKRIPSIKAN OBJEK DAN PARAMETER YANG DIGUNAKA DALAM FUNGSI DI CLASS Author
         __init__   = FUNGSINYA UNTUK LANGSUNG MENJALANKAN DEF TAMPA DI DEKLASI LAGI
         self       = OBJEK
         name       = PARAMETER BERTIPE STR
         birth_year = PARAMETER BERTIPE INT
        ------------------------------------------------------------------------------------------------------------------------------------
        self.name       = name
        self.birth_year = birth_year
        
        MENYIPAN NILAI PARAMETER PADA OBJEKNYA MASING-MASING 
        """

    def get_age(self, current_year) -> int:
        """
        MENGHITUNG UMUR PENULIS BERDASARKAN TAHUN SEKARANG
        """
        return current_year - self.birth_year
