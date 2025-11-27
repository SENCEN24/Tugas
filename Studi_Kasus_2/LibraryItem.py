class LibraryItem:

    def __init__(self, item_id: int, title: str):
        self.item_id = item_id
        self.title = title

        """
         MENDESKRIPSIKAN OBJEK DAN PARAMETER YANG DIGUNAKA DALAM FUNGSI DI CLASS Author
         __init__   = FUNGSINYA UNTUK LANGSUNG MENJALANKAN DEF TAMPA DI DEKLASI LAGI
         self       = OBJEK
         item_id    = PARAMETER BERTIPE INT
         title      = PARAMETER BERTIPE STR
        ------------------------------------------------------------------------------------------------------------------------------------
        self.item_id    = item_id
        self.title      = title
        
        MENYIPAN NILAI PARAMETER PADA OBJEKNYA MASING-MASING 
        """

    def display_info(self) -> None:
        """
        MENAPILKAN INFORMASI BUKU YANG DI JALAN SUBCLASS
        """
        print(f"ID: {self.item_id}")
        print(f"Judul: {self.title}")

    def calculate_late_fee(self, days_late) -> float:
        """
        MENGHITUNG DENTANG KETERLAMBATAN
        """
        # Denda Rp 1000 per hari
        return days_late * 1000.0
