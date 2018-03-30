#
#  This code is based on an NCL code of John Ertl at the
#  Fleet Numerical Meteorology and Oceanography Center
#
import copy

#
#  Import all names from the NetCDF module.
#
from Scientific.IO.NetCDF import NetCDFFile

#
#  Import Numeric and sys.
#
import Numeric,sys

#
#  Import the PyNGL module names.
#
import Ngl

#
#  9-point smoother function.
#
def smth9(x,p,q):
#
#  Run a 9-point smoother on the 2D Numeric array x using weights
#  p and q.  Return the smoothed array.
#

#
#  Get array dimensions and check on sizes.
#
  ni = x.shape[0]
  nj = x.shape[1]
  if (ni < 3 or nj < 3):
    print "smth9: both array dimensions must be at least three."
    sys.exit()

#
#  Smooth.
#
  po4 = p/4.
  qo4 = q/4.

  output = Numeric.zeros([ni,nj],Numeric.Float0)
  for j in xrange(1,nj-1):
    for i in xrange(1,ni-1):
      jm1 = j-1
      jp1 = j+1
      im1 = i-1
      ip1 = i+1
      term1 = po4*(x[im1,j]+x[i,jm1]+x[ip1,j]+x[i,jp1]-4.*x[i,j])
      term2 = qo4*(x[im1,jp1]+x[im1,jm1]+x[ip1,jm1]+x[ip1,jp1]-4.*x[i,j])
      output[i,j] = float(x[i,j]) + term1 + term2

#
#  Set the perimeter values to the original x values.
#
  output[0,:]    = x[0,:]
  output[ni-1,:] = x[ni-1,:]
  output[:,0]    = x[:,0]
  output[:,nj-1] = x[:,nj-1]

#
#  Return smoothed array.
#
  return output

#
#  Main program.
#

#
#  Read in the data variables from the NetCDF file.
#
cdf_file   = NetCDFFile(Ngl.ncargpath("data") + "/cdf/meteo_data.nc","r")
tempisobar = cdf_file.variables["tempisobar"][:,:]  # temperature
levels     = cdf_file.variables["levels"][:]        # levels
taus       = cdf_file.variables["taus"][:]          # taus
rh         = cdf_file.variables["rh"][:,:]          # realtive humidity
ugrid      = cdf_file.variables["ugrid"][:,:]       # horizontal winds 
vgrid      = cdf_file.variables["vgrid"][:,:]       # vertical winds
rain03     = cdf_file.variables["rain03"][:]        # rainfall
tempht     = cdf_file.variables["tempht"][:]        # surface temperatures

#
#  Smooth temperature and humidity.
#  
smothtemp = smth9(tempisobar, 0.50, -0.25)
smothrh   = smth9(        rh, 0.50, -0.25)

#
#  Set up a color map and open an output workstation.
#
colors = Numeric.array([                                               \
                         [255,255,255], [  0,  0,  0], [255,255,255],  \
                         [255,255,255], [255,255,255], [240,255,240],  \
                         [220,255,220], [190,255,190], [120,255,120],  \
                         [ 80,255, 80], [ 50,200, 50], [ 20,150, 20],  \
                         [255,  0,  0]                                 \
                       ],Numeric.Float0) / 255.
rlist = Ngl.Resources()
rlist.wkColorMap = colors
wks_type = "ps"
wks = Ngl.open_wks(wks_type,"meteogram",rlist)

#
# Create a different resource list for every plot created.
#
rh_res      = Ngl.Resources()
rain_res    = Ngl.Resources()
tempsfc_res = Ngl.Resources()

#
#  Ngl.Resources that rh_res, temp_res, and uv_res share.
#
rh_res.trYReverse   = True     # Reverse the Y values.
rh_res.nglDraw      = False    # Don't draw individual plot.
rh_res.nglFrame     = False    # Don't advance frame.
rh_res.nglMaximize  = False    # Do not maximize plot in frame (default is
                               #   to maximize).
rh_res.vpXF         = 0.15     # x location
rh_res.vpYF         = 0.90     # y location
rh_res.vpWidthF     = 0.7      # width
rh_res.vpHeightF    = 0.40     # height

#
#  Copy the rh_res resources into two new resource files for
#  temperature and wind barbs.  "deepcopy" is used so that
#  subsequent changes to rh_res do not affect the new resources.
#
temp_res            = copy.deepcopy(rh_res)
uv_res              = copy.deepcopy(rh_res)

#
#  ------------ Relative humidity resources.. ----------------
#
rh_res.sfXArray       = taus             # Define X/Y axes values that
rh_res.sfYArray       = levels           # all three data fields are on
rh_res.tiYAxisString  = "Pressure (mb)"  # Y axes label.
rh_res.tiYAxisFont    = 21               # Y axes font.
rh_res.tiYAxisFontHeightF = 0.025        # Y axes font height.
rh_res.tmYLMode       = "Explicit"       # Define own tick mark labels.
rh_res.tmYLLabelFont  = 26               # Change the font.
rh_res.tmYLValues     = levels
rh_res.tmYLLabels     =  [                              \
                          "1000", "975", "950", "925",  \
                           "850", "700", "500", "400"   \
                         ]
rh_res.tmYLMinorOn    = False            # No minor tick marks.
rh_res.tiXAxisString        = ""         # X axes label.
rh_res.tmXBMode             = "Explicit" # Define own tick mark labels.
rh_res.tmXBLabelFont        = 26         # Change the font.
rh_res.tmXBValues           = taus
rh_res.tmXBLabelFontHeightF = .016  # Font size
rh_res.tmXBLabels           =                             \
                  [                                       \
                    "12z", "15z", "18z",  "21z", "Apr29", \
                    "03z", "06z", "09z",  "12z", "15z",   \
                    "18z", "21z", "Apr30","03z", "06z",   \
                    "09z", "12z", "15z",  "18z", "21z",   \
                  "May01", "03z", "06z",  "09z", "12z"    \
                  ]

#
# insert a list
#
rh_res.tmXBLabelAngleF      = 90.        # change label angle
rh_res.tmXBMinorOn       = False        # No minor tick marks.
rh_res.tmXBLabelJust     = "CenterCenter"
rh_res.nglSpreadColorEnd = -2           # save last color (red) for cntr lines

rh_res.cnFillOn        = True           # turns on color fill
rh_res.cnLineLabelsOn  = True           # no contour labels
rh_res.tiMainString    = "Meteogram for LGSA, 28/12Z"
rh_res.tiMainFont      = 22
rh_res.cnFillOn        = True           # turns on the color
rh_res.pmLabelBarDisplayMode = "Never"  # turn off plotting label bar (on
                                        #   by default.

#
#  ------------ Temperature resources. ----------------------
#
temp_res.sfXArray         = taus    # Define X/Y axes values that
temp_res.sfYArray         = levels  # all three data fields are on
temp_res.cnLineLabelsOn   = True    # no contour labels
temp_res.cnLineThicknessF = 3.0     # line thickness
temp_res.cnLineColor      = "Red"

# ------------- wind barbs resources ------------------------
uv_res.vfXArray            = taus   # Define X/Y axes values that
uv_res.vfYArray            = levels # all three data fields are on
uv_res.vcRefAnnoOn         = False  # turns off the ref box
uv_res.vcRefLengthF        = 0.040
uv_res.vcGlyphStyle        = "WindBarb"
uv_res.vcMonoWindBarbColor = True   # color the windbarbs with
                                    #   respect to speed use False

# ------------- Rain histogram resources ---------------------
rain_res.nglFrame        = False
rain_res.vpXF            = 0.15   # The left side of the box
rain_res.vpYF            = 0.36   # The top side of the plot box
rain_res.vpWidthF        = 0.72   # The Width of the plot box
rain_res.vpHeightF       = 0.10   # The height of the plot box
rain_res.trYMinF         = 0.0    # min value on y-axis
rain_res.trYMaxF         = 0.5    # max value on y-axis

rain_res.tiXAxisString  = ""         # X axes label.
rain_res.tmXBMode       = "Explicit" # Define own tick mark labels.
rain_res.tmXBLabelFont  = 26         # Change the font.
rain_res.tmYLLabelFont  = 26         # Change the font.
rain_res.tmXBValues     = taus
rain_res.tmXBLabels     = taus
rain_res.tmXTOn         = False      # turn off the top tickmarks
rain_res.tmXBMinorOn    = False      # No minor tick marks.

rain_res.tmXBMajorLengthF        = 0.01    # Force tickmarks to point
rain_res.tmXBMajorOutwardLengthF = 0.01    # out by making the outward
rain_res.tmYLMajorLengthF        = 0.01    # tick length equal to the
rain_res.tmYLMajorOutwardLengthF = 0.01    # total tick length
rain_res.tmYLMinorLengthF        = 0.005
rain_res.tmYLMinorOutwardLengthF = 0.005
rain_res.tiYAxisFont    = 21               # Y axes font.
rain_res.tiYAxisFontHeightF = 0.015        # Y axes font height.
rain_res.tiYAxisString           = "3hr rain total"  # Y axis label.


rain_res.nglDraw         = False     # Don't draw individual plot.
rain_res.nglFrame        = False     # Don't advance frame.
rain_res.nglMaximize     = False     # Do not maximize plot in frame

# -------------- temp sfc time series ------------------------
tempsfc_res.vpXF            = 0.15   # The left side of the box
tempsfc_res.vpYF            = 0.17   # The top side of the plot box
tempsfc_res.vpWidthF        = 0.72   # The Width of the plot box
tempsfc_res.vpHeightF       = 0.10   # The height of the plot box

tempsfc_res.tiXAxisString  = ""            # X axes label.
tempsfc_res.tiYAxisFont    = 21               # Y axes font.
tempsfc_res.tiYAxisFontHeightF = 0.015        # Y axes font height.
tempsfc_res.tiYAxisString  = "Temp at 2m"  # Y axis label.
tempsfc_res.tmXBMode       = "Explicit"    # Define own tick mark labels.
tempsfc_res.tmXBLabelFont  = 26            # Change the font.
tempsfc_res.tmYLLabelFont  = 26            # Change the font.
tempsfc_res.tmXBValues     = taus
tempsfc_res.tmXBLabels     = taus
tempsfc_res.tmXTOn         = False         # turn off the top tickmarks
tempsfc_res.xyLineThicknesses = 2
tempsfc_res.xyLineColor    =  "red"

tempsfc_res.nglDraw         = False     # Don't draw individual plot.
tempsfc_res.nglFrame        = False     # Don't advance frame.
tempsfc_res.nglMaximize     = False    # Do not maximize plot in frame 

#
#  Create the four plots (they won't get drawn here, because nglDraw
#  was set to False for all three of them.
#
rhfill    = Ngl.contour(wks,smothrh,rh_res)
templine  = Ngl.contour(wks,smothtemp,temp_res)
windlayer = Ngl.vector(wks,ugrid,vgrid,uv_res)
rainhist  = Ngl.xy(wks,taus,rain03,rain_res)

#
# For the rain plot, we want filled bars instead of a curve, so create
# a dummy plot with all the Y values equal to rain_res.trYMinF. This
# will insure no curve gets drawn. Then, add the bars and bar outlines
# later with Ngl.add_polygon and Ngl.add_polyline.
#
#
# Make dummy data equal to min Y axis value.
#
dummy = rain_res.trYMinF * Numeric.ones([len(rain03)],rain03.typecode())

#
# Make sure there's enough room for a bar at the first and last
# X points of the data.
#
dx               = min(taus[1:24]-taus[0:23]) # Calculate bar width.
rain_res.trXMinF = min(taus) - dx/2.
rain_res.trXMaxF = max(taus) + dx/2.

#
# Create dummy plot.
#
rainhist  = Ngl.xy(wks,taus,dummy,rain_res)

#
# Get indices where rain data is above zero. Draw filled bars for each
# of these points.
#
above_zero     = Numeric.greater(rain03,0.0)
ind_above_zero = Numeric.nonzero(above_zero)  # We know that the values are 
                                              # above zero.
num_above = len(ind_above_zero)

#
# Create arrays to hold polygon points. Since we are drawing a rectangle,
# we just need 5 points for the filled rectangle, and we can use the
# first four points of each for the outline.
#
px = Numeric.zeros(5*num_above,taus.typecode())
py = Numeric.zeros(5*num_above,rain03.typecode())

#
# Create resource list for polygons.
#
pgres             = Ngl.Resources()
pgres.gsFillColor = "green"

taus_above_zero = Numeric.take(taus,ind_above_zero)
px[0::5] = (taus_above_zero - dx/2.).astype(taus.typecode())
px[1::5] = (taus_above_zero - dx/2.).astype(taus.typecode())
px[2::5] = (taus_above_zero + dx/2.).astype(taus.typecode())
px[3::5] = (taus_above_zero + dx/2.).astype(taus.typecode())
px[4::5] = (taus_above_zero - dx/2.).astype(taus.typecode())
py[0::5] = rain_res.trYMinF
py[1::5] = Numeric.take(rain03,ind_above_zero)
py[2::5] = Numeric.take(rain03,ind_above_zero)
py[3::5] = rain_res.trYMinF
py[4::5] = rain_res.trYMinF
polyg    = Ngl.add_polygon(wks,rainhist,px,py,pgres)

#
# For the outlines, we don't need the fifth point.
#
polyl    = Ngl.add_polyline(wks,rainhist,px,py,pgres)
temptmsz  = Ngl.xy(wks,taus,tempht,tempsfc_res)

# ---------------------- overlay, draw, and advance frame ---------
Ngl.overlay(rhfill,templine)   # Overlay temperature contour on rh plot.
Ngl.overlay(rhfill,windlayer)  # Overlay windbarbs on rh plot.

Ngl.draw(rhfill)
Ngl.draw(rainhist)
Ngl.draw(temptmsz)
Ngl.frame(wks)

Ngl.end()
