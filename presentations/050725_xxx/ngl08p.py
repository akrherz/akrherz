#
#  Import NumPy.
#
#
#  Import Ngl support functions.
#
import Ngl
import Numeric

#
#  Open the ASCII file.
#
seismic = Ngl.asciiread("seismic.asc", [52, 3], "float")

x = Numeric.array(seismic[:, 0], Numeric.Float0)
y = Numeric.array(seismic[:, 1], Numeric.Float0)
z = Numeric.array(seismic[:, 2], Numeric.Float0)

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

#
#  Define a color map and open four different types of workstations.
#
cmap = Numeric.array(
    [
        [1.00, 1.00, 1.00],
        [0.00, 0.00, 0.00],
        [1.00, 0.00, 0.00],
        [1.00, 0.00, 0.40],
        [1.00, 0.00, 0.80],
        [1.00, 0.20, 1.00],
        [1.00, 0.60, 1.00],
        [0.60, 0.80, 1.00],
        [0.20, 0.80, 1.00],
        [0.20, 0.80, 0.60],
        [0.20, 0.80, 0.00],
        [0.20, 0.40, 0.00],
        [0.20, 0.45, 0.40],
        [0.20, 0.40, 0.80],
        [0.60, 0.40, 0.80],
        [0.60, 0.80, 0.80],
        [0.60, 0.80, 0.40],
        [1.00, 0.60, 0.80],
    ],
    Numeric.Float0,
)
rlist = Ngl.Resources()
rlist.wkColorMap = cmap
xwks = Ngl.open_wks("x11", "ngl08p", rlist)  # Open an X11 workstation.
cgmwks = Ngl.open_wks("ncgm", "ngl08p", rlist)  # Open an NCGM workstation.
pswks = Ngl.open_wks("ps", "ngl08p", rlist)  # Open a PS workstation.
pdfwks = Ngl.open_wks("pdf", "ngl08p", rlist)  # Open a PDF workstation.

# ----------- Begin first plot -----------------------------------------

resources = Ngl.Resources()
resources.sfXArray = xo  # X axes data points
resources.sfYArray = yo  # Y axes data points

resources.tiMainString = "Depth of a subsurface stratum"
resources.tiMainFont = "Times-Bold"
resources.tiXAxisString = "x values"  # X axis label.
resources.tiYAxisString = "y values"  # Y axis label.

resources.cnFillOn = True  # Turn on contour fill.
resources.cnInfoLabelOn = False  # Turn off info label.
resources.cnLineLabelsOn = False  # Turn off line labels.

resources.lbOrientation = "Horizontal"  # Draw it horizontally.
# label bar.
resources.nglSpreadColors = False  # Do not interpolate color space.
resources.vpYF = 0.9  # Change Y location of plot.

zt = Numeric.transpose(zo)
contour = Ngl.contour(xwks, zt, resources)

# ----------- Begin second plot -----------------------------------------

del resources
resources = Ngl.Resources()
resources.tiMainString = ":F26:slices"  # Define a title.

resources.xyLineColors = [2, 8, 10, 14]  # Define line colors.
resources.xyLineThicknessF = 3.0  # Define line thickness.

resources.pmLegendDisplayMode = "Always"  # Turn on the drawing
resources.pmLegendZone = 0  # Change the location
resources.pmLegendOrthogonalPosF = 0.31  # of the legend
resources.lgJustification = "BottomRight"
resources.pmLegendWidthF = 0.4  # Change width and
resources.pmLegendHeightF = 0.12  # height of legend.
resources.pmLegendSide = "Top"  # Change location of
resources.lgPerimOn = False  # legend and turn off
# the perimeter.

resources.xyExplicitLegendLabels = ["zo(i,2)", "zo(i,4)", "zo(i,6)", "zo(i,8)"]

resources.vpYF = 0.90  # Change size and location of plot.
resources.vpXF = 0.18
resources.vpWidthF = 0.74
resources.vpHeightF = 0.74
resources.trYMaxF = 980  # Set the maximum value for the Y axes.

resources.tiYAxisString = "Depth of a subsurface stratum"

xy = Ngl.xy(xwks, xo, zt[2:9:2, :], resources)  # Draw an XY plot.

# ----------- Draw to other workstations  ------------------------------

Ngl.change_workstation(contour, cgmwks)  # Change the workstation that the
Ngl.change_workstation(xy, cgmwks)  # contour and XY plot is drawn to.
Ngl.draw(contour)  # Draw the contour plot to the new
Ngl.frame(cgmwks)  # workstation and advance the frame.
Ngl.draw(xy)  # Draw the XY plot to the new
Ngl.frame(cgmwks)  # workstation and advance the frame.

Ngl.change_workstation(contour, pswks)  # Do the same for the PostScript
Ngl.change_workstation(xy, pswks)  # workstation.
Ngl.draw(contour)
Ngl.frame(pswks)
Ngl.draw(xy)
Ngl.frame(pswks)

Ngl.change_workstation(contour, pdfwks)  # And for the PDF workstation...
Ngl.change_workstation(xy, pdfwks)
Ngl.draw(contour)
Ngl.frame(pdfwks)
Ngl.draw(xy)
Ngl.frame(pdfwks)

del xy
del contour

Ngl.end()
