#!/bin/bash
while read nama_user; do
	# Membuat user baru
	sudo useradd -m "$nama_user"

	# Mengatur password secara otomatis menjadi namauser@123
	echo "$nama_user:$nama_user@123" | sudo chpasswd

	echo "User $nama_user berhasil dibuat dengan password $nama_user@123"
done < daftar_nama.txt
