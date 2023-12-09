#
#  Import NumPy.
#
import Numeric

#
#  Import Ngl support functions.
#
import Ngl

#
#  Import all names from the NetCDF module.
#
from Scientific.IO.NetCDF import NetCDFFile

#
# Open a netCDF file containing storm data.
#
dirc = Ngl.ncargpath("data")
tfile = NetCDFFile(dirc + "/cdf/Tstorm.cdf", "r")

#
# Access the temperature arrays for the first 6 time steps.
#
nplots = 6
temp = tfile.variables["t"]

#
# Save lat and lon to Numeric arrays.
#
lat = tfile.variables["lat"][:]
lon = tfile.variables["lon"][:]

#
# Define a color map.
#
cmap = Numeric.array(
    [
        [1.00, 1.00, 1.00],
        [0.00, 0.00, 0.00],
        [1.00, 0.000, 0.000],
        [0.950, 0.010, 0.000],
        [0.870, 0.050, 0.000],
        [0.800, 0.090, 0.000],
        [0.700, 0.090, 0.000],
        [0.700, 0.120, 0.000],
        [0.700, 0.180, 0.000],
        [0.700, 0.260, 0.000],
        [0.700, 0.285, 0.000],
        [0.680, 0.330, 0.000],
        [0.570, 0.420, 0.000],
        [0.560, 0.530, 0.000],
        [0.550, 0.550, 0.000],
        [0.130, 0.570, 0.000],
        [0.060, 0.680, 0.000],
        [0.000, 0.690, 0.000],
        [0.000, 0.700, 0.100],
        [0.000, 0.600, 0.300],
        [0.000, 0.500, 0.500],
        [0.000, 0.400, 0.700],
        [0.000, 0.300, 0.700],
        [0.000, 0.200, 0.700],
        [0.000, 0.100, 0.700],
        [0.000, 0.000, 0.700],
        [0.100, 0.100, 0.700],
        [0.200, 0.200, 0.700],
        [0.300, 0.300, 0.700],
        [0.420, 0.400, 0.700],
        [0.560, 0.500, 0.700],
        [0.610, 0.600, 0.700],
        [0.700, 0.700, 0.700],
    ],
    Numeric.Float0,
)

#
# Set the color map and open a workstation.
#
rlist = Ngl.Resources()
rlist.wkColorMap = cmap

wks_type = "ps"
if wks_type == "ps" or wks_type == "pdf":
    rlist.wkOrientation = "Portrait"  # For PS or PDF output only.

wks = Ngl.open_wks(wks_type, "panel1", rlist)  # Open an X11 workstation.

#
# Turn off draw for the individual plots, since we are going to
# panel them later.
#
resources = Ngl.Resources()
resources.nglDraw = False
resources.nglFrame = False

#
#  Set the scalarfield missing value if temp has one specified.
#
if hasattr(temp, "_FillValue"):
    resources.sfMissingValueV = temp._FillValue

#
# Loop through the timesteps and create each plot, titling each
# one according to which timestep it is.
#
plot = []
resources.cnFillOn = True  # Turn on contour fill.
resources.lbLabelStride = 2  # Label every other box
resources.lbLabelFontHeightF = 0.02

for i in range(0, nplots):
    resources.tiMainString = "Temperature at time = " + str(i)
    plot.append(Ngl.contour(wks, temp[i, :, :], resources))


Ngl.panel(wks, plot[0:4], [2, 2])  # Draw 2 rows/2 columns of plots.

#
# Now add some extra white space around each plot.
#

panelres = Ngl.Resources()
panelres.nglPanelYWhiteSpacePercent = 5.0
panelres.nglPanelXWhiteSpacePercent = 5.0
Ngl.panel(wks, plot[0:4], [2, 2], panelres)  # Draw 2 rows/2 columns of plots.

#
# This section will set resources for drawing contour plots over a map.
#
del resources.tiMainString  # Don't set a main title.

resources.sfXArray = lon  # Portion of map on which to overlay
resources.sfYArray = lat  # contour plot.

resources.cnLineLabelsOn = False  # Turn off contour line labels.
resources.cnLinesOn = False  # Turn off contour lines.
resources.cnFillOn = True  # Turn on contour fill.

resources.cnLevelSelectionMode = "ManualLevels"  # Select contour levels.
resources.cnMinLevelValF = 245.0
resources.cnMaxLevelValF = 302.5
resources.cnLevelSpacingF = 2.5

resources.mpLimitMode = "LatLon"  # Limit portion of map that is viewed.
resources.mpMinLatF = min(lat)
resources.mpMaxLatF = max(lat)
resources.mpMinLonF = min(lon)
resources.mpMaxLonF = max(lon)
resources.pmLabelBarDisplayMode = "Never"  # Turn off labelbar, since we
# will use a global labelbar
# in the panel.

resources.mpPerimOn = True  # Turn on map perimeter.
resources.mpGridAndLimbOn = False  # Turn off map grid.

plot = []
for i in range(0, nplots):
    plot.append(Ngl.contour_map(wks, temp[i, :, :], resources))

#
# Set some resources for the paneled plots.
#
panelres = Ngl.Resources()
panelres.nglFrame = False  # Don't advance the frame.

#
# Set up some labelbar resources.  Set nglPanelLabelBar to True to
# indicate you want to draw a common labelbar at the bottom of the
# plots.
#
panelres.nglPanelLabelBar = True  # Turn on panel labelbar
panelres.nglPanelLabelBarLabelFontHeightF = 0.015  # Labelbar font height
panelres.nglPanelLabelBarHeightF = 0.1750  # Height of labelbar
panelres.nglPanelLabelBarWidthF = 0.700  # Width of labelbar
panelres.lbLabelFont = "helvetica-bold"  # Labelbar font
panelres.nglPanelTop = 0.935
panelres.nglPanelFigureStrings = ["A", "B", "C", "D", "E", "F"]
panelres.nglPanelFigureStringsJust = "BottomRight"

#
# You can have PyNGL selection the best paper orientation for
# the shape of plots you are drawing.  This resource is for PDF or
# PS output only.
#
if wks_type == "ps" or wks_type == "pdf":
    panelres.nglPaperOrientation = "Auto"

#
# Draw 3 rows and 2 columns of plots.
#
Ngl.panel(wks, plot[0:nplots], [3, 2], panelres)

#
# Draw two titles at the top.
#
textres = Ngl.Resources()
textres.txFontHeightF = 0.025  # Size of title.

Ngl.text_ndc(
    wks, ":F26:Temperature (K) at every six hours", 0.5, 0.97, textres
)

textres.txFontHeightF = 0.02  # Make second title slightly smaller.

Ngl.text_ndc(wks, ":F26:January 1996", 0.5, 0.935, textres)

Ngl.frame(wks)  # Advance the frame.

Ngl.end()
