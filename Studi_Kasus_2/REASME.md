1. Struktur File
   project-folder
      - main.py
      - Author.py
      - Book.py
      - LibraryItem.py
      - LibraryMember.py
      - README.md
2. Struktur relasi
      - LibraryItem  class induk
         - memiliki atribut dasar   : item_id, title
         - memiliki method          : display_info() → None, calculate_late_fee() -> float
      - Book(LibraryItem) class turunan
         - menambah atribut : isbn, author
         - memiliki method  : display_info() -> None, calculate_late_fee() -> float:
      - Author() class sendiri
         - menambah atribut : name, birth_year
         - memiliki method  : get_age(current_year) → int
      - LibraryMember class sendiri
         - menambah atribut : member_id, name, borrowed_items
         - memiliki method  : borrow_item(item: LibraryItem) → None, return_item(item: LibraryItem) → None


program ini menggunakan data dummy dimana hanya cukup menjalankan main.py

3. Alur Program 
      1. Program di Jalankan dengan main.py
      2. Data Menggunakan Data Dummy
      3. Program menampilkan output lengkap:
         - data penulis  
         - data buku  
         - data anggota 
         - proses pinjam    
         - daftar pinjaman anggota
         - proses pengembalian
         - daftar pengembalin 
         - denda 


3. Contoh Output Program
        =============== OUTPUT SISTEM PERPUSTAKAAN ===============
        ==========================================================
                            DATA PENULIS
        Nama Penulis 1     : I Gusti Ngurah Astawa
        Tahun Lahir        : 2001
        Umur               : 24 tahun

        Nama Penulis 2     : I Putu Pariasa
        Tahun Lahir        : 1967
        Umur               : 58 tahun
        ----------------------------------------------------------

        ==========================================================
                            DATA BUKU
        ID Buku            : 101
        ISBN               : 00001
        Judul              : Jago Trading Dalam 5 Menit
        Penulis            : I Gusti Ngurah Astawa

        ID Buku            : 102
        ISBN               : 00002
        Judul              : Mempelajarin Mood Wanita
        Penulis            : I Putu Pariasa
        ----------------------------------------------------------

        ==========================================================
                            DATA ANGGOTA
        Nama Anggota 1     : Dwi
        ID Anggota         : 1

        Nama Anggota 2     : Edwin
        ID Anggota         : 2
        ----------------------------------------------------------

        =============== PROSES PEMINJAMAN ===============
        Dwi Berhasil Meminjam Buku       : Jago Trading Dalam 5 Menit
        Total item dipinjam Dwi          : 1
        Dwi Berhasil Meminjam Buku       : Mempelajarin Mood Wanita
        Total item dipinjam Dwi          : 2
        Edwin Berhasil Meminjam Buku     : Jago Trading Dalam 5 Menit
        Total item dipinjam Edwin        : 1
        ----------------------------------------------------------

        ============== DAFTAR PINJAMAN ANGGOTA ==============
        Pinjaman Dwi:
        1. Jago Trading Dalam 5 Menit (ID: 101)
        2. Mempelajarin Mood Wanita (ID: 102)
        Pinjaman Edwin:
        1. Jago Trading Dalam 5 Menit (ID: 101)
        ----------------------------------------------------------

        ================= PROSES PENGEMBALIAN =================

        Dwi berhasil mengembalikan : Jago Trading Dalam 5 Menit
        Sisa item dipinjam         : 1
        --------------------------------------------------------

        ========= DAFTAR PINJAMAN SETELAH PENGEMBALIAN =========
        1. Mempelajarin Mood Wanita (ID: 102)
        --------------------------------------------------------

        =================== PERHITUNGAN DENDA ===================
        Keterlambatan      : 5 hari
        Denda Buku         : Rp 10,000
        ==========================================================
        ====================== PROGRAM SELESAI ======================