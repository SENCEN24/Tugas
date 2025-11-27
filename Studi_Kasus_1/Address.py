class Address:
    def __init__(self, street, city, state, postalCode, country):
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country

        """
         MENDESKRIPSIKAN OBJEK DAN PARAMETER YANG DIGUNAKA DALAM FUNGSI DI CLASS ADDRESS
         __init__   = FUNGSINYA UNTUK LANGSUNG MENJALANKAN DEF TAMPA DI DEKLASI LAGI
         self       = OBJEK
         street     = PARAMETER BERTIPE STR
         city       = PARAMETER BERTIPE STR
         state      = PARAMETER BERTIPE STR
         postalCode = PARAMETER BERTIPE INT
         country    = PARAMETER BERTIPE STR
        ------------------------------------------------------------------------------------------------------------------------------------
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country
        
        MENYIPAN NILAI PARAMETER PADA OBJEKNYA MASING-MASING 
        """

    def validate(self):

        # if not self.postalCode:
        #     return self.postalCode == 0
        return all([self.street, self.city, self.state, self.country])
        """
        FUNGSI VALIDASI DIMANA SAYA MENGGUNKAN METHOD ALL() YANG AKAN MENGECEK APAKAH SELURUH DATA YANG 
        ADA DI DALAM METHOT ALL() ADA ISINYA
        """

    def outputAsLabel(self):

        street = self.street if self.street else "-"
        city = self.city if self.city else "-"
        state = self.state if self.state else "-"
        country = self.country if self.country else "-"

        return f"{street}, {city}, {state}, {self.postalCode}, {country}"

        """
        FUNGSI DARI outputAsLabel UNTUK MENGELUARKAN SELURUH DATA DARI 
        street,city,state,postalCode,country
        DAN SAYA JUGA MEMBUAT SUATU KONDISI MENGGUNKAN IF DIMANA JIKA DATA DARI OBJEK NULL ATAU NONE 
        MAKAN AKAN DI ISI DENGAN -
        """
