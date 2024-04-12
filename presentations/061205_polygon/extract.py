#!/usr/bin/env python

import glob
import re

files = glob.glob("output/svr_2005_???.html")
for file in files:
    wfo = re.findall("([A-Z]{3}).html", file)[0]
    d = open(file, "r").read()
    far, pod, csi = re.findall(
        "PARSEME: FAR:([0-9\.]*) POD:([0-9\.]*) CSI:([0-9\.]*)", d
    )[0]
    print("%s,%s,%s,%s," % (wfo, far, pod, csi))
