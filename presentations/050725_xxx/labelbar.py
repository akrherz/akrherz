#
#  Import Ngl support functions.
#
import Ngl

wks_type = "ps"
wks = Ngl.open_wks(wks_type,"labelbar")

labels = ["One","Two","Three","Four","Five","Six"]

#
# Generate a labelbar with the default settings.
#
lb = Ngl.labelbar_ndc(wks,5,labels,0.3,0.9)
Ngl.frame(wks)

#
# Change the font and alignment of the labels.
#
rlist                  = Ngl.Resources()
rlist.lbLabelFont      = 21
rlist.lbLabelAlignment = "InteriorEdges"

lb = Ngl.labelbar_ndc(wks,5,labels,0.3,0.9,rlist)
Ngl.frame(wks)

#
# Change the size, orientation, the fill to solid fill.
#
rlist.vpWidthF          = 0.85
rlist.vpHeightF         = 0.20
rlist.lbMonoFillPattern = 21
rlist.lbFillPattern     = "SolidFill"
rlist.lbOrientation     = "Horizontal"
rlist.lbLabelAlignment  = "ExternalEdges"
lb = Ngl.labelbar_ndc(wks,5,labels,0.1,0.2,rlist)
Ngl.frame(wks)

#
# Do a lot of labels. Notice how the labelbar labels are automatically
# adjusted and not every one is shown. To turn this off, set
# lbAutoStride to False, but then your labels will run into each other.
# You could set lbLabelAngleF to -45 or 90 to get slanted labels.
#

lotta_labels = ["AL","AR","AZ","CA","CO","CT","DE","FL","GA","IA","ID","IL",\
                "IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT",\
                "NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA",\
                "RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY"]

rlist.lbLabelAlignment   = "InteriorEdges"
rlist.lbLabelFontHeightF = 0.014
lb = Ngl.labelbar_ndc(wks,len(lotta_labels),lotta_labels,0.1,0.5,rlist)
Ngl.frame(wks)


Ngl.end()
