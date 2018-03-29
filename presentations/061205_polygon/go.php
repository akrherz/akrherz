<?php
include("/home/akrherz/projects/iemwebsite/include/wfoLocs.php");


while (list($wfo, $v) = each($wfos))
{
`wget -q -O output/svr_2005_${wfo}.html 'http://mesonet.agron.iastate.edu/cow/?syear=2005\&smonth=1&sday=1&shour=1&eyear=2005&emonth=12&eday=31&ehour=23&wfo=${wfo}&wtype%5B%5D=SV&hail=0.75&ltype%5B%5D=SV'`;
 echo $wfo ;
}
echo "\n";
?>
