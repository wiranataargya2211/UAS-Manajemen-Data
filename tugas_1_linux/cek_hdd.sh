#!/bin/bash
# Mengambil persentase 'Use%' dari partisi utama (/) dan membuang simbol %
pemakaian=$(df / | awk 'NR==2 {print $5}' | tr -d '%')

# Menghitung sisa space
sisa_space=$((100 - pemakaian))

echo "Notifikasi: space hdd anda tersisa $sisa_space%"
