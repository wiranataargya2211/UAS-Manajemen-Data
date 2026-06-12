# Menggunakan sistem operasi Linux minimal dengan Python 3.9
FROM python:3.9-slim

# Menentukan direktori kerja di dalam container
WORKDIR /app

# Meng-copy file requirements dan menginstalnya
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Meng-copy seluruh kode program ke dalam container
COPY . .

# Membuka port 5000 untuk akses HTTP
EXPOSE 5000

# Perintah yang dijalankan saat container menyala
CMD ["python", "app.py"]
