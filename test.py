from treeset import TreeSet
from hllcounter import HllCounter
import pickle
import struct
import numpy

s = 100000
data1 = numpy.random.random_integers(0, 100000, size=s)
hc = HllCounter(k=10)
hc1 = HllCounter(k=10)
for i in range(len(data1)):
  hc.put(data1[i])
  if i <= s / 2:
    hc1.put(data1[i])
hcpk = open('hc.pk', 'wb')
hc1pk = open('hc1.pk', 'wb')
pickle.dump(hc, hcpk)
pickle.dump(hc1, hc1pk)
hcpk.close()
hc1pk.close()
print hc.size()
print hc1.size()
hcarray = [hc, hc1]
print "first:", HllCounter.intersect(hcarray)
print "second:", HllCounter.intersect(hcarray)

