<?php
    header("Content-Type:text/event-stream;charset=utf-8");
    header("Access-Control-Allow-Origin:http://3w.sse:8888/");
    // 必须添加 data: 和 两个换行
    echo "data: 今天是 " . date("H:i:s") . "\n\n";
