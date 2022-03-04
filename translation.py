class Translation(object):
    START_TEXT = """<b>Queen Scrapper Membantu anda Untuk Mengambil APP ID dan API Hash dengan Mudah!
━━━━━━━━━━━━━━━━━━━━━━━━
Masukin Nomor HP Lu Tod! Jangan Lupa Pake +62.
Contoh : +628xxxxxxx</b>
"""
    AFTER_RECVD_CODE_TEXT = """Udah Masuk Nih Tod!
kirim kode yang dari Telegram Nyed!

Kode ini cuma dipake buat dapet ID APP dari my.telegram.org
Kalo lu gak percaya botnya, Ngambil Manual aja Ngentod !
"""
    BEFORE_SUCC_LOGIN = "Kode Dah Masuk Nyomot Data Dari Telegram..."
    ERRED_PAGE = """Hadeh Error. Coba dengan Cara Manual

Cara Ambil APP ID dan API HASH Secara Manual
1. Buka my.telegram.org/auth
2. Loginkan akun telegram kalian
3. klik menu API Development
4. isi data seperti dibawah ini :
• App Title : tgbot
• Short Name : tgbot
• URL : (kosongin)
• Platform : desktop
5. Selesai

Bila Berhasil Ambil Manual Silahkan Coba Lagi di Bot ini"""
    CANCELLED_MESG = "Bye! Silahkan /start kembali untuk mengulang"
    IN_VALID_CODE_PVDED = "Kode Nya Salah Ngentod"
    IN_VALID_PHNO_PVDED = "No HP SALAH, Silahkan Masukkan Nomor Telepon Telegram Anda Dengan Format Kode Negara.\nContoh: +628xxxxxxx"
