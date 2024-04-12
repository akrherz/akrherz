import sys

sys.path.append("/home/akrherz/projects/iemwebsite/scripts/lib/")
import os

import iemplot
import mx.DateTime
import Nio
import numpy

# 18-19 19-20 20-21 21-22 22-23 23-24

sts = mx.DateTime.DateTime(2008, 4, 25, 13)
ets = mx.DateTime.DateTime(2008, 4, 26, 12)
interval = mx.DateTime.RelativeDateTime(hours=1)
now = sts
while now <= ets:
    fp = now.strftime("ST4.%Y%m%d%H.01h.grib")
    a = Nio.open_file(fp)
    if now == sts:
        running = a.variables["A_PCP_GDS5_SFC_acc1h"][:]
    else:
        running = running + a.variables["A_PCP_GDS5_SFC_acc1h"][:]
    now += interval

b = Nio.open_file("ST4.2008042612.24h.grib")
grid = b.variables["A_PCP_GDS5_SFC_acc24h"][:] - running
mask = numpy.where(grid < 0.02, numpy.where(grid > -0.02, 1, 0), 0)
grid_ma = numpy.ma.array(grid, mask=mask)

cfg = {
    "cnLevelSelectionMode": "ManualLevels",
    "cnLevelSpacingF": 0.5,
    "cnMinLevelValF": -5,
    "cnMaxLevelValF": 5,
    # 'wkColorMap': 'WhViBlGrYeOrRe',
    "wkColorMap": "BlAqGrYeOrRe",
    "nglSpreadColorStart": -1,
    "nglSpreadColorEnd": 2,
    "cnFillMode": "RasterFill",
    "_title": "Difference Between 24 Hour Stage4 File and Associated 1 Hour Files",
    "_valid": "25 Apr 2008 12z  - 26 Apr 2008 12z",
    "lbTitleString": "[mm]",
    "pmLabelBarHeightF": 0.6,
    "pmLabelBarWidthF": 0.1,
    "lbLabelFontHeightF": 0.025,
    # 'mpMaskAreaSpecifiers' : ["Conterminous US",],
    # 'mpOutlineSpecifiers' : ["Conterminous US : States",],
    # 'mpMinLonF'          : -95.0,
    # 'mpMaxLonF'          : -60.0,
    # 'mpMinLatF'          : 29.0,
    # 'mpMaxLatF'          : 47.0
}
# Generates tmp.ps
iemplot.simple_grid_fill(
    b.variables["g5_lon_1"][:], b.variables["g5_lat_0"][:], grid_ma, cfg
)

os.system(
    "convert -rotate -90 -trim -border 5 -bordercolor '#fff' -resize 900x700 -density 120 +repage tmp.ps tmp.png"
)
if os.environ["USER"] == "akrherz":
    os.system("xv tmp.png")
