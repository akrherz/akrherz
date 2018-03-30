#
#  Import Ngl support functions.
#
import Ngl

wks_type = "ps"
wks = Ngl.open_wks(wks_type,"legend")

labels = ["One","Two","Three","Four","Five","Six"]

#
# Generate a legend with the default settings.
#
lg = Ngl.legend_ndc(wks,5,labels,0.3,0.9)
Ngl.frame(wks)

#
# Change the font of the labels.
#
rlist                  = Ngl.Resources()
rlist.lgLabelFont      = 21

lg = Ngl.legend_ndc(wks,5,labels,0.3,0.9,rlist)
Ngl.frame(wks)

#
# Change the orientation and size.
#
rlist.vpWidthF          = 0.85
rlist.vpHeightF         = 0.20
rlist.lgOrientation     = "Horizontal"
lg = Ngl.legend_ndc(wks,6,labels,0.1,0.2,rlist)
Ngl.frame(wks)

#
# Generate a lot of labels. Notice how the legend labels are automatically
# adjusted and not every one is shown. To turn this off, set
# lgAutoStride to False, but then your labels will run into each other.
# You could set lgLabelAngleF to -45 or 90 to get slanted labels.
#

lotta_labels = ["AL","AR","AZ","CA","CO","CT","DE","FL","GA","IA","ID","IL",\
                "IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT",\
                "NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA",\
                "RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"]

rlist.lgLabelAlignment   = "AboveItems"
rlist.lgLabelFontHeightF = 0.014
rlist.lgMonoDashIndex    = True
lg = Ngl.legend_ndc(wks,len(lotta_labels),lotta_labels,0.1,0.5,rlist)
Ngl.frame(wks)


Ngl.end()
