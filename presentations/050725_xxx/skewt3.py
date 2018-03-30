#
#   File:    skewt3.py
#
#   Author:  Fred Clare (based on an NCL example of Dennis Shea)
#            National Center for Atmospheric Research
#            PO 3007, Boulder, Colorado
#
#   Date:    Tue Mar  1 14:58:28 MST 2005
# 
#   Description:
#            Produces two plots using real data:
#              1. Shows the full radiosonde.
#              2. This "thins" the number of wind barbs plotted and 
#                 uses a Centigrade scale.  Setting Wthin to 3 causes
#                 the plotting of every third wind barb.
#    
import Ngl
  
nlvl = 65
ncol = 7
TestData =  Ngl.asciiread(Ngl.ncargpath("data") + "/asc/sounding_ATS.asc", \
                          [nlvl,ncol], "float")

#
# Order: Surface is 'bottom'  eg: 1000,950,935,897,...  
#
p    = TestData[:,0]    # pressure     [mb / hPa] 
tc   = TestData[:,1]    # temperature  [C]    
tdc  = TestData[:,2]    # dew pt temp  [C]   
z    = TestData[:,4]    # geopotential [gpm] 
wspd = TestData[:,5]    # wind speed   [knots or m/s]    
wdir = TestData[:,6]    # meteorological wind dir   

wks_type = "ps"
wks = Ngl.open_wks(wks_type, "skewt3")

#
#  Plot1 - Create background skew-T and plot sounding.
#
skewtOpts                 = Ngl.Resources()
skewtOpts.sktDrawColAreaFill = True    # default is False

#
#  Change the title function code flag to "~" (away from
#  colon), since there will be colons in the titles.
#
skewtOpts.tiMainFuncCode  = "~"
skewtOpts.tiMainString    = "ATS Rawindsonde: default dataOpts" 

skewt_bkgd = Ngl.skewt_bkg(wks, skewtOpts)
skewt_data = Ngl.skewt_plt(wks, skewt_bkgd, p, tc, tdc, z, \
                                  wspd,wdir)
Ngl.draw(skewt_bkgd)
Ngl.draw(skewt_data)
Ngl.frame(wks)

#
#  Plot 2 - thin the wind barbs and use Centigrade.
#
dataOpts       = Ngl.Resources()
dataOpts.sktWthin = 3                  # Plot every 3rd wind barb
skewtOpts.tiMainString   = "ATS Rawindsonde: degC + Thin wind" 
skewtOpts.sktDrawFahrenheit = False   # default is True

skewt_bkgd = Ngl.skewt_bkg(wks, skewtOpts)
skewt_data = Ngl.skewt_plt(wks, skewt_bkgd, p, tc, tdc, z,  \
                            wspd,wdir, dataOpts)
Ngl.draw (skewt_bkgd)
Ngl.draw (skewt_data)
Ngl.frame(wks)
Ngl.end()
