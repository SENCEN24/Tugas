from datetime import datetime

from Author import Author
from LibraryItem import LibraryItem
from LibraryMember import LibraryMember
from Book import Book


def main():

    author1 = Author("I Gusti Ngurah Astawa", 2001)
    author2 = Author("I Putu Pariasa", 1967)
    current_year = datetime.now().year
    book1 = Book(101, "00001", "Jago Trading Dalam 5 Menit", author1)
    book2 = Book(102, "00002", "Mempelajarin Mood Wanita", author2)
    member1 = LibraryMember(1, "Dwi")
    member2 = LibraryMember(2, "Edwin")
    days_late = 5
    fee = book1.calculate_late_fee(days_late)
    items_after_return = member1.display_borrowed_items()

    print("\n=============== OUTPUT SISTEM PERPUSTAKAAN ===============")
    print("==========================================================")
    print("                     DATA PENULIS                         ")

    print(f"Nama Penulis 1     : {author1.name}")
    print(f"Tahun Lahir        : {author1.birth_year}")
    print(f"Umur               : {author1.get_age(current_year)} tahun\n")
    print(f"Nama Penulis 2     : {author2.name}")
    print(f"Tahun Lahir        : {author2.birth_year}")
    print(f"Umur               : {author2.get_age(current_year)} tahun")
    print("----------------------------------------------------------\n")

    print("==========================================================")
    print("                       DATA BUKU                          ")

    print(f"ID Buku            : {book1.item_id}")
    print(f"ISBN               : {book1.isbn}")
    print(f"Judul              : {book1.title}")
    print(f"Penulis            : {book1.author.name}\n")
    print(f"ID Buku            : {book2.item_id}")
    print(f"ISBN               : {book2.isbn}")
    print(f"Judul              : {book2.title}")
    print(f"Penulis            : {book2.author.name}")
    print("----------------------------------------------------------\n")

    print("==========================================================")
    print("                    DATA ANGGOTA                          ")
    print(f"Nama Anggota 1     : {member1.name}")
    print(f"ID Anggota         : {member1.member_id}\n")
    print(f"Nama Anggota 2     : {member2.name}")
    print(f"ID Anggota         : {member2.member_id}")
    print("----------------------------------------------------------\n")

    print("=============== PROSES PEMINJAMAN ===============")
    member1.borrow_item(book1)
    print(f"{member1.name} Berhasil Meminjam Buku       : {book1.title}")
    print(
        f"Total item dipinjam {member1.name}          : {len(member1.borrowed_items)}"
    )
    member1.borrow_item(book2)
    print(f"{member1.name} Berhasil Meminjam Buku       : {book2.title}")
    print(
        f"Total item dipinjam {member1.name}          : {len(member1.borrowed_items)}"
    )
    member2.borrow_item(book1)
    print(f"{member2.name} Berhasil Meminjam Buku     : {book1.title}")
    print(f"Total item dipinjam {member2.name}        : {len(member2.borrowed_items)}")
    print("----------------------------------------------------------\n")

    print("============== DAFTAR PINJAMAN ANGGOTA ==============")
    print(f"Pinjaman {member1.name}:")
    items1 = member1.display_borrowed_items()
    if not items1:
        print("  Tidak ada item yang dipinjam")
    else:
        for i, item in enumerate(items1, 1):
            print(f"  {i}. {item.title} (ID: {item.item_id})")

    print(f"Pinjaman {member2.name}:")
    items2 = member2.display_borrowed_items()
    if not items2:
        print("  Tidak ada item yang dipinjam")
    else:
        for i, item in enumerate(items2, 1):
            print(f"  {i}. {item.title} (ID: {item.item_id})")
    print("----------------------------------------------------------\n")

    print("================= PROSES PENGEMBALIAN =================")
    if member1.return_item(book1):
        print(f"\n{member1.name} berhasil mengembalikan : {book1.title}")
        print(f"Sisa item dipinjam         : {len(member1.borrowed_items)}")
    else:
        print(f"\nItem '{book1.title}' tidak ditemukan dalam daftar pinjaman")

    print("--------------------------------------------------------\n")

    print("========= DAFTAR PINJAMAN SETELAH PENGEMBALIAN =========")
    if not items_after_return:
        print("  Tidak ada item yang dipinjam")
    else:
        for i, item in enumerate(items_after_return, 1):
            print(f"  {i}. {item.title} (ID: {item.item_id})")
    print("--------------------------------------------------------\n")

    print("=================== PERHITUNGAN DENDA ===================")
    print(f"Keterlambatan      : {days_late} hari")
    print(f"Denda Buku         : Rp {fee:,.0f}")
    print("==========================================================")

    print("\n====================== PROGRAM SELESAI ======================")


if __name__ == "__main__":
    main()
