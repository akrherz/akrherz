#!/mesonet/python/bin/python

from pyIEM import iemdb
i = iemdb.iemdb()
access = i['iem']

rs = access.query("SELECT round(tmpf::numeric,0) as t from current_log WHERE date(valid) = 'YESTERDAY' and station = 'DSM' and extract(minute from valid) = 54").dictresult()

data = []
for i in range(len(rs)):
  data.append( int(rs[i]['t']) )

print sum(data)
print sum(data) / 24.0
print sum(data) / 24
