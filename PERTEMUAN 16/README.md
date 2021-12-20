<h1>Penjelasan Program</h1>
<hr>
<h3>Kreshna Putra Adi Wicaksana</h3>
<h3>V3920032</h3>
<h3>TI-D</h3>
<hr>
<h1>Penjelasan Program yang digunakan</h1>
<hr>
<h2>Komponen yang digunakan</h2>
<ol>
  <li>Resistor</li>
  <li>Sensor LDR</li>
  <li>BreadBoard</li>
  <li>NodeMCU ESP8266</li>
</ol>
<hr>

<h2>Penjelasan Program Arduino yang dibuat</h2>
<ol>
  <li>Line 1 dan 2 digunakan untuk memasukkan library dari NodeMCU</li>
  <li>line 5 hingga 7 digunakan untuk mendekalrasikan jaringan yang akan digunakan</li>
  <li>line 9 digunakan untuk mengatur kecepatan pengiriman menerima port</li>
  <li>line 12 dan 13 digunakan untuk membuat hostname dan mengkoneksikan komponen dengan jaringan inernet</li>
  <li>line 16 hingga 25 digunakan untuk mengecek sebuah kondisi jaringan</li>
  <li>line 32 hingga 37 digunakan untuk mendeklarasikan sebuah wifi yang sudah terhubung menjadi sebuah client dan mengecek kondisi database yang dimana jika gagal akan mencetak koneksi gagal</li>
  <li>digunakan untuk mengecek sebuah link input hasil sensor ke dalam database dengan diberikan delay selama 1 detik</li>
</ol>
<hr>

<h2>Penjelasan ceksensor.php</h2>
<ol>
  <li>line 2 digunakan untuk mengkoneksikan ke database</li>
  <li>line 4 digunakan untuk mengambil data dari sensor</li>
  <li>line 5 digunakan untuk mengambil data array</li>
  <li>line 6 digunakan untuk mengambil nilai sensor dengan array</li>
  <li>line 8 digunakan untuk mencetak nilai</li>
</ol>
<hr>

<h2>Penjelasan kirimdata.php</h2>
<ol>
  <li>line 2 digunakan untuk mengkoneksikan ke database</li>
  <li>line 5 digunakan untuk mengambil data dari sensor</li>
  <li>line 7 digunakan untuk mengupdate data ke database</li>
</ol>
<hr>

<h2>Penjelasan index.php</h2>
<ol>
  <li>pada line 12 hingga 18 ini berupa script javascript yang digunakan untuk merefresh website dan mengambil data</li>
  <li>line 23 hingga 30 digunakan untuk menempatkan data yang ditampilkan</li>
</ol>

<b><i>*Ini saja yang dapat saya jelaskan dalam program yang saya buat, kurang lebihnya mohon maaf. Terimakasih :)</i></b>
