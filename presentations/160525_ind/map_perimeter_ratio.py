import psycopg2

POSTGIS = psycopg2.connect(database="postgis", host="iemdb", user="nobody")
cursor = POSTGIS.cursor()

data = {}
cursor.execute(
    """SELECT wfo, sum(overlap) / sum(perimeter) * 100.0,
  sum(case when (overlap / perimeter) > 0.1 then 1 else 0 end), count(*),
  (sum(county_area) - sum(poly_area)) / sum(county_area) * 100.0  from
  ferree GROUP by wfo"""
)
for row in cursor:
    if row[4] is None:
        continue
    data[row[0]] = row[2] / float(row[3]) * 100.0

# for line in open("ferree3.txt"):
#    tokens = line.split(",")
#    data[ tokens[0] ] = float(tokens[3])

from pyiem.plot import MapPlot

m = MapPlot(
    sector="nws",
    title="% of SVR+TOR SBW Above 10% Perimeter Influence (~2km buf)",
    subtitle="Period: 1 Oct 2007 - 28 Feb 2014",
)
m.fill_cwas(data, lblformat="%.0f")
m.postprocess(filename="perim10.png")
