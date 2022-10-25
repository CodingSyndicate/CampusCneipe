<?php

$day = $_GET['day'];
$name = $_GET['name'];
$date = $_GET['date'];
$time = $_GET['time'];
$person = $_GET['person'];
$mail = $_GET['mail'];


$cardName = $day . "%20" . $date . "%20" . $time . "%20" . $name . "%20" . $person;
$cardDesc = $mail;

$apikey = getenv("TRELLO_APIKEY");
$apitoken = getenv("TRELLO_APITOKEN");
$listId = getenv("TRELLO_LISTID");

function getUrlContent($url) {
    fopen("cookies.txt", "w");
    $parts = parse_url($url);
    $host = $parts['host'];
    $ch = curl_init();
    $header = array('POST /1575051 HTTP/1.1',
        "Host: {$host}",
        'Accept:application/json',
        'Accept-Language:en-US,en;q=0.8',
        'Cache-Control:max-age=0',
        'Connection:keep-alive',
        'Host:trello.com',
        'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    );

    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 0);
    curl_setopt($ch, CURLOPT_COOKIESESSION, true);
    curl_setopt($ch, CURLOPT_POST, true);

    curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookies.txt');
    curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookies.txt');
    curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
    $result = curl_exec($ch);
    curl_close($ch);
    return $result;
}

$url = "https://api.trello.com/1/cards?idList=" . $listId . "&name=" . $cardName . "&desc=" . $cardDesc . "&key=" . $apikey . "&token=" . $apitoken;

$response = getUrlContent($url);

echo $response;
?>