#!/usr/bin/env python

import myfort
import numarray
from Scientific.IO import NetCDF

nc = NetCDF.NetCDFFile("testdata.nc", "r")

h = numarray.array(nc.variables["h"].getValue())
u = numarray.array(nc.variables["u"].getValue())
v = numarray.array(nc.variables["v"].getValue())

dhdt = numarray.zeros((10, 10))
dx = 1000.01
dy = 1000.01

dhdt = myfort.divg(h, u, v, dhdt, dx, dy)
print(dhdt)
