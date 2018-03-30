#
#  Import NumPy.
#
import Numeric

#
#  Import the NetCDF reader.
#
from Scientific.IO.NetCDF import NetCDFFile

#
#  Import Ngl support functions.
#
import Ngl
#
#  Open three netCDF files and get variables.
#
data_dir  = Ngl.ncargpath("data")
cdf_file1 = NetCDFFile(data_dir + "/cdf/941110_P.cdf","r")
cdf_file2 = NetCDFFile(data_dir + "/cdf/sstdata_netcdf.nc","r")
cdf_file3 = NetCDFFile(data_dir + "/cdf/Pstorm.cdf","r")

psl = cdf_file1.variables["Psl"]   
sst = cdf_file2.variables["sst"]  
pf  = cdf_file3.variables["p"]  

psl_lon  =  cdf_file1.variables["lon"][:]
psl_lat  =  cdf_file1.variables["lat"][:]
psl_nlon =  len(psl_lon)
psl_nlat =  len(psl_lat)

sst_lon  =  cdf_file2.variables["lon"][:]
sst_lat  =  cdf_file2.variables["lat"][:]
sst_nlon =  len(sst_lon)
sst_nlat =  len(sst_lat)

pf_lon  =  cdf_file3.variables["lon"][:]
pf_lat  =  cdf_file3.variables["lat"][:]
pf_nlon =  len(pf_lon)
pf_nlat =  len(pf_lat)

#
#  Open a workstation.
#
wks_type = "ps"
wks = Ngl.open_wks(wks_type,"ngl05p")

#----------- Begin first plot -----------------------------------------
 
resources = Ngl.Resources()

resources.sfXCStartV = min(psl_lon)
resources.sfXCEndV   = max(psl_lon)
resources.sfYCStartV = min(psl_lat)
resources.sfYCEndV   = max(psl_lat)

map = Ngl.contour_map(wks,psl,resources)

#----------- Begin second plot -----------------------------------------

cmap = Ngl.get_MDfloat_array(wks,"wkColorMap")
cmap[0] = [1.,1.,1.]
cmap[1] = [0.,0.,0.]

rlist = Ngl.Resources()
rlist.wkColorMap = cmap
Ngl.set_values(wks,rlist)

resources.mpProjection = "Orthographic" # Change the map projection.
resources.mpCenterLonF = 180.           # Rotate the projection.
resources.mpFillOn     = True           # Turn on map fill.
resources.mpFillColors = [0,-1,28,-1]   # Fill land and leave oceans
                                          # and inland water transparent.

resources.vpXF      = 0.1    # Change the size and location of the
resources.vpYF      = 0.9    # plot on the viewport.
resources.vpWidthF  = 0.7
resources.vpHeightF = 0.7

mnlvl = 0                        # Minimum contour level.
mxlvl = 28                       # Maximum contour level.
spcng = 2                        # Contour level spacing.
ncn   = (mxlvl-mnlvl)/spcng + 1  # Number of contour levels.

resources.cnLevelSelectionMode = "ManualLevels" # Define your own
resources.cnMinLevelValF       = mnlvl          # contour levels.
resources.cnMaxLevelValF       = mxlvl
resources.cnLevelSpacingF      = spcng

resources.cnLineThicknessF     = 2.0   # Double the line thickness.

resources.cnFillOn           = True  # Turn on contour level fill.
resources.cnMonoFillColor    = True  # Use one fill color.
resources.cnMonoFillPattern  = False # Use multiple fill patterns.
FillPatterns = Numeric.zeros([ncn+1],Numeric.Int)-1
FillPatterns[ncn-1:ncn+1] =  17
resources.cnFillPatterns     = FillPatterns
resources.cnLineDrawOrder      = "Predraw" # Draw lines and filled
resources.cnFillDrawOrder      = "Predraw" # areas before map gets
                                             # drawn.

resources.tiMainString = ":F26:" + cdf_file2.title

resources.sfXCStartV = min(sst_lon)   # Define where contour plot
resources.sfXCEndV   = max(sst_lon)   # should lie on the map plot.
resources.sfYCStartV = min(sst_lat)
resources.sfYCEndV   = max(sst_lat)

resources.pmLabelBarDisplayMode = "Never"  # Turn off the label bar.

map = Ngl.contour_map(wks,sst[0,:,:],resources) # Draw contours over a map.

#----------- Begin third plot -----------------------------------------

del resources
resources = Ngl.Resources()

if hasattr(pf,"_FillValue"):
  resources.sfMissingValueV = pf._FillValue

resources.tiXAxisString = ":F25:longitude"
resources.tiYAxisString = ":F25:latitude"

resources.cnFillOn              = True     # Turn on contour fill.
resources.cnLineLabelsOn        = False    # Turn off line labels.
resources.cnInfoLabelOn         = False    # Turn off info label.
resources.nglSpreadColors = False    # Do not interpolate color space.

resources.sfXCStartV = min(pf_lon)   # Define where contour plot
resources.sfXCEndV   = max(pf_lon)   # should lie on the map plot.
resources.sfYCStartV = min(pf_lat)
resources.sfYCEndV   = max(pf_lat)

resources.mpProjection = "LambertEqualArea"  # Change the map projection.
resources.mpCenterLonF = (pf_lon[pf_nlon-1] + pf_lon[0])/2
resources.mpCenterLatF = (pf_lat[pf_nlat-1] + pf_lat[0])/2

resources.mpLimitMode = "LatLon"    # Limit the map view.
resources.mpMinLonF   = min(pf_lon)
resources.mpMaxLonF   = max(pf_lon)
resources.mpMinLatF   = min(pf_lat)
resources.mpMaxLatF   = max(pf_lat)
resources.mpPerimOn   = True        # Turn on map perimeter.

resources.pmTickMarkDisplayMode = "Never"  # Turn off map tickmarks.

resources.tiMainString = ":F26:January 1996 storm" # Set a title.

resources.vpXF      = 0.1    # Change the size and location of the
resources.vpYF      = 0.9    # plot on the viewport.
resources.vpWidthF  = 0.7
resources.vpHeightF = 0.7

resources.nglFrame = False # Don't advance frame.

#
#  Extract the dataset from pf and scale by 0.01, making sure to
#  retain the original missing values.
#
pfa = pf[0,:,:]
if hasattr(pf,"_FillValue"):
  pfa = 0.01*(pfa*Numeric.not_equal(pfa,pf._FillValue)) +   \
        pf._FillValue*Numeric.equal(pfa,pf._FillValue)
else:
  pfa = 0.01*pfa
#
# draw contours over map.
#
map = Ngl.contour_map(wks,pfa,resources) # Convert pf to "mb" and

txres = Ngl.Resources()
txres.txFontHeightF = 0.025  # for a text string.
txres.txFontColor   = 4
Ngl.text_ndc(wks,":F25:Pressure (mb)",.41,.185,txres)
Ngl.frame(wks)   # Advance the frame.

#---------- Begin fourth plot ------------------------------------------

del resources.tiXAxisString  # Delete some resources you don't
del resources.tiYAxisString  # need anymore.
del resources.nglFrame

del cmap
cmap = Numeric.array([[1.00, 1.00, 1.00], [0.00, 0.00, 0.00], \
                      [.560, .500, .700], [.300, .300, .700], \
                      [.100, .100, .700], [.000, .100, .700], \
                      [.000, .300, .700], [.000, .500, .500], \
                      [.000, .400, .200], [.000, .600, .000], \
                      [.000, 1.00, .000], [.550, .550, .000], \
                      [.570, .420, .000], [.700, .285, .000], \
                      [.700, .180, .000], [.870, .050, .000], \
                      [1.00, .000, .000], [0.00, 1.00, 1.00], \
                      [.700, .700, .700]],Numeric.Float0)

rlist = Ngl.Resources()
rlist.wkColorMap = cmap
Ngl.set_values(wks,rlist)

resources.mpFillOn              = True         # Turn on map fill.
resources.mpFillAreaSpecifiers  = ["Water","Land","USStatesWater"]
resources.mpSpecifiedFillColors = [17,18,17]
resources.mpAreaMaskingOn       = True            # Indicate we want to
resources.mpMaskAreaSpecifiers  = "USStatesLand"  # mask land.
resources.mpPerimOn             = True            # Turn on a perimeter.
resources.mpGridMaskMode        = "MaskLand"      # Mask grid over land.
resources.cnFillDrawOrder       = "Predraw"       # Draw contours first.

resources.cnLevelSelectionMode = "ExplicitLevels" # Define own levels.
resources.cnLevels             = Numeric.arange(985.,1046.,5.)

resources.lbTitleString  = ":F25:pressure (mb)" # Title for label bar.
resources.cnLinesOn      = False         # Turn off contour lines.
resources.lbOrientation  = "Horizontal"  # Label bar orientation.

#
#  Extract the dataset from pf and scale by 0.01, making sure to
#  retain the original missing values.
#
pfa = pf[1,:,:]
if hasattr(pf,"_FillValue"):
  pfa = 0.01*(pfa*Numeric.not_equal(pfa,pf._FillValue)) +   \
        pf._FillValue*Numeric.equal(pfa,pf._FillValue)
else:
  pfa = 0.01*pfa
map = Ngl.contour_map(wks,pfa,resources)

del map
del resources
del rlist
del txres

Ngl.end()
