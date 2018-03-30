#!/mesonet/python/bin/python

from Scientific.IO import NetCDF

nc = NetCDF.NetCDFFile('test.nc', 'a')

tmpk = nc.variables['temperature']
tmpk[0] = 273.5
recNum = nc.dimensions['recNum']

nc.close()
