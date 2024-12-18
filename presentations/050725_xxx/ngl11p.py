#
#  Import NumPy.
#

#
#  Import NGL support functions.
#
import Ngl
import Numeric

#
#  Define a color table and open a workstation.
#
cmap = Numeric.zeros((2, 3), Numeric.Float0)
cmap[0] = [1.0, 1.0, 1.0]
cmap[1] = [0.0, 0.0, 0.0]
rlist = Ngl.Resources()
rlist.wkColorMap = cmap
wks_type = "ps"
wks = Ngl.open_wks(wks_type, "ngl11p", rlist)

dirc = Ngl.ncargpath("data")
data = Ngl.asciiread(dirc + "/asc/u.cocos", (39, 14), "float")

pressure = data[:, 0]  # First column of data is pressure (mb).
height = data[:, 1]  # Second column is height (km).
u = data[:, 2:14]  # Rest of columns are climatological zonal winds
# (u: m/s)
unew = Ngl.add_cyclic(u)  # Add cyclic points to u.

# ----------- Begin first plot -----------------------------------------

resources = Ngl.Resources()

resources.tiMainString = ":F26:Cocos Island"  # Main title.
resources.tiYAxisString = ":F25:Pressure (mb)"  # Y axes label.

resources.sfYCStartV = max(pressure)  # Indicate start and end of left
resources.sfYCEndV = min(pressure)  # Y axes values.

resources.trYReverse = True  # Reverse the Y values.
resources.trYLog = True  # Use log scale.

resources.tmXBMode = "Explicit"  # Define your own tick mark labels.
resources.tmXBLabelFont = 25  # Change font of labels.
resources.tmXBLabelFontHeightF = 0.015  # Change font height of labels.
resources.tmXBMinorOn = False  # No minor tick marks.
resources.tmXBValues = range(0, 13, 1)  # Location to put tick mark labels
# (13 points with January repeated).
resources.tmXBLabels = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
    "Jan",
]

resources.tmYUseLeft = False  # Keep right axis independent of left.
resources.tmYRLabelsOn = True  # Turn on right axis labels.
resources.tmYRLabelFont = 25  # Change font of labels.
resources.tmYROn = True  # Turn on right axis tick marks.
resources.tmYRMinorOn = False  # No minor tick marks.

resources.tmYRMode = "Explicit"  # Define own tick mark labels.
hnice = range(0, 23, 2)  # Set range of "nice" height values.
pnice = Ngl.ftcurv(
    height, pressure, hnice
)  # Calculate "nice" pressure values.
resources.tmYRValues = pnice  # At each "nice" pressure value,
resources.tmYRLabels = hnice  # put a "height" value label.

resources.tmYLMode = "Explicit"  # Define own tick mark labels.
resources.tmYLLabelFont = 25  # Change the font.
resources.tmYLValues = [
    1000.0,
    800.0,
    700.0,
    500.0,
    400.0,
    300.0,
    250.0,
    200.0,
    150.0,
    100.0,
    50.0,
]
resources.tmYLLabels = [
    "1000",
    "800",
    "700",
    "500",
    "400",
    "300",
    "250",
    "200",
    "150",
    "100",
    "50",
]
resources.tmYLMinorOn = False  # No minor tick marks.

resources.cnFillOn = True  # Turn on contour level fill.
resources.cnMonoFillColor = True  # Use one fill color.
resources.cnMonoFillPattern = False  # Use multiple fill patterns.

resources.cnLineLabelAngleF = 0.0  # Draw contour line labels right-side up.
resources.cnLevelSpacingF = 1.0

resources.nglDraw = False  # Don't draw the plot or advance the
resources.nglFrame = False  # frame in the call to Ngl.contour.

resources.nglMaximize = False
resources.pmLabelBarDisplayMode = "Never"  # Turn off label bar.
contour = Ngl.contour(wks, unew, resources)  # Create a contour plot.

levels = Ngl.get_float_array(contour, "cnLevels")

patterns = Numeric.zeros((len(levels) + 1), Numeric.Int)
patterns[:] = -1

for i in xrange(len(levels)):
    if levels[i] <= -6.0:
        patterns[i] = 5
    else:
        if levels[i] > 0.0:
            patterns[i] = 17.0
patterns[-1] = 17  # last pattern

rlist = Ngl.Resources()
rlist.cnFillPatterns = patterns
rlist.cnFillScaleF = 0.8
Ngl.set_values(contour, rlist)

Ngl.draw(contour)  # Draw the contour plot.

txres = Ngl.Resources()  # Annotate plot with some text.
txres.txFontHeightF = 0.015
Ngl.text_ndc(wks, ":F25:U Component", 0.270, 0.815, txres)
Ngl.text_ndc(wks, ":F25:(m-s:S:-1:N:)", 0.765, 0.815, txres)


txres.txFontHeightF = 0.025  # Label right Y axis.
txres.txAngleF = 90.0
Ngl.text_ndc(wks, ":F25:Height (km)", 0.89, 0.5, txres)

Ngl.frame(wks)  # Advance the frame.

# ----------- Begin second plot -----------------------------------------

del resources
resources = Ngl.Resources()

resources.tiMainString = ":F26:Cocos Island"
resources.tiXAxisString = ":F25:Month"
resources.tiYAxisString = ":F25:Amplitude (m/s)"

resources.tmXBMode = "Explicit"  # Define your own tick mark labels.
resources.tmXBLabelFont = 25  # Change font of labels.
resources.tmXBLabelFontHeightF = 0.015  # Change font height of labels.
resources.tmXBMinorOn = False  # No minor tick marks.
resources.tmXBValues = range(0, 13, 1)  # Values from 0 to 12.
resources.tmXBLabels = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
    "Jan",
]

xy = Ngl.xy(
    wks, range(0, 13, 1), unew, resources
)  # Create and draw an XY plot.

Ngl.end()
