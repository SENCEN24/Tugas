from Author import Author
from LibraryItem import LibraryItem


class Book(LibraryItem):

    def __init__(self, item_id, isbn, title, author=None):
        LibraryItem.__init__(self, item_id, title)
        self.isbn = isbn
        self.author = author

        """
         MENDESKRIPSIKAN OBJEK DAN PARAMETER YANG DIGUNAKA DALAM FUNGSI DI CLASS PERSON
         __init__           = FUNGSINYA UNTUK LANGSUNG MENJALANKAN DEF TAMPA DI DEKLASI LAGI
         self               = OBJEK
         isbn               = PARAMETER BERTIPE STR
         author             = PARAMETER BERTIPE YANG DIMANA DI GUNAKAN UNTUK MENGAMBIL NILAI author PADA CLASS author NILAI AWALNYA NONE ATAU NULL
         ------------------------------------------------------------------------------------------------------------------------------------
        LibraryItem.__init__(self, item_id, title)
         MEMANGGIL CONSTRUCTOR MILIK CLASS LibraryItem
         
        self.isbn = isbn
        self.author = author
        
         MENYIPAN NILAI PARAMETER PADA OBJEKNYA MASING MASING
        """

    def display_info(self) -> None:
        """
        MENAMPILKAN INFO BUKU
        """

    def calculate_late_fee(self, days_late) -> float:
        """
        MENGHITUNG DENDA BUKU
        """
        return days_late * 2000.0
