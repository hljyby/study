<?php

// header("Content-type:appliacetion/json;charset=utf-8");
header("Cache-Control:max-age=0");

$res = array('msg' => 'ok', 'code' => 0, 'data' => 'Hello World!!!');

for ($i = 0; $i < 10; $i++) {
    sleep(1);
    echo json_encode($res);
    ob_flush();
    flush();
}
