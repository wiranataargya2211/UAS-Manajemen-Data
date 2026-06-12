#!bin/bash
# Nama file backup menggunakan tanggal dan jam saat ini
NAMA_FILE="backup_$(date +%Y%m%d_%H%M).tar.gz"

# Proses compress direktori ke dalam folder /backup yang sudah di-mount
sudo tar -czvf /backup/$NAMA_FILE /home/argya/tugas_uas_manajemen_data

echo "Backup selesai: /backup/$NAMA_FILE"
