<?php
require_once "/opt/iem/config/settings.inc.php";

require_once "/opt/iem/include/myview.php";

$t = new MyView();
$t->title = "ISP TI 8 May 2025";
$t->thispage = "iem-present";

$t->content = <<<EOM

<p><a href="introslides.pptx">Intro PowerPoint Slides</a></p>

<h3>Example Event and Links to Data</h3>

<p>I-880 3MM on March 19, 2025, around 10:50AM.
(SE of Missouri Valley, SW Iowa)</p>

<div class="row">
<div class="col-md-4 well">
<h4>Observations</h4>

<p>Info -&gt; Station Data &amp; Metadata
<br /><a href="/sites/locate.php?network=IA_RWIS">Iowa RWIS</a>
<br />Pick Missouri Valley RMVI4, then go to Ob History, select 3/19/2025
<br /><a href="/sites/obhistory.php?station=RMVI4&network=IA_RWIS&metar=0&madis=0&year=2025&month=3&day=19&sortdir=asc">Obs Listing</a>
</p>

<p>Info -&gt; Station Data &amp; Metadata
<br /><a href="/sites/locate.php?network=IA_ASOS">Iowa ASOS</a>
<br />Pick Council Bluffs CBF, then go to Ob History, select 3/19/2025
<br /><a href="/sites/obhistory.php?station=CBF&network=IA_ASOS&metar=0&madis=0&year=2025&month=3&day=19&sortdir=asc">Obs Listing</a>
</p>

<ol>
<li><a href="/request/asos/1min.phtml">Federal ASOS (big airports) 1 Minute</a>
(Network Tab -&gt; ASOS)</li>
<li><a href="/archive/">BUFKIT Profiles</a>
(Areas Tab -&gt; Archive Mainpage)</li>
<li><a href="/plotting/auto/?q=160">HML River Stage Forecasts</a>
(NWS Tab -&gt; NWS Mainpage -&gt; HML section)</li>
</ol>

</div><!-- ./observations -->
<div class="col-md-4 well">
<h4>Iowa Specific Archives</h4>

<p>Webcam archives (Iowa RWIS + Track-A-Plow + Some TV stations)
<br /><a href="/current/viewer.phtml#IDOT-090/2025-03-19T15:50:00Z">IEM Webcam Viewer</a>

</div><!-- ./iowa specific archives -->
<div class="col-md-4 well">
<h4>NWS Warnings + Forecasts</h4>

<ol>
<li><a href="/lsr/#/202503190500/202503200500/111010">Local Storm Report App</a>
(NWS Data Tab -&gt; Local Storm Report App)</li>
<li><a href="/wx/afos/list.phtml?by=cccc&source=OAX&pil=AFD&year=2025&month=3&day=19&year2=2025&month2=5&day2=5&view=grid&order=asc">NWS Text Archives</a>
(NWS Tab -&gt; NWS Text by WFO/Center)</li>
<li><a href="/timemachine/?product=59&timestamp=202503191655">NWS WaWa Map</a>
(Apps Tab -&gt; Time Machine -&gt; Select NWS WWA Map)</li>
<li><a href="/request/gis/watchwarn.phtml">Watch Warning Advisories Geometries</a>
(NWS Tab -&gt; NWS Mainpage)</li>
<li><a href="/vtec/search.php#eventsbypoint/-95.8891/41.5185/0.00">Search for Warnings</a>
(NWS Tab -&gt; VTEC Browser)</li>
</ol>

</div><!-- ./nws data -->
</div><!-- end row -->

EOM;
$t->render("single.phtml");
