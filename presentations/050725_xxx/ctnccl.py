#
#  Import NumPy.
#
#
#  Import Ngl support functions.
#
import Ngl
import Numeric

#
#  Import all names from the NetCDF module.
#
from Scientific.IO.NetCDF import *

#
#  Open a netCDF file containing data off the coast of North Carolina.
#
#  This data is from the Naval Research Laboratory at the Stennis
#  Space Center. For more information about this grid, see the
#  article "Application of a Shelf-Scale Model to Wave-Induced
#  Circulation: Rip Currents" (Mark Cobb and Cheryl Ann Blain,
#  Ocean Dynamics and Prediction Branch).
#
dirc = Ngl.ncargpath("data")
cfile = NetCDFFile(dirc + "/cdf/ctnccl.nc", "r")

#
#  Read the lat/lon/ele/depth arrays to Numeric arrays.
#
lat = cfile.variables["lat"][:]
lon = cfile.variables["lon"][:]
ele = cfile.variables["ele"][:]
depth = cfile.variables["dat"][:]

#
# Create colormap
#
cmap = Numeric.zeros((104, 3), Numeric.Float0)
cmap[0] = [1.0, 1.0, 1.0]
cmap[1] = [0.0, 0.0, 0.0]
cmap[2] = [0.5, 0.5, 0.5]
cmap[3] = [0.8, 0.8, 0.8]

iofc = 151
iolc = 250
for i in xrange(151, 251):
    p = (1.0 * iolc - i) / (1.0 * iolc - 1.0 * iofc)
    q = (i - 1.0 * iofc) / (1.0 * iolc - 1.0 * iofc)
    cmap[i - 147] = [0.0, p, q]

#
#  Open workstation.
#
rlist = Ngl.Resources()
rlist.wkColorMap = cmap
wks_type = "ps"
wks = Ngl.open_wks(wks_type, "ctnccl", rlist)

#
#  The next set of resources will apply to the contour plot.
#
resources = Ngl.Resources()

resources.nglSpreadColorStart = 4

resources.sfXArray = lon  # Portion of map on which to overlay
resources.sfYArray = lat  # contour plot.
resources.sfElementNodes = ele
resources.sfFirstNodeIndex = 1

resources.cnFillOn = True
resources.cnFillMode = "RasterFill"
resources.cnRasterSmoothingOn = True
resources.cnLinesOn = False
resources.cnLineLabelsOn = False
resources.cnLevelSelectionMode = "ExplicitLevels"
resources.cnLevels = [
    1.0,
    2.0,
    3.0,
    4.0,
    5.0,
    6.0,
    7.0,
    8.0,
    9.0,
    10.0,
    15.0,
    20.0,
    25.0,
    30.0,
    35.0,
    40.0,
    45.0,
    50.0,
    100.0,
    200.0,
    300.0,
    400.0,
    500.0,
    600.0,
    700.0,
    800.0,
    900.0,
    1000.0,
    1250.0,
    1500.0,
    1750.0,
    2000.0,
    2250.0,
    2500.0,
    2750.0,
    3000.0,
    3250.0,
    3500.0,
    3750.0,
    4000.0,
    4250.0,
    4500.0,
    4750.0,
    5000.0,
]

resources.tiMainString = "North Carolina Coast (depth in meters)"
resources.tiMainFontHeightF = 0.015

resources.nglDraw = False
resources.nglFrame = False

contour = Ngl.contour(wks, depth, resources)

#
# Retrieve the actual lat/lon end points of the scalar array so
# we know where to overlay on map.
#
xs = Ngl.get_float(contour.sffield, "sfXCActualStartF")
xe = Ngl.get_float(contour.sffield, "sfXCActualEndF")
ys = Ngl.get_float(contour.sffield, "sfYCActualStartF")
ye = Ngl.get_float(contour.sffield, "sfYCActualEndF")

#
#  The next set of resources will apply to the map plot.
#
resources.mpProjection = "CylindricalEquidistant"

#
# If you want high resolution map coastlines, download the RANGS/GSHHS
# files from:
#
#     http://www.io-warnemuende.de/homepages/rfeistel/index.html
#
# The files you need are:
#
#   rangs(0).zip    gshhs(0).zip
#   rangs(1).zip    gshhs(1).zip
#   rangs(2).zip    gshhs(2).zip
#   rangs(3).zip    gshhs(3).zip
#   rangs(4).zip    gshhs(4).zip
#
# Once you unzip these files, put them in the directory
# $python_prefx/pythonX.Y/site-packages/PyNGL/ncarg/database/rangs
#
# Now you can change the following resource to "HighRes".
#
resources.mpDataBaseVersion = "MediumRes"
resources.mpLimitMode = "LatLon"
resources.mpMinLonF = xs
resources.mpMaxLonF = xe
resources.mpMinLatF = ys
resources.mpMaxLatF = ye
resources.mpPerimOn = True
resources.mpGridAndLimbOn = False
resources.mpPerimDrawOrder = "PostDraw"
resources.mpFillDrawOrder = "PostDraw"
resources.mpFillOn = True
resources.mpFillColors = [
    "background",
    "transparent",
    "LightGray",
    "transparent",
]
resources.lbLabelFontHeightF = 0.01
resources.lbBoxLinesOn = False
resources.lbOrientation = "Horizontal"

resources.pmTickMarkDisplayMode = "Never"
resources.pmLabelBarOrthogonalPosF = -0.05

resources.nglDraw = True
resources.nglFrame = True

map = Ngl.contour_map(wks, depth, resources)

Ngl.end()
