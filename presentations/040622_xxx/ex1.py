#!/mesonet/python/bin/python

# Python Imports
from Scientific.IO.ArrayIO import *
import Numeric
from Scientific.IO.NetCDF import *

# Load up the precip data from file
precip = readFloatArray("precip.dat")
# Get the shape of this precip array
shp = Numeric.shape(precip)

# Read lat and lon values from file
latitudes = readFloatArray("lats.dat")
longitudes = readFloatArray("lons.dat")

# Create NetCDF file
nc = NetCDFFile("precip.nc", 'w')
# Create two dimensions with the size of the precip data
nc.createDimension("x", shp[1])
nc.createDimension("y", shp[0])

# Create three variables
lat = nc.createVariable("latitude", Numeric.Float, ("y", "x") )
lon = nc.createVariable("longitude", Numeric.Float, ("y", "x") )
prec = nc.createVariable("precip", Numeric.Float, ("y", "x") )

# Assign in.
lat.assignValue(latitudes)
lon.assignValue(longitudes)
prec.assignValue(precip)

# Close file, we are done!
nc.close()
