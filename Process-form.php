<?php

$name = $_POST["name"];
$email-id = $_POST["Email-id"];
$password = $_POST["password"];
$accounttype = filter_input(INPUT_POST, "Account type", FILTER_VALIDATE_INT);


if ( ! $accounttype) {
    die("Account type must be selected");
}   

$host = "localhost";
$dbname = "games_scratch";
$username = "root";
$password = "Praneel@2310";
        
$conn = mysqli_connect(hostname: $host,
                       username: $username,
                       password: $password,
                       database: $dbname);
        
if (mysqli_connect_errno()) {
    die("Connection error: " . mysqli_connect_error());
}           
        
$sql = "INSERT INTO message (name, body, priority, type)
        VALUES (?, ?, ?, ?)";

$stmt = mysqli_stmt_init($conn);

if ( ! mysqli_stmt_prepare($stmt, $sql)) {
 
    die(mysqli_error($conn));
}

mysqli_stmt_bind_param($stmt, "ssii",
                       $name,
                       $password,
                       $Accounttype);

mysqli_stmt_execute($stmt);

echo "Record saved.";