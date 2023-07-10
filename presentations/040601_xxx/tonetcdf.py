#!/mesonet/python/bin/python

# Python Imports
from Scientific.IO import NetCDF
import Numeric, re, string

# Open the NetCDF file
nc = NetCDF.NetCDFFile("disks.nc", "w")

#### DIMENSIONS
# Create a dimension for records, it is unlimited length in size.
nc.createDimension("recNum", None)
# Recall that NetCDF does not work with Strings, so we must have
# a dimension for a character array
nc.createDimension("mountslen", 30)

#### VARIABLES
# mount will store the names of our mounts
mount = nc.createVariable("mount", Numeric.Character, ("recNum", "mountslen"))
# usage will store out disk usage as an Int
usage = nc.createVariable("usage", Numeric.Int, ("recNum",))

# Sync netcdf contents to disk.
nc.sync()

# Open out Comma delimited disk usage file
lines = open("disks.csv", "r").readlines()

# Sentinel to keep track of position
counter = 0
for line in lines[1:]:
    # Split line into tokens via the re module
    tokens = re.split(",", line)
    # m is the name of the disk mount, position 1 in the split line
    m = "%-30s" % (tokens[1],)
    # u is our disk usage, we strip off the trailing /n
    u = string.strip(tokens[3])
    # Assign in the int value of our disk usage
    usage[counter] = int(float(u))
    # Assign in the name of our mount point
    mount[counter] = Numeric.array(list(m))
    # Increment our sentinel
    counter += 1

# Close the NETCDF
nc.close()
