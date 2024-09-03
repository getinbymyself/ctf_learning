<?php

$car_s=$_POST['txtCar'];

$loginUrl = 'http://127.0.0.1:8000/querycar?car='.$car_s;

$ch = curl_init();
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_URL,$loginUrl);

$result=curl_exec($ch);

curl_close($ch);

echo "After running the API url: ".$loginUrl. "<br>";

echo "The result of JSON data:<hr>";
var_dump($result);
echo "<br><br>";
echo "<hr>";

echo "To JSON object data:<hr>";
$cars=json_decode($result,true);

var_dump($cars);


/*以下是解析json数据的结果*/
echo "<br><br>";
echo "<hr>";
echo $cars["make"].'|'.$cars["model"].'|'.$cars["colour"].'|'.$cars["owner"];
echo "<hr>";
/*请大家自己补充HTML代码*/
?>