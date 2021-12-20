<?php 
$conn = mysqli_connect("localhost", "root", "", "uassensor");

$sql = mysqli_query($conn, "SELECT * FROM sensor");
$data = mysqli_fetch_array($sql);
$nilai = $data["nilai_sensor"];

echo $nilai;
?>
