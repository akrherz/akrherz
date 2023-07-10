import Ngl, Numeric

#
#  Draw some wind barbs over a map.
#

#
#  Specify a color map and open an output workstation.
#
cmap = Numeric.array(
    [[1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]], Numeric.Float0
)
rlist = Ngl.Resources()
rlist.wkColorMap = cmap
wks_type = "x11"
wks = Ngl.open_wks(wks_type, "wmbarbmap", rlist)  # Open a workstation.

#
#  Set some map resources.
#
mpres = Ngl.Resources()
mpres.mpProjection = "Orthographic"
mpres.mpLimitMode = "LatLon"
mpres.mpMinLonF = -40.0
mpres.mpMaxLonF = 20.0
mpres.mpMinLatF = 55.0
mpres.mpMaxLatF = 85.0
mpres.mpCenterLatF = 70.0
mpres.mpCenterLonF = -10.0
mpres.nglFrame = False

#
#  Draw the map.
#
map = Ngl.map(wks, mpres)

#
#  Draw an array of vertical wind barbs over the above map.
#
lat = Numeric.zeros([3, 2, 5], Numeric.Float0)
lon = Numeric.zeros([3, 2, 5], Numeric.Float0)
u = Numeric.zeros([3, 2, 5], Numeric.Float0)
v = Numeric.zeros([3, 2, 5], Numeric.Float0)

lat[0, :, :] = 65
lat[1, :, :] = 70
lat[2, :, :] = 75

for i in range(5):
    lon[:, 0, i] = -40.0 + i * 5.0
    lon[:, 1, i] = -15.0 + i * 5.0

u[:, :, :] = 0.0
v[:, :, :] = 90.0

Ngl.wmsetp("col", 2)  # Draw in red.
Ngl.wmsetp("wbs", 0.06)  # Increase the size of the barbs.
Ngl.wmbarbmap(wks, lat, lon, u, v)  # Plot barbs.
Ngl.frame(wks)

Ngl.end()
