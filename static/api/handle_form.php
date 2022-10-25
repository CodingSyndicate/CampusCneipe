<?php

$infoMail = getenv("INFO_MAIL");
$eventMail = getenv("EVENT_MAIL");
$personalMail = getenv("PERSONAL_MAIL");

$inputJSON = file_get_contents('php://input');
$input = json_decode($inputJSON, TRUE); //convert JSON into array

if (!isset($input)) {
    echo "No form data provided";
    exit();
}

$from = $input['email'];
$to = "raiser@campus-cneipe.de";
if($input['requesttype'] == "I") {
    $to = $infoMail;
} else if($input['requesttype'] == "E") {
    $to = $eventMail;
} else if($input['requesttype'] == "P") {
    $to = $personalMail;
}
$subject = "Anfrage: " . $input['request'];
$message = $input['message'] . "\n\n---\n" . $input['name'] . " (" . $input['email'] . ")\nGesendet über das Kontaktformular.";

if ($input['challenge'] != '9' and
    !filter_var($from, FILTER_VALIDATE_EMAIL)) {
    echo "Falsche Eingabe!";
    exit();
}

// https://doku.lrz.de/display/PUBLIC/Mailversand+aus+dem+Webhosting
$headers = "From: " . $to ."\r\n" .
         "Reply-To: " . $from ."\r\n" .
         "Envelope-From: " . $to ."\r\n";

if(mail($to, $subject, $message, $headers)) {
    http_response_code(200);
    echo "Mail sent";
    exit();
} else {
    echo "Message was not sent.";
    http_response_code(400);
    exit();
}
?>
