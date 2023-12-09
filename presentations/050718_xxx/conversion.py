#!/usr/bin/env python

import temperature

for i in range(100):
    t = temperature.temperature(i, "C")
    print("%6.2f C %6.2f F" % (i, t.toUnit("F")))
