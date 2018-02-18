
import network
nt = network.Table("WFO")

data = {}
for sid in nt.sts.keys():
    data[sid if len(sid) == 3 else sid[1:]] = 5

data['LOT'] = 10
data['DVN'] = 2

from pyiem.plot import MapPlot

p = MapPlot(sector='nws', axisbg='white',
                 title='Weather Bureau Office Coolness Factor')
p.fill_cwas(data, bins=range(0,11), lblformat='%.0f', units='awesome')
p.postprocess(filename='coolness.png')
