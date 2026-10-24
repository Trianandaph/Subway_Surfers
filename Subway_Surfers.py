class KarakterSurfer:
    def __init__(self, nama):
        # TODO 1: Inisialisasi properties (nama, skor = 0, koin = 0, is_running = True)
        self.nama_karakter = nama
        self.skor = 0
        self.koin = 0
        self.is_running = False
        pass

    def berlari(self):
        # TODO 2: Buat behavior agar karakter mulai berlari (cetak pesan dan ubah is_running menjadi True)
        self.is_running = True
        self.skor += 1
        print(f"Karakter mulai berlari.")
        pass

    def ambil_koin(self, jumlah):
        # TODO 3: Tambahkan jumlah koin ke properties koin dan berikan output informasi
        self.koin += jumlah
        print(f"Koin bertambah {jumlah}. Koin sekarang : {self.koin}")
        pass

    def tabrak_rintangan(self):
        # TODO 4: Jika menabrak rintangan, ubah is_running menjadi False dan cetak pesan game over
        self.is_running = False
        print(f"Kamu menabrak. GAME OVER")
        pass

    def info_player(self):
        # TODO 5: Cetak status terkini (nama, skor, jumlah koin, dan status berlari)
        print("---Status/Hasil---")
        print("Nama :", (self.nama_karakter))
        print("Skor :", (self.skor))
        print("Koin :", (self.koin))
        print("Status :", "Sedang Berlari" if self.is_running else "Menabrak" )
        pass

# --- PENGUJIAN OBJEK ---
# Buat objek dengan nama variabel "player1" (misal: "Jake")
player1 = KarakterSurfer("Jake")
player1.info_player()
player1.berlari()
player1.ambil_koin(5)
player1.ambil_koin(5)
player1.tabrak_rintangan()
player1.info_player()
