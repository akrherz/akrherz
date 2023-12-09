#!/mesonet/python/bin/python

from pyIEM import mesonet

obs = [
    60,
    60,
    59,
    58,
    59,
    58,
    58,
    62,
    66,
    70,
    73,
    75,
    75,
    77,
    79,
    76,
    79,
    78,
    75,
    72,
    68,
    66,
    65,
    63,
]

data = []
for i in obs:
    data.append(mesonet.f2c(i))

"""
print sum(data)
print sum(data) / 24.0
print sum(data) / 24
print mesonet.c2f( sum(data) / 24.0 )
print mesonet.c2f( sum(data) / 24 )
"""
