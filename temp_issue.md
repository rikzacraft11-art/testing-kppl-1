### Deskripsi Tugas
Kita perlu melakukan pengaturan awal (scaffolding) untuk project Python ini dan menambahkan satu fitur logika dasar, yaitu pengecekan bilangan ganjil/genap. 

### Langkah-langkah (Tasks)
- [ ] **1. Scaffolding Project Python**
  - Rapikan struktur folder project. Pastikan file kode utama berada pada tempat yang tepat.
  - Periksa pengaturan awal di `pyproject.toml` dan pastikan informasi project sudah memadai.
- [ ] **2. Install Dependencies**
  - Identifikasi package/library dasar yang dibutuhkan (misalnya `pytest` untuk mempermudah testing kedepannya).
  - Gunakan `uv` untuk mengelola dependensi (misal: `uv sync` atau `uv add pytest`).
- [ ] **3. Buat Fitur Ganjil/Genap (`feature/ganjil-genap`)**
  - Buat branch baru dari main bernama `feature/ganjil-genap`.
  - Buat fungsi sederhana di dalam project yang menerima satu angka bulat (integer) dan mengembalikan nilai boolean (`True` jika genap, `False` jika ganjil).
  - Simpan, commit perubahan tersebut, lalu push branch `feature/ganjil-genap` ke repository GitHub.

### Kriteria Penerimaan (Acceptance Criteria)
- [ ] Branch `feature/ganjil-genap` berhasil dibuat dan di-push.
- [ ] Fungsi bilangan ganjil/genap berjalan tanpa error syntax.
- [ ] Struktur project standar sudah rapi (file tidak berantakan di root directory jika tidak diperlukan).
