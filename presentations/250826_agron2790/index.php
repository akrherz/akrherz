<?php
require_once "/opt/iem/config/settings.inc.php";

require_once "/opt/iem/include/myview.php";

$t = new MyView();
$t->title = "Agronomy 2790 - 27 August 2024";
$t->thispage = "iem-present";

$t->content = <<<EOF

<a href="iem.pptx">Powerpoint Presentation</a>

<h4>Today's Task List</h4>

<ol>
  <li>Use <a href="/explorer/" target="_blank">IEM Explorer</a> to locate nearby stations.
  <br />The IEM website collects data from many different observing networks.  Knowing the closest
  station to your location of interest is half the battle of using the website.  The primary
  stations you want to know are the closest airport station (in ASOS network) and closest long-term
  climate location (in COOP network).</li>

  <li>Use <a href="/climodat/" target="_blank">Climodat Reports</a> to find monthly precip totals.
  <br />Given that you found a nearby long term climate site, you can use that site to find a report
  table of monthly precipitation along with the climatology.</li>

  <li>Consult <a href="/agweather/" target="_blank">AgWeather Mainpage</a> for growing season plot options.
  <br />The IEM has a number of applications that generate maps/plots of totals over a variable period of
  days.</li>

  <li>View <a href="/agclimate/soilt.php" target="_blank">Iowa County Soil Temperature Maps</a>
  <br />This page now includes daily GFS forecast plots going out two weeks.</li>

  <li>Search for <a href="/vtec/search.php" target="_blank">NWS Warnings</a>
  <br />You can search for warnings by counties / points and drill down to get more details about this
  warning including damage reports and the raw warning text.</li>

  <li>Generate a <a href="/sites/dyn_windrose.phtml?station=AMW&network=IA_ASOS" target="_blank">Custom Wind Rose</a> for Ames.
  <br />These informative plots are useful to illustrate prevailing wind speed and direction
  over a period of time.</li>

  <li>View <a href="/current/viewer.phtml" target="_blank">Archived Webcam Imagery</a>
  <br />These images are a gold mine for quick visual assessment of conditions back on a date
  of your choice.</li>

  <li>Create a <a href="/plotting/auto/?q=84" target="_blank">Map of High Res Precip Estimates</a>
  <br />Often big rainfall events are highly isolated within a given county.  You can generate
  maps of these events for a given date or range of dates.</li>
</ol>

<p>The bottom line, email me any and all questions, problems, and/or complaints!  akrherz@iastate.edu</p>


EOF;
$t->render('single.phtml');
