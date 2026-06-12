from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # 1. Membuat sekumpulan data dummy mahasiswa
    data = {
        'Nama': ['Andi', 'Budi', 'Citra', 'Dewi', 'Eka'],
        'Tugas': [85, 70, 90, 88, 75],
        'UTS': [80, 75, 85, 92, 80],
        'UAS': [88, 78, 92, 85, 79]
    }
    df = pd.DataFrame(data)

    # 2. Proses Analisa Data (Menghitung Nilai Akhir dan Sorting Peringkat)
    df['Nilai Akhir'] = (df['Tugas'] * 0.3) + (df['UTS'] * 0.3) + (df['UAS'] * 0.4)
    df['Peringkat'] = df['Nilai Akhir'].rank(ascending=False).astype(int)
    df_sorted = df.sort_values('Peringkat')

    # 3. Menyiapkan tampilan HTML sederhana untuk diakses via browser
    html_template = """
    <html>
        <head>
            <title>Analisis Nilai Mahasiswa</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                table { border-collapse: collapse; width: 60%; margin-top: 20px; }
                th, td { border: 1px solid #dddddd; text-align: left; padding: 8px; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h2>Sistem Analisis Data Nilai Mahasiswa (Student Score Analyzer)</h2>
            <p>Berikut adalah hasil kalkulasi dan pemeringkatan nilai akhir mahasiswa:</p>
            {{ table_html|safe }}
        </body>
    </html>
    """

    # Mengubah DataFrame Pandas menjadi tabel HTML
    return render_template_string(html_template, table_html=df_sorted.to_html(index=False))

if __name__ == '__main__':
    # Berjalan di port 5000 agar bisa diekspos oleh Docker
    app.run(host='0.0.0.0', port=5000)
