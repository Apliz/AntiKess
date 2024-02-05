
<?php
$myFile = "../JSON/orbital_data.json";

$fh = fopen($myFile, 'w') or die("can't open file");
$stringData = $_GET["data"];
// echo $stringData;
fwrite($fh, "$stringData");
fclose($fh)
?>