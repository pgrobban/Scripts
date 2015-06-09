<?php
// vad blir det för mat på Strike?

libxml_use_internal_errors(true);
date_default_timezone_set("Europe/Stockholm");

$swedish_day_names = array("Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag");
$swedish_day_today = $swedish_day_names[date('N')-1]; // start array at 0
echo "** Idag är det ".$swedish_day_today." ** \n";

$doc = new DOMDocument(); 
//$doc->loadHTML(file_get_contents('lunchmeny.html')); // debug
$doc->loadHTML(file_get_contents('http://www.strikebowlinggoteborg.se/restaurang/lunchmeny/'));
$xpath = new DOMXpath($doc);

// förväntad html-struktur:
/*
<p><span style="text-decoration: underline;">Måndag</span></p>
<ul>
<li>Kött: Mustig korvstroganoff serveras med basmatiris och saltgurka samt gräddfil.</li>
<li>Kött: Cheddargratinerad kycklingfilé serveras med friterade pommes och en bacon– och rostad vitlöksdipp.</li>
<li>Pasta: Havets frukter i en vitlöksdoftande tomatsås.</li>
</ul>
*/
$elements = $xpath->query("//ul[preceding::p[1]/span[.='".$swedish_day_today."']]");
foreach ($elements as $element) {
    echo $element->nodeValue, PHP_EOL;
}
