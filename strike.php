<?php
// vad blir det för mat på Strike?
// @author Robert Sebescen

libxml_use_internal_errors(true);
date_default_timezone_set("Europe/Stockholm");

$swedish_day_names = array("Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag");
if (count($argv) === 1) // no extra arg given
	$swedish_day_to_look = $swedish_day_names[date('N')-1]; // look up today. start array at 0
else
	$swedish_day_to_look = ucwords($argv[1]);
echo "** Hämtar mat för ".mb_strtolower($swedish_day_to_look, "utf-8")." ** \n\n";

$doc = new DOMDocument(); 
//$doc->loadHTML(file_get_contents('lunchmeny.html')); // debug
$doc->loadHTML(file_get_contents('http://www.strikebowlinggoteborg.se/restaurang/lunchmeny/'));
$xpath = new DOMXpath($doc);

// exempel på förväntad html-struktur:
/*
<p><span style="text-decoration: underline;">Måndag</span></p>
<ul>
<li>Kött: Mustig korvstroganoff serveras med basmatiris och saltgurka samt gräddfil.</li>
<li>Kött: Cheddargratinerad kycklingfilé serveras med friterade pommes och en bacon– och rostad vitlöksdipp.</li>
<li>Pasta: Havets frukter i en vitlöksdoftande tomatsås.</li>
</ul>
*/
$elements = $xpath->query("//ul[preceding::p[1]/span[.='".$swedish_day_to_look."']]");
if ($elements->length === 0)
{
	echo "Ingen mat idag :(\n";
}
else
{
	foreach ($elements as $element) 
	{
	    echo $element->nodeValue, PHP_EOL;
	}
}
