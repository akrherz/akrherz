
import network
nt = network.Table("WFO")

data = {}
for sid in nt.sts.keys():
    data[sid] = 5

data['MPX'] = 10
data['ARX'] = 2

from pyiem.plot import MapPlot

p = MapPlot(sector='nws',
                 title='Weather Bureau Office Coolness Factor')
p.fill_cwas(data, bins=range(0,11), lblformat='%.0f', units='awesome')
p.postprocess(filename='coolness.png')
