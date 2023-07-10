#!/usr/bin/env python

import mx.DateTime
import sys

gmt = mx.DateTime.gmt()
# Set hour from stdin
myhour = int(sys.argv[1])
gmt += mx.DateTime.RelativeDateTime(hour=myhour)

endgmt = gmt + mx.DateTime.RelativeDateTime(days=+2)

dict = {}
dict["syear"] = gmt.year
dict["smonth"] = gmt.month
dict["sday"] = gmt.day
dict["shour"] = gmt.hour
dict["eyear"] = endgmt.year
dict["emonth"] = endgmt.month
dict["eday"] = endgmt.day
dict["ehour"] = endgmt.hour


s = (
    """&record1




 START_YEAR  = %(syear)s
 START_MONTH = %(smonth)s
 START_DAY   = %(sday)s
 START_HOUR  = %(shour)s

 END_YEAR  = %(eyear)s
 END_MONTH = %(emonth)s
 END_DAY   = %(eday)s
 END_HOUR  = %(ehour)s



 INTERVAL = 10800






/
"""
    % dict
)

out = open("my.namelist", "w")
out.write(s)
out.close()
