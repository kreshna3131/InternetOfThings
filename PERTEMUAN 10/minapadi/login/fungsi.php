<?php
// koneksi ke database
// urutannya string(nama host), username mysql, password, namadatabase
$conn = mysqli_connect("localhost", "root", "", "minapadi");

function query($query)
{
    global $conn;
    $result = mysqli_query($conn, $query);
    $rows = [];
    while ($row = mysqli_fetch_assoc($result)) {
        $rows[] = $row;
    }
    return $rows;
}

?>