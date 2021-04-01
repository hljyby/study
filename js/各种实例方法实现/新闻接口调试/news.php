<?php
$method = "GET";
$url = "120.76.205.241:8000/news/qihoo?apikey=cXHbhftNWpcYm2I9tcKQz7qk4I6a28Ag4iKiwDEpVdwcEmuHowdzvkTJ7xjEayIz&kw=" . $_POST['kw'] . "&pageToken=" . $_POST['pageToken'];
$curl = curl_init();
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, $method);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_FAILONERROR, false);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
// curl_setopt($curl, CURLOPT_HEADER, true);
curl_setopt($curl, CURLOPT_ENCODING, "gzip");
echo curl_exec($curl);
?>