from LibraryItem import LibraryItem
from typing import List, Optional


class LibraryMember:

    def __init__(self, member_id: int, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_items = []

        """
         MENDESKRIPSIKAN OBJEK DAN PARAMETER YANG DIGUNAKA DALAM FUNGSI DI CLASS Author
         __init__   = FUNGSINYA UNTUK LANGSUNG MENJALANKAN DEF TAMPA DI DEKLASI LAGI
         self       = OBJEK
         member_id  = PARAMETER BERTIPE INT
         name       = PARAMETER BERTIPE STR
        ------------------------------------------------------------------------------------------------------------------------------------
        self.item_id        = item_id
        self.title          = title
        self.borrowed_items = [] DIMANA NILAI DI SETING KOSONG YANG AKAN MENAMPUNG NILAI DARI LibraryItem
        
        MENYIPAN NILAI PARAMETER PADA OBJEKNYA MASING-MASING 
        """

    def borrow_item(self, item: LibraryItem) -> None:
        """
        MIMINJAM BUKU
        """
        self.borrowed_items.append(item)

    def return_item(self, item: LibraryItem) -> None:
        """
        MENGEMBALIKAN BUKU
        """
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            return True
        else:
            return False

    def display_borrowed_items(self) -> None:
        """
        MENAMPILKAN DAFTAR BUKU YANG DI PIINJAM
        """
        return self.borrowed_items
