<?php 
$conn = mysqli_connect("localhost", "root", "", "uassensor");

// baca data yang dikirim nodemcu
$nilai = $_GET["sensor"];
// update data pada database
mysqli_query($conn, "UPDATE sensor SET nilai_sensor='$nilai'");
