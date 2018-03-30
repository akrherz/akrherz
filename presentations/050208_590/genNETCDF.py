#!/usr/bin/env python

# Generate the NetCDF Test dataset

from Scientific.IO import NetCDF
import numarray

nc = NetCDF.NetCDFFile('testdata.nc', 'w')

nc.createDimension('x', 10)
nc.createDimension('y', 10)

def funcform(x,y):
  return  (x-5)**2 + (y-5)**2

h = nc.createVariable('h', 'd', ('x','y') )
h.assignValue( numarray.fromfunction( funcform, (10,10) ) )

u = nc.createVariable('u', 'd', ('x','y') )
u.assignValue( numarray.identity(10) * 10 )

v = nc.createVariable('v', 'd', ('x','y') )
v.assignValue( numarray.ones( (10,10) ) * 5 )

nc.close()
