<h6>Nama  : Kreshna Putra Adi Wicaksana</h6>
<h6>NIM   : V3920032</h6>
<h6>Kelas : TI-D</h6>
<hr>
<h2>Penjelasan Program yang sudah dibuat</h2>
<hr>
Pada praktikum iot pertemuan 13 ini kita belajar mengenai cara mengkoneksikan arduino ke web server. Langkah pertama yang kita lakukan adalah mendownload dan menambahkan library ethercard terlebih dahulu. kemudian kita ubah STATIC 0 menjadi STATIC 1 untuk mematikan DHCP dan menggunakan ip yang akan kita buat pada script static byte gwip[] ip gateway yg digunakan untuk mengatur alamat ip pada komputer / device. sedangkan untuk static byte myip[] untuk membuka server diweb.
<br><br>
kemudian setelah script di compile atau di kompilasi, kita masuk ke proteus dan memasukkan directory file.hex nya yang dimana file hex ini kita dapatkan dari hasil compile tadi. Kemudian kita atur ip gateway di modul ENC2860 agar arduino ini bisa terhubung ke web server, kemudian saat di web kita mengetikkan alamat ip server yang telah dibuat akan muncul nama, nim, tanggal lahir dan email yg merupakan scipt HTML biasa yg telah dibuat di arduino.
