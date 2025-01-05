# NDP URL Shortener

Aplikasi pemendek URL modern yang dibangun dengan Django, dengan fitur pelacakan statistik dan manajemen tautan.

![NDP URL Shortener Screenshot](<Screencast%202025-01-05%2022-45-57%20(1).gif>)

## 🚀 Fitur Utama

- ✂️ Pemendek URL dengan judul otomatis
- 📊 Statistik kunjungan detail
- 📱 Responsif di semua perangkat
- 🎯 Pelacakan pengunjung (IP, browser, referrer)
- 📌 Simpan dan kelola URL favorit
- 🔍 Riwayat kunjungan
- 📈 Grafik kunjungan 30 hari terakhir
- 🔗 Bagikan ke media sosial
- 📋 Salin URL dengan satu klik

## 🛠️ Teknologi yang Digunakan

- Django 5.1.4
- Python 3.13
- SQLite Database
- HTML5 & CSS3
- JavaScript (Vanilla)
- Chart.js untuk visualisasi data
- Font Awesome untuk ikon
- BeautifulSoup4 untuk ekstraksi judul website

## 💻 Persyaratan Sistem

- Python 3.8 atau lebih tinggi
- pip (Python package installer)
- Virtual environment (direkomendasikan)

## 🔧 Cara Instalasi

1. Clone repositori ini:

   ```markdown
   git clone https://github.com/NDP4/sortlink-django.git
   ```

2. Buat dan aktifkan virtual environment:

```markdown
python -m venv myenv
source myenv/bin/activate # Linux/Mac
myenv\Scripts\activate # Windows
```

3. Install dependensi:

```markdown
pip install -r requirements.txt
```

4. Lakukan migrasi database:

```markdown
python manage.py makemigrations
python manage.py migrate
```

5. Jalankan server development:

```markdown
python manage.py runserver
```

📝 Cara Penggunaan
Memendekkan URL

1. Buka halaman utama
2. Tempel atau ketik URL panjang di input field
3. Klik tombol "Perpendek URL"
4. Salin URL pendek yang dihasilkan
   Melihat Statistik
5. Klik "Lihat Statistik" pada halaman sukses
6. Atau tambahkan "/stats" di akhir URL pendek
   Menyimpan URL
7. Buka halaman statistik URL
8. Klik tombol "Simpan ke Bookmark"
9. Isi nama dan catatan (opsional)
10. Klik "Simpan"

📁 Struktur Proyek

```markdown
sortlink/
├── manage.py
├── requirements.txt
├── sortlinkndp/
│ ├── **init**.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── shortener/
├── models.py
├── views.py
├── urls.py
└── templates/
└── shortener/
├── home.html
├── success.html
├── stats.html
├── privacy.html
└── terms.html
```

⚙️ Konfigurasi
Sesuaikan file settings.py untuk mengubah:

- Database (default: SQLite)
- Zona waktu (default: UTC)
- Host yang diizinkan
- Pengaturan keamanan
  
  🔐 Fitur Keamanan
- CSRF protection
- XSS prevention
- Sanitasi URL
- Validasi input
- Rate limiting
- Pembatasan akses admin
  
  📈 Pengembangan Mendatang
- <input disabled="" type="checkbox"> Sistem autentikasi pengguna
- <input disabled="" type="checkbox"> API endpoint
- <input disabled="" type="checkbox"> Custom URL pendek
- <input disabled="" type="checkbox"> QR Code generator
- <input disabled="" type="checkbox"> Dashboard admin
- <input disabled="" type="checkbox"> Export statistik
- <input disabled="" type="checkbox"> Integrasi media sosial lebih lanjut
  
  🐛 Pelaporan Bug
  Jika Anda menemukan bug atau masalah, silakan buat issue baru di repositori GitHub dengan:

1. Deskripsi masalah
2. Langkah-langkah untuk mereproduksi
3. Screenshot (jika ada)
4. Informasi sistem (browser, OS)
   
   🤝 Kontribusi
   Kontribusi sangat diterima! Langkah-langkah:

1. Fork repositori
2. Buat branch fitur (git checkout -b fitur-baru)
3. Commit perubahan (git commit -m 'Menambah fitur baru')
4. Push ke branch (git push origin fitur-baru)
5. Buat Pull Request
    
   📄 Lisensi
   Proyek ini dilisensikan di bawah MIT License (LICENSE)

👨‍💻 Author

- Nama: NDP
- Email: nurdwipriyambodo@proton.me
- Website: ndpshortener.com
  
  🙏 Terima Kasih Kepada
- Django Team
- Chart.js
- Font Awesome
- Beautiful Soup
- Komunitas Open Source
  
  📞 Kontak
  Untuk pertanyaan dan saran:

- Email: nurdwipriyambodo@proton.me
- WhatsApp: +62 859 5165 7887
- Lokasi: Semarang, Indonesia
  © 2024 NDP Shortener. Hak Cipta Dilindungi.

