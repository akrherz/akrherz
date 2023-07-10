#!/usr/bin/env python

from Scientific.IO import NetCDF
import Numeric
import Ngl

nc = NetCDF.NetCDFFile("MMOUT_DOMAIN2.nc")

t2 = nc.variables["t2"]
lats = nc.variables["latitcrs"]
lons = nc.variables["longicrs"]

y = Numeric.ravel(lats)
x = Numeric.ravel(lons)
z = Numeric.ravel(t2[1])

numxout = 20  # Define output grid for call to "natgrid".
numyout = 20
xmin = min(x)
ymin = min(y)
xmax = max(x)
ymax = max(y)

xc = (xmax - xmin) / (numxout - 1)
yc = (ymax - ymin) / (numyout - 1)

xo = xmin + xc * Numeric.arange(0, numxout)
yo = ymin + yc * Numeric.arange(0, numxout)
zo = Ngl.natgrid(x, y, z, xo, yo)  # Interpolate.

rlist = Ngl.Resources()
rlist.wkColorMap = "rainbow+white+gray"
pswks = Ngl.open_wks("ps", "ngl08p", rlist)  # Open a PS workstation.

resources = Ngl.Resources()
resources.sfXArray = xo  # X axes data points
resources.sfYArray = yo  # Y axes data points

resources.mpProjection = "LambertEqualArea"  # Change the map projection.
resources.mpCenterLonF = -95.0
resources.mpCenterLatF = 42.0

resources.mpLimitMode = "LatLon"  # Limit the map view.
resources.mpMinLonF = -97.0
resources.mpMaxLonF = -90.0
resources.mpMinLatF = 40.0
resources.mpMaxLatF = 44.0
resources.mpPerimOn = True
resources.mpOutlineBoundarySets = "geophysicalandusstates"
resources.mpDataBaseVersion = "mediumres"
resources.mpDataSetName = "Earth..2"
resources.mpGridAndLimbOn = False
resources.mpUSStateLineThicknessF = 2


resources.cnFillOn = True  # Turn on contour fill.
resources.cnInfoLabelOn = False  # Turn off info label.
resources.cnLineLabelsOn = False  # Turn off line labels.

resources.lbOrientation = "Horizontal"  # Draw it horizontally.
# label bar.
resources.nglSpreadColors = True  # Do not interpolate color space.
resources.vpYF = 0.9  # Change Y location of plot.


zt = Numeric.transpose(zo)
contour = Ngl.contour_map(pswks, zt, resources)

del contour
