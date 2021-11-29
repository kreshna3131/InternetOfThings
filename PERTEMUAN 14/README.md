<h2>Nama: Kreshna Putra Adi Wicaksana</h2>
<h2>NIM: V3920032</h2>

#Penjelasan
yang pertama kita lakukan dalam membuat program ini adalah menyiapkan perlengkapannya, yang kita butuhkan adalah PIR Sensor, Arduino Uno, LCD, Ground, dan Power.
kemudian kita hubungkan sesuai dengan port atau posisi yang sudah dibuat.
selanjutnya kita membuat programnya di arduino dengan membuat programnya yang dimana kita deklarasi int dengan pirState = digitalRead(1), kemudian kita setting kursor 0,0 dan mencetak nama Kreshna Putra.
selanjutnya kita membuat kondisi if else yang dimana jika pirStatenya ini = LOW maka kita tampilkan NIM, kemudian jika piStatenya = HIGH maka yang sebelumnya ini NIM menjadi tanggal kelahiran saya. kemudian saya memberi delay sebesar 0,5s
